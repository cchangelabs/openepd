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
import pydantic

from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes, OpenEpdExtension
from openepd.model.common import Ingredient, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import (
    DEVELOPER_DESCRIPTION,
    PROGRAM_OPERATOR_DESCRIPTION,
    THIRD_PARTY_VERIFIER_DESCRIPTION,
    BaseDeclaration,
    OriginalDataFormat,
    RefBase,
    WithEpdDeveloperMixin,
    WithProgramOperatorMixin,
    WithVerifierMixin,
)
from openepd.model.geography import Geography
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org, Plant
from openepd.model.specs.singular import Specs
from openepd.model.versioning import OpenEpdVersions, Version

MANUFACTURER_DESCRIPTION = (
    'JSON object for declaring Org. Sometimes called the "Declaration Holder" or "Declaration Owner".'
)

PLANT_DESCRIPTION = "List of object(s) for one or more plant(s) that this declaration applies to."

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


class Ec3EpdExtension(OpenEpdExtension):
    """Extension for EC3 specific fields on openEPD."""

    # While the extensions should be stored under the 'ext' key - extension point of the BaseOpenepdModel - the EC3
    # extension was started before the introduction of extension management, and so is located at the root of the EPD
    # object.

    @classmethod
    def get_extension_name(cls) -> str:
        """Return the name of the extension."""
        return "ec3"

    uaGWP_a1a2a3_traci21: float | None = pydantic.Field(
        default=None,
        description="""The A1A2A3 uncertainty-adjusted GWP, in kgCO2e per declared unit, calculated for the TRACI 2.1
        LCIA method. This is the value that should be used to compare EPDs against each other, or against an
        uncertainty-adjusted limit/benchmark, once both have been converted to the same declared unit. This is a
        materialized value provided for the convenience of integrators, and can be regenerated at any time from the
         specificity and EC3 category. The value is provided per comparison_unit.""",
        examples=[22.5],
    )
    uaGWP_a1a2a3_ar5: float | None = pydantic.Field(
        default=None,
        description="""The A1A2A3 uncertainty-adjusted GWP, calculated for the IPCC AR5 LCIA method. This is the value
        that should be used to compare EPDs against each other, or against an uncertainty-adjusted limit/benchmark,
        once both have been converted to the same declared unit. This is a materialized value, and can be regenerated
        at any time from the specificity and EC3 category.""",
        examples=[22.5],
    )
    category: str | None = pydantic.Field(
        default=None,
        description="The category of the EPD in EC3 notation. Same as EC3 category from root EPD's product_classes for "
        "EC3.",
    )
    manufacturer_specific: bool | None = pydantic.Field(
        default=None,
        description="""An EPD is Manufacturer Specific if it is based on data from a single manufacturer, as opposed
        to an industry group, sector, or generic process. This field should always be true for openEPD documents
        (as opposed to openIndustryEPDs).""",
    )
    plant_specific: bool | None = pydantic.Field(
        default=None,
        description="""An EPD is Product Specific if it is based on data regarding the specific product being
        delivered, as opposed to a range of products whose GWP per unit may vary by more than 10%.""",
    )
    product_specific: bool | None = pydantic.Field(
        default=None,
        description="""An EPD is Product Specific if it is based on data regarding the specific product being
        delivered, as opposed to a range of products whose GWP per unit may vary by more than 10%.""",
    )
    batch_specific: bool | None = pydantic.Field(
        default=None,
        description="""An EPD is Product Specific if it is created with production data for a single production run of
         no more than 90 days. Typically these must be generated on a just-in-time or on-demand basis.""",
    )
    supply_chain_specificity: float | None = pydantic.Field(
        default=None,
        description="""An EPD is Supply Chain Specific to the extent that impacts of process inputs are based on
        product-specific, facility-specific EPDs or third-party verified LCA for those inputs. For example, a concrete
        where the cement impacts are based on a plant-specific, product-specific EPD for the actual cement used would
         have around 85% supply chain specificity.""",
    )

    original_data_format: OriginalDataFormat | None = pydantic.Field(default=None)


class EpdRef(RefBase, title="EPD (Ref)"):
    """Reference (short) version of EPD object."""

    pass


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

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    doctype: str = pydantic.Field(
        description='Describes the type and schema of the document. Must always always read "openEPD".',
        default="openEPD",
    )

    product_name: str | None = pydantic.Field(
        max_length=200,
        description="The name of the product described by this EPD",
        examples=["Mix 12345AC"],
        default=None,
    )
    product_sku: str | None = pydantic.Field(
        max_length=200,
        description="Unique stock keeping identifier assigned by manufacturer",
        default=None,
    )
    product_description: str | None = pydantic.Field(
        max_length=2000,
        description="1-paragraph description of product. Supports plain text or github flavored markdown.",
        default=None,
    )
    manufacturer: Org | None = pydantic.Field(description=MANUFACTURER_DESCRIPTION, default=None)
    plants: list[Plant] = pydantic.Field(
        max_length=32,
        description=PLANT_DESCRIPTION,
        default_factory=list,
    )

    annual_production: float | None = pydantic.Field(
        gt=0,
        default=None,
        description="Approximate annual production volume, in declared units, of product covered by this EPD. "
        "This value is intended to be used for weighting of averages. "
        "Providing this data is optional, and it is acceptable to round or obfuscate it downwards "
        "(but not upwards) by any amount desired to protect confidentiality. For example, if the "
        "product volume is 123,456 m3, a value of 120,000, 100,000 or even 87,654 would be acceptable.",
        examples=[10000],
    )
    applicable_in: list[Geography] | None = pydantic.Field(
        max_length=100,
        default=None,
        description="Jurisdiction(s) in which EPD is applicable. An empty array, or absent properties, "
        "implies global applicability. Accepts "
        "[2-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), "
        "[M49 region codes](https://unstats.un.org/unsd/methodology/m49/), "
        'or the alias "EU27" for the 27 members of the Euro bloc, or the alias "NAFTA" '
        "for the members of North American Free Trade Agreement",
        examples=[["US", "CA", "MX", "EU27", "NAFTA"]],
    )
    product_usage_description: str | None = pydantic.Field(
        default=None,
        description="Text description of how product is typically used. Can be used to describe accessories "
        "like fasteners, adhesives, etc.  Supports plain text or github flavored markdown.",
    )
    product_usage_image: pydantic.AnyUrl | None = pydantic.Field(
        description="Pointer (url) to image illustrating how the product is used. No more than 10MB.",
        default=None,
    )
    manufacturing_description: str | None = pydantic.Field(
        default=None,
        description="Text description of manufacturing process.  Supports plain text or github flavored markdown.",
    )
    manufacturing_image: pydantic.AnyUrl | None = pydantic.Field(
        description="Pointer (url) to an image illustrating the manufacturing process. No more than 10MB.",
        default=None,
    )

    specs: Specs = pydantic.Field(
        default_factory=Specs,
        description="Data structure(s) describing performance specs of product. Unique for each material type.",
    )
    includes: list[Ingredient] = pydantic.Field(
        max_length=255,
        description="List of JSON objects pointing to product components. "
        "Each one should be an EPD or digitized LCI process.",
        default_factory=list,
    )
    ec3: Ec3EpdExtension | None = pydantic.Field(default=None, description="EC3-specific EPD extension.")

    @pydantic.field_validator("doctype", mode="before")
    def validate_doctype(cls, v: str | None) -> str:
        """
        Handle possible mixed case options for doctype.

        Required for backward compatibility as some code might have already used 'doctype: OpenEPD' instead of 'openEPD'
        """
        if not v or v.lower() == "openepd":
            return "openEPD"
        msg = "Invalid doctype"
        raise ValueError(msg)


EpdPreview = EpdPreviewV0


class EpdV0(WithLciaMixin, EpdPreviewV0, title="EPD (Full)"):
    """Represent an EPD."""

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "epd"

    @pydantic.field_validator("compliance", mode="before")
    def validate_compliance(cls, v: list | None):
        """Handle correctly None values for compliance field."""
        if v is None:
            return []
        return v

    @pydantic.field_validator("includes", mode="before")
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

    manufacturer: Org | None = pydantic.Field(description=MANUFACTURER_DESCRIPTION, default=None)  # type: ignore[assignment]
    epd_developer: Org | None = pydantic.Field(description=DEVELOPER_DESCRIPTION, default=None)  # type: ignore[assignment]
    program_operator: Org | None = pydantic.Field(description=PROGRAM_OPERATOR_DESCRIPTION, default=None)  # type: ignore[assignment]
    third_party_verifier: Org | None = pydantic.Field(description=THIRD_PARTY_VERIFIER_DESCRIPTION, default=None)  # type: ignore[assignment]


EpdWithDeps = EpdWithDepsV0


class EpdFactory(BaseDocumentFactory[BaseDeclaration]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = OpenEpdDoctypes.Epd
    VERSION_MAP: dict[Version, type[BaseDeclaration]] = {OpenEpdVersions.Version0: EpdV0}
