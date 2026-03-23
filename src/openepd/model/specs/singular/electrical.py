#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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
    "BatteriesV1",
    "CableTrayAccsV1",
    "CableTraysV1",
    "ChargingStationsV1",
    "ElectricPowerV1",
    "ElectricalBoxAccsV1",
    "ElectricalBusesV1",
    "ElectricalCableAccsV1",
    "ElectricalCablesV1",
    "ElectricalConduitV1",
    "ElectricalConnectorsV1",
    "ElectricalDistSwitchgearV1",
    "ElectricalGenerationEquipmentV1",
    "ElectricalGroundingConnectorsV1",
    "ElectricalMVFusesV1",
    "ElectricalMVInterruptersV1",
    "ElectricalMVSwitchesV1",
    "ElectricalPowerStorageV1",
    "ElectricalV1",
    "ElectricityFromPowerGridV1",
    "ElectricityFromSpecificGeneratorV1",
    "FloorEquipmentBoxesV1",
    "FueledElectricalGeneratorsV1",
    "LightbulbsV1",
    "LightingControlsV1",
    "LightingFixturesV1",
    "LightingV1",
    "LowVoltBusesV1",
    "LowVoltageElectricalDistributionV1",
    "MedVoltBusesV1",
    "OtherElectricalEquipmentV1",
    "OtherElectricalPowerStorageV1",
    "OtherGenerationV1",
    "OutdoorLightingV1",
    "PhotovoltaicsV1",
    "PowerDistributionUnitsV1",
    "PowerPurchaseAgreementsV1",
    "RacewaysV1",
    "SpecialtyLightingV1",
    "TaskLightingV1",
    "WindTurbinesV1",
)

import pydantic

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import CableTraysMaterial, EnergySource, RacewaysMaterial
from openepd.model.specs.singular.mixins.conduit_mixin import ConduitMixin
from openepd.model.validation.quantity import (
    ColorTemperatureStr,
    LengthMmStr,
    LengthMStr,
    LuminosityStr,
    MassKgStr,
    PowerStr,
    UtilizationStr,
    validate_quantity_ge_factory,
    validate_quantity_le_factory,
    validate_quantity_unit_factory,
)


class LowVoltBusesV1(BaseOpenEpdHierarchicalSpec):
    """Busbars and Busways of 600V or less."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="LowVoltBuses",
        display_name="Low Voltage Busbars and Busways",
        short_name="Low Voltage",
        historical_names=["Electrical >> Distribution >> Buses >> Low Voltage"],
        description="Busbars and Busways of 600V or less",
        masterformat="26 25 00 Low Voltage Enclosed Bus Assemblies",
        declared_unit=Amount(qty=1, unit="m"),
    )


class MedVoltBusesV1(BaseOpenEpdHierarchicalSpec):
    """Busbars and Busways over 600V."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MedVoltBuses",
        display_name="Med Voltage Busbars and Busways",
        short_name="Medium Voltage",
        historical_names=["Electrical >> Distribution >> Buses >> Medium Voltage"],
        description="Busbars and Busways over 600V",
        masterformat="26 15 00 Medium-Voltage Enclosed Bus Assemblies",
        declared_unit=Amount(qty=1, unit="m"),
    )


class BatteriesV1(BaseOpenEpdHierarchicalSpec):
    """Battery equipment, including central batteries, battery charging, and UPS."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Batteries",
        display_name="Battery Equipment",
        short_name="Battery",
        historical_names=["Electrical >> Storage >> Battery"],
        description="Battery equipment, including central batteries, battery charging, and UPS",
        masterformat="26 33 00 Battery Equipment",
    )


class OtherElectricalPowerStorageV1(BaseOpenEpdHierarchicalSpec):
    """Other electrical power storage performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherElectricalPowerStorage",
        display_name="Other",
        historical_names=["Electrical >> Storage >> Other"],
        description="Other electrical power storage equipment.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kWh"),
    )


class CableTrayAccsV1(BaseOpenEpdHierarchicalSpec):
    """Accessories for cable trays."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CableTrayAccs",
        display_name="Cable Tray Accessories",
        short_name="Accessories",
        historical_names=["Electrical >> Distribution >> Cable Trays >> Accessories"],
        description="Accessories for cable trays",
        masterformat="26 05 36 Cable Trays for Electrical Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )


class CableTraysV1(BaseOpenEpdHierarchicalSpec):
    """Mechanical support for electrial or communications cabling, typically suspended from a roof or wall."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="CableTrays",
        display_name="Cable Trays",
        historical_names=["Electrical >> Distribution >> Cable Trays"],
        description="Mechanical support for electrial or communications cabling, typically suspended from a roof or wall.",
        masterformat="26 05 36 Cable Trays for Electrical Systems",
        declared_unit=Amount(qty=1, unit="m"),
    )

    # Own fields:
    height: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    width: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    depth: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    static_load: MassKgStr | None = pydantic.Field(default=None, description="", examples=["1 kg"])
    ventilated: bool | None = pydantic.Field(
        default=None,
        description="At least 40% of the tray base is open to air flow",
        examples=[True],
    )
    cable_trays_material: CableTraysMaterial | None = pydantic.Field(
        default=None, description="", examples=["Stainless Steel"]
    )

    # Nested specs:
    CableTrayAccs: CableTrayAccsV1 | None = None


class ElectricalCableAccsV1(BaseOpenEpdHierarchicalSpec):
    """Accessories for cabling, including ties and supports."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalCableAccs",
        display_name="Low and Medium Voltage Cable Accessories",
        short_name="Accessories",
        historical_names=["Electrical >> Distribution >> Cables >> Accessories"],
        description="Accessories for cabling, including ties and supports.",
        masterformat="26 05 29 Hangers and Supports for Electrical Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalCablesV1(BaseOpenEpdHierarchicalSpec):
    """Insulated building power distribution conductors to connect electrical equipment within a structure at 600V or less."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalCables",
        display_name="Low and Medium Voltage Cables",
        short_name="Cables",
        historical_names=["Electrical >> Distribution >> Cables"],
        description="Insulated building power distribution conductors to connect electrical equipment within a structure at 600V or less.",
        masterformat="26 05 13 Medium-Voltage Cables",
        declared_unit=Amount(qty=1, unit="m"),
    )

    # Nested specs:
    ElectricalCableAccs: ElectricalCableAccsV1 | None = None


class ElectricalBusesV1(BaseOpenEpdHierarchicalSpec):
    """
    Power distribution, in the form of busbars or of insulted ducts made of copper or aluminum busbars.

    It is an alternative means of conducting electricity compared toto power cables or cable bus. Also called
    bus ducts.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalBuses",
        display_name="Busbars and Busways",
        short_name="Buses",
        historical_names=["Electrical >> Distribution >> Buses"],
        description="Power distribution, in the form of busbars or of insulted ducts made of copper or aluminum busbars. It is an alternative means of conducting electricity compared toto power cables or cable bus. Also called bus ducts.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="m"),
    )

    # Nested specs:
    LowVoltBuses: LowVoltBusesV1 | None = None
    MedVoltBuses: MedVoltBusesV1 | None = None


class ElectricalBoxAccsV1(BaseOpenEpdHierarchicalSpec):
    """Accessories for electrical equipment boxes or their contents."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalBoxAccs",
        display_name="Electrical Box Accessories",
        short_name="Accessories",
        historical_names=["Electrical >> Distribution >> Boxes >> Accessories"],
        description="Accessories for electrical equipment boxes or their contents.",
        masterformat="26 05 33.16 Boxes for Electrical Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )


class FloorEquipmentBoxesV1(BaseOpenEpdHierarchicalSpec):
    """Equipment boxes for power or electronic equipment embedded in an accessible floor."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="FloorEquipmentBoxes",
        display_name="Floor Equipment Boxes",
        short_name="Boxes",
        historical_names=["Electrical >> Distribution >> Boxes"],
        description="Equipment boxes for power or electronic equipment embedded in an accessible floor.",
        masterformat="26 05 33.16 Boxes for Electrical Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    ElectricalBoxAccs: ElectricalBoxAccsV1 | None = None


class PowerDistributionUnitsV1(BaseOpenEpdHierarchicalSpec):
    """Switched electrical distribution units placed very close to the point of consumption, for example inside a rack of electronic equipment."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PowerDistributionUnits",
        display_name="Power Distribution Units (PDUs)",
        short_name="PDUs",
        historical_names=["Electrical >> Distribution >> PDUs"],
        description="Switched electrical distribution units placed very close to the point of consumption, for example inside a rack of electronic equipment.",
        masterformat="26 26 00 Power Distribution Units",
        declared_unit=Amount(qty=1, unit="item"),
    )


class RacewaysV1(BaseOpenEpdHierarchicalSpec):
    """Mechanical guideways for eletrical communications cabling, typically embedded in an accessible floor."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Raceways",
        display_name="Raceways",
        historical_names=["Electrical >> Distribution >> Raceways"],
        description="Mechanical guideways for electrical communications cabling, often embedded in an accessible floor.",
        masterformat="26 05 33 Raceway and Boxes for Electrical Systems",
        declared_unit=Amount(qty=1, unit="m"),
    )

    # Own fields:
    width: LengthMStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    depth: LengthMStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    painted: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    divided: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    raceways_material: RacewaysMaterial | None = pydantic.Field(default=None, description="", examples=["Aluminum"])


class ElectricalGroundingConnectorsV1(BaseOpenEpdHierarchicalSpec):
    """Grounding connectors are safety devices that establish a low-resistance path to ground."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalGroundingConnectors",
        display_name="Electrical Grounding Connectors",
        short_name="Grounding",
        historical_names=["Electrical >> Distribution >> Connectors >> Grounding"],
        description="Grounding connectors are safety devices that establish a low-resistance path to ground",
        masterformat="26 05 26 Grounding and Bonding for Electrical Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalConnectorsV1(BaseOpenEpdHierarchicalSpec):
    """Devices that join electrical conductors or cables together."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalConnectors",
        display_name="Electrical Connectors",
        short_name="Connectors",
        historical_names=["Electrical >> Distribution >> Connectors"],
        description="Devices that join electrical conductors or cables together",
        masterformat="26 05 83 Wiring Connections",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    ElectricalGroundingConnectors: ElectricalGroundingConnectorsV1 | None = None


class ElectricalMVSwitchesV1(BaseOpenEpdHierarchicalSpec):
    """Devices that control electrical circuits by opening or closing a connection to turn power on and off, under manual or other intentional control."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalMVSwitches",
        display_name="Electrical Switches (Med/Low Voltage)",
        short_name="Switches",
        historical_names=["Electrical >> Distribution >> Switchgear >> Switches"],
        description="Devices that control electrical circuits by opening or closing a connection to turn power on and off, under manual or other intentional control.",
        masterformat="26 28 16.16 Enclosed Switches",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalMVInterruptersV1(BaseOpenEpdHierarchicalSpec):
    """Protective devices that automatically disconnect circuits when detecting faults, surges, or abnormal current conditions."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalMVInterrupters",
        display_name="Electrical Interrupters (Med/Low Voltage)",
        short_name="Interrupters",
        historical_names=["Electrical >> Distribution >> Switchgear >> Interrupters"],
        description="Protective devices that automatically disconnect circuits when detecting faults, surges, or abnormal current conditions",
        masterformat="26 28 16.13 Enclosed Circuit Breakers",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalMVFusesV1(BaseOpenEpdHierarchicalSpec):
    """Single-use protective devices that melt and break a circuit when current exceeds a safe level."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalMVFuses",
        display_name="Electrical Fuses (Med/Low Voltage)",
        short_name="Fuses",
        historical_names=["Electrical >> Distribution >> Switchgear >> Fuses"],
        description="Single-use protective devices that melt and break a circuit when current exceeds a safe level.",
        masterformat="26 28 13 Fuses",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalDistSwitchgearV1(BaseOpenEpdHierarchicalSpec):
    """Equipment for interrupting and controlling high-power electrical flows for protection, isolation, or control of electrical equipment."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalDistSwitchgear",
        display_name="Electrical Switchgear (Med/Low Voltage)",
        short_name="Switchgear",
        historical_names=["Electrical >> Distribution >> Switchgear"],
        description="Equipment for interrupting and controlling high-power electrical flows for protection, isolation, or control of electrical equipment.",
        masterformat="26 13 00 Medium-Voltage Switchgear",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    ElectricalMVSwitches: ElectricalMVSwitchesV1 | None = None
    ElectricalMVInterrupters: ElectricalMVInterruptersV1 | None = None
    ElectricalMVFuses: ElectricalMVFusesV1 | None = None


class ChargingStationsV1(BaseOpenEpdHierarchicalSpec):
    """Outdoor charging stations, particularly for electric vehicles (EVs)."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ChargingStations",
        display_name="Outdoor Charging Stations",
        short_name="Charging Stations",
        historical_names=["Electrical >> Distribution >> Charging Stations"],
        description="Outdoor charging stations, particularly for electric vehicles (EVs)",
        masterformat="26 27 36 Outdoor Charging Stations",
        declared_unit=Amount(qty=1, unit="item"),
    )


class FueledElectricalGeneratorsV1(BaseOpenEpdHierarchicalSpec):
    """Fueled electrical generators."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FueledElectricalGenerators",
        display_name="Fueled Electrical Generators",
        short_name="Generators",
        historical_names=["Electrical >> Generation >> Generators"],
        description="Fueled electrical generators.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kW"),
    )


class OtherGenerationV1(BaseOpenEpdHierarchicalSpec):
    """Other generation."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherGeneration",
        display_name="Other Generation",
        short_name="Other",
        historical_names=["Electrical >> Generation >> Other"],
        description="Other generation.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kW"),
    )


class PhotovoltaicsV1(BaseOpenEpdHierarchicalSpec):
    """Solar photovoltaics, rated on a nameplate capacity basis."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Photovoltaics",
        display_name="Photovoltaics",
        alt_names=["solar panel"],
        historical_names=["Electrical >> Generation >> Photovoltaics"],
        description="Solar photovoltaics, rated on a nameplate capacity basis.",
        masterformat="26 31 00 Photovoltaic Collectors",
        declared_unit=Amount(qty=1, unit="kW"),
    )


class WindTurbinesV1(BaseOpenEpdHierarchicalSpec):
    """Wind generators, rated on a nameplate capacity basis."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WindTurbines",
        display_name="Wind Turbines",
        short_name="Wind",
        historical_names=["Electrical >> Generation >> Wind"],
        description="Wind generators, rated on a nameplate capacity basis.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kW"),
    )


class ElectricityFromPowerGridV1(BaseOpenEpdHierarchicalSpec):
    """Electrical energy drawn from a specific utility grid."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricityFromPowerGrid",
        display_name="Electricity from Power Grid",
        short_name="Grid Electricity",
        historical_names=["Electrical >> Power >> Grid Electricity"],
        description="Electrical energy drawn from a specific utility grid.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kWh"),
    )


class ElectricityFromSpecificGeneratorV1(BaseOpenEpdHierarchicalSpec):
    """Electrical energy from a specific power plant, such as a wind farm using a specific type of turbine."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricityFromSpecificGenerator",
        display_name="ElectricityFromSpecificGenerator",
        short_name="Generated Electricity",
        historical_names=["Electrical >> Power >> Generated Electricity"],
        description="Electrical energy from a specific power plant, such as a wind farm using a specific type of turbine.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kWh"),
    )

    # Own fields:
    energy_source: EnergySource | None = pydantic.Field(default=None, description="", examples=["Grid"])


class PowerPurchaseAgreementsV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical energy subject to a verified power purchase agreement.

    The impact of electricity generation is allocated specifically to the agreement and not to the general grid.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PowerPurchaseAgreements",
        display_name="PowerPurchaseAgreements",
        short_name="PPAs",
        historical_names=["Electrical >> Power >> PPAs"],
        description="Electrical energy subject to a verified power purchase agreement in which the impact of electricity generation is allocated specifically to the agreement and not to the general grid.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kWh"),
    )

    # Own fields:
    energy_source: EnergySource | None = pydantic.Field(default=None, description="", examples=["Grid"])


class LightbulbsV1(BaseOpenEpdHierarchicalSpec):
    """Various types of light bulbs, including LED, CFL, halogen, and incandescent."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Lightbulbs",
        display_name="Lightbulbs",
        short_name="Bulbs",
        historical_names=["Electrical >> Lighting >> Bulbs"],
        description="Various types of light bulbs, including LED, CFL, halogen, and incandescent.",
        masterformat="26 51 00 Interior Lighting",
        declared_unit=Amount(qty=1, unit="item"),
    )


class LightingControlsV1(BaseOpenEpdHierarchicalSpec):
    """Devices used to control the operation of lighting, including dimmers, sensors, and smart controls."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="LightingControls",
        display_name="Lighting Controls",
        short_name="Controls",
        historical_names=["Electrical >> Lighting >> Controls"],
        description="Devices used to control the operation of lighting, including dimmers, sensors, and smart controls.",
        masterformat="26 09 23 Lighting Control Devices",
        declared_unit=Amount(qty=1, unit="item"),
    )


class LightingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Permanent lighting fixtures for interior spaces, including ceiling, wall-mounted, and pendant fixtures."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="LightingFixtures",
        display_name="Lighting Fixtures",
        short_name="Fixtures",
        historical_names=["Electrical >> Lighting >> Fixtures"],
        description="Permanent lighting fixtures for interior spaces, including ceiling, wall-mounted, and pendant fixtures.",
        masterformat="26 51 00 Interior Lighting",
        declared_unit=Amount(qty=1, unit="item"),
    )


class OutdoorLightingV1(BaseOpenEpdHierarchicalSpec):
    """Lighting products designed for outdoor use, including landscape and security lighting."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OutdoorLighting",
        display_name="Outdoor Lighting",
        short_name="Outdoor",
        historical_names=["Electrical >> Lighting >> Outdoor"],
        description="Lighting products designed for outdoor use, including landscape and security lighting.",
        masterformat="26 56 00 Exterior Lighting",
        declared_unit=Amount(qty=1, unit="item"),
    )


class SpecialtyLightingV1(BaseOpenEpdHierarchicalSpec):
    """Specialized lighting for niche applications like emergency, medical, or theatrical lighting."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SpecialtyLighting",
        display_name="Specialty Lighting",
        short_name="Specialty",
        historical_names=["Electrical >> Lighting >> Specialty"],
        description="Specialized lighting for niche applications like emergency, medical, or theatrical lighting.",
        masterformat="26 51 00 Interior Lighting",
        declared_unit=Amount(qty=1, unit="item"),
    )


class TaskLightingV1(BaseOpenEpdHierarchicalSpec):
    """Lighting designed for specific tasks such as desk lamps, under-cabinet lighting, and reading lamps."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="TaskLighting",
        display_name="Task Lighting",
        historical_names=["Electrical >> Lighting >> Task Lighting"],
        description="Lighting designed for specific tasks such as desk lamps, under-cabinet lighting, and reading lamps.",
        masterformat="26 51 13 Interior Lighting Fixtures, Lamps, And Ballasts",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalPowerStorageV1(BaseOpenEpdHierarchicalSpec):
    """Electrical Power Storage."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalPowerStorage",
        display_name="ElectricalPowerStorage",
        short_name="Storage",
        historical_names=["Electrical >> Storage"],
        description="Electrical Power Storage.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kWh"),
    )

    # Nested specs:
    Batteries: BatteriesV1 | None = None
    OtherElectricalPowerStorage: OtherElectricalPowerStorageV1 | None = None


class LowVoltageElectricalDistributionV1(BaseOpenEpdHierarchicalSpec):
    """Low Voltage Electrical Distribution."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="LowVoltageElectricalDistribution",
        display_name="LowVoltageElectricalDistribution",
        short_name="Distribution",
        historical_names=["Electrical >> Distribution"],
        description="Low Voltage Electrical Distribution.",
        masterformat="26 20 00 Low Voltage Electrical Distribution",
    )

    # Nested specs:
    CableTrays: CableTraysV1 | None = None
    ElectricalCables: ElectricalCablesV1 | None = None
    ElectricalBuses: ElectricalBusesV1 | None = None
    FloorEquipmentBoxes: FloorEquipmentBoxesV1 | None = None
    PowerDistributionUnits: PowerDistributionUnitsV1 | None = None
    Raceways: RacewaysV1 | None = None
    ElectricalConnectors: ElectricalConnectorsV1 | None = None
    ElectricalDistSwitchgear: ElectricalDistSwitchgearV1 | None = None
    ChargingStations: ChargingStationsV1 | None = None


class ElectricalGenerationEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for generating electrical power.

    This category is primarily for smaller-scale. (e.g. on premises) generation, rather than utility-scale equipment.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalGenerationEquipment",
        display_name="ElectricalGenerationEquipment",
        short_name="Generation",
        historical_names=["Electrical >> Generation"],
        description="Equipment for generating electrical power. This category is primarily for smaller-scale (e.g. on premises) generation, rather than utility-scale equipment.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kW"),
    )

    # Nested specs:
    FueledElectricalGenerators: FueledElectricalGeneratorsV1 | None = None
    OtherGeneration: OtherGenerationV1 | None = None
    Photovoltaics: PhotovoltaicsV1 | None = None
    WindTurbines: WindTurbinesV1 | None = None


class ElectricPowerV1(BaseOpenEpdHierarchicalSpec):
    """Electrical energy drawn from a utility grid."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricPower",
        display_name="ElectricPower",
        short_name="Power",
        historical_names=["Electrical >> Power"],
        description="Electrical energy drawn from a utility grid.",
        masterformat="26 00 00 Electrical",
        declared_unit=Amount(qty=1, unit="kWh"),
    )

    # Nested specs:
    ElectricityFromPowerGrid: ElectricityFromPowerGridV1 | None = None
    ElectricityFromSpecificGenerator: ElectricityFromSpecificGeneratorV1 | None = None
    PowerPurchaseAgreements: PowerPurchaseAgreementsV1 | None = None


class LightingV1(BaseOpenEpdHierarchicalSpec):
    """Lamps and lightbulbs and lamp components."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Lighting",
        display_name="Lighting",
        description="Lamps and lightbulbs and lamp components",
        masterformat="26 50 00 Lighting",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    color_temperature: ColorTemperatureStr | None = pydantic.Field(default=None, description="", examples=["1 K"])
    typical_utilization: UtilizationStr | None = pydantic.Field(default=None, description="", examples=["1 h / yr"])
    luminosity: LuminosityStr | None = pydantic.Field(default=None, description="", examples=["1 lumen"])
    wattage: PowerStr | None = pydantic.Field(default=None, description="")
    color_rendering_index: float | None = pydantic.Field(default=None, description="", examples=[2.3])
    dimmable: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )

    @pydantic.field_validator("color_temperature")
    def _color_temperature_quantity_ge_validator(cls, value):
        return validate_quantity_ge_factory("1E+03 K")(cls, value)

    @pydantic.field_validator("color_temperature")
    def _color_temperature_quantity_le_validator(cls, value):
        return validate_quantity_le_factory("1E+04 K")(cls, value)

    @pydantic.field_validator("typical_utilization")
    def _typical_utilization_unit_validator(cls, value):
        return validate_quantity_unit_factory("h / yr")(cls, value)

    @pydantic.field_validator("typical_utilization")
    def _typical_utilization_quantity_ge_validator(cls, value):
        return validate_quantity_ge_factory("25 h / yr")(cls, value)

    @pydantic.field_validator("luminosity")
    def _luminosity_quantity_ge_validator(cls, value):
        return validate_quantity_ge_factory("450 lumen")(cls, value)

    @pydantic.field_validator("luminosity")
    def _luminosity_quantity_le_validator(cls, value):
        return validate_quantity_le_factory("2.6E+03 lumen")(cls, value)

    @pydantic.field_validator("wattage")
    def _wattage_quantity_ge_validator(cls, value):
        return validate_quantity_ge_factory("5 W")(cls, value)

    @pydantic.field_validator("wattage")
    def _wattage_quantity_le_validator(cls, value):
        return validate_quantity_le_factory("100 W")(cls, value)

    # Nested specs:
    Lightbulbs: LightbulbsV1 | None = None
    LightingControls: LightingControlsV1 | None = None
    LightingFixtures: LightingFixturesV1 | None = None
    OutdoorLighting: OutdoorLightingV1 | None = None
    SpecialtyLighting: SpecialtyLightingV1 | None = None
    TaskLighting: TaskLightingV1 | None = None


class ElectricalConduitV1(BaseOpenEpdHierarchicalSpec, ConduitMixin):
    """Tubing used to protect and route electrical wiring in a building or structure."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalConduit",
        display_name="Electrical Conduit",
        short_name="Conduit",
        historical_names=["Electrical >> Conduit"],
        description="Tubing used to protect and route electrical wiring in a building or structure",
        masterformat="26 05 33.13 Electrical Conduit",
        declared_unit=Amount(qty=1, unit="m"),
    )


class OtherElectricalEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Other Electrical Equipment."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherElectricalEquipment",
        display_name="OtherElectricalEquipment",
        short_name="Other",
        historical_names=["Electrical >> Other", "Other"],
        description="Other Electrical Equipment.",
        masterformat="26 00 00 Electrical",
    )


class ElectricalV1(BaseOpenEpdHierarchicalSpec):
    """Electric power and equipment."""

    _EXT_VERSION = "1.2"
    _CATEGORY_META = CategoryMeta(
        unique_name="Electrical",
        display_name="Electrical",
        alt_names=["Electric", "Power"],
        description="Electric power and equipment",
        masterformat="26 00 00 Electrical",
    )

    # Nested specs:
    ElectricalPowerStorage: ElectricalPowerStorageV1 | None = None
    LowVoltageElectricalDistribution: LowVoltageElectricalDistributionV1 | None = None
    ElectricalGenerationEquipment: ElectricalGenerationEquipmentV1 | None = None
    ElectricPower: ElectricPowerV1 | None = None
    Lighting: LightingV1 | None = None
    ElectricalConduit: ElectricalConduitV1 | None = None
    OtherElectricalEquipment: OtherElectricalEquipmentV1 | None = None
