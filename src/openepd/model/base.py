#
#  Copyright 2023 by C Change Labs Inc. www.c-change-labs.com
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
import abc
from typing import Any, Optional, Type, TypeVar

import pydantic

AnySerializable = int | str | bool | float | list | dict | pydantic.BaseModel | None
TAnySerializable = TypeVar("TAnySerializable", bound=AnySerializable)


class BaseOpenEpdSchema(pydantic.BaseModel):
    """Base class for all OpenEPD models."""

    model_config = pydantic.ConfigDict(validate_assignment=False, populate_by_name=True, use_enum_values=True)

    ext: dict[str, AnySerializable] | None = pydantic.Field(alias="ext", default=None)

    def to_serializable(self, *args, **kwargs) -> dict[str, Any]:
        """
        Return a serializable dict representation of the DTO.

        It expects the same arguments as the pydantic.BaseModel.json() method.
        """
        return self.model_dump(mode="json", *args, **kwargs)

    def has_values(self) -> bool:
        """Return True if the model has any values."""
        return len(self.model_dump(mode="python", exclude_unset=True, exclude_none=True)) > 0

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
        if issubclass(target_type, pydantic.BaseModel) and isinstance(value, dict):
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


class BaseOpenEpdSpec(BaseOpenEpdSchema):
    """Base class for all OpenEPD specs."""

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
