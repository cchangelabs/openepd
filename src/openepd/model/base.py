#
#  Copyright 2025 by C Change Labs Inc. www.c-change-labs.com
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
from collections.abc import Callable
from enum import StrEnum
from typing import Any, ClassVar, Generic, Literal, NotRequired, Optional, Self, TypeAlias, TypedDict, TypeVar, Unpack

from cqd import open_xpd_uuid  # type:ignore[import-untyped]
import pydantic
from pydantic import ConfigDict
import pydantic_core

from openepd.model.validation.common import validate_version_compatibility, validate_version_format
from openepd.model.versioning import OpenEpdVersions, Version

AnySerializable: TypeAlias = int | str | bool | float | list | dict | pydantic.BaseModel | None
TAnySerializable = TypeVar("TAnySerializable", bound=AnySerializable)

OPENEPD_VERSION_FIELD = "openepd_version"
"""Field name for the openEPD format version."""

OPENAPI_SCHEMA_SERVICE_PROPERTIES = ["ext_version", "ext"]
"""OpenAPI properties which should be moved to the bottom of specification if present. """


class OpenEpdDoctypes(StrEnum):
    """Enum of supported openEPD document types."""

    Epd = "openEPD"
    GenericEstimate = "openGenericEstimate"
    IndustryEpd = "openIndustryEpd"


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


class SerializingArgs(TypedDict):
    include: NotRequired[set[int] | set[str] | dict[int, Any] | dict[str, Any] | None]
    exclude: NotRequired[set[int] | set[str] | dict[int, Any] | dict[str, Any] | None]
    by_alias: NotRequired[bool]
    exclude_unset: NotRequired[bool]
    exclude_defaults: NotRequired[bool]
    exclude_none: NotRequired[bool]
    round_trip: NotRequired[bool]
    warnings: NotRequired[bool]


class BaseOpenEpdSchema(pydantic.BaseModel):
    """Base class for all OpenEPD models."""

    ext: dict[str, AnySerializable] | None = pydantic.Field(alias="ext", default=None)
    model_config: ClassVar[ConfigDict] = ConfigDict(
        validate_assignment=False,
        populate_by_name=True,
        use_enum_values=True,
    )

    def to_serializable(
        self, mode: Literal["json", "python"] | str = "json", **kwargs: Unpack[SerializingArgs]
    ) -> dict[str, Any]:
        """
        Return a serializable dict representation of the DTO.

        It expects the same arguments as the pydantic.BaseModel.model_dump_json() method.
        """
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("exclude_unset", True)
        kwargs.setdefault("by_alias", True)
        return self.model_dump(mode=mode, **kwargs)

    def to_json(self, indent: int = 0, **kwargs: Unpack[SerializingArgs]):
        """
        Return a JSON string representation of the DTO.

        It expects the same arguments as the pydantic.BaseModel.model_dump_json() method.
        """
        kwargs.setdefault("exclude_none", True)
        kwargs.setdefault("exclude_unset", True)
        kwargs.setdefault("by_alias", True)
        return self.model_dump_json(indent=indent, **kwargs)

    def to_dict(self, **kwargs: Unpack[SerializingArgs]) -> dict[str, Any]:
        """
        Return a dictionary representation of the DTO.

        The main difference with `to_serializable` is that it doesn't convert all native python types
        (e.g. datetime won't be converted into string) into JSON-compatible types.

        Method expects the same kwargs as the pydantic.BaseModel.model_dump() method.
        """
        return self.to_serializable(mode="python", **kwargs)

    def has_values(self, exclude_fields: set[str] | None = None) -> bool:
        """Return True if the model has any values."""
        if isinstance(self, RootDocument) and exclude_fields is None:
            exclude_fields = {"doctype", "openepd_version"}
        return len(self.model_dump(exclude_unset=True, exclude_none=True, exclude=exclude_fields)) > 0

    def revalidate(self, strict: bool | None = None) -> Self:
        """
        Re-run validation against current model and return a new validated instance.

        Note: This method returns a validated _COPY_ of the object.

        :param strict: If True, will raise an error if any field is missing or has an invalid value.
        """
        return self.model_validate(self.to_dict(), strict=strict)

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
        self,
        key: str,
        target_type: type[TAnySerializable],
        default: TAnySerializable | None = None,
    ) -> TAnySerializable:
        """
        Get an extension field from the model and convert it to the target type.

        :raise ValueError: if the value cannot be converted to the target type.
        """
        value = self.get_ext_field(key, default)
        if value is None:
            return None  # type: ignore
        if issubclass(target_type, pydantic.BaseModel) and isinstance(value, dict):
            return target_type.model_validate(value)  # type: ignore[return-value]
        elif isinstance(value, target_type):
            return value
        msg = f"Cannot convert {value} to {target_type}"
        raise ValueError(msg)

    def get_ext(self, ext_type: type["TOpenEpdExtension"]) -> Optional["TOpenEpdExtension"]:
        """Get an extension field from the model or None if it doesn't exist."""
        return self.get_typed_ext_field(ext_type.get_extension_name(), ext_type, None)

    def get_ext_or_empty(self, ext_type: type["TOpenEpdExtension"]) -> "TOpenEpdExtension":
        """Get an extension field from the model or an empty instance if it doesn't exist."""
        return self.get_typed_ext_field(ext_type.get_extension_name(), ext_type, ext_type.model_construct(**{}))  # type: ignore[return-value]

    @classmethod
    def is_allowed_field_name(cls, field_name: str) -> bool:
        """
        Return True if the field name is defined in the module.

        Both property name and aliases are checked.
        """
        if field_name in cls.model_fields:
            return True
        else:
            for x in cls.model_fields.values():
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


class BaseOpenEpdGenericSchema(BaseOpenEpdSchema):
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
TOpenEpdObjectClass = TypeVar("TOpenEpdObjectClass", bound=type[BaseOpenEpdSchema])


class RootDocument(abc.ABC, BaseOpenEpdSchema):
    """Base class for all objects representing openEPD root element. E.g. Epd, IndustryEpd, GenericEstimate, etc."""

    _FORMAT_VERSION: ClassVar[str]
    """Version of this document format. Must be defined in the concrete class."""

    doctype: str = pydantic.Field(
        description='Describes the type and schema of the document. Must always always read "openEPD".',
        default="openEPD",
    )
    openepd_version: str = pydantic.Field(
        description="Version of the document format, related to /doctype",
        default=OpenEpdVersions.get_current().as_str(),
    )

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        if not hasattr(self, "_FORMAT_VERSION"):
            msg = f"RootDocument subclass {self.__class__.__name__} must define _FORMAT_VERSION class variable."
            raise ValueError(msg)
        if "openepd_version" not in self.model_fields_set:
            self.openepd_version = self._FORMAT_VERSION
        self.doctype = self.__class__.model_fields["doctype"].default  # type: ignore[assignment]

    @pydantic.field_validator(OPENEPD_VERSION_FIELD)
    def version_format_validator(cls, value: str) -> str:
        """Validate the correctness of version format."""
        return validate_version_format(value)

    @pydantic.field_validator(OPENEPD_VERSION_FIELD)
    def version_major_match_validator(cls, value: str) -> str:
        """Validate that the version major matches the class version major."""
        return validate_version_compatibility("_FORMAT_VERSION")(cls, value)  # type: ignore[arg-type]


TRootDocument = TypeVar("TRootDocument", bound=RootDocument)


class BaseDocumentFactory(Generic[TRootDocument]):
    """
    Base class for document factories.

    Extend it to create a factory for a specific document type e.g. for industry epd, epd, etc.
    """

    DOCTYPE_CONSTRAINT: OpenEpdDoctypes
    VERSION_MAP: dict[Version, type[TRootDocument]] = {}

    @classmethod
    def from_dict(cls, data: dict) -> TRootDocument:
        """Create a document from a dictionary."""
        doctype: str | None = data.get("doctype")
        if doctype is None:
            msg = "Doctype not found in the data."
            raise ValueError(msg)
        if doctype.lower() != cls.DOCTYPE_CONSTRAINT.lower():
            msg = f"Document type {doctype} not supported. This factory supports {cls.DOCTYPE_CONSTRAINT} only."
            raise ValueError(msg)
        version = Version.parse_version(data.get(OPENEPD_VERSION_FIELD, ""))
        for x, doc_cls in cls.VERSION_MAP.items():
            if x.major == version.major:
                if version.minor <= x.minor:
                    return doc_cls.model_validate(data)
                else:
                    msg = (
                        f"Unsupported version: {version}. The highest supported version from branch {x.major}.x is {x}"
                    )
                    raise ValueError(msg)
        supported_versions = ", ".join(f"{v.major}.x" for v in cls.VERSION_MAP.keys())
        msg = f"Version {version} is not supported. Supported versions are: {supported_versions}"
        raise ValueError(msg)


class OpenXpdUUID(str):
    """
    An open xpd UUID format for IDs of openEPD documents.

    See https://github.com/cchangelabs/open-xpd-uuid-lib for details.
    """

    @classmethod
    def _validate_id(cls, value: Any, _: pydantic_core.core_schema.ValidatorFunctionWrapHandler) -> Any:
        if not isinstance(value, str | None):
            msg = f"Invalid value type: {type(value)}"
            raise ValueError(msg)

        try:
            open_xpd_uuid.validate(open_xpd_uuid.sanitize(str(value)))
            return value
        except open_xpd_uuid.GuidValidationError as e:
            msg = "Invalid format"
            raise ValueError(msg) from e

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: Any,
        handler: Callable[[Any], pydantic_core.core_schema.CoreSchema],
    ) -> pydantic_core.core_schema.CoreSchema:
        # In this example we assume that the underlying type to validate is a string.
        # If it's different, adjust the call to handler() accordingly.
        underlying_schema = handler(str)
        # Wrap the underlying schema with your custom validator.
        return pydantic_core.core_schema.no_info_wrap_validator_function(cls._validate_id, underlying_schema)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = handler(core_schema)
        json_schema.update(
            examples=["XC300001"],
        )
        return json_schema
