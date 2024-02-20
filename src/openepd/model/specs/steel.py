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

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.numbers import RatioFloat


class SteelMakingRoute(BaseOpenEpdSchema):
    """Steel making route."""

    bof: bool | None = pyd.Field(default=None, title="Steel Making Route BOF", description="Basic oxygen furnace")
    eaf: bool | None = pyd.Field(default=None, title="Steel Making Route EAF", description="Electric arc furnace")
    ohf: bool | None = pyd.Field(default=None, title="Steel Making Route OHF", description="Open hearth furnace")


class SteelComposition(StrEnum):
    """Steel composition enum."""

    CARBON = "Carbon"
    ALLOY = "Alloy"
    STAINLESS = "Stainless"
    TOOL = "Tool"
    OTHER = "Other"


class RebarSteelV1(BaseOpenEpdHierarchicalSpec):
    """Rebar steel spec."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema):
        """Rebar steel options."""

        epoxy: bool | None = pyd.Field(default=None, title="Epoxy Coated")
        fabricated: bool | None = pyd.Field(default=None, title="Fabricated", description="Fabricated")

    options: Options = pyd.Field(
        title="Rebar Steel Options", description="Rebar Steel options", default_factory=Options
    )


class SteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel spec."""

    _EXT_VERSION = "1.0"

    class Options(BaseOpenEpdSchema):
        """Steel spec options."""

        galvanized: bool | None = pyd.Field(default=None, title="Galvanized")
        cold_finished: bool | None = pyd.Field(default=None, title="Cold Finished")

    recycled_content: RatioFloat | None = pyd.Field(
        default=None,
        title="Scrap Recycled Content",
        description="Scrap steel inputs from other processes.  Includes "
        "Post-Consumer content, if any.  This percentage may be "
        "used to evaluate the EPD w.r.t. targets or limits that are"
        " different for primary and recycled content.",
    )
    steel_composition: SteelComposition | None = pyd.Field(
        default=None, title="Steel Composition", description="Basic chemical composition"
    )
    making_route: SteelMakingRoute | None = pyd.Field(
        default=None, title="Steel Making Route", description="Steel making route"
    )
    options: Options | None = pyd.Field(description="Steel options", default_factory=Options)

    # Nested specs
    RebarSteel: RebarSteelV1 | None = None
