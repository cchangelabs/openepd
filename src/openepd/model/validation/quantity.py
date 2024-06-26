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
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Callable, ClassVar

from openepd.model.common import OpenEPDUnit

if TYPE_CHECKING:
    from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

    QuantityValidatorType = Callable[[type[BaseOpenEpdHierarchicalSpec], str], str]


class QuantityValidator(ABC):
    """
    Interface for quantity validator.

    The openEPD models are mapped using the simple types. Caller code should provide their own implementation of this
    and set it with `set_unit_validator` function.
    """

    @abstractmethod
    def validate_unit_correctness(self, value: str, dimensionality: str) -> None:
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

    @abstractmethod
    def validate_quantity_greater_or_equal(self, value: str, min_value: str) -> None:
        """
        Validate the quantity is greater than minimal value.

        Args:
            value: The value to validate, like "2.4 kg"
            min_value: The value to compare with, like "102.4 kg"
        Returns:
            None if the value is valid, raises an error otherwise.
        Raises:
            ValueError: If the value is not valid.
        """
        pass

    @abstractmethod
    def validate_quantity_less_or_equal(self, value: str, max_value: str) -> None:
        """
        Validate the quantity is less than minimal value.

        Args:
            value: The value to validate, like "2.4 kg"
            max_value: The value to compare with, like "0.4 kg"
        Returns:
            None if the value is valid, raises an error otherwise.
        Raises:
            ValueError: If the value is not valid.
        """
        pass


def validate_unit_factory(dimensionality: OpenEPDUnit | str) -> "QuantityValidatorType":
    """Create validator for quantity field to check unit matching."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_unit_correctness(value, dimensionality)
        return value

    return validator


def validate_quantity_ge_factory(min_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is greater than or equal to min_value."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_quantity_greater_or_equal(value, min_value)
        return value

    return validator


def validate_quantity_le_factory(max_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is less than or equal to max_value."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_quantity_less_or_equal(value, max_value)
        return value

    return validator


def validate_quantity_for_new_validator(max_value: str) -> Callable:
    """Create validator to check that quantity is less than or equal to max_value."""

    def validator(value: str) -> str:
        cls = BaseOpenEpdHierarchicalSpec
        if hasattr(cls, "_QUANTITY_VALIDATOR") and cls._QUANTITY_VALIDATOR is not None:
            cls._QUANTITY_VALIDATOR.validate_quantity_less_or_equal(value, max_value)
        return value

    return validator


# for arbitrary non-standard quantity
# todo these types should be replaced by Annotated[str, AfterValidator...] as we move completely to pydantic 2


class QuantityStr(str):
    """
    Quantity string type.

    Should be used in models where the physical value (quantity) is expected.

    Checks for dimensionality and for the fact that value is greater than zero.
    """

    unit: ClassVar[str]

    @classmethod
    def __get_validators__(cls):
        yield validate_unit_factory(cls.unit)
        yield validate_quantity_ge_factory(f"0 {cls.unit}")

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            example=f"1 {cls.unit}",
        )


class PressureMPaStr(QuantityStr):
    """Pressure quantity type."""

    unit = OpenEPDUnit.MPa


class MassKgStr(QuantityStr):
    """Mass quantity type."""

    unit = OpenEPDUnit.kg


class AreaM2Str(QuantityStr):
    """Area quantity type."""

    unit = OpenEPDUnit.m2


class LengthMStr(QuantityStr):
    """Length (m) quantity type."""

    unit = OpenEPDUnit.m


class LengthMmStr(QuantityStr):
    """Length (mm) quantity type."""

    unit = OpenEPDUnit.m

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            example="6 mm",
        )


class LengthInchStr(QuantityStr):
    """Length (inch) quantity type."""

    unit = OpenEPDUnit.m

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(
            example="2.5 inch",
        )


class TemperatureCStr(QuantityStr):
    """Temperature celsius quantity type."""

    unit = OpenEPDUnit.degree_c


class GwpKgCo2eStr(QuantityStr):
    """GWP intensity quantity type."""

    unit = OpenEPDUnit.kg_co2


class CapacityPerHourStr(QuantityStr):
    """Capacity per-hour quantity type."""

    unit = f"{OpenEPDUnit.hour}^-1"


class RValueStr(QuantityStr):
    """R-Value quantity type."""

    unit = "K * m2 / W"


class SpeedStr(QuantityStr):
    """Speed quantity type."""

    unit = "m / s"


class ColorTemperatureStr(QuantityStr):
    """Color temp quantity type."""

    unit = "K"


class LuminosityStr(QuantityStr):
    """Luminosity quantity type."""

    unit = "lumen"


class PowerStr(QuantityStr):
    """Power quantity type."""

    unit = "W"


class ElectricalCurrentStr(QuantityStr):
    """Current quantity type."""

    unit = "A"


class VolumeStr(QuantityStr):
    """Volume quantity type."""

    unit = "m3"


class AirflowStr(QuantityStr):
    """Air flow quantity type."""

    unit = "m3 / s"


class FlowRateStr(QuantityStr):
    """Liquid flow rate quantity type."""

    unit = "l / min"


class MassPerLengthStr(QuantityStr):
    """Mass per unit of length quantity type."""

    unit = "kg / m"


class AreaPerVolumeStr(QuantityStr):
    """Area per unit of volume quantity type."""

    unit = "m2 / l"
