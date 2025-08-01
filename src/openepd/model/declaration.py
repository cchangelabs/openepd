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
import abc
import datetime
from enum import StrEnum

import pydantic

from openepd.model.base import BaseOpenEpdSchema, OpenXpdUUID, RootDocument
from openepd.model.common import Amount
from openepd.model.geography import Geography
from openepd.model.org import Org
from openepd.model.pcr import Pcr
from openepd.model.specs.range import SpecsRange
from openepd.model.standard import Standard
from openepd.model.validation.common import ReferenceStr
from openepd.model.validation.quantity import AmountGWP, AmountMass

DEVELOPER_DESCRIPTION = "The organization responsible for the underlying LCA (and subsequent summarization as EPD)."
PROGRAM_OPERATOR_DESCRIPTION = "JSON object for program operator Org"
THIRD_PARTY_VERIFIER_DESCRIPTION = "JSON object for Org that performed a critical review of the EPD data"


class BaseDeclaration(RootDocument, abc.ABC):
    """Base class for declaration-related documents (EPDs, Industry-wide EPDs, Generic Estimates)."""

    id: OpenXpdUUID | None = pydantic.Field(
        description="The unique ID for this document.  To ensure global uniqueness, should be registered at "
        "open-xpd-uuid.cqd.io/register or a coordinating registry.",
        examples=["1u7zsed8"],
        default=None,
    )
    date_of_issue: datetime.datetime | None = pydantic.Field(
        examples=[datetime.datetime(day=11, month=9, year=2019, tzinfo=datetime.UTC)],
        description="Date the document was issued. This should be the first day on which the document is valid.",
        default=None,
    )
    valid_until: datetime.datetime | None = pydantic.Field(
        examples=[datetime.datetime(day=11, month=9, year=2028, tzinfo=datetime.UTC)],
        description="Last date the document is valid on, including any extensions.",
        default=None,
    )

    version: pydantic.NonNegativeInt | None = pydantic.Field(
        description="Version of this document. The document's issuer should increment it anytime even a single "
        "character changes, as this value is used to determine the most recent version.",
        examples=[1],
        default=None,
    )

    declared_unit: Amount | None = pydantic.Field(
        description="SI declared unit for this document.  If a functional unit is "
        "utilized, the declared unit shall refer to the amount of "
        "product associated with the A1-A3 life cycle stage.",
        default=None,
    )
    kg_per_declared_unit: AmountMass | None = pydantic.Field(
        default=None,
        description="Mass of the product, in kilograms, per declared unit",
        examples=[Amount(qty=12.5, unit="kg").to_serializable(exclude_unset=True)],
    )
    compliance: list[Standard] = pydantic.Field(
        description="Standard(s) to which this document is compliant.",
        default_factory=list,
    )

    # TODO: add product_alt_names? E.g. ILCD has a list of synonymous names
    product_classes: dict[str, str | list[str]] = pydantic.Field(
        description="List of classifications, including Masterformat and UNSPC",
        default_factory=dict,
    )

    language: str | None = pydantic.Field(
        min_length=2,
        max_length=2,
        description="Language this document is captured in, as an ISO 639-1 code",
        examples=["en"],
        default=None,
    )
    private: bool | None = pydantic.Field(
        default=False,
        description="This document's author does not wish the contents published. "
        "Useful for draft, partial, or confidential declarations.  "
        "How (or whether) privacy is implemented is up to the receiving system.  "
        "Null is treated as false (public).  Private (draft) entries have a reduced "
        "number of required fields, to allow for multiple systems to coordinate "
        "incomplete EPDs.",
    )

    pcr: Pcr | None = pydantic.Field(
        description="JSON object for product category rules. Should point to the "
        "most-specific PCR that applies; the PCR entry should point to any "
        "parent PCR.",
        default=None,
    )
    lca_discussion: str | None = pydantic.Field(
        max_length=20000,
        description="""A rich text description containing information for experts reviewing the document contents.
    Text descriptions required by ISO 14025, ISO 21930, EN 15804, relevant PCRs, or program instructions and which do not
    have specific openEPD fields should be entered here.  This field may be large, and may contain multiple sections
    separated by github flavored markdown formatting.""",
        examples=[
            """# Packaging

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
        ],
        default=None,
    )

    product_image_small: pydantic.AnyUrl | None = pydantic.Field(
        description="Pointer to image illustrating the product, which is no more than 200x200 pixels",
        default=None,
    )
    product_image: pydantic.AnyUrl | pydantic.FileUrl | None = pydantic.Field(
        description="pointer to image illustrating the product no more than 10MB",
        default=None,
    )
    declaration_url: str | None = pydantic.Field(
        description="Link to data object on original registrar's site",
        examples=["https://epd-online.com/EmbeddedEpdList/Download/6029"],
        default=None,
    )
    kg_C_per_declared_unit: AmountMass | None = pydantic.Field(
        default=None,
        description="Mass of elemental carbon, per declared unit, contained in the product itself at the manufacturing "
        "facility gate.  Used (among other things) to check a carbon balance or calculate incineration "
        "emissions.  The source of carbon (e.g. biogenic) is not relevant in this field.",
        examples=[Amount(qty=8.76, unit="kgCO2e").to_serializable(exclude_unset=True)],
    )
    kg_C_biogenic_per_declared_unit: AmountGWP | None = pydantic.Field(
        default=None,
        description="Mass of elemental carbon from biogenic sources, per declared unit, contained in the product "
        "itself at the manufacturing facility gate.  It may be presumed that any biogenic carbon content "
        "has been accounted for as -44/12 kgCO2e per kg C in stages A1-A3, per EN15804 and ISO 21930.",
        examples=[Amount(qty=8.76, unit="kgCO2e").to_serializable(exclude_unset=True)],
    )
    product_service_life_years: float | None = pydantic.Field(
        gt=0.0009,
        lt=101,
        description="Reference service life of the product, in years.  Serves as a maximum for replacement interval, "
        "which may also be constrained by usage or the service life of what the product goes into "
        "(e.g. a building).",
        examples=[50.0],
        default=None,
    )

    @pydantic.field_validator("language", mode="before")
    def strip_language(cls, value: str | None) -> str | None:
        """Strip whitespace from language."""
        if isinstance(value, str):
            return value.strip()
        return value


class AverageDatasetMixin(pydantic.BaseModel, title="Average Dataset"):
    """Fields common for average dataset (Industry-wide EPDs, Generic Estimates)."""

    description: str | None = pydantic.Field(
        max_length=2000,
        description="1-paragraph description of the average dataset. Supports plain text or github flavored markdown.",
        default=None,
    )

    geography: list[Geography] | None = pydantic.Field(
        description="Jurisdiction(s) in which the LCA result is applicable.  An empty array, or absent properties, "
        "implies global applicability.",
        default=None,
    )

    specs: SpecsRange | None = pydantic.Field(
        default=None,
        description="Average dataset material performance specifications.",
    )


class WithProgramOperatorMixin(pydantic.BaseModel):
    """Object which has a connection to ProgramOperator."""

    program_operator: Org | None = pydantic.Field(description=PROGRAM_OPERATOR_DESCRIPTION, default=None)
    program_operator_doc_id: str | None = pydantic.Field(
        max_length=200,
        description="Document identifier from Program Operator.",
        examples=["123-456.789/b"],
        default=None,
    )
    program_operator_version: str | None = pydantic.Field(
        max_length=200, description="Document version number from Program Operator.", examples=["4.3.0"], default=None
    )


class WithVerifierMixin(pydantic.BaseModel):
    """Set of fields related to verifier."""

    third_party_verifier: Org | None = pydantic.Field(description=THIRD_PARTY_VERIFIER_DESCRIPTION, default=None)
    third_party_verification_url: pydantic.AnyUrl | None = pydantic.Field(
        description="Optional link to a verification statement.",
        examples=["https://we-verify-epds.com/en/letters/123-456.789b.pdf"],
        default=None,
    )
    third_party_verifier_email: pydantic.EmailStr | None = pydantic.Field(
        description="Email address of the third party verifier",
        examples=["john.doe@example.com"],
        default=None,
    )
    third_party_verifier_name: str | None = pydantic.Field(
        description="The publishable name of the third party verifier", examples=["John Doe"], default=None
    )


class WithEpdDeveloperMixin(pydantic.BaseModel):
    """Set of fields related to EPD Developer."""

    epd_developer: Org | None = pydantic.Field(
        description=DEVELOPER_DESCRIPTION,
        default=None,
    )
    epd_developer_email: pydantic.EmailStr | None = pydantic.Field(
        default=None,
        examples=["john.doe@we-do-lca.com"],
        description="Email contact for inquiries about development of this EPD. "
        "This must be an email which can be publicly shared.",
    )


class RefBase(BaseOpenEpdSchema, title="Ref Object"):
    """Base class for reference-style objects."""

    id: OpenXpdUUID | None = pydantic.Field(
        description="The unique ID for this object. To ensure global uniqueness, should be registered at "
        "open-xpd-uuid.cqd.io/register or a coordinating registry.",
        examples=["1u7zsed8"],
        default=None,
    )

    name: str | None = pydantic.Field(max_length=200, description="Name of the object", default=None)

    ref: ReferenceStr | None = pydantic.Field(
        default=None,
        examples=["https://openepd.buildingtransparency.org/api/generic_estimates/EC300001"],
        description="Reference to this JSON object",
    )


class OriginalDataFormat(StrEnum):
    """
    Original data format for this EPD.

    A system receiving an EPD via openEPD should preserve this field if it exists.  Otherwise, it is up to the
    receiving system to infer the original data format based on the source.
    """

    OPENEPD_1_0 = "openEPDv1.0"
    """
    Data was generated in an openEPD-compliant system, such as by manual entry in EC3 or generation in an openEPD
    compliant EPD generator.
    """

    CUSTOM_API = "custom_api"
    """
    Data was gathered from a non-standardized API offered by a data provider.  Numerical and text data is very likely
    to be correct and up to date, but important fields may be absent and identification of organizations, plants, and
     addresses may be ambiguous.
    """

    ILCD_EPD_v1_2 = "ILCD+EPDv1_2"
    """
    Data was generated and published in ILCD+EPD format, version 1.2  Numerical and text data is very likely to be
    correct and up to date, but important fields may be absent and identification of organizations, plants, and
    addresses may be ambiguous.
    """

    ILCD_EPD_v1_1 = "ILCD+EPDv1_1"
    """
    Data was generated and published in ILCD+EPD format, version 1.1  Numerical and text data is very likely to be
    correct and up to date, but important fields may be absent and identification of organizations, plants, and
    addresses may be ambiguous.
    """

    ILCD_EPD_v1_0 = "ILCD+EPDv1_0"
    """
    Data was generated and published in ILCD+EPD format, version 1.0  Numerical and text data is very likely to be
    correct and up to date, but important fields may be absent and identification of organizations, plants, and
    addresses may be ambiguous.
    """

    WEB = "web"
    """
    Data was gathered through comprehension of a viewable HTML page, typically offered by a program operator.
    This is more reliable than PDF, but less reliable than API or a standardized XML like ILCD+EPD.
    """

    PDF_MANUAL = "pdf_manual"
    """
    Data was entered by hand based on PDF and/or validated by a qualified professional.
    """

    PDF_MIXED = "pdf_mixed"
    """
    Data is a mix of structured data from an information system, but with significant missing data filled in by
    extraction from a PDF.
    """

    PDF = "pdf"
    """
    Data was extracted by analyzing or comprehending a PDF document.  Includes documents where up to 4 fields (e.g.
    program operator) were inferred from sources outside the PDF.  This method is prone to errors and omissions due
    to the many different formats and terms used in these relatively unstructured documents.
    """

    OTHER = "other"
    """
    Data source is not of a type listed here.
    """
