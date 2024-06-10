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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import CableTraysMaterial, EnergySource, RacewaysMaterial
from openepd.model.validation.quantity import (
    ColorTemperatureStr,
    LengthMmStr,
    LengthMStr,
    LuminosityStr,
    MassKgStr,
    PowerStr,
    validate_quantity_ge_factory,
    validate_quantity_le_factory,
    validate_unit_factory,
)


class LowVoltBusesV1(BaseOpenEpdHierarchicalSpec):
    """Busbars and Busways of 600V or less."""

    _EXT_VERSION = "1.0"


class MedVoltBusesV1(BaseOpenEpdHierarchicalSpec):
    """Busbars and Busways over 600V."""

    _EXT_VERSION = "1.0"


class BatteriesV1(BaseOpenEpdHierarchicalSpec):
    """Battery equipment, including central batteries, battery charging, and UPS."""

    _EXT_VERSION = "1.0"


class OtherElectricalPowerStorageV1(BaseOpenEpdHierarchicalSpec):
    """Other electrical power storage performance specification."""

    _EXT_VERSION = "1.0"


class CableTraysV1(BaseOpenEpdHierarchicalSpec):
    """Mechanical support for electrial or communications cabling, typically suspended from a roof or wall."""

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


class ElectricalBusesV1(BaseOpenEpdHierarchicalSpec):
    """
    Power distribution, in the form of busbars or of insulted ducts made of copper or aluminum busbars.

    It is an alternative means of conducting electricity compared toto power cables or cable bus. Also called
    bus ducts.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    LowVoltBuses: LowVoltBusesV1 | None = None
    MedVoltBuses: MedVoltBusesV1 | None = None


class FloorEquipmentBoxesV1(BaseOpenEpdHierarchicalSpec):
    """Equipment boxes for power or electronic equipment embedded in an accessible floor."""

    _EXT_VERSION = "1.0"


class PowerDistributionUnitsV1(BaseOpenEpdHierarchicalSpec):
    """Switched electrical distribution units placed very close to the point of consumption, for example inside a rack of electronic equipment."""

    _EXT_VERSION = "1.0"


class RacewaysV1(BaseOpenEpdHierarchicalSpec):
    """Mechanical guideways for eletrical communications cabling, typically embedded in an accessible floor."""

    _EXT_VERSION = "1.0"

    # Own fields:
    width: LengthMStr | None = pyd.Field(default=None, description="", example="100 mm")
    depth: LengthMStr | None = pyd.Field(default=None, description="", example="100 mm")
    painted: bool | None = pyd.Field(default=None, description="", example=True)
    divided: bool | None = pyd.Field(default=None, description="", example=True)
    raceways_material: RacewaysMaterial | None = pyd.Field(default=None, description="", example="Aluminum")


class FueledElectricalGeneratorsV1(BaseOpenEpdHierarchicalSpec):
    """Fueled electrical generators."""

    _EXT_VERSION = "1.0"


class OtherGenerationV1(BaseOpenEpdHierarchicalSpec):
    """Other generation."""

    _EXT_VERSION = "1.0"


class PhotovoltaicsV1(BaseOpenEpdHierarchicalSpec):
    """Solar photovoltaics, rated on a nameplate capacity basis."""

    _EXT_VERSION = "1.0"


class WindTurbinesV1(BaseOpenEpdHierarchicalSpec):
    """Wind generators, rated on a nameplate capacity basis."""

    _EXT_VERSION = "1.0"


class ElectricityFromPowerGridV1(BaseOpenEpdHierarchicalSpec):
    """Electrical energy drawn from a specific utility grid."""

    _EXT_VERSION = "1.0"


class ElectricityFromSpecificGeneratorV1(BaseOpenEpdHierarchicalSpec):
    """Electrical energy from a specific power plant, such as a wind farm using a specific type of turbine."""

    _EXT_VERSION = "1.0"

    # Own fields:
    energy_source: EnergySource | None = pyd.Field(default=None, description="", example="Grid")


class PowerPurchaseAgreementsV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical energy subject to a verified power purchase agreement.

    The impact of electricity generation is allocated specifically to the agreement and not to the general grid.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    energy_source: EnergySource | None = pyd.Field(default=None, description="", example="Grid")


class LightbulbsV1(BaseOpenEpdHierarchicalSpec):
    """Various types of light bulbs, including LED, CFL, halogen, and incandescent."""

    _EXT_VERSION = "1.0"


class LightingControlsV1(BaseOpenEpdHierarchicalSpec):
    """Devices used to control the operation of lighting, including dimmers, sensors, and smart controls."""

    _EXT_VERSION = "1.0"


class LightingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Permanent lighting fixtures for interior spaces, including ceiling, wall-mounted, and pendant fixtures."""

    _EXT_VERSION = "1.0"


class OutdoorLightingV1(BaseOpenEpdHierarchicalSpec):
    """Lighting products designed for outdoor use, including landscape and security lighting."""

    _EXT_VERSION = "1.0"


class SpecialtyLightingV1(BaseOpenEpdHierarchicalSpec):
    """Specialized lighting for niche applications like emergency, medical, or theatrical lighting."""

    _EXT_VERSION = "1.0"


class TaskLightingV1(BaseOpenEpdHierarchicalSpec):
    """Lighting designed for specific tasks such as desk lamps, under-cabinet lighting, and reading lamps."""

    _EXT_VERSION = "1.0"


class ElectricalPowerStorageV1(BaseOpenEpdHierarchicalSpec):
    """Electrical Power Storage."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Batteries: BatteriesV1 | None = None
    OtherElectricalPowerStorage: OtherElectricalPowerStorageV1 | None = None


class LowVoltageElectricalDistributionV1(BaseOpenEpdHierarchicalSpec):
    """Low Voltage Electrical Distribution."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    CableTrays: CableTraysV1 | None = None
    ElectricalBuses: ElectricalBusesV1 | None = None
    FloorEquipmentBoxes: FloorEquipmentBoxesV1 | None = None
    PowerDistributionUnits: PowerDistributionUnitsV1 | None = None
    Raceways: RacewaysV1 | None = None


class ElectricalGenerationEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for generating electrical power.

    This category is primarily for smaller-scale. (e.g. on premises) generation, rather than utility-scale equipment.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    FueledElectricalGenerators: FueledElectricalGeneratorsV1 | None = None
    OtherGeneration: OtherGenerationV1 | None = None
    Photovoltaics: PhotovoltaicsV1 | None = None
    WindTurbines: WindTurbinesV1 | None = None


class ElectricPowerV1(BaseOpenEpdHierarchicalSpec):
    """Electrical energy drawn from a utility grid."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ElectricityFromPowerGrid: ElectricityFromPowerGridV1 | None = None
    ElectricityFromSpecificGenerator: ElectricityFromSpecificGeneratorV1 | None = None
    PowerPurchaseAgreements: PowerPurchaseAgreementsV1 | None = None


class LightingV1(BaseOpenEpdHierarchicalSpec):
    """Lamps and lightbulbs and lamp components."""

    _EXT_VERSION = "1.0"

    # Own fields:
    color_temperature: ColorTemperatureStr | None = pyd.Field(default=None, description="", example="1 K")
    typical_utilization: str | None = pyd.Field(default=None, description="", example="1 h / yr")
    luminosity: LuminosityStr | None = pyd.Field(default=None, description="", example="1 lumen")
    wattage: PowerStr | None = pyd.Field(default=None, description="")
    color_rendering_index: float | None = pyd.Field(default=None, description="", example=2.3)
    dimmable: bool | None = pyd.Field(default=None, description="", example=True)

    _color_temperature_quantity_ge_validator = pyd.validator("color_temperature", allow_reuse=True)(
        validate_quantity_ge_factory("1E+03 K")
    )
    _color_temperature_quantity_le_validator = pyd.validator("color_temperature", allow_reuse=True)(
        validate_quantity_le_factory("1E+04 K")
    )
    _typical_utilization_unit_validator = pyd.validator("typical_utilization", allow_reuse=True)(
        validate_unit_factory("h / yr")
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
    """Electric power and equipment."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ElectricalPowerStorage: ElectricalPowerStorageV1 | None = None
    LowVoltageElectricalDistribution: LowVoltageElectricalDistributionV1 | None = None
    ElectricalGenerationEquipment: ElectricalGenerationEquipmentV1 | None = None
    ElectricPower: ElectricPowerV1 | None = None
    Lighting: LightingV1 | None = None
