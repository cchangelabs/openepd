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

from openepd.api.dto.base import BaseOpenEpdApiModel


class MaterialFilterDefinition(BaseOpenEpdApiModel):
    """
    Material filter definition.

    This object includes material filter itself as well as its hash.
    """

    mf: str = pydantic.Field(
        title="MaterialFilter",
        examples=['!EC3 search("AluminiumBillets") !pragma oMF("1.0/1")'],
        description="MaterialFilter in string format",
    )
    mf_hash: str = pydantic.Field(
        title="MaterialFilter hash",
        examples=["22bf5b78cee5b79e1c76e818873d521c3972688b"],
        description="MaterialFilter hash. Can be used to compare filters for equality, put to cache etc.",
    )


class MaterialFilterMeta(BaseOpenEpdApiModel):
    """Meta holding supplementary information about OMF query execution."""

    excluded_fields: list[str] | None = pydantic.Field(
        examples=[["building_jurisdiction", "jurisdiction"]],
        description="list of fields excluded by server process for any reason",
        default=None,
    )
    effective_omf: MaterialFilterDefinition = pydantic.Field(
        description="Effective OpenMaterialFilter as applied to search, after transformations if any"
    )


class MaterialFilterMetaMixin(BaseOpenEpdApiModel):
    """Mixing for adding MaterialFilterMeta to MetaCollection."""

    material_filter: MaterialFilterMeta | None
