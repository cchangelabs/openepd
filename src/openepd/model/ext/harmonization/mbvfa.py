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

import pydantic as pyd

from openepd.model.ext.harmonization.base import HarmonizationFactorBase


class MbvfaTrackingApproach(StrEnum):
    """
    Chain-of-custody/accounting approach used for MBVFA.

    * `physical`: Upstream impacts are based on estimated average content in final product and output flows using
      ISO 22095 physical chain-of-custody models such as identity preserved, segregated, controlled blending, or
      rolling average mass balance.
    * `credit-based-mass-balance`: ISO 22095 chain-of-custody model where materials with specified
      characteristics are mixed with other materials, and claims are tracked mathematically so total claimed does not
      exceed total consumed.
    * `book-and-claim`: ISO 22095 chain-of-custody model where the administrative record flow is not necessarily
      connected to physical flow (also called certificate or credit trading).
    """

    PHYSICAL = "physical"
    CREDIT_BASED_MASS_BALANCE = "credit-based-mass-balance"
    BOOK_AND_CLAIM = "book-and-claim"


class MbvfaAttribute(StrEnum):
    """Input attribute being allocated through MBVFA accounting."""

    RECYCLED_CONTENT = "recycled-content"
    BIOBASED_CONTENT = "biobased-content"


class MbvfaHarmonizationFactor(HarmonizationFactorBase):
    """Mass Balanced Virtual Feedstock Allocation (MBVFA) harmonization factor."""

    tracking_approach: MbvfaTrackingApproach | None = pyd.Field(
        default=None,
        description="Mass-balance or book-and-claim tracking approach used for allocation.",
        examples=[MbvfaTrackingApproach.BOOK_AND_CLAIM],
    )
    attribute: MbvfaAttribute | None = pyd.Field(
        default=None,
        description="Allocated low-emitting input attribute represented by this factor.",
        examples=[MbvfaAttribute.RECYCLED_CONTENT],
    )
