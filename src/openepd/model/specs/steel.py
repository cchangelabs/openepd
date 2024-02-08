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
from typing import Annotated, Literal

import pydantic

from openepd.model.base import BaseOpenEpdSchema, BaseOpenEpdSpec


class SteelMakingRoute(BaseOpenEpdSchema):
    bof: bool | None = pydantic.Field(default=None, title="Steel Making Route BOF", description="Basic oxygen furnace")
    eaf: bool | None = pydantic.Field(default=None, title="Steel Making Route EAF", description="Electric arc furnace")
    ohf: bool | None = pydantic.Field(default=None, title="Steel Making Route OHF", description="Open hearth furnace")


class SteelComposition(StrEnum):
    CARBON = "Carbon"
    ALLOY = "Alloy"
    STAINLESS = "Stainless"
    TOOL = "Tool"
    OTHER = "Other"


RatioFloat = Annotated[float, pydantic.Field(ge=0, le=1)]


class Steel(BaseOpenEpdSpec):
    class Config:
        use_enum_values = False


class SteelV1(Steel):
    class Options(BaseOpenEpdSchema):
        galvanized: bool | None = pydantic.Field(default=None, title="Galvanized")
        cold_finished: bool | None = pydantic.Field(default=None, title="Cold Finished")

    def __init__(self, *args, version=1, **kwargs):
        super().__init__(*args, version=version, **kwargs)

    version: Literal[1] = pydantic.Field(default=1, title="Version 1")

    recycled_content: RatioFloat | None = pydantic.Field(
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
    options: Options | None = pydantic.Field(
        title="Steel Options", description="Steel options", default_factory=Options
    )


class SteelV2(Steel):
    def __init__(self, *args, version=2, **kwargs):
        super().__init__(*args, version=version, **kwargs)

    version: Literal[2] = pydantic.Field(default=2, title="Version 2", const=True)
    steel_composition: SteelComposition | None = pydantic.Field(
        default=None, title="Steel Composition", description="Basic chemical composition"
    )


class RebarSteel(BaseOpenEpdSpec):
    pass


class RebarSteelV1(RebarSteel):
    class Options(BaseOpenEpdSchema):
        epoxy: bool | None = pydantic.Field(default=None, title="Epoxy Coated")
        fabricated: bool | None = pydantic.Field(default=None, title="Fabricated", description="Fabricated")

    def __init__(self, *args, version=1, **kwargs):
        super().__init__(*args, version=version, **kwargs)

    version: Literal[1] = pydantic.Field(default=1, title="Version 1")

    options: Options = pydantic.Field(
        title="Rebar Steel Options", description="Rebar Steel options", default_factory=Options
    )


SteelAllVersions = Annotated[SteelV1 | SteelV2, pydantic.Field(discriminator="version")]
RebarSteelAllVersions = RebarSteelV1
