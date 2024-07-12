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
import abc
import datetime

from openepd.compat.pydantic import pyd
from openepd.model.base import RootDocument
from openepd.model.common import Amount
from openepd.model.pcr import Pcr
from openepd.model.standard import Standard


class BaseDeclaration(RootDocument, abc.ABC):
    """Base class for declaration-related documents (EPDs, Industry-wide EPDs, Generic Estimates)."""

    # TODO: Add validator for open-xpd-uuid on this field
    id: str | None = pyd.Field(
        description="The unique ID for this document.  To ensure global uniqueness, should be registered at "
        "open-xpd-uuid.cqd.io/register or a coordinating registry.",
        example="1u7zsed8",
        default=None,
    )
    date_of_issue: datetime.datetime | None = pyd.Field(
        example=datetime.datetime(day=11, month=9, year=2019, tzinfo=datetime.timezone.utc),
        description="Date the document was issued. This should be the first day on which the document is valid.",
    )
    valid_until: datetime.datetime | None = pyd.Field(
        example=datetime.datetime(day=11, month=9, year=2028, tzinfo=datetime.timezone.utc),
        description="Last date the document is valid on, including any extensions.",
    )

    declared_unit: Amount | None = pyd.Field(
        description="SI declared unit for this document.  If a functional unit is "
        "utilized, the declared unit shall refer to the amount of "
        "product associated with the A1-A3 life cycle stage."
    )
    kg_per_declared_unit: Amount | None = pyd.Field(
        default=None,
        description="Mass of the product, in kilograms, per declared unit",
        example=Amount(qty=12.5, unit="kg"),
    )
    compliance: list[Standard] = pyd.Field(
        description="Standard(s) to which this document is compliant.", default_factory=list
    )

    # TODO: add product_alt_names? E.g. ILCD has a list of synonymous names
    product_classes: dict[str, str | list[str]] = pyd.Field(
        description="List of classifications, including Masterformat and UNSPC", default_factory=dict
    )

    language: str | None = pyd.Field(
        min_length=2,
        max_length=2,
        strip_whitespace=True,
        description="Language this document is captured in, as an ISO 639-1 code",
        example="en",
    )
    private: bool = pyd.Field(
        default=False,
        description="This document's author does not wish the contents published. "
        "Useful for draft, partial, or confidential declarations.  "
        "How (or whether) privacy is implemented is up to the receiving system.  "
        "Null is treated as false (public).  Private (draft) entries have a reduced "
        "number of required fields, to allow for multiple systems to coordinate "
        "incomplete EPDs.",
    )

    pcr: Pcr | None = pyd.Field(
        description="JSON object for product category rules. Should point to the "
        "most-specific PCR that applies; the PCR entry should point to any "
        "parent PCR.",
        default=None,
    )
    lca_discussion: str | None = pyd.Field(
        max_length=20000,
        description="""A rich text description containing information for experts reviewing the document contents.
    Text descriptions required by ISO 14025, ISO 21930, EN 15804,, relevant PCRs, or program instructions and which do not
    have specific openEPD fields should be entered here.  This field may be large, and may contain multiple sections
    separated by github flavored markdown formatting.""",
        example="""# Packaging

    Information on product-specific packaging: type, composition and possible reuse of packaging materials (paper,
    strapping, pallets, foils, drums, etc.) shall be included in this Section. The EPD shall describe specific packaging
    scenario assumptions, including disposition pathways for each packaging material by reuse, recycling, or landfill
    disposal based on packaging type.*

    # Product Installation

    A description of the type of processing, machinery, tools, dust extraction equipment, auxiliary materials, etc.
    to be used during installation shall be included. Information on industrial and environmental protection may be
    included in this section. Any waste treatment included within the system boundary of installation waste should be
    specified.

    # Use Conditions

    Use-stage environmental impacts of flooring products during building operations depend on product cleaning assumptions.
    Information on cleaning frequency and cleaning products shall be provided based on the manufacturer’s recommendations.
    In the absence of primary data, cleaning assumptions shall be documented.
    """,
    )
