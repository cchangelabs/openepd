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
    "ConveyingEquipmentRangeV1",
    "ElevatorsRangeV1",
    "EscalatorsRangeV1",
)

import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import ElevatorsBuildingRise, ElevatorsUsageIntensity
from openepd.model.validation.quantity import (
    AmountRangeCapacityPerHour,
    AmountRangeLengthMm,
    AmountRangeMass,
    AmountRangeSpeed,
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class EscalatorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Escalators category performance specification.

    A moving staircase consisting of a circulating belt of steps driven by a motor,
    which conveys people between the floors of a building.

    Range version.
    """

    _EXT_VERSION = "1.1"

    vertical_rise: AmountRangeLengthMm | None = pydantic.Field(
        default=None,
        description="The vertical distance between the top and bottom landings of an escalator",
    )
    speed: AmountRangeSpeed | None = pydantic.Field(default=None, description="Reference speed of the escalator")
    step_width: AmountRangeLengthMm | None = pydantic.Field(default=None, description="Width of the escalator steps")
    max_capacity: AmountRangeCapacityPerHour | None = pydantic.Field(
        default=None, description="Max capacity of escalator in persons per hour"
    )
    indoor: bool | None = pydantic.Field(default=None, description="Escalator can be used for indoor applications")
    outdoor: bool | None = pydantic.Field(default=None, description="Escalator can be used for outdoor applications")


class ElevatorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Car that moves in a vertical shaft to carry passengers or freight between the levels of a multistory building.

    Range version.
    """

    _EXT_VERSION = "1.0"

    usage_intensity: list[ElevatorsUsageIntensity] | None = pydantic.Field(default=None, description="")
    travel_length: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    rated_load: AmountRangeMass | None = pydantic.Field(default=None, description="")
    rated_speed: AmountRangeSpeed | None = pydantic.Field(default=None, description="")
    building_rise: list[ElevatorsBuildingRise] | None = pydantic.Field(default=None, description="")


class ConveyingEquipmentRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Conveying Equipment.

    Range version.
    """

    _EXT_VERSION = "1.1"

    Elevators: ElevatorsRangeV1 | None = None
    Escalators: EscalatorsRangeV1 | None = None
