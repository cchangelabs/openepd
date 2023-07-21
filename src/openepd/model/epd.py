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
from typing import Annotated

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Amount, Ingredient, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.lcia import Impacts, OutputFlowSet, ResourceUseSet
from openepd.model.org import Org, Plant
from openepd.model.pcr import Pcr
from openepd.model.specs import Specs
from openepd.model.standard import Standard


class Epd(WithAttachmentsMixin, WithAltIdsMixin, BaseOpenEpdSchema):
    """Represent an EPD."""

    # TODO: Add validator for open-xpd-uuid on this field
    id: str | None = pyd.Field(
        description="The unique ID for this EPD.  To ensure global uniqueness, should be registered at "
        "open-xpd-uuid.cqd.io/register or a coordinating registry.",
        default=None,
        json_schema_extra=dict(example="1u7zsed8"),
    )
    doctype: str = pyd.Field(
        description='Describes the type and schema of the document. Must always always read "openEPD".',
        default="OpenEPD",
    )
    product_name: str | None = pyd.Field(
        max_length=200,
        description="The name of the product described by this EPD",
        json_schema_extra=dict(example="Mix 12345AC"),
    )
    product_sku: str | None = pyd.Field(
        default=None, max_length=200, description="Unique stock keeping identifier assigned by manufacturer"
    )
    product_description: str | None = pyd.Field(
        max_length=2000,
        description="1-paragraph description of product. " "Supports plain text or github flavored markdown.",
    )
    # TODO: add product_alt_names? E.g. ILCD has a list of synonymous names
    product_classes: dict[str, str | list[str]] = pyd.Field(
        description="List of classifications, including Masterformat and UNSPC", default_factory=dict
    )
    product_image_small: pyd.AnyUrl | None = pyd.Field(
        description="Pointer to image illustrating the product, which is no more than 200x200 pixels", default=None
    )
    product_image: pyd.AnyUrl | None = pyd.Field(
        description="pointer to image illustrating the product no more than 10MB", default=None
    )
    version: pyd.PositiveInt | None = pyd.Field(
        description="Version of this document. The document's issuer should increment it anytime even a single "
        "character changes, as this value is used to determine the most recent version.",
        default=None,
        json_schema_extra=dict(example=1),
    )
    language: str | None = pyd.Field(
        default=None,
        min_length=2,
        max_length=2,
        description="Language this EPD is captured in, as an ISO 639-1 code",
        json_schema_extra=dict(example="en"),
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
        default=None,
        description="Link to data object on original registrar's site",
        json_schema_extra=dict(example="https://epd-online.com/EmbeddedEpdList/Download/6029"),
    )
    manufacturer: Org | None = pyd.Field(
        default=None,
        description="JSON object for declaring Org. Sometimes called the "
        '"Declaration Holder" or "Declaration Owner".',
    )
    epd_developer: Org | None = pyd.Field(
        default=None,
        description="The organization responsible for the underlying LCA (and subsequent summarization as EPD).",
    )
    epd_developer_email: pyd.EmailStr | None = pyd.Field(
        default=None,
        description="Email contact for inquiries about development of this EPD. "
        "This must be an email which can be publicly shared.",
        json_schema_extra=dict(example="john.doe@we-do-lca.com"),
    )
    plants: list[Plant] = pyd.Field(
        max_length=32,
        description="List of object(s) for one or more plant(s) that this declaration applies to.",
        default_factory=list,
    )
    program_operator: Org | None = pyd.Field(description="JSON object for program operator Org")
    program_operator_doc_id: str | None = pyd.Field(
        default=None,
        max_length=200,
        description="Document identifier from Program Operator.",
        json_schema_extra=dict(example="123-456.789/b"),
    )
    program_operator_version: str | None = pyd.Field(
        default=None,
        max_length=200,
        description="Document version number from Program Operator.",
        json_schema_extra=dict(example="4.3.0"),
    )
    third_party_verifier: Org | None = pyd.Field(
        default=None, description="JSON object for Org that performed a critical review of the EPD data"
    )
    third_party_verification_url: pyd.AnyUrl | None = pyd.Field(
        default=None,
        description="Optional link to a verification statement.",
        json_schema_extra=dict(example="https://we-verify-epds.com/en/letters/123-456.789b.pdf"),
    )
    third_party_verifier_email: pyd.EmailStr | None = pyd.Field(
        description="Email address of the third party verifier",
        default=None,
        json_schema_extra=dict(example="john.doe@example.com"),
    )
    date_of_issue: datetime.date | None = pyd.Field(
        default=None,
        description="Date the EPD was issued. This should be the first day on which the EPD is valid.",
        json_schema_extra=dict(example=datetime.date(day=11, month=9, year=2019)),
    )
    valid_until: datetime.date | None = pyd.Field(
        default=None,
        description="Last date the EPD is valid on, including any extensions.",
        json_schema_extra=dict(example=datetime.date(day=11, month=9, year=2028)),
    )
    pcr: Pcr | None = pyd.Field(
        description="JSON object for product category rules. Should point to the "
        "most-specific PCR that applies; the PCR entry should point to any "
        "parent PCR.",
        default=None,
    )
    declared_unit: Amount | None = pyd.Field(
        description="SI declared unit for this EPD.  If a functional unit is "
        "utilized, the declared unit shall refer to the amount of "
        "product associated with the A1-A3 life cycle stage."
    )
    kg_per_declared_unit: Amount | None = pyd.Field(
        default=None,
        description="Mass of the product, in kilograms, per declared unit",
        json_schema_extra=dict(example=Amount(qty=12.5, unit="kg")),
    )
    kg_C_per_declared_unit: Amount | None = pyd.Field(
        default=None,
        description="Mass of elemental carbon, per declared unit, contained in the product itself at the manufacturing "
        "facility gate.  Used (among other things) to check a carbon balance or calculate incineration "
        "emissions.  The source of carbon (e.g. biogenic) is not relevant in this field.",
        json_schema_extra=dict(example=Amount(qty=8.76, unit="kg")),
    )
    kg_C_biogenic_per_declared_unit: Amount | None = pyd.Field(
        default=None,
        description="Mass of elemental carbon from biogenic sources, per declared unit, contained in the product "
        "itself at the manufacturing facility gate.  It may be presumed that any biogenic carbon content "
        "has been accounted for as -44/12 kgCO2e per kg C in stages A1-A3, per EN15804 and ISO 21930.",
        json_schema_extra=dict(example=Amount(qty=8.76, unit="kg")),
    )
    product_service_life_years: float | None = pyd.Field(
        default=None,
        gt=0.0009,
        lt=101,
        description="Reference service life of the product, in years.  Serves as a maximum for replacement interval, "
        "which may also be constrained by usage or the service life of what the product goes into "
        "(e.g. a building).",
        json_schema_extra=dict(example=50.0),
    )
    annual_production: float | None = pyd.Field(
        gt=0,
        default=None,
        description="Approximate annual production volume, in declared units, of product covered by this EPD. "
        "This value is intended to be used for weighting of averages. "
        "Providing this data is optional, and it is acceptable to round or obfuscate it downwards "
        "(but not upwards) by any amount desired to protect confidentiality. For example, if the "
        "product volume is 123,456 m3, a value of 120,000, 100,000 or even 87,654 would be acceptable.",
        json_schema_extra=dict(example=10000),
    )
    applicable_in: list[Annotated[str, pyd.Field(min_length=2, max_length=2)]] | None = pyd.Field(
        max_length=100,
        default=None,
        description="Jurisdiction(s) in which EPD is applicable. An empty array, or absent properties, "
        "implies global applicability.",
        json_schema_extra=dict(example=["US", "CA", "MX"]),
    )
    product_usage_description: str | None = pyd.Field(
        default=None,
        description="Text description of how product is typically used. Can be used to describe accessories "
        "like fasteners, adhesives, etc.  Supports plain text or github flavored markdown.",
    )
    product_usage_image: pyd.AnyUrl | None = pyd.Field(
        description="Pointer (url) to image illustrating how the product is used. No more than 10MB.", default=None
    )
    manufacturing_description: str | None = pyd.Field(
        default=None,
        description="Text description of manufacturing process.  Supports plain text or github flavored markdown.",
    )
    manufacturing_image: pyd.AnyUrl | None = pyd.Field(
        description="Pointer (url) to an image illustrating the manufacturing process. No more than 10MB.", default=None
    )
    impacts: Impacts | None = pyd.Field(
        description="List of environmental impacts, compiled per one of the standard Impact Assessment methods"
    )
    resource_uses: ResourceUseSet | None = pyd.Field(
        description="Set of Resource Use Indicators, over various LCA scopes"
    )
    output_flows: OutputFlowSet | None = pyd.Field(
        description="Set of Waste and Output Flow indicators which describe the waste categories "
        "and other material output flows derived from the LCI."
    )
    compliance: list[Standard] = pyd.Field(
        description="Standard(s) to which this declaration is compliant.", default_factory=list
    )
    specs: Specs = pyd.Field(
        default_factory=Specs,
        description="Data structure(s) describing performance specs of product. Unique for each material type.",
    )
    includes: list[Ingredient] = pyd.Field(
        max_length=255,
        description="List of JSON objects pointing to product components. "
        "Each one should be an EPD or digitized LCI process.",
        default_factory=list,
    )
    lca_discussion: str | None = pyd.Field(
        max_length=20000,
        description="""A rich text description containing information for experts reviewing the EPD contents. 
Text descriptions required by ISO 14025, ISO 21930, EN 15804,, relevant PCRs, or program instructions and which do not 
have specific openEPD fields should be entered here.  This field may be large, and may contain multiple sections 
separated by github flavored markdown formatting.""",
        json_schema_extra=dict(
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
    """
        ),
    )

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "epd"
