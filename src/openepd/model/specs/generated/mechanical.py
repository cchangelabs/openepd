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
from openepd.model.validation.quantity import PressureMPaStr, validate_unit_factory


class HvacVrfControlV1(BaseOpenEpdHierarchicalSpec):
    """Hvac vrf control performance specification."""

    _EXT_VERSION = "1.0"


class HvacVrfIndoorV1(BaseOpenEpdHierarchicalSpec):
    """Hvac vrf indoor performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    heating_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    cooling_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    airflow_rate: str | None = pyd.Field(default=None, description="", example="1 m3 / s")
    air_volume: str | None = pyd.Field(default=None, description="", example="1 m3")

    _heating_capacity_is_quantity_validator = pyd.validator("heating_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _cooling_capacity_is_quantity_validator = pyd.validator("cooling_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _airflow_rate_is_quantity_validator = pyd.validator("airflow_rate", allow_reuse=True)(
        validate_unit_factory("m3 / s")
    )
    _air_volume_is_quantity_validator = pyd.validator("air_volume", allow_reuse=True)(validate_unit_factory("m3"))


class HvacVrfOutdoorV1(BaseOpenEpdHierarchicalSpec):
    """Hvac vrf outdoor performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    heating_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    cooling_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    airflow_rate: str | None = pyd.Field(default=None, description="", example="1 m3 / s")
    air_volume: str | None = pyd.Field(default=None, description="", example="1 m3")

    _heating_capacity_is_quantity_validator = pyd.validator("heating_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _cooling_capacity_is_quantity_validator = pyd.validator("cooling_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _airflow_rate_is_quantity_validator = pyd.validator("airflow_rate", allow_reuse=True)(
        validate_unit_factory("m3 / s")
    )
    _air_volume_is_quantity_validator = pyd.validator("air_volume", allow_reuse=True)(validate_unit_factory("m3"))


class HvacAirDiffusersV1(BaseOpenEpdHierarchicalSpec):
    """Hvac air diffusers performance specification."""

    _EXT_VERSION = "1.0"


class HvacAirFiltersV1(BaseOpenEpdHierarchicalSpec):
    """Hvac air filters performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    merv_rating: AirFiltersMervRating | None = pyd.Field(default=None, description="", example="MERV 1")
    media_type: AirFiltersMediaType | None = pyd.Field(default=None, description="", example="Acrylic")


class HvacAHUsV1(BaseOpenEpdHierarchicalSpec):
    """Hvac a h us performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    installation: MechanicalInstallation | None = pyd.Field(default=None, description="", example="Indoor")
    airflow_rate: str | None = pyd.Field(default=None, description="", example="1 m3 / s")
    air_volume: str | None = pyd.Field(default=None, description="", example="1 m3")
    cooling_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    heating_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    airflow_control: AhuAirflowControl | None = pyd.Field(default=None, description="", example="CAV")
    zone_control: AhuZoneControl | None = pyd.Field(default=None, description="", example="Single Zone")

    _airflow_rate_is_quantity_validator = pyd.validator("airflow_rate", allow_reuse=True)(
        validate_unit_factory("m3 / s")
    )
    _air_volume_is_quantity_validator = pyd.validator("air_volume", allow_reuse=True)(validate_unit_factory("m3"))
    _cooling_capacity_is_quantity_validator = pyd.validator("cooling_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _heating_capacity_is_quantity_validator = pyd.validator("heating_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )


class HvacBoilersV1(BaseOpenEpdHierarchicalSpec):
    """Hvac boilers performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    flow_rate: str | None = pyd.Field(default=None, description="", example="1 l / min")
    heating_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    configuration: BoilerConfiguration | None = pyd.Field(default=None, description="", example="Hot water")
    fuel_type: BoilerEquipmentFuelType | None = pyd.Field(default=None, description="", example="Coal")

    _flow_rate_is_quantity_validator = pyd.validator("flow_rate", allow_reuse=True)(validate_unit_factory("l / min"))
    _heating_capacity_is_quantity_validator = pyd.validator("heating_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )


class HvacChillersV1(BaseOpenEpdHierarchicalSpec):
    """Hvac chillers performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    installation: MechanicalInstallation | None = pyd.Field(default=None, description="", example="Indoor")
    heating_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    cooling_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    air_volume: str | None = pyd.Field(default=None, description="", example="1 m3")
    airflow_rate: str | None = pyd.Field(default=None, description="", example="1 m3 / s")

    _heating_capacity_is_quantity_validator = pyd.validator("heating_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _cooling_capacity_is_quantity_validator = pyd.validator("cooling_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _air_volume_is_quantity_validator = pyd.validator("air_volume", allow_reuse=True)(validate_unit_factory("m3"))
    _airflow_rate_is_quantity_validator = pyd.validator("airflow_rate", allow_reuse=True)(
        validate_unit_factory("m3 / s")
    )


class HvacFansV1(BaseOpenEpdHierarchicalSpec):
    """Hvac fans performance specification."""

    _EXT_VERSION = "1.0"


class HvacHeatPumpsV1(BaseOpenEpdHierarchicalSpec):
    """Hvac heat pumps performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    cooling_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    heating_capacity: str | None = pyd.Field(default=None, description="", example="1000.0 W")
    air_volume: str | None = pyd.Field(default=None, description="", example="1 m3")
    airflow_rate: str | None = pyd.Field(default=None, description="", example="1 m3 / s")
    heat_pumps_type: HeatPumpType | None = pyd.Field(default=None, description="", example="Air-to-Water")

    _cooling_capacity_is_quantity_validator = pyd.validator("cooling_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _heating_capacity_is_quantity_validator = pyd.validator("heating_capacity", allow_reuse=True)(
        validate_unit_factory("W")
    )
    _air_volume_is_quantity_validator = pyd.validator("air_volume", allow_reuse=True)(validate_unit_factory("m3"))
    _airflow_rate_is_quantity_validator = pyd.validator("airflow_rate", allow_reuse=True)(
        validate_unit_factory("m3 / s")
    )


class HvacHeatExV1(BaseOpenEpdHierarchicalSpec):
    """Hvac heat exchangers performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    refrigerants: list[MechanicalRefrigerants] | None = pyd.Field(default=None, description="", example=["R11"])
    heat_exchangers_type: HvacHeatExchangersType | None = pyd.Field(
        default=None, description="", example="Shell and Tube"
    )


class HvacPumpsV1(BaseOpenEpdHierarchicalSpec):
    """Hvac pumps performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    flow_rate: str | None = pyd.Field(default=None, description="", example="1 l / min")
    pump_discharge_pressure: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    pump_horsepower: str | None = pyd.Field(default=None, description="", example="1000.0 W")

    _flow_rate_is_quantity_validator = pyd.validator("flow_rate", allow_reuse=True)(validate_unit_factory("l / min"))
    _pump_discharge_pressure_is_quantity_validator = pyd.validator("pump_discharge_pressure", allow_reuse=True)(
        validate_unit_factory("MPa")
    )
    _pump_horsepower_is_quantity_validator = pyd.validator("pump_horsepower", allow_reuse=True)(
        validate_unit_factory("W")
    )


class HvacRTUsV1(BaseOpenEpdHierarchicalSpec):
    """Hvac r t us performance specification."""

    _EXT_VERSION = "1.0"


class HvacVrfSystemsV1(BaseOpenEpdHierarchicalSpec):
    """Hvac vrf systems performance specification."""

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
