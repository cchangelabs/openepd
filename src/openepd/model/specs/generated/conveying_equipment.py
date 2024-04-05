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
from openepd.model.specs.generated.enums import ElevatorsBuildingRise, ElevatorsUsageIntensity
from openepd.model.validation.quantity import LengthMStr, MassKgStr, validate_unit_factory


class ElevatorsV1(BaseOpenEpdHierarchicalSpec):
    """Elevators performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    elevators_usage_intensity: list[ElevatorsUsageIntensity] | None = pyd.Field(
        default=None, description="", example="['Very low']"
    )
    elevators_travel_length: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    elevators_rated_load: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    elevators_rated_speed: str | None = pyd.Field(default=None, description="", example="1 m / s")
    elevators_building_rise: ElevatorsBuildingRise | None = pyd.Field(default=None, description="", example="Low-rise")

    _elevators_travel_length_is_quantity_validator = pyd.validator("elevators_travel_length", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _elevators_rated_load_is_quantity_validator = pyd.validator("elevators_rated_load", allow_reuse=True)(
        validate_unit_factory("kg")
    )
    _elevators_rated_speed_is_quantity_validator = pyd.validator("elevators_rated_speed", allow_reuse=True)(
        validate_unit_factory("m / s")
    )


class ConveyingEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Conveying equipment performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Elevators: ElevatorsV1 | None = None