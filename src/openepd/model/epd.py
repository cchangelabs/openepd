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
from typing import Annotated

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes
from openepd.model.common import Amount, Ingredient, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import BaseDeclaration
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org, Plant
from openepd.model.specs import Specs
from openepd.model.versioning import OpenEpdVersions, Version

MANUFACTURER_DESCRIPTION = (
    'JSON object for declaring Org. Sometimes called the "Declaration Holder" or "Declaration Owner".'
)
DEVELOPER_DESCRIPTION = "The organization responsible for the underlying LCA (and subsequent summarization as EPD)."
PROGRAM_OPERATOR_DESCRIPTION = "JSON object for program operator Org"
THIRD_PARTY_VERIFIER_DESCRIPTION = "JSON object for Org that performed a critical review of the EPD data"


class EpdPreviewV0(WithAttachmentsMixin, WithAltIdsMixin, BaseDeclaration, title="EPD (Preview)"):
    """
    EPD preview, used in API list responses and where there is no need for a full object.

    Excludes LCIA data.

    """

    product_name: str | None = pyd.Field(
        max_length=200, description="The name of the product described by this EPD", example="Mix 12345AC", default=None
    )
    product_sku: str | None = pyd.Field(
        max_length=200, description="Unique stock keeping identifier assigned by manufacturer"
    )
    product_description: str | None = pyd.Field(
        max_length=2000,
        description="1-paragraph description of product. Supports plain text or github flavored markdown.",
    )
    product_image_small: pyd.AnyUrl | None = pyd.Field(
        description="Pointer to image illustrating the product, which is no more than 200x200 pixels", default=None
    )
    product_image: pyd.AnyUrl | pyd.FileUrl | None = pyd.Field(
        description="pointer to image illustrating the product no more than 10MB", default=None
    )
    version: pyd.PositiveInt | None = pyd.Field(
        description="Version of this document. The document's issuer should increment it anytime even a single "
        "character changes, as this value is used to determine the most recent version.",
        example=1,
        default=None,
    )
    declaration_url: str | None = pyd.Field(
        description="Link to data object on original registrar's site",
        example="https://epd-online.com/EmbeddedEpdList/Download/6029",
    )
    manufacturer: Org | None = pyd.Field(description=MANUFACTURER_DESCRIPTION)
    epd_developer: Org | None = pyd.Field(
        description=DEVELOPER_DESCRIPTION,
        default=None,
    )
    epd_developer_email: pyd.EmailStr | None = pyd.Field(
        default=None,
        example="john.doe@we-do-lca.com",
        description="Email contact for inquiries about development of this EPD. "
        "This must be an email which can be publicly shared.",
    )
    plants: list[Plant] = pyd.Field(
        max_items=32,
        description="List of object(s) for one or more plant(s) that this declaration applies to.",
        default_factory=list,
    )
    program_operator: Org | None = pyd.Field(description=PROGRAM_OPERATOR_DESCRIPTION)
    program_operator_doc_id: str | None = pyd.Field(
        max_length=200, description="Document identifier from Program Operator.", example="123-456.789/b"
    )
    program_operator_version: str | None = pyd.Field(
        max_length=200, description="Document version number from Program Operator.", example="4.3.0"
    )
    third_party_verifier: Org | None = pyd.Field(description=THIRD_PARTY_VERIFIER_DESCRIPTION)
    third_party_verification_url: pyd.AnyUrl | None = pyd.Field(
        description="Optional link to a verification statement.",
        example="https://we-verify-epds.com/en/letters/123-456.789b.pdf",
    )
    third_party_verifier_email: pyd.EmailStr | None = pyd.Field(
        description="Email address of the third party verifier", example="john.doe@example.com", default=None
    )
    kg_C_per_declared_unit: Amount | None = pyd.Field(
        default=None,
        description="Mass of elemental carbon, per declared unit, contained in the product itself at the manufacturing "
        "facility gate.  Used (among other things) to check a carbon balance or calculate incineration "
        "emissions.  The source of carbon (e.g. biogenic) is not relevant in this field.",
        example=Amount(qty=8.76, unit="kg"),
    )
    kg_C_biogenic_per_declared_unit: Amount | None = pyd.Field(
        default=None,
        description="Mass of elemental carbon from biogenic sources, per declared unit, contained in the product "
        "itself at the manufacturing facility gate.  It may be presumed that any biogenic carbon content "
        "has been accounted for as -44/12 kgCO2e per kg C in stages A1-A3, per EN15804 and ISO 21930.",
        example=Amount(qty=8.76, unit="kg"),
    )
    product_service_life_years: float | None = pyd.Field(
        gt=0.0009,
        lt=101,
        description="Reference service life of the product, in years.  Serves as a maximum for replacement interval, "
        "which may also be constrained by usage or the service life of what the product goes into "
        "(e.g. a building).",
        example=50.0,
    )
    annual_production: float | None = pyd.Field(
        gt=0,
        default=None,
        description="Approximate annual production volume, in declared units, of product covered by this EPD. "
        "This value is intended to be used for weighting of averages. "
        "Providing this data is optional, and it is acceptable to round or obfuscate it downwards "
        "(but not upwards) by any amount desired to protect confidentiality. For example, if the "
        "product volume is 123,456 m3, a value of 120,000, 100,000 or even 87,654 would be acceptable.",
        example=10000,
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

    specs: Specs = pyd.Field(
        default_factory=Specs,
        description="Data structure(s) describing performance specs of product. Unique for each material type.",
    )
    includes: list[Ingredient] = pyd.Field(
        max_items=255,
        description="List of JSON objects pointing to product components. "
        "Each one should be an EPD or digitized LCI process.",
        default_factory=list,
    )


EpdPreview = EpdPreviewV0


class EpdV0(WithLciaMixin, EpdPreviewV0, title="EPD (Full)"):
    """Represent an EPD."""

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "epd"

    @pyd.validator("compliance", always=True, pre=True)
    def validate_compliance(cls, v: list | None):
        """Handle correctly None values for compliance field."""
        if v is None:
            return []
        return v

    @pyd.validator("includes", always=True, pre=True)
    def validate_includes(cls, v: list | None):
        """Handle correctly None values for includes field."""
        if v is None:
            return []
        return v


Epd = EpdV0


class EpdWithDepsV0(EpdV0, title="EPD (with Dependencies)"):
    """
    Expanded version of the EPD.

    Contains related entities - orgs - with full fields, to support object matching in implementations.
    For now the implementation matches the above EpdV0 entity, but they will diverge as normal Epd would have
    some required fields in Org (like web_domain), and WithDeps would not.
    """

    manufacturer: Org | None = pyd.Field(description=MANUFACTURER_DESCRIPTION)
    epd_developer: Org | None = pyd.Field(description=DEVELOPER_DESCRIPTION, default=None)
    program_operator: Org | None = pyd.Field(description=PROGRAM_OPERATOR_DESCRIPTION)
    third_party_verifier: Org | None = pyd.Field(description=THIRD_PARTY_VERIFIER_DESCRIPTION)


EpdWithDeps = EpdWithDepsV0


class EpdFactory(BaseDocumentFactory[BaseDeclaration]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = OpenEpdDoctypes.Epd
    VERSION_MAP: dict[Version, type[BaseDeclaration]] = {OpenEpdVersions.Version0: EpdV0}
