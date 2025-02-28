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
import pydantic

from openepd.api.dto.base import BaseMetaDto, BaseOpenEpdApiModel


class PerformanceMeta(BaseMetaDto):
    """Meta for performance information."""

    execution_time_ms: int


class PerformanceMetaMixin(BaseMetaDto):
    """Mixin for adding performance meta to MetaCollection."""

    performance: PerformanceMeta | None = None


class PagingMeta(BaseMetaDto):
    """Meta for paging information."""

    total_count: int = pydantic.Field(
        title="Total results",
        examples=[1233],
        description="Total number of records for the search",
    )
    total_pages: int = pydantic.Field(title="Total pages", examples=[20], description="Total pages available")
    page_size: int = pydantic.Field(title="Page size", examples=[150], description="Number of records in page")


class PagingMetaMixin(BaseOpenEpdApiModel):
    """Mixin for adding paging meta to MetaCollection."""

    paging: PagingMeta | None = pydantic.Field(default=None, description="Paging information")


class WarningMessageDto(BaseOpenEpdApiModel):
    """DTO for warning messages."""

    message: str = pydantic.Field(
        title="Warning message",
        examples=["Categories limited during search, see effective_omf in meta"],
    )
    code: str = pydantic.Field(title="Warning code", examples=["CATEGORIES_LIMITED"])
    field: str | None = pydantic.Field(
        title="Field",
        description="Field to which the warning relates",
        examples=["subcategories"],
    )


class WarningMetaMixin(BaseOpenEpdApiModel):
    """Mixin for adding warnings meta to MetaCollection."""

    warnings: list[WarningMessageDto] | None = None
