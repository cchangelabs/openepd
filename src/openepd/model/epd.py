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
from typing import Literal

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Amount, ExternallyIdentifiableMixin
from openepd.model.lcia import ImpactSet, OutputFlowSet, ResourceUseSet
from openepd.model.orgs import Org, Plant


class Epd(ExternallyIdentifiableMixin, BaseOpenEpdSchema):
    """Represent an EPD."""

    # TODO: Add validator for open-xpd-uuid on this field
    id: str = pyd.Field(
        description="The unique ID for this EPD.  To ensure global uniqueness, should be registered at "
        "open-xpd-uuid.cqd.io/register or a coordinating registry.",
        example="1u7zsed8",
    )
    doctype: Literal["OpenEPD", "ILCD_EPD"] = pyd.Field(
        description='Describes the type and schema of the document. Must always always read "openEPD".',
        default="OpenEPD",
    )
    product_name: str = pyd.Field(
        max_length=200, description="The name of the product described by this EPD", example="Mix 12345AC"
    )
    # TODO: add product_alt_names? E.g. ILCD has a list of synonymous names
    version: pyd.PositiveInt = pyd.Field(
        description="Version of this document. The document's issuer should increment it anytime even a single "
        "character changes, as this value is used to determine the most recent version.",
        example=1,
    )
    language: str | None = pyd.Field(
        min_length=2,
        max_length=2,
        strip_whitespace=True,
        description="Language this EPD is captured in, as an ISO 639-1 code",
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
    declaration_url: pyd.AnyUrl | None = pyd.Field(
        description="Link to data object on original registrar's site",
        example="https://epd-online.com/EmbeddedEpdList/Download/6029",
    )
    # ilcd_uuid: str | None = pyd.Field(description="An optional UUID (for use with ILCD and similar systems)")
    manufacturer: Org | None = pyd.Field(
        description="JSON object for declaring Org. Sometimes called the "
        '"Declaration Holder" or "Declaration Owner".'
    )
    plants: list[Plant] = pyd.Field(
        max_items=32,
        description="List of object(s) for one or more plant(s) that this declaration applies to.",
        default=[],
    )
    program_operator: Org | None = pyd.Field(description="JSON object for program operator Org")
    program_operator_doc_id: str | None = pyd.Field(
        max_length=200, description="Document identifier from Program Operator.", example="123-456.789/b"
    )
    program_operator_version: str | None = pyd.Field(
        max_length=200, description="Document version number from Program Operator.", example="4.3.0"
    )
    third_party_verifier: Org | None = pyd.Field(
        description="JSON object for Org that performed a critical review of the EPD data"
    )
    third_party_verification_url: pyd.AnyUrl | None = pyd.Field(
        description="Optional link to a verification statement.",
        example="https://we-verify-epds.com/en/letters/123-456.789b.pdf",
    )
    date_of_issue: datetime.date | None = pyd.Field(
        example=datetime.date(day=11, month=9, year=2019),
        description="Date the EPD was issued. This should be the first day on which the EPD is valid.",
    )
    valid_until: datetime.date | None = pyd.Field(
        example=datetime.date(day=11, month=9, year=2028),
        description="Last date the EPD is valid on, including any extensions.",
    )
    product_class: dict[str, str] = pyd.Field(
        description="List of classifications, including Masterformat and UNSPC", default_factory=dict
    )
    declared_unit: Amount | None = pyd.Field(
        description="SI declared unit for this EPD.  If a functional unit is "
        "utilized, the declared unit shall refer to the amount of "
        "product associated with the A1-A3 life cycle stage."
    )
    impacts: ImpactSet | None = pyd.Field(
        description="List of environmental impacts, compiled per one of the standard Impact Assessment methods"
    )
    resource_uses: ResourceUseSet | None = pyd.Field(
        description="Set of Resource Use Indicators, over various LCA scopes"
    )
    output_flows: OutputFlowSet | None = pyd.Field(
        description="Set of Waste and Output Flow indicators which describe the waste categories "
        "and other material output flows derived from the LCI."
    )
