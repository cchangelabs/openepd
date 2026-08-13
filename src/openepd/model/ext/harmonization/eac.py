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
from enum import StrEnum

from openepd.compat.pydantic import pyd
from openepd.model.ext.harmonization.base import HarmonizationFactorBase


class EacStandard(StrEnum):
    """Energy Attribute Certificate accounting standards."""

    GRID = "Grid"
    GREEN_E_REC = "Green-e REC"
    EN16325_GOO = "EN16325 GoO"
    PPA = "PPA"
    OTHER = "Other"


class EacCoverage(StrEnum):
    """Scope of EAC retirement coverage for the product/facility/manufacturer."""

    SELECTED_PRODUCTS = "Selected Products"
    ENTIRE_FACILITY = "Entire Facility"
    MANUFACTURER_WIDE = "Manufacturer-wide"


class EacHarmonizationFactor(HarmonizationFactorBase):
    """Documents the use and effects of EACs (e.g., RECs and GoOs) rather than grid emissions."""

    eac_standard: EacStandard | None = pyd.Field(
        alias="EAC_standard",
        default=None,
        description="EAC accounting standard applied to electricity claims.",
        example=EacStandard.GREEN_E_REC,
    )
    eac_standard_version: str | None = pyd.Field(
        alias="EAC_standard_version",
        default=None,
        description="Version of the EAC standard.",
        example="4.5",
        min_length=1,
        max_length=50,
    )
    eac_coverage: EacCoverage | None = pyd.Field(
        alias="EAC_coverage",
        default=None,
        description="Coverage scope over which EACs are retired.",
        example=EacCoverage.ENTIRE_FACILITY,
    )
    eac_verification_link: pyd.AnyUrl | None = pyd.Field(
        alias="EAC_verification_link",
        default=None,
        description="Link confirming retirement of sufficient EACs up to product delivery date.",
    )
