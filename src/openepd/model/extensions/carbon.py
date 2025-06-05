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

from openepd.model.base import OpenEpdExtension
from openepd.model.lcia import ScopeSet


class CarbonIndicatorsExtension(OpenEpdExtension):
    """Extension for carbon indicators in openEPD documents."""

    @classmethod
    def get_extension_name(cls) -> str:
        """Return the name of the extension."""
        return "carbon_indicators"

    ghg_luc: ScopeSet | None = pydantic.Field(
        default=None,
        description="GHG emissions from land use change",
    )
    bcpr: ScopeSet | None = pydantic.Field(
        default=None,
        description="Biogenic carbon removals associated with biogenic carbon content contained within "
        "bio‑based products",
    )
    bcpe: ScopeSet | None = pydantic.Field(
        default=None,
        description="Biogenic carbon emissions associated with biogenic carbon content contained within "
        "bio‑based productss",
    )
    bcwr: ScopeSet | None = pydantic.Field(
        default=None,
        description="Biogenic carbon emissions from combustion of waste from renewable resources used in "
        "production processes",
    )
    bcwn: ScopeSet | None = pydantic.Field(
        default=None,
        description="Carbon emissions from combustion of waste from non‑renewable resources used in "
        "production processes",
    )
    ccal: ScopeSet | None = pydantic.Field(
        default=None,
        description="Carbon emissions from calculation",
    )
    ccar: ScopeSet | None = pydantic.Field(
        default=None,
        description="Carbon removals from carbonation",
    )
