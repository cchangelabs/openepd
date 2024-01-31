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
from typing import Annotated

import pydantic

from openepd.model.base import BaseOpenEpdSpec


class SteelMakingRoute(BaseOpenEpdSpec):
    bof: bool | None = pydantic.Field(default=None, title="Steel Making Route BOF", description="Basic Oxygen Furnace")
    eaf: bool | None = pydantic.Field(default=None, title="Steel Making Route EAF", description="Electric Arc Furnace")
    ohf: bool | None = pydantic.Field(default=None, title="Steel Making Route OHF", description="Open Hearth Furnace")


RatioFloat = Annotated[float, pydantic.Field(ge=0, le=1)]


class Steel(BaseOpenEpdSpec):
    scrap_recycling_content: RatioFloat | None = pydantic.Field(
        default=None,
        title="Scrap Recycled Content",
        description="Scrap steel inputs from other processes.  Includes "
        "Post-Consumer content, if any.  This percentage may be "
        "used to evaluate the EPD w.r.t. targets or limits that are"
        " different for primary and recycled content.",
    )
    making_route: SteelMakingRoute | None = pydantic.Field(
        default=None, title="Steel Making Route", description="Steel making route"
    )


class RebarSteel(BaseOpenEpdSpec):
    steel_fabricated: bool | None = pydantic.Field(
        default=None, title="Steel Fabricated", description="Steel fabricated"
    )
