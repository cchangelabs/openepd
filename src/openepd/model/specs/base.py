#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from collections import defaultdict
from typing import TYPE_CHECKING, Any, Iterable, Self, Type

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.validation.common import validate_version_compatibility, validate_version_format
from openepd.model.validation.quantity import QuantityValidator
from openepd.model.versioning import Version, WithExtVersionMixin

if TYPE_CHECKING:
    from . import Specs


class SpecPath(list[str]):
    """Class representing a hierarchical path to the material spec."""

    DEFAULT_DELIMITER = "."

    def __init__(self, *args, delimiter=DEFAULT_DELIMITER) -> None:
        super().__init__(args)
        self.delimiter = delimiter

    def to_string(self, delimiter: str | None = None):
        """Convert the path to string representation."""
        if delimiter is None:
            delimiter = self.delimiter
        return delimiter.join([str(x) for x in self])

    def __str__(self) -> str:
        return self.to_string(self.DEFAULT_DELIMITER)

    def create(self, *args) -> "SpecPath":
        """
        Create a copy of the current object with args appended at the end.

        :param args: elements to append
        :return: new HierarchicalPath
        """
        _new = SpecPath(*self)
        for x in args:
            _new.append(x)
        return _new

    @classmethod
    def from_str(cls, input_str: str, delimiter=DEFAULT_DELIMITER) -> "SpecPath":
        """
        Parse given string and creates new SpecPath entity.

        :param input_str: input string representing hierarchy
        :param delimiter: delimiter used to separate elements in the hierarchy
        """
        if not input_str:
            return SpecPath()
        return SpecPath(*input_str.split(delimiter))

    @classmethod
    def new(cls, input_: "AnySpecPath", delimiter: str = DEFAULT_DELIMITER) -> "SpecPath":
        """Create a new object."""
        if isinstance(input_, str):
            return SpecPath.from_str(input_, delimiter)
        return SpecPath(*input_, delimiter=delimiter)

    def copy(self) -> "SpecPath":
        """Create a copy of the current object."""
        return SpecPath(*self, delimiter=self.delimiter)


AnySpecPath = SpecPath | str | Iterable[str]
"""
Pointer to the material specification in a form of a dotted path(str) 
or iterable of strings representing full path components.
"""


class BaseOpenEpdSpec(BaseOpenEpdSchema):
    """Base class for all OpenEPD specs."""

    class Config:
        use_enum_values = False  # we need to store enums as strings and not values


class WithHierarchicalOperationsMixin:
    """Mixin for hierarchical operations."""

    def get_child_spec(self, path: AnySpecPath) -> "BaseOpenEpdHierarchicalSpec":
        """Get a child spec by a path."""
        from .factory import spec_factory

        if isinstance(path, str):
            if spec_factory.hierarchy_delimiter not in path:
                path = spec_factory.any_name_to_full_name(path)
            full_path = SpecPath.from_str(path, spec_factory.hierarchy_delimiter)
        else:
            full_path = SpecPath.new(path, spec_factory.hierarchy_delimiter)
        if not full_path:
            return self  # type: ignore
        child = getattr(self, full_path[0], None)
        if not child or not isinstance(child, BaseOpenEpdHierarchicalSpec):
            raise ValueError(f"Child spec `{full_path.to_string()}` doesn't exist")
        return child.get_child_spec(full_path[1:])


class BaseOpenEpdHierarchicalSpec(BaseOpenEpdSpec, WithExtVersionMixin, WithHierarchicalOperationsMixin):
    """Base class for new specs (hierarchical, versioned)."""

    # external validator for quantities (e.g. length, mass, etc.) which should be setup by the user of the library.
    _QUANTITY_VALIDATOR: QuantityValidator | None = None

    def __init__(self, **data: Any) -> None:
        # ensure that all the concrete spec objects fail on creations if they dont have _EXT_VERSION declared to
        # something meaningful
        if not hasattr(self, "_EXT_VERSION") or self._EXT_VERSION is None:
            raise ValueError(f"Class {self.__class__} must declare an extension version")
        Version.parse_version(self._EXT_VERSION)  # validate format correctness
        super().__init__(**{"ext_version": self._EXT_VERSION, **data})

    @classmethod
    def get_parent_spec_name(cls) -> str | None:
        """Get the name of the parent spec."""
        from .factory import spec_factory

        return spec_factory.get_parent_spec_name(spec_factory.get_name_for_spec(cls))

    @classmethod
    def get_spec_path(cls) -> SpecPath:
        """Get the path to the spec."""
        from .factory import spec_factory

        return SpecPath.from_str(spec_factory.get_full_name_for_spec(cls))

    @classmethod
    def get_parent_spec_class(cls) -> Type[Self] | None:
        """Get the parent spec class."""
        from .factory import spec_factory

        parent_name = cls.get_parent_spec_name()
        if parent_name:
            return spec_factory.get_by_full_name(parent_name)
        return None

    _version_format_validator = pyd.validator("ext_version", allow_reuse=True, check_fields=False)(
        validate_version_format
    )
    _version_major_match_validator = pyd.validator("ext_version", allow_reuse=True, check_fields=False)(
        validate_version_compatibility("_EXT_VERSION")
    )


def setup_external_validators(quantity_validator: QuantityValidator):
    """Set the implementation unit validator for specs."""
    BaseOpenEpdHierarchicalSpec._QUANTITY_VALIDATOR = quantity_validator


class SpecsFactory:
    """Factory for the specs."""

    def __init__(
        self,
        all_specs: dict[str, Iterable[Type[BaseOpenEpdHierarchicalSpec]]] | None = None,
        hierarchy_delimiter: str = ".",
    ):
        self.hierarchy_delimiter = hierarchy_delimiter
        self._short_name_2_spec: dict[str, list[Type[BaseOpenEpdHierarchicalSpec]]] = defaultdict(list)
        self._full_name_2_spec: dict[str, list[Type[BaseOpenEpdHierarchicalSpec]]] = defaultdict(list)
        self._spec_to_full_name: dict[Type[BaseOpenEpdHierarchicalSpec], str] = {}
        if all_specs:
            for full_name, specs in all_specs.items():
                for s in specs:
                    self.register_spec(full_name, s)
            self.init()

    def register_spec(self, full_name: str, spec: Type[BaseOpenEpdHierarchicalSpec]):
        """Register the spec."""
        short_name: str = self._full_name_2_short_name(full_name)
        self._short_name_2_spec[short_name].append(spec)
        self._full_name_2_spec[full_name].append(spec)
        self._spec_to_full_name[spec] = full_name

    def init(self):
        """
        Initialize the library of specs.

        It must be invoked avery time you add a new spec to the library e.g. by calling register_spec.
        """
        for s in self._short_name_2_spec.values():
            s.sort(key=lambda x: Version.parse_version(x.get_ext_version()).as_int())
        for s in self._full_name_2_spec.values():
            s.sort(key=lambda x: Version.parse_version(x.get_ext_version()).as_int())

    def get_by_name(self, short_name: str, version: Version | str | None = None) -> Type[BaseOpenEpdHierarchicalSpec]:
        """Get the spec by its short name."""
        candidates = self._short_name_2_spec.get(short_name, [])
        return self._resolve_spec_versions(candidates, version)

    def get_by_full_name(self, full_name: str, version: Version | str | None = None):
        """Get the spec by its full name."""
        candidates = self._full_name_2_spec.get(full_name, [])
        return self._resolve_spec_versions(candidates, version)

    def get_full_name_for_spec(self, spec: BaseOpenEpdHierarchicalSpec | Type[BaseOpenEpdHierarchicalSpec]) -> str:
        """Get the full name of the spec."""
        spec_cls = spec if isinstance(spec, type) else type(spec)
        try:
            return self._spec_to_full_name[spec_cls]
        except KeyError:
            raise ValueError("Spec not found")

    def get_name_for_spec(self, spec: BaseOpenEpdHierarchicalSpec | Type[BaseOpenEpdHierarchicalSpec]) -> str:
        """Get the short name of the spec."""
        return self._full_name_2_short_name(self.get_full_name_for_spec(spec))

    def get_parent_spec_name(self, spec_name: str) -> str | None:
        """Get the name of the parent spec."""

        full_name = self.any_name_to_full_name(spec_name)
        if self.hierarchy_delimiter not in full_name:
            return None
        else:
            parent_name = full_name.rsplit(self.hierarchy_delimiter, 1)[0]
            if parent_name not in self._full_name_2_spec:
                raise ValueError(f"Parent spec `{full_name}` is not registered. Data error?")
            return parent_name

    def create_spec(self, name_or_path: AnySpecPath) -> tuple["Specs", SpecPath]:
        """
        Create an instance of the Specs object with pre-created specs by a given name or path.

        :param name_or_path: name or path to the spec
        :return: tuple of the created Specs object and the path to the spec
        """
        full_name = self.any_name_to_full_name(
            SpecPath.new(name_or_path, delimiter=self.hierarchy_delimiter).to_string()
        )
        hierarchy_components = SpecPath.from_str(full_name, self.hierarchy_delimiter)
        from . import Specs

        result = Specs()
        current_obj: BaseOpenEpdSchema = result
        for cur_name in hierarchy_components:
            cur_spec = self._create_single_spec_by_name(cur_name)
            setattr(current_obj, cur_name, cur_spec)
            current_obj = cur_spec

        return result, hierarchy_components

    def _create_single_spec_by_name(self, name: str, data: dict[str, Any] | None = None) -> BaseOpenEpdHierarchicalSpec:
        spec_cls = self.get_by_full_name(self.any_name_to_full_name(name))
        return spec_cls(**(data or {}))

    def _resolve_spec_versions(
        self, candidates: list[Type[BaseOpenEpdHierarchicalSpec]], version: Version | str | None
    ) -> Type[BaseOpenEpdHierarchicalSpec]:
        if not candidates:
            raise ValueError("No spec found for the given name")
        resolved_spec = self._get_specific_version(candidates, version)
        if resolved_spec is None:
            raise ValueError("No spec found for the given version")
        return resolved_spec

    def _get_specific_version(
        self, spec_versions: list[Type[BaseOpenEpdHierarchicalSpec]], version: Version | str | None
    ) -> Type[BaseOpenEpdHierarchicalSpec] | None:
        if not spec_versions:
            return None
        target_version: Version | None = Version.parse_version(version) if isinstance(version, str) else version

        # No target version means the most one
        if target_version is None:
            return spec_versions[-1]

        # We compare just major component as minor versions are compatible
        for spec in spec_versions:
            if Version.parse_version(spec.get_ext_version()).major == target_version.major:
                return spec

        return None

    def any_name_to_full_name(self, name: str) -> str:
        """
        Convert any given name (long or short) to a full name.

        :raise ValueError: if the spec with the given name doesn't exist.
        """
        if self.hierarchy_delimiter in name:
            if name in self._full_name_2_spec:
                name = self._full_name_2_short_name(name)
            else:
                raise ValueError(f"Spec `{name}` doesn't exist")
        spec = self.get_by_name(name)
        return self.get_full_name_for_spec(spec)

    def _full_name_2_short_name(self, full_name: str) -> str:
        return full_name.rsplit(self.hierarchy_delimiter, 1)[-1]
