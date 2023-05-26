#
#  Copyright 2023 by C Change Labs Inc. www.c-change-labs.com
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
from typing import Optional

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import WithAttachmentsMixin
from openepd.model.org import Org


class Pcr(WithAttachmentsMixin, BaseOpenEpdSchema):
    """Represent a PCR (Product Category Rules)."""

    id: str = pyd.Field(
        description="The unique ID for this PCR.  To ensure global uniqueness, should be registered "
        "at open-xpd-uuid.cqd.io/register or a coordinating registry.",
        example="ec3xpgq2",
    )
    issuer: Org | None = pyd.Field(description="Organization issuing this PCR", default=None)
    issuer_doc_id: str | None = pyd.Field(
        max_length=40,
        description="Document ID or code created by issuer",
        example="c-PCR-003",
    )
    name: str | None = pyd.Field(
        max_length=200,
        description="Full document name as listed in source document",
        example="c-PCR-003 Concrete and concrete elements (EN 16757)",
    )
    short_name: str | None = pyd.Field(
        max_length=40,
        description="A shortened name without boilerplate text.",
        example="Concrete and Concrete Elements",
    )
    version: pyd.PositiveInt = pyd.Field(
        description="Document version, as expressed in document.",
        example="1.0.2",
    )
    date_of_issue: datetime.date | None = pyd.Field(
        example=datetime.date(day=11, month=2, year=2022),
        description="First day on which the document is valid",
    )
    valid_until: datetime.date | None = pyd.Field(
        example=datetime.date(day=11, month=2, year=2024),
        description="Last day on which the document is valid",
    )
    parent: Optional["Pcr"] = pyd.Field(
        description="The parent PCR, base PCR, `Part A` PCR",
        default=None,
    )
    # TODO: why plural?
    product_classes: dict[str, str | list[str]] = pyd.Field(
        description="List of classifications, including Masterformat and UNSPC", default_factory=dict
    )
