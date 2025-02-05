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
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.base import BaseOpenEpdSpec
from openepd.model.validation.numbers import RatioFloat


class ConcreteTypicalApplication(BaseOpenEpdSpec):
    """Typical Application for Concrete."""

    fnd: bool | None = pyd.Field(
        description="Foundation. Typically used in direct contact with soil, e.g. footings, piles, mass concrete, "
        "mat foundations, and similar applications.",
        example=True,
        default=None,
    )
    sog: bool | None = pyd.Field(
        description="Slab on Grade. Typically used in continuously supported horizontal "
        "applications e.g. slab on grade, topping slabs, sidewalks, and roadways.",
        example=True,
        default=None,
    )
    hrz: bool | None = pyd.Field(
        description="Elevated Horizontal. Typically used in elevated horizontal applications, either on metal deck or "
        "where soffit formwork must be removed, e.g. post-tension plates, rebar plates, beams and slabs, "
        "waffle slabs.",
        example=True,
        default=None,
    )
    vrt_wall: bool | None = pyd.Field(description="Vertical Wall.", example=True, default=None)
    vrt_column: bool | None = pyd.Field(description="Vertical Column.", example=True, default=None)
    vrt_other: bool | None = pyd.Field(
        description="Vertical Other. Typically used in vertical applications other than "
        "walls or columns, e.g. sloped surfaces where formwork is required "
        "on multiple faces.",
        example=True,
        default=None,
    )
    sht: bool | None = pyd.Field(
        description="Shotcrete. Pneumatically applied, without formwork on all sides.", example=True, default=None
    )
    cdf: bool | None = pyd.Field(
        description="Flowable Fill (CDF). Typically used to fill voids, backfill retaining "
        "walls, as a sub-base, and similar applications. Also called Controlled "
        "Density Fill (CDF) or Controlled Low Strength Materials (CLSM).",
        example=True,
        default=None,
    )
    sac: bool | None = pyd.Field(
        description="Typically used in concrete sidewalks and barrier curbs.", example=True, default=None
    )
    pav: bool | None = pyd.Field(description="Typically used in pervious concrete", example=True, default=None)
    oil: bool | None = pyd.Field(
        description="Concretes for use in creation, maintenance, and decommissioning of "
        "petroleum extraction wells and similar applications. Includes foamed "
        "cement; often called cement in the drilling industry. Differs from "
        "flowable fill and grout in that it contains no sand or other aggregates.",
        example=True,
        default=None,
    )
    grt: bool | None = pyd.Field(
        description="Cement grouting is a slurry that is placed as a flowable liquid. It is "
        "an effective material for filling and strengthening granular soils, "
        "voids in rocks, foundation underpinnings, and other underground voids. "
        "Also called structural grout, these materials typically impart"
        " significant strength to the system",
        example=True,
        default=None,
    )
    ota: bool | None = pyd.Field(
        description="Typical application not covered by other values.", example=True, default=None
    )


class Cementitious(BaseOpenEpdSchema):
    """List of cementitious materials, and proportion by mass."""

    opc: RatioFloat | None = pyd.Field(
        default=None, description="Ordinary Gray Portland Cement", example=0.5, ge=0, le=1
    )
    wht: RatioFloat | None = pyd.Field(default=None, description="White Portland Cement", example=0.5, ge=0, le=1)
    ggbs: RatioFloat | None = pyd.Field(
        default=None, description="Ground Granulated Blast Furnace Slag", example=0.5, ge=0, le=1
    )
    flyAsh: RatioFloat | None = pyd.Field(
        default=None, description="Fly Ash, including types F, CL, and CH", example=0.5, ge=0, le=1
    )
    siFume: RatioFloat | None = pyd.Field(default=None, description="Silica Fume", example=0.5, ge=0, le=1)
    gg45: RatioFloat | None = pyd.Field(
        default=None, description="Ground Glass, 45um or smaller", example=0.5, ge=0, le=1
    )
    natPoz: RatioFloat | None = pyd.Field(default=None, description="Natural pozzolan", example=0.5, ge=0, le=1)
    mk: RatioFloat | None = pyd.Field(default=None, description="Metakaolin", example=0.5, ge=0, le=1)
    CaCO3: RatioFloat | None = pyd.Field(default=None, description="Limestone", example=0.5, ge=0, le=1)
    other: RatioFloat | None = pyd.Field(default=None, description="Other SCMs", example=0.5, ge=0, le=1)
