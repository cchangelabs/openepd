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


class OffsetCoverage(StrEnum):
    """
    Scope over which offsets are retired.

    * `Selected Products`: Offsets are bundled with this product, but not all products at the facility.
    * `Entire Facility`: Offsets are retired equally for all products made at the facility/facilities.
    * `Manufacturer`: Offsets are retired equally for all products manufactured by the manufacturer.
    """

    SELECTED_PRODUCTS = "Selected Products"
    ENTIRE_FACILITY = "Entire Facility"
    MANUFACTURER = "Manufacturer"


class OffsetStandard(StrEnum):
    """Offset standards/programs used for retirement or registration."""

    NO_OFFSETS = "No Offsets"
    VCS = "VCS"
    GOLD = "Gold"
    ACR = "ACR"
    CAR = "CAR"
    CARB = "CARB"
    EU_ETS = "EU ETS"
    CORSIA = "CORSIA"


class OffsetsHarmonizationFactor(HarmonizationFactorBase):
    """Documents offsets used for electricity and related reported impact adjustments."""

    offset_standards: list[OffsetStandard] = pyd.Field(
        default_factory=list,
        description="List of offset standards the offsets comply with or are registered to.",
    )
    offset_standard_version: str | None = pyd.Field(
        default=None,
        description="Version of the offset standard.",
        example="4.5",
        min_length=1,
        max_length=50,
    )
    offset_coverage: OffsetCoverage | None = pyd.Field(
        default=None,
        description="Coverage scope over which offsets are retired.",
        example=OffsetCoverage.ENTIRE_FACILITY,
    )
    offset_verification_link: pyd.AnyUrl | None = pyd.Field(
        default=None,
        description="Link confirming retirement of sufficient offsets up to product delivery date.",
    )
