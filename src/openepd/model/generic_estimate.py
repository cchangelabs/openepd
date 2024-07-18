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
from enum import StrEnum

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseDocumentFactory, BaseOpenEpdSchema, OpenEpdDoctypes
from openepd.model.common import WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import BaseDeclaration
from openepd.model.geography import Geography
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org
from openepd.model.validation.common import ReferenceStr
from openepd.model.versioning import OpenEpdVersions, Version


class LicenseTerms(StrEnum):
    """Licensing terms."""

    CC_BY = "CC-BY"
    """
    Creative Commons attribution-only license https://creativecommons.org/licenses/by/4.0/.
    """
    ODbL = "ODbL"
    """
    Open Database License per https://opendatacommons.org/licenses/odbl/
    """
    Government = "Government"
    """
    The data is offered at no charge by a government body such as the USDA or Okobaudat.
    """
    Other = "Other"
    """
    Review estimate documentation to determine license terms.
    """


class GenericEstimateRef(BaseOpenEpdSchema, title="Generic Estimate (Ref)"):
    """Reference (short) version of Generic Estimate object."""

    id: str | None = pyd.Field(
        description="The unique ID for this document.  To ensure global uniqueness, should be registered at "
        "open-xpd-uuid.cqd.io/register or a coordinating registry.",
        example="1u7zsed8",
        default=None,
    )

    name: str | None = pyd.Field(max_length=200, description="Name of the generic estimate", default=None)

    ref: ReferenceStr | None = pyd.Field(
        default=None,
        example="https://openepd.buildingtransparency.org/api/generic_estimates/EC300001",
        description="Reference to this GenericEstimate JSON object",
    )


class GenericEstimatePreviewV0(
    WithAttachmentsMixin, GenericEstimateRef, BaseDeclaration, title="Generic Estimate (preview)"
):
    """
    Generic Estimate preview, used in API list responses and where there is no need for a full object.

    Excludes LCIA data.
    """

    doctype: str = pyd.Field(
        description='Describes the type and schema of the document. Must always be "openGenericEstimate"',
        default="openGenericEstimate",
    )

    description: str | None = pyd.Field(
        max_length=2000,
        description="1-paragraph description of the Generic Estimate. Supports plain text or github flavored markdown.",
    )

    publisher: Org | None = pyd.Field(description="Organization that published the LCA results.")
    reviewer_email: pyd.EmailStr | None = pyd.Field(
        description="Email address of the third party verifier", example="john.doe@example.com", default=None
    )
    reviewer: Org | None = pyd.Field(description="Org that performed a critical review of the LCA.")
    license_terms: LicenseTerms | None = pyd.Field(description="The license terms for use of the data.")
    geography: list[Geography] | None = pyd.Field(
        "Jurisdiction(s) in which the LCA result is applicable.  An empty array, or absent properties, implies global applicability."
    )
    model_repository: pyd.AnyUrl | None = pyd.Field(
        default=None, description="A link to the shared git repository containing the LCA model used for this estimate."
    )


GenericEstimatePreview = GenericEstimatePreviewV0


class GenericEstimateV0(GenericEstimatePreviewV0, WithLciaMixin, WithAltIdsMixin, title="Generic Estimate (Full)"):
    """
    Represent a full Generic Estimate object.

    This is considered the most complete valid openEPD object for GenericEstimate. In addition to it, several related
    models are defined, either with fewer fields (to be used in APIs for list requests) or with more relaxed structure
    to support related entities matching.
    """

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()


GenericEstimate = GenericEstimateV0


class GenericEstimateWithDepsV0(GenericEstimateV0, title="Generic Estimate (with Dependencies)"):
    """
    Expanded version of the GenericEstimate.

    Contains related entities - orgs - with full fields, to support object matching in implementations.

    For now the implementation matches the above GenericEstimate entity, but they will diverge as normal GE would have
    some required fields in Org (like web_domain), and WithDeps would not.

    """

    publisher: Org | None = pyd.Field(description="Organization that published the LCA results.")
    reviewer: Org | None = pyd.Field(description="Org that performed a critical review of the LCA.")


GenericEstimateWithDeps = GenericEstimateWithDepsV0


class GenericEstimateFactory(BaseDocumentFactory[GenericEstimate]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = OpenEpdDoctypes.GenericEstimate
    VERSION_MAP: dict[Version, type[GenericEstimate]] = {OpenEpdVersions.Version0: GenericEstimateV0}
