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
from enum import StrEnum
from typing import Literal

import pydantic

from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes
from openepd.model.common import WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import AverageDatasetMixin, BaseDeclaration, RefBase
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org
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


class GenericEstimateRef(RefBase, title="Generic Estimate (Ref)"):
    """Reference (short) version of Generic Estimate object."""


class GenericEstimatePreviewV0(
    WithAttachmentsMixin,
    AverageDatasetMixin,
    GenericEstimateRef,
    BaseDeclaration,
    title="Generic Estimate (preview)",
):
    """
    Generic Estimate preview, used in API list responses and where there is no need for a full object.

    Excludes LCIA data.
    """

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    doctype: Literal["openGenericEstimate"] = pydantic.Field(
        description='Describes the type and schema of the document. Must always be "openGenericEstimate"',
        default="openGenericEstimate",
    )

    publisher: Org | None = pydantic.Field(description="Organization that published the LCA results.", default=None)
    reviewer: Org | None = pydantic.Field(description="Org that performed a critical review of the LCA.", default=None)
    reviewer_email: pydantic.EmailStr | None = pydantic.Field(
        description="Email address of the third party verifier",
        examples=["john.doe@example.com"],
        default=None,
    )

    license_terms: LicenseTerms | None = pydantic.Field(
        description="The license terms for use of the data.", default=None
    )
    model_repository: pydantic.AnyUrl | None = pydantic.Field(
        default=None,
        description="A link to the shared git repository containing the LCA model used for this estimate.",
    )

    model_config = pydantic.ConfigDict(
        protected_namespaces=(),
    )


GenericEstimatePreview = GenericEstimatePreviewV0


class GenericEstimateV0(
    GenericEstimatePreviewV0,
    WithLciaMixin,
    WithAltIdsMixin,
    title="Generic Estimate (Full)",
):
    """Full Generic Estimate object."""


GenericEstimate = GenericEstimateV0


class GenericEstimateWithDepsV0(GenericEstimateV0, title="Generic Estimate (with Dependencies)"):
    """
    Expanded version of the GenericEstimate.

    Contains related entities - orgs - with full fields, to support object matching in implementations.
    """

    publisher: Org | None = pydantic.Field(description="Organization that published the LCA results.", default=None)  # type: ignore[assignment]
    reviewer: Org | None = pydantic.Field(description="Org that performed a critical review of the LCA.", default=None)  # type: ignore[assignment]


GenericEstimateWithDeps = GenericEstimateWithDepsV0


class GenericEstimateFactory(BaseDocumentFactory[GenericEstimate]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = OpenEpdDoctypes.GenericEstimate
    VERSION_MAP: dict[Version, type[GenericEstimate]] = {OpenEpdVersions.Version0: GenericEstimateV0}
