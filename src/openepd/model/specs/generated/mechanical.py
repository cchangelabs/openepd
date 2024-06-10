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
from openepd.model.specs.generated.enums import (
    AhuAirflowControl,
    AhuZoneControl,
    AirFiltersMediaType,
    AirFiltersMervRating,
    BoilerConfiguration,
    BoilerEquipmentFuelType,
    HeatPumpType,
    HvacHeatExchangersType,
    MechanicalInstallation,
    MechanicalRefrigerants,
)
from openepd.model.validation.quantity import AirflowStr, FlowRateStr, PowerStr, PressureMPaStr, VolumeStr


class HvacVrfControlV1(BaseOpenEpdHierarchicalSpec):
    """Controller for adjusting airflow across the VRF system."""

    _EXT_VERSION = "1.0"


class HvacVrfIndoorV1(BaseOpenEpdHierarchicalSpec):
    """Heating and cooling unit located on the inside of a building and supplies air to specific indoor zones."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    heating_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    cooling_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    airflow_rate: AirflowStr | None = pyd.Field(default=None, description="", example="1 m3 / s")
    air_volume: VolumeStr | None = pyd.Field(default=None, description="", example="1 m3")


class HvacVrfOutdoorV1(BaseOpenEpdHierarchicalSpec):
    """Heating and cooling unit that is on the outside of a building and distributes air to the indoor units."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    heating_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    cooling_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    airflow_rate: AirflowStr | None = pyd.Field(default=None, description="", example="1 m3 / s")
    air_volume: VolumeStr | None = pyd.Field(default=None, description="", example="1 m3")


class HvacAirDiffusersV1(BaseOpenEpdHierarchicalSpec):
    """Room-side terminals for air distribution. This is different from Terminal Heating & Cooling Units."""

    _EXT_VERSION = "1.0"


class HvacAirFiltersV1(BaseOpenEpdHierarchicalSpec):
    """Device for filtering particles of dust, soot, etc., from the air passing through it."""

    _EXT_VERSION = "1.0"

    # Own fields:
    merv_rating: AirFiltersMervRating | None = pyd.Field(default=None, description="", example="MERV 1")
    media_type: AirFiltersMediaType | None = pyd.Field(default=None, description="", example="Acrylic")


class HvacAHUsV1(BaseOpenEpdHierarchicalSpec):
    """
    Device which provides healthy, dust free air to buildings with a good energy efficiency.

    Usually a large metal box containing a blower, heating or cooling elements, filter racks or chambers, sound
    attenuators, and dampers.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    installation: MechanicalInstallation | None = pyd.Field(default=None, description="", example="Indoor")
    airflow_rate: AirflowStr | None = pyd.Field(default=None, description="", example="1 m3 / s")
    air_volume: VolumeStr | None = pyd.Field(default=None, description="", example="1 m3")
    cooling_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    heating_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    airflow_control: AhuAirflowControl | None = pyd.Field(default=None, description="", example="CAV")
    zone_control: AhuZoneControl | None = pyd.Field(default=None, description="", example="Single Zone")


class HvacBoilersV1(BaseOpenEpdHierarchicalSpec):
    """Closed vessel for heating fluid."""

    _EXT_VERSION = "1.0"

    # Own fields:
    flow_rate: FlowRateStr | None = pyd.Field(default=None, description="", example="1 l / min")
    heating_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    configuration: BoilerConfiguration | None = pyd.Field(default=None, description="", example="Hot water")
    fuel_type: BoilerEquipmentFuelType | None = pyd.Field(default=None, description="", example="Coal")


class HvacChillersV1(BaseOpenEpdHierarchicalSpec):
    """
    Machine that removes heat from a liquid coolant.

    Uses a vapor-compression, adsorption refrigeration, or absorption refrigeration cycles. Incldues centrifugal,
    water-cooled chillers, etc.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    installation: MechanicalInstallation | None = pyd.Field(default=None, description="", example="Indoor")
    heating_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    cooling_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    air_volume: VolumeStr | None = pyd.Field(default=None, description="", example="1 m3")
    airflow_rate: AirflowStr | None = pyd.Field(default=None, description="", example="1 m3 / s")


class HvacFansV1(BaseOpenEpdHierarchicalSpec):
    """Apparatus with rotating blades that creates a current of air for cooling or ventilation."""

    _EXT_VERSION = "1.0"


class HvacHeatPumpsV1(BaseOpenEpdHierarchicalSpec):
    """Device that transfers thermal energy between spaces, including ground and air source heat pumps."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    cooling_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    heating_capacity: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")
    air_volume: VolumeStr | None = pyd.Field(default=None, description="", example="1 m3")
    airflow_rate: AirflowStr | None = pyd.Field(default=None, description="", example="1 m3 / s")
    heat_pumps_type: HeatPumpType | None = pyd.Field(default=None, description="", example="Air-to-Water")


class HvacHeatExV1(BaseOpenEpdHierarchicalSpec):
    """
    HVAC heat exchangers.

    Systems that with heat exchange cell which recovers and retains the heat that would otherwise be lost from the
    extracted air.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    heat_exchangers_type: HvacHeatExchangersType | None = pyd.Field(
        default=None, description="", example="Shell and Tube"
    )


class HvacPumpsV1(BaseOpenEpdHierarchicalSpec):
    """
    Pumps.

    Mechanical device using suction or pressure to raise or move liquids, compress gases, or force air into
    inflatable objects such as tires.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    flow_rate: FlowRateStr | None = pyd.Field(default=None, description="", example="1 l / min")
    pump_discharge_pressure: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    pump_horsepower: PowerStr | None = pyd.Field(default=None, description="", example="1000.0 W")


class HvacRTUsV1(BaseOpenEpdHierarchicalSpec):
    """An air handler designed for outdoor use, typically on roofs."""

    _EXT_VERSION = "1.0"


class HvacVrfSystemsV1(BaseOpenEpdHierarchicalSpec):
    """
    Variable refrigerant flow (VRF).

    Also known as variable refrigerant volume (VRV), is an HVAC technology that allows for varying degrees of cooling
    in more specific areas.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    HvacVrfControl: HvacVrfControlV1 | None = None
    HvacVrfIndoor: HvacVrfIndoorV1 | None = None
    HvacVrfOutdoor: HvacVrfOutdoorV1 | None = None


class MechanicalV1(BaseOpenEpdHierarchicalSpec):
    """Mechanical performance specification."""

    _EXT_VERSION = "1.0"

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
