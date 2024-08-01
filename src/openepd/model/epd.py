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
from openepd.model.common import Ingredient, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import (
    DEVELOPER_DESCRIPTION,
    PROGRAM_OPERATOR_DESCRIPTION,
    THIRD_PARTY_VERIFIER_DESCRIPTION,
    BaseDeclaration,
    WithEpdDeveloperMixin,
    WithProgramOperatorMixin,
    WithVerifierMixin,
)
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org, Plant
from openepd.model.specs import Specs
from openepd.model.versioning import OpenEpdVersions, Version

MANUFACTURER_DESCRIPTION = (
    'JSON object for declaring Org. Sometimes called the "Declaration Holder" or "Declaration Owner".'
)


class EpdPreviewV0(
    WithAttachmentsMixin,
    WithProgramOperatorMixin,
    WithEpdDeveloperMixin,
    WithVerifierMixin,
    WithAltIdsMixin,
    BaseDeclaration,
    title="EPD (Preview)",
):
    """
    EPD preview, used in API list responses and where there is no need for a full object.

    Excludes LCIA data.

    """

    doctype: str = pyd.Field(
        description='Describes the type and schema of the document. Must always always read "openEPD".',
        default="openEPD",
    )

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
    manufacturer: Org | None = pyd.Field(description=MANUFACTURER_DESCRIPTION)
    plants: list[Plant] = pyd.Field(
        max_items=32,
        description="List of object(s) for one or more plant(s) that this declaration applies to.",
        default_factory=list,
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

    @pyd.validator("doctype")
    def validate_doctype(cls, v: str | None) -> str:
        """
        Handle possible mixed case options for doctype.

        Required for backward compatibility as some code might have already used 'doctype: OpenEPD' instead of 'openEPD'
        """
        if not v or v.lower() == "openepd":
            return "openEPD"
        raise ValueError("Invalid doctype")


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
