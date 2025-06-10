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
__all__ = (
    "BatteriesRangeV1",
    "CableTraysRangeV1",
    "ElectricPowerRangeV1",
    "ElectricalBusesRangeV1",
    "ElectricalConduitRangeV1",
    "ElectricalGenerationEquipmentRangeV1",
    "ElectricalPowerStorageRangeV1",
    "ElectricalRangeV1",
    "ElectricityFromPowerGridRangeV1",
    "ElectricityFromSpecificGeneratorRangeV1",
    "FloorEquipmentBoxesRangeV1",
    "FueledElectricalGeneratorsRangeV1",
    "LightbulbsRangeV1",
    "LightingControlsRangeV1",
    "LightingFixturesRangeV1",
    "LightingRangeV1",
    "LowVoltBusesRangeV1",
    "LowVoltageElectricalDistributionRangeV1",
    "MedVoltBusesRangeV1",
    "OtherElectricalPowerStorageRangeV1",
    "OtherGenerationRangeV1",
    "OutdoorLightingRangeV1",
    "PhotovoltaicsRangeV1",
    "PowerDistributionUnitsRangeV1",
    "PowerPurchaseAgreementsRangeV1",
    "RacewaysRangeV1",
    "SpecialtyLightingRangeV1",
    "TaskLightingRangeV1",
    "WindTurbinesRangeV1",
)

import pydantic

from openepd.model.common import RangeFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CableTraysMaterial, ConduitMaterial, EnergySource, RacewaysMaterial
from openepd.model.validation.quantity import (
    AmountRangeColorTemperature,
    AmountRangeLengthMm,
    AmountRangeLuminosity,
    AmountRangeMass,
    AmountRangePower,
    AmountRangeUtilization,
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class LowVoltBusesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Busbars and Busways of 600V or less.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MedVoltBusesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Busbars and Busways over 600V.

    Range version.
    """

    _EXT_VERSION = "1.0"


class BatteriesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Battery equipment, including central batteries, battery charging, and UPS.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherElectricalPowerStorageRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other electrical power storage performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CableTraysRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Mechanical support for electrial or communications cabling, typically suspended from a roof or wall.

    Range version.
    """

    _EXT_VERSION = "1.0"

    height: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    width: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    depth: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    static_load: AmountRangeMass | None = pydantic.Field(default=None, description="")
    ventilated: bool | None = pydantic.Field(
        default=None, description="At least 40% of the tray base is open to air flow"
    )
    cable_trays_material: list[CableTraysMaterial] | None = pydantic.Field(default=None, description="")


class ElectricalBusesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Power distribution, in the form of busbars or of insulted ducts made of copper or aluminum busbars.

    It is an alternative means of conducting electricity compared toto power cables or cable bus. Also called
    bus ducts.

    Range version.
    """

    _EXT_VERSION = "1.0"

    LowVoltBuses: LowVoltBusesRangeV1 | None = None
    MedVoltBuses: MedVoltBusesRangeV1 | None = None


class FloorEquipmentBoxesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment boxes for power or electronic equipment embedded in an accessible floor.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PowerDistributionUnitsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Switched electrical distribution units placed very close to the point of consumption, for example inside a rack of electronic equipment.

    Range version.
    """

    _EXT_VERSION = "1.0"


class RacewaysRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Mechanical guideways for eletrical communications cabling, typically embedded in an accessible floor.

    Range version.
    """

    _EXT_VERSION = "1.0"

    width: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    depth: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    painted: bool | None = pydantic.Field(default=None, description="")
    divided: bool | None = pydantic.Field(default=None, description="")
    raceways_material: list[RacewaysMaterial] | None = pydantic.Field(default=None, description="")


class FueledElectricalGeneratorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fueled electrical generators.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherGenerationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other generation.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PhotovoltaicsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Solar photovoltaics, rated on a nameplate capacity basis.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WindTurbinesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wind generators, rated on a nameplate capacity basis.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricityFromPowerGridRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical energy drawn from a specific utility grid.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricityFromSpecificGeneratorRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical energy from a specific power plant, such as a wind farm using a specific type of turbine.

    Range version.
    """

    _EXT_VERSION = "1.0"

    energy_source: list[EnergySource] | None = pydantic.Field(default=None, description="")


class PowerPurchaseAgreementsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical energy subject to a verified power purchase agreement.

    The impact of electricity generation is allocated specifically to the agreement and not to the general grid.

    Range version.
    """

    _EXT_VERSION = "1.0"

    energy_source: list[EnergySource] | None = pydantic.Field(default=None, description="")


class LightbulbsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Various types of light bulbs, including LED, CFL, halogen, and incandescent.

    Range version.
    """

    _EXT_VERSION = "1.0"


class LightingControlsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Devices used to control the operation of lighting, including dimmers, sensors, and smart controls.

    Range version.
    """

    _EXT_VERSION = "1.0"


class LightingFixturesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Permanent lighting fixtures for interior spaces, including ceiling, wall-mounted, and pendant fixtures.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OutdoorLightingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Lighting products designed for outdoor use, including landscape and security lighting.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SpecialtyLightingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Specialized lighting for niche applications like emergency, medical, or theatrical lighting.

    Range version.
    """

    _EXT_VERSION = "1.0"


class TaskLightingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Lighting designed for specific tasks such as desk lamps, under-cabinet lighting, and reading lamps.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricalPowerStorageRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical Power Storage.

    Range version.
    """

    _EXT_VERSION = "1.0"

    Batteries: BatteriesRangeV1 | None = None
    OtherElectricalPowerStorage: OtherElectricalPowerStorageRangeV1 | None = None


class LowVoltageElectricalDistributionRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Low Voltage Electrical Distribution.

    Range version.
    """

    _EXT_VERSION = "1.0"

    CableTrays: CableTraysRangeV1 | None = None
    ElectricalBuses: ElectricalBusesRangeV1 | None = None
    FloorEquipmentBoxes: FloorEquipmentBoxesRangeV1 | None = None
    PowerDistributionUnits: PowerDistributionUnitsRangeV1 | None = None
    Raceways: RacewaysRangeV1 | None = None


class ElectricalGenerationEquipmentRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for generating electrical power.

    This category is primarily for smaller-scale. (e.g. on premises) generation, rather than utility-scale equipment.

    Range version.
    """

    _EXT_VERSION = "1.0"

    FueledElectricalGenerators: FueledElectricalGeneratorsRangeV1 | None = None
    OtherGeneration: OtherGenerationRangeV1 | None = None
    Photovoltaics: PhotovoltaicsRangeV1 | None = None
    WindTurbines: WindTurbinesRangeV1 | None = None


class ElectricPowerRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical energy drawn from a utility grid.

    Range version.
    """

    _EXT_VERSION = "1.0"

    ElectricityFromPowerGrid: ElectricityFromPowerGridRangeV1 | None = None
    ElectricityFromSpecificGenerator: ElectricityFromSpecificGeneratorRangeV1 | None = None
    PowerPurchaseAgreements: PowerPurchaseAgreementsRangeV1 | None = None


class LightingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Lamps and lightbulbs and lamp components.

    Range version.
    """

    _EXT_VERSION = "1.0"

    color_temperature: AmountRangeColorTemperature | None = pydantic.Field(default=None, description="")
    typical_utilization: AmountRangeUtilization | None = pydantic.Field(default=None, description="")
    luminosity: AmountRangeLuminosity | None = pydantic.Field(default=None, description="")
    wattage: AmountRangePower | None = pydantic.Field(default=None, description="")
    color_rendering_index: RangeFloat | None = pydantic.Field(default=None, description="")
    dimmable: bool | None = pydantic.Field(default=None, description="")
    Lightbulbs: LightbulbsRangeV1 | None = None
    LightingControls: LightingControlsRangeV1 | None = None
    LightingFixtures: LightingFixturesRangeV1 | None = None
    OutdoorLighting: OutdoorLightingRangeV1 | None = None
    SpecialtyLighting: SpecialtyLightingRangeV1 | None = None
    TaskLighting: TaskLightingRangeV1 | None = None


class ElectricalConduitRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Tubing used to protect and route electrical wiring in a building or structure.

    Range version.
    """

    _EXT_VERSION = "1.1"

    nominal_diameter: AmountRangeLengthMm | None = None
    outer_diameter: AmountRangeLengthMm | None = None
    inner_diameter: AmountRangeLengthMm | None = None
    wall_thickness: AmountRangeLengthMm | None = None
    material: list[ConduitMaterial] | None = None


class ElectricalRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electric power and equipment.

    Range version.
    """

    _EXT_VERSION = "1.1"

    ElectricalPowerStorage: ElectricalPowerStorageRangeV1 | None = None
    LowVoltageElectricalDistribution: LowVoltageElectricalDistributionRangeV1 | None = None
    ElectricalGenerationEquipment: ElectricalGenerationEquipmentRangeV1 | None = None
    ElectricPower: ElectricPowerRangeV1 | None = None
    Lighting: LightingRangeV1 | None = None
    ElectricalConduit: ElectricalConduitRangeV1 | None = None
