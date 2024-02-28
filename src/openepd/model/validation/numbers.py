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
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Annotated

import pydantic as pyd

from openepd.model.common import OpenEPDUnit

if TYPE_CHECKING:
    from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

RatioFloat = Annotated[float, pyd.Field(ge=0, le=1, example=0.5)]
"""Float field which represents a percentage ratio between 0 and 1."""


class QuantityValidator(ABC):
    """
    Interface for quantity validator.

    The openEPD models are mapped using the simple types. Caller code should provide their own implementation of this
    and set it with `set_unit_validator` function.
    """

    @abstractmethod
    def validate(self, value: str, dimensionality: str) -> None:
        """
        Validate the given string value against the given dimensionality.

        Args:
            value: The value to validate, like "102.4 kg"
            dimensionality: The dimensionality to validate against, like "kg"
        Returns:
            None if the value is valid, raises an error otherwise.
        Raises:
            ValueError: If the value is not valid.
        """
        pass


def validate_unit_factory(dimensionality: OpenEPDUnit | str):
    """Create validator for unit field."""

    def validator(cls: "BaseOpenEpdHierarchicalSpec", value: str) -> str:
        if hasattr(cls, "_QUNATITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate(value, dimensionality)
        return value

    return validator
