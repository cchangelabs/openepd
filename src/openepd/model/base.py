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
import abc
from enum import StrEnum
import json
from typing import Any, Callable, Generic, Optional, Type, TypeAlias, TypeVar

from openepd.compat.pydantic import pyd, pyd_generics
from openepd.model.validation.common import validate_version_compatibility, validate_version_format
from openepd.model.versioning import OpenEpdVersions, Version

AnySerializable: TypeAlias = int | str | bool | float | list | dict | pyd.BaseModel | None
TAnySerializable = TypeVar("TAnySerializable", bound=AnySerializable)

OPENEPD_VERSION_FIELD = "openepd_version"
"""Field name for the openEPD format version."""

OPENAPI_SCHEMA_SERVICE_PROPERTIES = ["ext_version", "ext"]
"""OpenAPI properties which should be moved to the bottom of specification if present. """


class OpenEpdDoctypes(StrEnum):
    """Enum of supported openEPD document types."""

    Epd = "openEPD"


def modify_pydantic_schema(schema_dict: dict, cls: type) -> dict:
    """
    Modify the schema dictionary to add the required fields.

    :param schema_dict: schema dictionary
    :param cls: class for which the schema was generated
    :return: modified schema dictionary
    """
    for prop_name in OPENAPI_SCHEMA_SERVICE_PROPERTIES:
        prop = schema_dict.get("properties", {}).get(prop_name, None)
        # move to bottom
        if prop is not None:
            del schema_dict["properties"][prop_name]
            schema_dict["properties"][prop_name] = prop

    return schema_dict


class PydanticClassAttributeExposeModelMetaclass(pyd.main.ModelMetaclass):
    """
    Extension of the pydantic's ModelMetaclass which restores class attribute lookup for fields.

    In pydantic, while the model fields are defined in the model as class-level attributes, in runtime they disappear
    due to ModelMetaclass logic. ModelMetaclass takes the defined attributes, removes them from class dict and puts
    into a special __fields__ attribute to avoid naming conflict.

    We would like to be able to access the attributes via dot notation in the runtimes, since it makes refactoring
    easier.

    This class exposes the original fields when accessed via class name. For example, one can call `Pcr.name` and get
    `ModelField`, in addition to calling `pcr.__fields__` on an instance.
    """

    def __getattr__(cls, name: str) -> Any:
        if name in cls.__fields__:
            return cls.__fields__[name]
        return getattr(super, name)


class BaseOpenEpdSchema(pyd.BaseModel, metaclass=PydanticClassAttributeExposeModelMetaclass):
    """Base class for all OpenEPD models."""

    ext: dict[str, AnySerializable] | None = pyd.Field(alias="ext", default=None)

    class Config:
        allow_mutation = True
        validate_assignment = False
        allow_population_by_field_name = True
        use_enum_values = True
        schema_extra: Callable | dict = modify_pydantic_schema

    def to_serializable(self, *args, **kwargs) -> dict[str, Any]:
        """
        Return a serializable dict representation of the DTO.

        It expects the same arguments as the pyd.BaseModel.json() method.
        """
        return json.loads(self.json(*args, **kwargs))

    def has_values(self) -> bool:
        """Return True if the model has any values."""
        return len(self.dict(exclude_unset=True, exclude_none=True)) > 0

    def set_ext(self, ext: "OpenEpdExtension") -> None:
        """Set the extension field."""
        self.set_ext_field(ext.get_extension_name(), ext)

    def set_ext_field(self, key: str, value: AnySerializable) -> None:
        """Add an extension field to the model."""
        if self.ext is None:
            self.ext = {}
        self.ext[key] = value

    def set_ext_field_if_any(self, key: str, value: AnySerializable) -> None:
        """Add an extension field to the model if the value is not None."""
        if value is not None:
            self.set_ext_field(key, value)

    def get_ext_field(self, key: str, default: AnySerializable = None) -> AnySerializable | None:
        """Get an extension field from the model."""
        if self.ext is None:
            return default
        return self.ext.get(key, default)

    def get_typed_ext_field(
        self, key: str, target_type: Type[TAnySerializable], default: Optional[TAnySerializable] = None
    ) -> TAnySerializable:
        """
        Get an extension field from the model and convert it to the target type.

        :raise ValueError: if the value cannot be converted to the target type.
        """
        value = self.get_ext_field(key, default)
        if value is None:
            return None  # type: ignore
        if issubclass(target_type, pyd.BaseModel) and isinstance(value, dict):
            return target_type.construct(**value)  # type: ignore
        elif isinstance(value, target_type):
            return value
        raise ValueError(f"Cannot convert {value} to {target_type}")

    def get_ext(self, ext_type: Type["TOpenEpdExtension"]) -> Optional["TOpenEpdExtension"]:
        """Get an extension field from the model or None if it doesn't exist."""
        return self.get_typed_ext_field(ext_type.get_extension_name(), ext_type, None)

    def get_ext_or_empty(self, ext_type: Type["TOpenEpdExtension"]) -> "TOpenEpdExtension":
        """Get an extension field from the model or an empty instance if it doesn't exist."""
        return self.get_typed_ext_field(ext_type.get_extension_name(), ext_type, ext_type.construct(**{}))

    @classmethod
    def is_allowed_field_name(cls, field_name: str) -> bool:
        """
        Return True if the field name is defined in the module.

        Both property name and aliases are checked.
        """
        if field_name in cls.__fields__:
            return True
        else:
            for x in cls.__fields__.values():
                if x.alias == field_name:
                    return True
        return False

    @classmethod
    def get_asset_type(cls) -> str | None:
        """
        Return the asset type as it should be written into bundle.

        Only independent (e.g. Pcr, Org, Epd, etc) objects have asset type.
        Supplementary objects (e.g. ResourceUseSet, Location, LatLng) must always return None.
        """
        return None


class BaseOpenEpdGenericSchema(pyd_generics.GenericModel, BaseOpenEpdSchema):
    """Base class for all OpenEPD generic models."""

    pass


class OpenEpdExtension(BaseOpenEpdSchema, metaclass=abc.ABCMeta):
    """Base class for OpenEPD extension models."""

    @classmethod
    @abc.abstractmethod
    def get_extension_name(cls) -> str:
        """Return the name of the extension."""
        pass


TOpenEpdExtension = TypeVar("TOpenEpdExtension", bound=OpenEpdExtension)
TOpenEpdObject = TypeVar("TOpenEpdObject", bound=BaseOpenEpdSchema)
TOpenEpdObjectClass = TypeVar("TOpenEpdObjectClass", bound=Type[BaseOpenEpdSchema])


class RootDocument(abc.ABC, BaseOpenEpdSchema):
    """Base class for all objects representing openEPD root element. E.g. Epd, IndustryEpd, GenericEstimate, etc."""

    _FORMAT_VERSION: str
    """Version of this document format. Must be defined in the concrete class."""

    doctype: str = pyd.Field(
        description='Describes the type and schema of the document. Must always always read "openEPD".',
        default="OpenEPD",
    )
    openepd_version: str = pyd.Field(
        description="Version of the document format, related to /doctype",
        default=OpenEpdVersions.get_current().as_str(),
    )

    _version_format_validator = pyd.validator(OPENEPD_VERSION_FIELD, allow_reuse=True, check_fields=False)(
        validate_version_format
    )
    _version_major_match_validator = pyd.validator(OPENEPD_VERSION_FIELD, allow_reuse=True, check_fields=False)(
        validate_version_compatibility("_FORMAT_VERSION")
    )


TRootDocument = TypeVar("TRootDocument", bound=RootDocument)


class BaseDocumentFactory(Generic[TRootDocument]):
    """
    Base class for document factories.

    Extend it to create a factory for a specific document type e.g. for industry epd, epd, etc.
    """

    DOCTYPE_CONSTRAINT: str = ""
    VERSION_MAP: dict[Version, type[TRootDocument]] = {}

    @classmethod
    def from_dict(cls, data: dict) -> TRootDocument:
        """Create a document from a dictionary."""
        doctype: str | None = data.get("doctype")
        if doctype is None:
            raise ValueError("Doctype not found in the data.")
        if doctype.lower() != cls.DOCTYPE_CONSTRAINT.lower():
            raise ValueError(
                f"Document type {doctype} not supported. This factory supports {cls.DOCTYPE_CONSTRAINT} only."
            )
        version = Version.parse_version(data.get(OPENEPD_VERSION_FIELD, ""))
        for x, doc_cls in cls.VERSION_MAP.items():
            if x.major == version.major:
                if version.minor <= x.minor:
                    return doc_cls(**data)
                else:
                    raise ValueError(
                        f"Unsupported version: {version}. "
                        f"The highest supported version from branch {x.major}.x is {x}"
                    )
        supported_versions = ", ".join(f"{v.major}.x" for v in cls.VERSION_MAP.keys())
        raise ValueError(f"Version {version} is not supported. Supported versions are: {supported_versions}")
