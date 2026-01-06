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
from openepd.model.specs.enums import ElevatorsBuildingRise, ElevatorsUsageIntensity
from openepd.model.validation.quantity import CapacityPerHourStr, LengthMStr, MassKgStr, SpeedStr


class EscalatorsV1(BaseOpenEpdHierarchicalSpec):
    """
    Escalators category performance specification.

    A moving staircase consisting of a circulating belt of steps driven by a motor,
    which conveys people between the floors of a building.
    """

    vertical_rise: LengthMStr | None = pydantic.Field(
        default=None,
        description="The vertical distance between the top and bottom landings of an escalator",
        examples=["1 m"],
    )
    speed: SpeedStr | None = pydantic.Field(
        default=None,
        description="Reference speed of the escalator",
        examples=["1 m / s"],
    )
    step_width: LengthMStr | None = pydantic.Field(
        default=None, description="Width of the escalator steps", examples=["1 m"]
    )
    max_capacity: CapacityPerHourStr | None = pydantic.Field(
        default=None,
        description="Max capacity of escalator in persons per hour",
        examples=["1 hour^-1"],
    )
    indoor: bool | None = pydantic.Field(
        default=None,
        description="Escalator can be used for indoor applications",
        examples=[True],
    )
    outdoor: bool | None = pydantic.Field(
        default=None,
        description="Escalator can be used for outdoor applications",
        examples=[True],
    )

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="Escalators",
        display_name="Escalators",
        historical_names=["Conveying Equipment >> Escalators"],
        description="A moving staircase consisting of a circulating belt of steps driven by a motor, which conveys people between the floors of a building",
        masterformat="14 31 00 Escalators",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElevatorsV1(BaseOpenEpdHierarchicalSpec):
    """Car that moves in a vertical shaft to carry passengers or freight between the levels of a multistory building."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Elevators",
        display_name="Elevators",
        historical_names=["Conveying Equipment >> Elevators"],
        description="Car that moves in a vertical shaft to carry passengers or freight between the levels of a multistory building.",
        masterformat="14 20 00 Elevators",
        declared_unit=Amount(qty=1, unit="tkm"),
    )

    # Own fields:
    usage_intensity: list[ElevatorsUsageIntensity] | None = pydantic.Field(
        default=None, description="", examples=[["Very low"]]
    )
    travel_length: LengthMStr | None = pydantic.Field(default=None, description="", examples=["1 m"])
    rated_load: MassKgStr | None = pydantic.Field(default=None, description="", examples=["1 kg"])
    rated_speed: SpeedStr | None = pydantic.Field(default=None, description="", examples=["1 m / s"])
    building_rise: ElevatorsBuildingRise | None = pydantic.Field(default=None, description="", examples=["Low-rise"])


class ConveyingEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Conveying Equipment."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="ConveyingEquipment",
        display_name="Conveying Equipment",
        description="Conveying Equipment",
        masterformat="14 00 00 Conveying Equipment",
        declared_unit=Amount(qty=1, unit="tkm"),
    )

    # Nested specs:
    Elevators: ElevatorsV1 | None = None
    Escalators: EscalatorsV1 | None = None
