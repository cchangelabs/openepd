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
    "HvacAHUsRangeV1",
    "HvacAirDiffusersRangeV1",
    "HvacAirFiltersRangeV1",
    "HvacBoilersRangeV1",
    "HvacChillersRangeV1",
    "HvacDuctsRangeV1",
    "HvacFansRangeV1",
    "HvacHeatExRangeV1",
    "HvacHeatPumpsRangeV1",
    "HvacPumpsRangeV1",
    "HvacRTUsRangeV1",
    "HvacVrfControlRangeV1",
    "HvacVrfIndoorRangeV1",
    "HvacVrfOutdoorRangeV1",
    "HvacVrfSystemsRangeV1",
    "MechanicalRangeV1",
)

import pydantic

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
from openepd.model.validation.quantity import (
    AmountRangeAirflow,
    AmountRangeAreaPerVolume,
    AmountRangePower,
    AmountRangePressureMpa,
    AmountRangeVolume,
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class HvacVrfControlRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Controller for adjusting airflow across the VRF system.

    Range version.
    """

    _EXT_VERSION = "1.0"


class HvacVrfIndoorRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Heating and cooling unit located on the inside of a building and supplies air to specific indoor zones.

    Range version.
    """

    _EXT_VERSION = "1.0"

    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="")
    heating_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    cooling_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    airflow_rate: AmountRangeAirflow | None = pydantic.Field(default=None, description="")
    air_volume: AmountRangeVolume | None = pydantic.Field(default=None, description="")


class HvacVrfOutdoorRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Heating and cooling unit that is on the outside of a building and distributes air to the indoor units.

    Range version.
    """

    _EXT_VERSION = "1.0"

    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="")
    heating_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    cooling_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    airflow_rate: AmountRangeAirflow | None = pydantic.Field(default=None, description="")
    air_volume: AmountRangeVolume | None = pydantic.Field(default=None, description="")


class HvacAirDiffusersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Room-side terminals for air distribution. This is different from Terminal Heating & Cooling Units.

    Range version.
    """

    _EXT_VERSION = "1.0"


class HvacAirFiltersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Device for filtering particles of dust, soot, etc., from the air passing through it.

    Range version.
    """

    _EXT_VERSION = "1.0"

    merv_rating: list[AirFiltersMervRating] | None = pydantic.Field(default=None, description="")
    media_type: list[AirFiltersMediaType] | None = pydantic.Field(default=None, description="")


class HvacAHUsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Device which provides healthy, dust free air to buildings with a good energy efficiency.

    Usually a large metal box containing a blower, heating or cooling elements, filter racks or chambers, sound
    attenuators, and dampers.

    Range version.
    """

    _EXT_VERSION = "1.0"

    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="")
    installation: list[MechanicalInstallation] | None = pydantic.Field(default=None, description="")
    airflow_rate: AmountRangeAirflow | None = pydantic.Field(default=None, description="")
    air_volume: AmountRangeVolume | None = pydantic.Field(default=None, description="")
    cooling_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    heating_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    airflow_control: list[AhuAirflowControl] | None = pydantic.Field(default=None, description="")
    zone_control: list[AhuZoneControl] | None = pydantic.Field(default=None, description="")


class HvacBoilersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Closed vessel for heating fluid.

    Range version.
    """

    _EXT_VERSION = "1.0"

    flow_rate: AmountRangeAreaPerVolume | None = pydantic.Field(default=None, description="")
    heating_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    configuration: list[BoilerConfiguration] | None = pydantic.Field(default=None, description="")
    fuel_type: list[BoilerEquipmentFuelType] | None = pydantic.Field(default=None, description="")


class HvacChillersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Machine that removes heat from a liquid coolant.

    Uses a vapor-compression, adsorption refrigeration, or absorption refrigeration cycles. Incldues centrifugal,
    water-cooled chillers, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="")
    installation: list[MechanicalInstallation] | None = pydantic.Field(default=None, description="")
    heating_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    cooling_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    air_volume: AmountRangeVolume | None = pydantic.Field(default=None, description="")
    airflow_rate: AmountRangeAirflow | None = pydantic.Field(default=None, description="")


class HvacFansRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Apparatus with rotating blades that creates a current of air for cooling or ventilation.

    Range version.
    """

    _EXT_VERSION = "1.0"


class HvacHeatPumpsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Device that transfers thermal energy between spaces, including ground and air source heat pumps.

    Range version.
    """

    _EXT_VERSION = "1.0"

    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="")
    cooling_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    heating_capacity: AmountRangePower | None = pydantic.Field(default=None, description="")
    air_volume: AmountRangeVolume | None = pydantic.Field(default=None, description="")
    airflow_rate: AmountRangeAirflow | None = pydantic.Field(default=None, description="")
    heat_pumps_type: list[HeatPumpType] | None = pydantic.Field(default=None, description="")


class HvacHeatExRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    HVAC heat exchangers.

    Systems that with heat exchange cell which recovers and retains the heat that would otherwise be lost from the
    extracted air.

    Range version.
    """

    _EXT_VERSION = "1.0"

    refrigerants: list[MechanicalRefrigerants] | None = pydantic.Field(default=None, description="")
    heat_exchangers_type: list[HvacHeatExchangersType] | None = pydantic.Field(default=None, description="")


class HvacPumpsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Pumps.

    Mechanical device using suction or pressure to raise or move liquids, compress gases, or force air into
    inflatable objects such as tires.

    Range version.
    """

    _EXT_VERSION = "1.0"

    flow_rate: AmountRangeAreaPerVolume | None = pydantic.Field(default=None, description="")
    pump_discharge_pressure: AmountRangePressureMpa | None = pydantic.Field(default=None, description="")
    pump_horsepower: AmountRangePower | None = pydantic.Field(default=None, description="")


class HvacRTUsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    An air handler designed for outdoor use, typically on roofs.

    Range version.
    """

    _EXT_VERSION = "1.0"


class HvacVrfSystemsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Variable refrigerant flow (VRF).

    Also known as variable refrigerant volume (VRV), is an HVAC technology that allows for varying degrees of cooling
    in more specific areas.

    Range version.
    """

    _EXT_VERSION = "1.0"

    HvacVrfControl: HvacVrfControlRangeV1 | None = None
    HvacVrfIndoor: HvacVrfIndoorRangeV1 | None = None
    HvacVrfOutdoor: HvacVrfOutdoorRangeV1 | None = None


class HvacDuctsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Ducts for HVAC systems performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

    shape: list[HvacDuctShape] | None = pydantic.Field(default=None, description="Hvac duct shape")
    material: list[HvacDuctMaterial] | None = pydantic.Field(default=None, description="Hvac duct material")
    type: list[HvacDuctType] | None = pydantic.Field(default=None, description="Hvac duct type")


class MechanicalRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Mechanical performance specification.

    Range version.
    """

    _EXT_VERSION = "1.1"

    HvacAirDiffusers: HvacAirDiffusersRangeV1 | None = None
    HvacAirFilters: HvacAirFiltersRangeV1 | None = None
    HvacAHUs: HvacAHUsRangeV1 | None = None
    HvacBoilers: HvacBoilersRangeV1 | None = None
    HvacChillers: HvacChillersRangeV1 | None = None
    HvacFans: HvacFansRangeV1 | None = None
    HvacHeatPumps: HvacHeatPumpsRangeV1 | None = None
    HvacHeatEx: HvacHeatExRangeV1 | None = None
    HvacPumps: HvacPumpsRangeV1 | None = None
    HvacRTUs: HvacRTUsRangeV1 | None = None
    HvacVrfSystems: HvacVrfSystemsRangeV1 | None = None
    HvacDucts: HvacDuctsRangeV1 | None = None
