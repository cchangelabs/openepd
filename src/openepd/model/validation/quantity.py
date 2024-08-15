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
from typing import TYPE_CHECKING, Any, Callable, ClassVar

from openepd.compat.pydantic import pyd
from openepd.model.common import Amount, OpenEPDUnit

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
    def validate_same_dimensionality(self, unit: str | None, dimensionality_unit: str) -> None:
        """
        Validate that a given unit ('kg') has the same dimesnionality as provided dimensionality_unit ('g').

        :param unit: unit to validate, not quantity
        :param dimensionality_unit: unit to check against
        :raise:
            ValueError if dimensionality is different
        :return: None
        """
        pass

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


class ExternalValidationConfig:
    """
    Configuration holder for external validator.

    Since openEPD library does not provide any facility for working with quantities/units, users should do this
    by implementing the protocol for this validator and setting it with setup_external_validators function.
    """

    QUANTITY_VALIDATOR: ClassVar[QuantityValidator | None] = None


def validate_unit_factory(dimensionality: OpenEPDUnit | str) -> "QuantityValidatorType":
    """Create validator for quantity field to check unit matching."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_unit_correctness(value, dimensionality)
        return value

    return validator


def validate_quantity_ge_factory(min_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is greater than or equal to min_value."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_quantity_greater_or_equal(value, min_value)
        return value

    return validator


def validate_quantity_le_factory(max_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is less than or equal to max_value."""

    def validator(cls: "type[BaseOpenEpdHierarchicalSpec]", value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_quantity_less_or_equal(value, max_value)
        return value

    return validator


def validate_quantity_for_new_validator(max_value: str) -> Callable:
    """Create validator to check that quantity is less than or equal to max_value."""

    def validator(value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_quantity_less_or_equal(value, max_value)
        return value

    return validator


# for arbitrary non-standard quantity
# todo these types should be replaced by Annotated[str, AfterValidator...] as we move completely to pydantic 2


class AmountWithDimensionality(Amount, ABC):
    """Class for dimensionality-validated amounts."""

    dimensionality_unit: ClassVar[str | None] = None

    # Unit for dimensionality to validate against, for example "kg"

    @pyd.root_validator
    def check_dimensionality_matches(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Check that this amount conforms to the same dimensionality as dimensionality_unit."""
        if not cls.dimensionality_unit:
            return values

        from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

        str_repr = f"{values['qty']} {values['unit']}"
        validate_unit_factory(cls.dimensionality_unit)(BaseOpenEpdHierarchicalSpec, str_repr)
        return values


class AmountMass(AmountWithDimensionality):
    """Amount of mass, measured in kg, t, etc."""

    dimensionality_unit = OpenEPDUnit.kg


class AmountGWP(AmountWithDimensionality):
    """Amount of Global Warming Potential, measured in kgCO2e."""

    dimensionality_unit = OpenEPDUnit.kg_co2


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
