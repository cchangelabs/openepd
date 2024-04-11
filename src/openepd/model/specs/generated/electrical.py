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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import CableTraysMaterial, EnergySource, RacewaysMaterial
from openepd.model.validation.quantity import (
    LengthMmStr,
    LengthMStr,
    MassKgStr,
    TemperatureCStr,
    validate_quantity_ge_factory,
    validate_quantity_le_factory,
    validate_unit_factory,
)


class LowVoltBusesV1(BaseOpenEpdHierarchicalSpec):
    """Low volt buses performance specification."""

    _EXT_VERSION = "1.0"


class MedVoltBusesV1(BaseOpenEpdHierarchicalSpec):
    """Med volt buses performance specification."""

    _EXT_VERSION = "1.0"


class BatteriesV1(BaseOpenEpdHierarchicalSpec):
    """Batteries performance specification."""

    _EXT_VERSION = "1.0"


class OtherElectricalPowerStorageV1(BaseOpenEpdHierarchicalSpec):
    """Other electrical power storage performance specification."""

    _EXT_VERSION = "1.0"


class CableTraysV1(BaseOpenEpdHierarchicalSpec):
    """Cable trays performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    height: LengthMmStr | None = pyd.Field(default=None, description="", example="100 mm")
    width: LengthMmStr | None = pyd.Field(default=None, description="", example="100 mm")
    depth: LengthMmStr | None = pyd.Field(default=None, description="", example="100 mm")
    static_load: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    ventilated: bool | None = pyd.Field(
        default=None, description="At least 40% of the tray base is open to air flow", example=True
    )
    cable_trays_material: CableTraysMaterial | None = pyd.Field(default=None, description="", example="Stainless Steel")

    _height_is_quantity_validator = pyd.validator("height", allow_reuse=True)(validate_unit_factory("m"))
    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))
    _depth_is_quantity_validator = pyd.validator("depth", allow_reuse=True)(validate_unit_factory("m"))
    _static_load_is_quantity_validator = pyd.validator("static_load", allow_reuse=True)(validate_unit_factory("kg"))


class ElectricalBusesV1(BaseOpenEpdHierarchicalSpec):
    """Electrical buses performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    LowVoltBuses: LowVoltBusesV1 | None = None
    MedVoltBuses: MedVoltBusesV1 | None = None


class FloorEquipmentBoxesV1(BaseOpenEpdHierarchicalSpec):
    """Floor equipment boxes performance specification."""

    _EXT_VERSION = "1.0"


class PowerDistributionUnitsV1(BaseOpenEpdHierarchicalSpec):
    """Power distribution units performance specification."""

    _EXT_VERSION = "1.0"


class RacewaysV1(BaseOpenEpdHierarchicalSpec):
    """Raceways performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    width: LengthMStr | None = pyd.Field(default=None, description="", example="100 mm")
    depth: LengthMStr | None = pyd.Field(default=None, description="", example="100 mm")
    painted: bool | None = pyd.Field(default=None, description="", example=True)
    divided: bool | None = pyd.Field(default=None, description="", example=True)
    raceways_material: RacewaysMaterial | None = pyd.Field(default=None, description="", example="Aluminum")

    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))
    _depth_is_quantity_validator = pyd.validator("depth", allow_reuse=True)(validate_unit_factory("m"))


class FueledElectricalGeneratorsV1(BaseOpenEpdHierarchicalSpec):
    """Fueled electrical generators performance specification."""

    _EXT_VERSION = "1.0"


class OtherGenerationV1(BaseOpenEpdHierarchicalSpec):
    """Other generation performance specification."""

    _EXT_VERSION = "1.0"


class PhotovoltaicsV1(BaseOpenEpdHierarchicalSpec):
    """Photovoltaics performance specification."""

    _EXT_VERSION = "1.0"


class WindTurbinesV1(BaseOpenEpdHierarchicalSpec):
    """Wind turbines performance specification."""

    _EXT_VERSION = "1.0"


class ElectricityFromPowerGridV1(BaseOpenEpdHierarchicalSpec):
    """Electricity from power grid performance specification."""

    _EXT_VERSION = "1.0"


class ElectricityFromSpecificGeneratorV1(BaseOpenEpdHierarchicalSpec):
    """Electricity from specific generator performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    energy_source: EnergySource | None = pyd.Field(default=None, description="", example="Grid")


class PowerPurchaseAgreementsV1(BaseOpenEpdHierarchicalSpec):
    """Power purchase agreements performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    energy_source: EnergySource | None = pyd.Field(default=None, description="", example="Grid")


class LightbulbsV1(BaseOpenEpdHierarchicalSpec):
    """Lightbulbs performance specification."""

    _EXT_VERSION = "1.0"


class LightingControlsV1(BaseOpenEpdHierarchicalSpec):
    """Lighting controls performance specification."""

    _EXT_VERSION = "1.0"


class LightingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Lighting fixtures performance specification."""

    _EXT_VERSION = "1.0"


class OutdoorLightingV1(BaseOpenEpdHierarchicalSpec):
    """Outdoor lighting performance specification."""

    _EXT_VERSION = "1.0"


class SpecialtyLightingV1(BaseOpenEpdHierarchicalSpec):
    """Specialty lighting performance specification."""

    _EXT_VERSION = "1.0"


class TaskLightingV1(BaseOpenEpdHierarchicalSpec):
    """Task lighting performance specification."""

    _EXT_VERSION = "1.0"


class ElectricalPowerStorageV1(BaseOpenEpdHierarchicalSpec):
    """Electrical power storage performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Batteries: BatteriesV1 | None = None
    OtherElectricalPowerStorage: OtherElectricalPowerStorageV1 | None = None


class LowVoltageElectricalDistributionV1(BaseOpenEpdHierarchicalSpec):
    """Low voltage electrical distribution performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    CableTrays: CableTraysV1 | None = None
    ElectricalBuses: ElectricalBusesV1 | None = None
    FloorEquipmentBoxes: FloorEquipmentBoxesV1 | None = None
    PowerDistributionUnits: PowerDistributionUnitsV1 | None = None
    Raceways: RacewaysV1 | None = None


class ElectricalGenerationEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Electrical generation equipment performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    FueledElectricalGenerators: FueledElectricalGeneratorsV1 | None = None
    OtherGeneration: OtherGenerationV1 | None = None
    Photovoltaics: PhotovoltaicsV1 | None = None
    WindTurbines: WindTurbinesV1 | None = None


class ElectricPowerV1(BaseOpenEpdHierarchicalSpec):
    """Electric power performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ElectricityFromPowerGrid: ElectricityFromPowerGridV1 | None = None
    ElectricityFromSpecificGenerator: ElectricityFromSpecificGeneratorV1 | None = None
    PowerPurchaseAgreements: PowerPurchaseAgreementsV1 | None = None


class LightingV1(BaseOpenEpdHierarchicalSpec):
    """Lighting performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    color_temperature: TemperatureCStr | None = pyd.Field(default=None, description="", example="1 K")
    typical_utilization: str | None = pyd.Field(default=None, description="", example="1 h / yr")
    luminosity: str | None = pyd.Field(default=None, description="", example="1 lumen")
    wattage: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    color_rendering_index: float | None = pyd.Field(default=None, description="", example=2.3)
    dimmable: bool | None = pyd.Field(default=None, description="", example=True)

    _color_temperature_quantity_ge_validator = pyd.validator("color_temperature", allow_reuse=True)(
        validate_quantity_ge_factory("1E+03 K")
    )
    _color_temperature_quantity_le_validator = pyd.validator("color_temperature", allow_reuse=True)(
        validate_quantity_le_factory("1E+04 K")
    )
    _typical_utilization_quantity_ge_validator = pyd.validator("typical_utilization", allow_reuse=True)(
        validate_quantity_ge_factory("25 h / yr")
    )
    _luminosity_quantity_ge_validator = pyd.validator("luminosity", allow_reuse=True)(
        validate_quantity_ge_factory("450 lumen")
    )
    _luminosity_quantity_le_validator = pyd.validator("luminosity", allow_reuse=True)(
        validate_quantity_le_factory("2.6E+03 lumen")
    )
    _wattage_quantity_ge_validator = pyd.validator("wattage", allow_reuse=True)(validate_quantity_ge_factory("5 W"))
    _wattage_quantity_le_validator = pyd.validator("wattage", allow_reuse=True)(validate_quantity_le_factory("100 W"))

    # Nested specs:
    Lightbulbs: LightbulbsV1 | None = None
    LightingControls: LightingControlsV1 | None = None
    LightingFixtures: LightingFixturesV1 | None = None
    OutdoorLighting: OutdoorLightingV1 | None = None
    SpecialtyLighting: SpecialtyLightingV1 | None = None
    TaskLighting: TaskLightingV1 | None = None


class ElectricalV1(BaseOpenEpdHierarchicalSpec):
    """Electrical performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ElectricalPowerStorage: ElectricalPowerStorageV1 | None = None
    LowVoltageElectricalDistribution: LowVoltageElectricalDistributionV1 | None = None
    ElectricalGenerationEquipment: ElectricalGenerationEquipmentV1 | None = None
    ElectricPower: ElectricPowerV1 | None = None
    Lighting: LightingV1 | None = None
