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
from enum import StrEnum

import pydantic

from openepd.model.base import BaseOpenEpdSchema, BaseOpenEpdSpec
from openepd.model.validation import RatioFloat


class SteelMakingRoute(BaseOpenEpdSchema):
    """Steel making route."""

    bof: bool | None = pydantic.Field(default=None, title="Steel Making Route BOF", description="Basic oxygen furnace")
    eaf: bool | None = pydantic.Field(default=None, title="Steel Making Route EAF", description="Electric arc furnace")
    ohf: bool | None = pydantic.Field(default=None, title="Steel Making Route OHF", description="Open hearth furnace")


class SteelComposition(StrEnum):
    """Steel composition enum."""

    CARBON = "Carbon"
    ALLOY = "Alloy"
    STAINLESS = "Stainless"
    TOOL = "Tool"
    OTHER = "Other"


class Steel(BaseOpenEpdSpec):
    """Steel spec."""

    class Options(BaseOpenEpdSchema):
        """Steel spec options."""

        galvanized: bool | None = pydantic.Field(default=None, title="Galvanized")
        cold_finished: bool | None = pydantic.Field(default=None, title="Cold Finished")

    class Config:
        use_enum_values = False

    recycled_content: RatioFloat | None = pydantic.Field(
        default=None,
        title="Scrap Recycled Content",
        description="Scrap steel inputs from other processes.  Includes "
        "Post-Consumer content, if any.  This percentage may be "
        "used to evaluate the EPD w.r.t. targets or limits that are"
        " different for primary and recycled content.",
    )
    steel_composition: SteelComposition | None = pydantic.Field(
        default=None, title="Steel Composition", description="Basic chemical composition"
    )
    making_route: SteelMakingRoute | None = pydantic.Field(
        default=None, title="Steel Making Route", description="Steel making route"
    )
    options: Options | None = pydantic.Field(
        title="Steel Options", description="Steel options", default_factory=Options
    )


class RebarSteel(BaseOpenEpdSpec):
    """Rebar steel spec."""

    class Options(BaseOpenEpdSchema):
        """Rebar steel options."""

        epoxy: bool | None = pydantic.Field(default=None, title="Epoxy Coated")
        fabricated: bool | None = pydantic.Field(default=None, title="Fabricated", description="Fabricated")

    options: Options = pydantic.Field(
        title="Rebar Steel Options", description="Rebar Steel options", default_factory=Options
    )
