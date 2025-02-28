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
from typing import TypeAlias

import pydantic

from openepd.api.dto.base import BaseOpenEpdApiModel
from openepd.api.dto.common import BaseMeta, OpenEpdApiResponse
from openepd.api.dto.meta import PagingMetaMixin, WarningMetaMixin
from openepd.api.dto.mf import MaterialFilterMetaMixin
from openepd.model.common import Amount
from openepd.model.epd import Epd


class StatisticsDto(BaseOpenEpdApiModel):
    """
    DTO describes statistics of EPD.

    Statistics contains aggregated parameters such as percentiles distributions of GWP and other parameters.
    """

    # percentiles
    pct10_gwp: float = pydantic.Field(
        description="10th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )
    achievable_target: float = pydantic.Field(
        description="Achievable target. 20th percentile of GWP measured in kgCO2e per declared unit",
        examples=[445.65],
    )
    pct30_gwp: float = pydantic.Field(
        description="30th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )
    pct40_gwp: float = pydantic.Field(
        description="40th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )
    pct50_gwp: float = pydantic.Field(
        description="50th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )
    pct60_gwp: float = pydantic.Field(
        description="60th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )
    pct70_gwp: float = pydantic.Field(
        description="70th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )
    conservative_estimate: float = pydantic.Field(
        description="Conservative estimate. 80th percentile of GWP per declared unit measured in kgCO2e",
        examples=[640.778],
    )
    pct90_gwp: float = pydantic.Field(
        description="70th percentile GWP for this statistics measured in kgCO2e per declared unit"
    )

    # stats
    average: float = pydantic.Field(description="Average GWP in kgCO2e per declared unit", examples=[554.2])
    min: float | None = pydantic.Field(
        description="Min GWP of returned results measured in kgCO2e per declared unit",
        examples=[998.3],
    )
    max: float | None = pydantic.Field(
        description="Max GWP of returned results measured in kgCO2e per declared unit",
        examples=[120.0],
    )

    # percentiles w/out burden of doubt
    pct20_gwp_no_bod: float | None = pydantic.Field(
        description="20th percentile of GWP (kgCO2e per declared unit), no burden of doubt",
        examples=[120],
    )
    pct40_gwp_no_bod: float | None = pydantic.Field(
        description="40th percentile of GWP (kgCO2e per declared unit), no burden of doubt",
        examples=[120],
    )
    pct60_gwp_no_bod: float | None = pydantic.Field(
        description="60th percentile of GWP (kgCO2e per declared unit), no burden of doubt",
        examples=[120],
    )
    pct80_gwp_no_bod: float | None = pydantic.Field(
        description="80th percentile of GWP (kgCO2e per declared unit), no burden of doubt",
        examples=[120],
    )
    average_gwp_no_bod: float | None = pydantic.Field(description="Average GWP, no burden of doubt", examples=[120])

    # set parameters
    standard_deviation: float = pydantic.Field(description="Standard deviation", examples=[87.62])
    epds_count: int = pydantic.Field(description="Number of EPDs participated in statistics", examples=[55])
    industry_epds_count: int = pydantic.Field(
        description="Number of Industry-wide EPDs participated in statistics",
        examples=[4],
    )
    generic_estimates_count: int = pydantic.Field(
        description="Number of Generic Estimates participated in statistics",
        examples=[0],
    )

    declared_unit: Amount = pydantic.Field(
        description="Declared unit for the statistics. "
        "Statistical values - percentiles, averages etc - are based on this unit of product"
    )


class EpdSearchMeta(MaterialFilterMetaMixin, PagingMetaMixin, WarningMetaMixin, BaseMeta):
    """Metadata for EPD Search endpoint."""

    pass


class EpdStatisticsMeta(MaterialFilterMetaMixin, WarningMetaMixin, BaseMeta):
    """Metadata for EPD Statistics endpoint."""

    pass


EpdSearchResponse: TypeAlias = OpenEpdApiResponse[list[Epd], EpdSearchMeta]
EpdStatisticsResponse: TypeAlias = OpenEpdApiResponse[StatisticsDto, EpdStatisticsMeta]
