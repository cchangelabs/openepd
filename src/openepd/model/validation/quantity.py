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
from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, ClassVar

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Amount, OpenEPDUnit, RangeAmount

if TYPE_CHECKING:
    QuantityValidatorType = Callable[[type, str], str]


class QuantityValidator(ABC):
    """
    Interface for quantity validator.

    The openEPD models are mapped using the simple types. Caller code should provide their own implementation of this
    and set it with `set_unit_validator` function.
    """

    @abstractmethod
    def validate_same_dimensionality(self, unit: str | None, dimensionality_unit: str | None) -> None:
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
    """Create validator for units (not quantities) to check for dimensionality."""

    def validator(cls: type | None, value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_same_dimensionality(value, dimensionality)
        return value

    return validator


def validate_quantity_unit_factory(dimensionality: OpenEPDUnit | str) -> "QuantityValidatorType":
    """Create validator for quantity field to check unit matching."""

    def validator(cls: type | None, value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_unit_correctness(value, dimensionality)
        return value

    return validator


def validate_quantity_ge_factory(min_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is greater than or equal to min_value."""

    def validator(cls: type | None, value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_quantity_greater_or_equal(value, min_value)
        return value

    return validator


def validate_quantity_le_factory(max_value: str) -> "QuantityValidatorType":
    """Create validator to check that quantity is less than or equal to max_value."""

    def validator(cls: type | None, value: str) -> str:
        if ExternalValidationConfig.QUANTITY_VALIDATOR is not None:
            ExternalValidationConfig.QUANTITY_VALIDATOR.validate_quantity_less_or_equal(value, max_value)
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
        unit = getattr(cls, "unit", None)
        if unit:
            yield validate_quantity_unit_factory(cls.unit)
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

    unit = "inch"

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


class ThermalConductivityStr(QuantityStr):
    """Thermal conductivity quantity type."""

    unit = "1 W / K / m"


class ThermalExpansionStr(QuantityStr):
    """Thermal conductivity quantity type."""

    unit = "1 / K"


class ForceNStr(QuantityStr):
    """Force (N) type."""

    unit = "1 N"


class YarnWeightStr(QuantityStr):
    """Yarn weight quantity type."""

    unit = "1 g / m2"


class UtilizationStr(QuantityStr):
    """Utilization quantity type."""

    unit = "1 h / yr"


class UFactorStr(QuantityStr):
    """Utilization quantity type."""

    unit = "1 USI"


class RFactorStr(QuantityStr):
    """R-Factor type."""

    unit = "1 RSI"


class WithDimensionalityMixin(BaseOpenEpdSchema):
    """Class for dimensionality-validated amounts."""

    dimensionality_unit: ClassVar[str | None] = None

    # Unit for dimensionality to validate against, for example "kg"

    @pyd.root_validator
    def check_dimensionality_matches(cls, values: dict[str, Any]) -> dict[str, Any]:
        """Check that this amount conforms to the same dimensionality as dimensionality_unit."""
        if not cls.dimensionality_unit:
            return values

        validate_unit_factory(cls.dimensionality_unit)(BaseOpenEpdSchema, values.get("unit"))  # type:ignore [arg-type]
        return values


class AmountRangeWithDimensionality(RangeAmount, WithDimensionalityMixin):
    """Mass amount, range."""

    class Config:
        """Pydantic config."""

        @staticmethod
        def schema_extra(schema: dict[str, Any], model: type["AmountRangeWithDimensionality"]) -> None:
            """Modify json schema."""
            schema["example"] = {"min": 1.2, "max": 3.4, "unit": str(model.dimensionality_unit) or None}


class WithMassKgMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = MassKgStr.unit


class AmountMass(Amount, WithMassKgMixin):
    """Amount of mass, measured in kg, t, etc."""

    pass


class AmountRangeMass(AmountRangeWithDimensionality, WithMassKgMixin):
    """Range of masses."""

    pass


class WithGwpMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = GwpKgCo2eStr.unit


class AmountGWP(Amount, WithGwpMixin):
    """Amount of Global Warming Potential, measured in kgCO2e."""

    pass


class AmountRangeGWP(AmountRangeWithDimensionality, WithGwpMixin):
    """Range of masses."""

    pass


class WithLengthMMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    pass


class AmountRangeLengthM(AmountRangeWithDimensionality, WithLengthMMixin):
    """Range of lengths (m)."""

    pass


class AmountLengthM(Amount, WithLengthMMixin):
    """Length (m)."""

    pass


class WithLengthMmMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = LengthMmStr.unit


class AmountLengthMm(Amount, WithLengthMMixin):
    """Length (mm)."""

    pass


class AmountRangeLengthMm(AmountRangeWithDimensionality, WithLengthMmMixin):
    """Range of lengths (mm)."""

    pass


class WithPressureMpaMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = PressureMPaStr.unit


class AmountPressureMpa(Amount, WithPressureMpaMixin):
    """Pressure (MPa)."""

    pass


class AmountRangePressureMpa(AmountRangeWithDimensionality, WithPressureMpaMixin):
    """Range of lengths (mm)."""

    pass


class WithAreaM2Mixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = AreaM2Str.unit


class AmountAreaM2(Amount, WithAreaM2Mixin):
    """Area (m2)."""

    pass


class AmountRangeAreaM2(AmountRangeWithDimensionality, WithAreaM2Mixin):
    """Range of Area (m2)."""

    pass


class WithLengthInchStr(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = LengthInchStr.unit


class AmountLengthInch(Amount, WithLengthInchStr):
    """Length (inch)."""

    pass


class AmountRangeLengthInch(AmountRangeWithDimensionality, WithLengthInchStr):
    """Range of Length (inch)."""

    pass


class WithTemperatureCMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = TemperatureCStr.unit


class AmountTemperatureC(Amount, WithTemperatureCMixin):
    """Temperature (degrees C)."""

    pass


class AmountRangeTemperatureC(AmountRangeWithDimensionality, WithTemperatureCMixin):
    """Range of Temperature (degrees C)."""

    pass


class WithCapacityPerHourMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = CapacityPerHourStr.unit


class AmountCapacityPerHour(Amount, WithCapacityPerHourMixin):
    """Capacity per hour."""

    pass


class AmountRangeCapacityPerHour(AmountRangeWithDimensionality, WithCapacityPerHourMixin):
    """Capacity per hour range."""

    pass


class WithRValueMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = RValueStr.unit


class AmountRValue(Amount, WithRValueMixin):
    """R-Value."""

    pass


class AmountRangeRValue(AmountRangeWithDimensionality, WithRValueMixin):
    """R-Value range."""

    pass


class WithSpeedMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = SpeedStr.unit


class AmountSpeed(Amount, WithSpeedMixin):
    """Speed."""

    pass


class AmountRangeSpeed(AmountRangeWithDimensionality, WithSpeedMixin):
    """Speed range."""

    pass


class WithColorTemperatureMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = ColorTemperatureStr.unit


class AmountColorTemperature(Amount, WithColorTemperatureMixin):
    """Color temperature."""

    pass


class AmountRangeColorTemperature(AmountRangeWithDimensionality, WithColorTemperatureMixin):
    """Color temperature range."""

    pass


class WithLuminosityMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = LuminosityStr.unit


class AmountLuminosity(Amount, WithLuminosityMixin):
    """Luminosity."""

    pass


class AmountRangeLuminosity(AmountRangeWithDimensionality, WithLuminosityMixin):
    """Luminosity range."""

    pass


class WithPowerMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = PowerStr.unit


class AmountPower(Amount, WithPowerMixin):
    """Power."""

    pass


class AmountRangePower(AmountRangeWithDimensionality, WithPowerMixin):
    """Power range."""

    pass


class WithElectricalCurrentMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = ElectricalCurrentStr.unit


class AmountElectricalCurrent(Amount, WithElectricalCurrentMixin):
    """Current."""

    pass


class AmountRangeElectricalCurrent(AmountRangeWithDimensionality, WithElectricalCurrentMixin):
    """Current range."""

    pass


class WithVolumeMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = VolumeStr.unit


class AmountVolume(Amount, WithVolumeMixin):
    """Volume."""

    pass


class AmountRangeVolume(AmountRangeWithDimensionality, WithVolumeMixin):
    """Volume range."""

    pass


class WithAirflowMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = AirflowStr.unit


class AmountAirflow(Amount, WithAirflowMixin):
    """Airflow."""

    pass


class AmountRangeAirflow(AmountRangeWithDimensionality, WithAirflowMixin):
    """Airflow range."""

    pass


class WithFlowRateMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = FlowRateStr.unit


class AmountFlowRate(Amount, WithFlowRateMixin):
    """Flow Rate."""

    pass


class AmountRangeFlowRate(AmountRangeWithDimensionality, WithFlowRateMixin):
    """Flow Rate range."""

    pass


class WithMassPerLengthMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = MassPerLengthStr.unit


class AmountMassPerLength(Amount, WithFlowRateMixin):
    """Mass per length."""

    pass


class AmountRangeMassPerLength(AmountRangeWithDimensionality, WithFlowRateMixin):
    """Mass per length range."""

    pass


class WithAreaPerVolumeMixin(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = AreaPerVolumeStr.unit


class AmountAreaPerVolume(Amount, WithFlowRateMixin):
    """Area per volume."""

    pass


class AmountRangeAreaPerVolume(AmountRangeWithDimensionality, WithFlowRateMixin):
    """Area per volume range."""

    pass


class WithThermalConductivity(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = ThermalConductivityStr.unit


class AmountThermalConductivityMixin(Amount, WithThermalConductivity):
    """Area per volume."""

    pass


class AmountRangeThermalConductivity(AmountRangeWithDimensionality, WithThermalConductivity):
    """Area per volume range."""

    pass


class WithForce(WithDimensionalityMixin):
    """
    Unit validation mixin.

    May the Force be with you.
    """

    dimensionality_unit = ForceNStr.unit


class AmountForce(Amount, WithForce):
    """Area per volume."""

    pass


class AmountRangeForce(AmountRangeWithDimensionality, WithForce):
    """Area per volume range."""

    pass


class WithYarnWeight(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = YarnWeightStr.unit


class AmountYarnWeight(Amount, WithYarnWeight):
    """Yarn weight."""

    pass


class AmountRangeYarnWeight(AmountRangeWithDimensionality, WithYarnWeight):
    """Yarn weight range."""

    pass


class WithThermalExpansion(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = ThermalExpansionStr.unit


class AmountThermalExpansion(Amount, WithThermalExpansion):
    """Yarn weight."""

    pass


class AmountRangeThermalExpansion(AmountRangeWithDimensionality, WithThermalExpansion):
    """Yarn weight range."""

    pass


class WithUtilization(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = UtilizationStr.unit


class AmountUtilization(Amount, WithUtilization):
    """Utilization."""

    pass


class AmountRangeUtilization(AmountRangeWithDimensionality, WithUtilization):
    """Utilization range."""

    pass


class WithUFactor(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = UFactorStr.unit


class AmountUFactor(Amount, WithUFactor):
    """U-Factor."""

    pass


class AmountRangeUFactor(AmountRangeWithDimensionality, WithUFactor):
    """U-Factor range."""

    pass


class WithRFactor(WithDimensionalityMixin):
    """Unit validation mixin."""

    dimensionality_unit = RFactorStr.unit


class AmountRFactor(Amount, WithRFactor):
    """R-Factor."""

    pass


class AmountRangeRFactor(AmountRangeWithDimensionality, WithRFactor):
    """R-Factor range."""

    pass


# known range amounts
SUPPORTED_RANGE_TYPES: tuple[type[AmountRangeWithDimensionality], ...] = (
    AmountRangeMass,
    AmountRangeGWP,
    AmountRangeLengthM,
    AmountRangeLengthMm,
    AmountRangePressureMpa,
    AmountRangeAreaM2,
    AmountRangeLengthInch,
    AmountRangeTemperatureC,
    AmountRangeCapacityPerHour,
    AmountRangeRValue,
    AmountRangeSpeed,
    AmountRangeColorTemperature,
    AmountRangeLuminosity,
    AmountRangePower,
    AmountRangeElectricalCurrent,
    AmountRangeVolume,
    AmountRangeAirflow,
    AmountRangeFlowRate,
    AmountRangeMassPerLength,
    AmountRangeAreaPerVolume,
    AmountRangeThermalConductivity,
    AmountRangeForce,
    AmountRangeYarnWeight,
    AmountRangeThermalExpansion,
    AmountRangeUtilization,
    AmountRangeUFactor,
    AmountRangeRFactor,
)

# known range amount mapping by unit
SUPPORTED_RANGES_BY_UNIT: dict[str, type[AmountRangeWithDimensionality]] = {
    str(t.dimensionality_unit): t for t in SUPPORTED_RANGE_TYPES
}
