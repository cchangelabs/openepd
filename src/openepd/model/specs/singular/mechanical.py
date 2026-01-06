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
import pydantic

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    AhuAirflowControl,
    AhuZoneControl,
    AirFiltersMediaType,
    AirFiltersMervRating,
    BoilerConfiguration,
    BoilerEquipmentFuelType,
    HeatPumpType,
    HvacDuctMaterial,
    HvacDuctShape,
    HvacDuctType,
    HvacHeatExchangersType,
    MechanicalInstallation,
    MechanicalRefrigerants,
)
from openepd.model.validation.quantity import AirflowStr, FlowRateStr, PowerStr, PressureMPaStr, VolumeStr


class HvacVrfControlV1(BaseOpenEpdHierarchicalSpec):
    """Controller for adjusting airflow across the VRF system."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacVrfControl",
        display_name="VRF Controllers",
        historical_names=["Mechanical >> VRF Systems >> VRF Controllers"],
        description="Controller for adjusting airflow across the VRF system.",
        masterformat="23 81 29 Variable Refrigerant Flow HVAC Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )


class HvacVrfIndoorV1(BaseOpenEpdHierarchicalSpec):
    """Heating and cooling unit located on the inside of a building and supplies air to specific indoor zones."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacVrfIndoor",
        display_name="VRF Indoor Units",
        historical_names=["Mechanical >> VRF Systems >> VRF Indoor Units"],
        description="Heating and cooling unit that is located on the inside of a building and supplies air to specific indoor zones.",
        masterformat="23 81 29 Variable Refrigerant Flow HVAC Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="", examples=[["R11"]])
    heating_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    cooling_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    airflow_rate: AirflowStr | None = pydantic.Field(default=None, description="", examples=["1 m3 / s"])
    air_volume: VolumeStr | None = pydantic.Field(default=None, description="", examples=["1 m3"])


class HvacVrfOutdoorV1(BaseOpenEpdHierarchicalSpec):
    """Heating and cooling unit that is on the outside of a building and distributes air to the indoor units."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacVrfOutdoor",
        display_name="VRF Outdoor Units",
        historical_names=["Mechanical >> VRF Systems >> VRF Outdoor Units"],
        description="Heating and cooling unit that is on the outside of a building and distributes air to the indoor units.",
        masterformat="23 81 29 Variable Refrigerant Flow HVAC Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="", examples=[["R11"]])
    heating_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    cooling_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    airflow_rate: AirflowStr | None = pydantic.Field(default=None, description="", examples=["1 m3 / s"])
    air_volume: VolumeStr | None = pydantic.Field(default=None, description="", examples=["1 m3"])


class HvacAirDiffusersV1(BaseOpenEpdHierarchicalSpec):
    """Room-side terminals for air distribution. This is different from Terminal Heating & Cooling Units."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacAirDiffusers",
        display_name="Air Diffusers",
        historical_names=["Mechanical >> Air Diffusers"],
        description="Room-side terminals for air distribution. This is different from Terminal Heating & Cooling Units.",
        masterformat="23 36 00 Air Terminal Units",
        declared_unit=Amount(qty=1, unit="item"),
    )


class HvacAirFiltersV1(BaseOpenEpdHierarchicalSpec):
    """Device for filtering particles of dust, soot, etc., from the air passing through it."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacAirFilters",
        display_name="Air Filters",
        historical_names=["Mechanical >> Air Filters"],
        description="Device for filtering particles of dust, soot, etc., from the air passing through it.",
        masterformat="23 40 00 HVAC Air Cleaning Devices",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    merv_rating: AirFiltersMervRating | None = pydantic.Field(default=None, description="", examples=["MERV 1"])
    media_type: AirFiltersMediaType | None = pydantic.Field(default=None, description="", examples=["Acrylic"])


class HvacAHUsV1(BaseOpenEpdHierarchicalSpec):
    """
    Device which provides healthy, dust free air to buildings with a good energy efficiency.

    Usually a large metal box containing a blower, heating or cooling elements, filter racks or chambers, sound
    attenuators, and dampers.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacAHUs",
        display_name="Air Handling Units",
        short_name="AHUs",
        historical_names=["Mechanical >> AHUs"],
        description="Device which provides healthy, dust free air to buildings with a good energy efficiency. Usually a large metal box containing a blower, heating or cooling elements, filter racks or chambers, sound attenuators, and dampers.",
        masterformat="23 74 00 Packaged Outdoor HVAC Equipment",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="", examples=[["R11"]])
    installation: MechanicalInstallation | None = pydantic.Field(default=None, description="", examples=["Indoor"])
    airflow_rate: AirflowStr | None = pydantic.Field(default=None, description="", examples=["1 m3 / s"])
    air_volume: VolumeStr | None = pydantic.Field(default=None, description="", examples=["1 m3"])
    cooling_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    heating_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    airflow_control: AhuAirflowControl | None = pydantic.Field(default=None, description="", examples=["CAV"])
    zone_control: AhuZoneControl | None = pydantic.Field(default=None, description="", examples=["Single Zone"])


class HvacBoilersV1(BaseOpenEpdHierarchicalSpec):
    """Closed vessel for heating fluid."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacBoilers",
        display_name="Boilers",
        historical_names=["Mechanical >> Boilers"],
        description="Closed vessel for heating fluid.",
        masterformat="23 52 00 Heating Boilers",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    flow_rate: FlowRateStr | None = pydantic.Field(default=None, description="", examples=["1 l / min"])
    heating_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    configuration: BoilerConfiguration | None = pydantic.Field(default=None, description="", examples=["Hot water"])
    fuel_type: BoilerEquipmentFuelType | None = pydantic.Field(default=None, description="", examples=["Coal"])


class HvacChillersV1(BaseOpenEpdHierarchicalSpec):
    """
    Machine that removes heat from a liquid coolant.

    Uses a vapor-compression, adsorption refrigeration, or absorption refrigeration cycles. Incldues centrifugal,
    water-cooled chillers, etc.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacChillers",
        display_name="Chillers",
        historical_names=["Mechanical >> Chillers"],
        description="Machine that removes heat from a liquid coolant via a vapor-compression, adsorption refrigeration, or absorption refrigeration cycles. Incldues centrifugal, water-cooled chillers, etc.",
        masterformat="23 64 00 Packaged Water Chillers",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="", examples=[["R11"]])
    installation: MechanicalInstallation | None = pydantic.Field(default=None, description="", examples=["Indoor"])
    heating_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    cooling_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    air_volume: VolumeStr | None = pydantic.Field(default=None, description="", examples=["1 m3"])
    airflow_rate: AirflowStr | None = pydantic.Field(default=None, description="", examples=["1 m3 / s"])


class HvacFansV1(BaseOpenEpdHierarchicalSpec):
    """Apparatus with rotating blades that creates a current of air for cooling or ventilation."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacFans",
        display_name="Fans",
        historical_names=["Mechanical >> Fans"],
        description="Apparatus with rotating blades that creates a current of air for cooling or ventilation.",
        masterformat="23 34 00 HVAC Fans",
        declared_unit=Amount(qty=1, unit="item"),
    )


class HvacHeatPumpsV1(BaseOpenEpdHierarchicalSpec):
    """Device that transfers thermal energy between spaces, including ground and air source heat pumps."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacHeatPumps",
        display_name="Heat Pumps",
        historical_names=["Mechanical >> Heat Pumps"],
        description="Device that transfers thermal energy between spaces, including ground and air source heat pumps.",
        masterformat="23 81 00 Decentralized Unitary HVAC Equipment",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="", examples=[["R11"]])
    cooling_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    heating_capacity: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])
    air_volume: VolumeStr | None = pydantic.Field(default=None, description="", examples=["1 m3"])
    airflow_rate: AirflowStr | None = pydantic.Field(default=None, description="", examples=["1 m3 / s"])
    heat_pumps_type: HeatPumpType | None = pydantic.Field(default=None, description="", examples=["Air-to-Water"])


class HvacHeatExV1(BaseOpenEpdHierarchicalSpec):
    """
    HVAC heat exchangers.

    Systems that with heat exchange cell which recovers and retains the heat that would otherwise be lost from the
    extracted air.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacHeatEx",
        display_name="HVAC Heat Exchangers",
        short_name="Heat Exchangers",
        historical_names=["Mechanical >> Heat Exchangers"],
        description="Systems that with heat exchange cell which recovers and retains the heat that would otherwise be lost from the extracted air.",
        masterformat="23 57 00 Heat Exchangers for HVAC",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="", examples=[["R11"]])
    heat_exchangers_type: HvacHeatExchangersType | None = pydantic.Field(
        default=None, description="", examples=["Shell and Tube"]
    )


class HvacPumpsV1(BaseOpenEpdHierarchicalSpec):
    """
    Pumps.

    Mechanical device using suction or pressure to raise or move liquids, compress gases, or force air into
    inflatable objects such as tires.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacPumps",
        display_name="Pumps",
        historical_names=["Mechanical >> Pumps"],
        description="Mechanical device using suction or pressure to raise or move liquids, compress gases, or force air into inflatable objects such as tires.",
        masterformat="23 20 00 HVAC Piping and Pumps",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Own fields:
    flow_rate: FlowRateStr | None = pydantic.Field(default=None, description="", examples=["1 l / min"])
    pump_discharge_pressure: PressureMPaStr | None = pydantic.Field(default=None, description="", examples=["1 MPa"])
    pump_horsepower: PowerStr | None = pydantic.Field(default=None, description="", examples=["1000.0 W"])


class HvacRTUsV1(BaseOpenEpdHierarchicalSpec):
    """An air handler designed for outdoor use, typically on roofs."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacRTUs",
        display_name="Rooftop Units",
        short_name="RTUs",
        historical_names=["Mechanical >> RTUs"],
        description="An air handler designed for outdoor use, typically on roofs.",
        masterformat="23 74 00 Packaged Outdoor HVAC Equipment",
        declared_unit=Amount(qty=1, unit="item"),
    )


class HvacVrfSystemsV1(BaseOpenEpdHierarchicalSpec):
    """
    Variable refrigerant flow (VRF).

    Also known as variable refrigerant volume (VRV), is an HVAC technology that allows for varying degrees of cooling
    in more specific areas.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacVrfSystems",
        display_name="Variable Refrigerant Flow Systems",
        short_name="VRF Systems",
        historical_names=["Mechanical >> VRF Systems"],
        description="Variable refrigerant flow (VRF), also known as variable refrigerant volume (VRV), is an HVAC technology that allows for varying degrees of cooling in more specific areas.",
        masterformat="23 81 29 Variable Refrigerant Flow HVAC Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    HvacVrfControl: HvacVrfControlV1 | None = None
    HvacVrfIndoor: HvacVrfIndoorV1 | None = None
    HvacVrfOutdoor: HvacVrfOutdoorV1 | None = None


class HvacDuctsV1(BaseOpenEpdHierarchicalSpec):
    """Ducts for HVAC systems performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HvacDucts",
        display_name="Ducts",
        historical_names=["Mechanical >> Ducts"],
        description="Passages used in heating, ventilation, and air conditioning to deliver and remove air from spaces.",
        masterformat="72151200 Heating and cooling and air conditioning HVAC construction and maintenance services",
    )

    shape: HvacDuctShape | None = pydantic.Field(default=None, description="Hvac duct shape", examples=["Rectangular"])
    material: HvacDuctMaterial | None = pydantic.Field(
        default=None, description="Hvac duct material", examples=["Galvanized Steel"]
    )
    type: HvacDuctType | None = pydantic.Field(default=None, description="Hvac duct type", examples=["Flexible"])


class MechanicalV1(BaseOpenEpdHierarchicalSpec):
    """Mechanical performance specification."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="Mechanical",
        display_name="Mechanical",
        alt_names=["HVAC", "Heating, Ventilating, and Air Conditioning", "Mechanical Systems"],
        description="Mechanical equipment used in the construction of buildings.",
        masterformat="23 00 00 Heating, Ventilating, and Air Conditioning (HVAC)",
    )

    # Nested specs:
    HvacAirDiffusers: HvacAirDiffusersV1 | None = None
    HvacAirFilters: HvacAirFiltersV1 | None = None
    HvacAHUs: HvacAHUsV1 | None = None
    HvacBoilers: HvacBoilersV1 | None = None
    HvacChillers: HvacChillersV1 | None = None
    HvacFans: HvacFansV1 | None = None
    HvacHeatPumps: HvacHeatPumpsV1 | None = None
    HvacHeatEx: HvacHeatExV1 | None = None
    HvacPumps: HvacPumpsV1 | None = None
    HvacRTUs: HvacRTUsV1 | None = None
    HvacVrfSystems: HvacVrfSystemsV1 | None = None
    HvacDucts: HvacDuctsV1 | None = None
