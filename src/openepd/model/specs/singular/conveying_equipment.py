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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import ElevatorsBuildingRise, ElevatorsUsageIntensity
from openepd.model.validation.quantity import CapacityPerHourStr, LengthMStr, MassKgStr, SpeedStr


class EscalatorsV1(BaseOpenEpdHierarchicalSpec):
    """
    Escalators category performance specification.

    A moving staircase consisting of a circulating belt of steps driven by a motor,
    which conveys people between the floors of a building.
    """

    vertical_rise: LengthMStr | None = pyd.Field(
        default=None,
        description="The vertical distance between the top and bottom landings of an escalator",
        example="1 m",
    )
    speed: SpeedStr | None = pyd.Field(default=None, description="Reference speed of the escalator", example="1 m / s")
    step_width: LengthMStr | None = pyd.Field(default=None, description="Width of the escalator steps", example="1 m")
    max_capacity: CapacityPerHourStr | None = pyd.Field(
        default=None, description="Max capacity of escalator in persons per hour", example="1 hour^-1"
    )
    indoor: bool | None = pyd.Field(
        default=None, description="Escalator can be used for indoor applications", example=True
    )
    outdoor: bool | None = pyd.Field(
        default=None, description="Escalator can be used for outdoor applications", example=True
    )

    _EXT_VERSION = "1.1"


class ElevatorsV1(BaseOpenEpdHierarchicalSpec):
    """Car that moves in a vertical shaft to carry passengers or freight between the levels of a multistory building."""

    _EXT_VERSION = "1.0"

    # Own fields:
    usage_intensity: list[ElevatorsUsageIntensity] | None = pyd.Field(
        default=None, description="", example=["Very low"]
    )
    travel_length: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    rated_load: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    rated_speed: SpeedStr | None = pyd.Field(default=None, description="", example="1 m / s")
    building_rise: ElevatorsBuildingRise | None = pyd.Field(default=None, description="", example="Low-rise")


class ConveyingEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Conveying Equipment."""

    _EXT_VERSION = "1.1"

    # Nested specs:
    Elevators: ElevatorsV1 | None = None
    Escalators: EscalatorsV1 | None = None
