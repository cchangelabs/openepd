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
import pydantic
from pydantic.generics import GenericModel

AnySerializable = int | str | bool | float | list | dict | pydantic.BaseModel | None


class BaseOpenEpdSchema(pydantic.BaseModel):
    """Base class for all OpenEPD models."""

    ext: dict[str, AnySerializable] | None = pydantic.Field(alias="ext", default=None)

    class Config:
        allow_mutation = True
        validate_assignment = False
        allow_population_by_field_name = True
        use_enum_values = True

    def has_values(self) -> bool:
        """Return True if the model has any values."""
        return len(self.dict(exclude_unset=True, exclude_none=True)) > 0

    def set_ext_field(self, key: str, value: AnySerializable) -> None:
        """Add an extension field to the model."""
        if self.ext is None:
            self.ext = {}
        self.ext[key] = value

    def get_ext_field(self, key: str, default: AnySerializable = None) -> AnySerializable | None:
        """Get an extension field from the model."""
        if self.ext is None:
            return default
        return self.ext.get(key, default)

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


class BaseOpenEpdGenericSchema(GenericModel, BaseOpenEpdSchema):
    """Base class for all OpenEPD generic models."""

    pass


class BaseOpenEpdSpec(BaseOpenEpdSchema):
    """Base class for all OpenEPD specs."""

    pass
