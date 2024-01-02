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
import datetime
from enum import StrEnum
from typing import Annotated, Optional

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.org import Org


class PcrStatus(StrEnum):
    """Status of a PCR."""

    InDevelopment = "InDevelopment"
    Published = "Published"
    NonPublic = "NonPublic"
    Expired = "Expired"
    Sunset = "Sunset"


class Pcr(WithAttachmentsMixin, WithAltIdsMixin, BaseOpenEpdSchema):
    """Represent a PCR (Product Category Rules)."""

    id: str | None = pyd.Field(
        description="The unique ID for this PCR.  To ensure global uniqueness, should be registered "
        "at open-xpd-uuid.cqd.io/register or a coordinating registry.",
        example="ec3xpgq2",
        default=None,
    )
    issuer: Org | None = pyd.Field(description="Organization issuing this PCR", default=None)
    issuer_doc_id: str | None = pyd.Field(
        max_length=40,
        default=None,
        description="Document ID or code created by issuer",
        example="c-PCR-003",
    )
    name: str | None = pyd.Field(
        max_length=200,
        default=None,
        description="Full document name as listed in source document",
        example="c-PCR-003 Concrete and concrete elements (EN 16757)",
    )
    short_name: str | None = pyd.Field(
        default=None,
        description="A shortened name without boilerplate text.",
        example="Concrete and Concrete Elements",
    )
    version: str | None = pyd.Field(
        description="Document version, as expressed in document.",
        example="1.0.2",
        default=None,
    )
    date_of_issue: datetime.datetime | None = pyd.Field(
        example=datetime.date(day=11, month=2, year=2022),
        default=None,
        description="First day on which the document is valid",
    )
    valid_until: datetime.datetime | None = pyd.Field(
        example=datetime.date(day=11, month=2, year=2024),
        default=None,
        description="Last day on which the document is valid",
    )
    doc: str | None = pyd.Field(default=None, description="URL to original document, preferably directly to a PDF.")
    parent: Optional["Pcr"] = pyd.Field(
        description="The parent PCR, base PCR, `Part A` PCR",
        default=None,
    )
    status: PcrStatus | None = pyd.Field(
        default=None,
        description="The current release status of this PCR. "
        "A PCR with valid_until in the past must have status Expired or Sunset; a PCR with valid_until "
        "more than 5 years in the past must have status Sunset. Compliant systems should automatically "
        "update these fields within 24 hours.",
    )
    product_classes: dict[str, str | list[str]] = pyd.Field(
        description="List of classifications, including Masterformat and UNSPC", default_factory=dict
    )
    applicable_in: list[Annotated[str, pyd.Field(min_length=2, max_length=2)]] | None = pyd.Field(
        max_items=100,
        default=None,
        description="Jurisdiction(s) in which EPD is applicable. An empty array, or absent properties, "
        "implies global applicability. Accepts "
        "[2-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), "
        "[M49 region codes](https://unstats.un.org/unsd/methodology/m49/), "
        'or the alias "EU27" for the 27 members of the Euro bloc, or the alias "NAFTA" '
        "for the members of North American Free Trade Agreement",
        example=["US", "CA", "MX", "EU27", "NAFTA"],
    )

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "pcr"
