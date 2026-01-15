#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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
from uuid import UUID

import pydantic

from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes
from openepd.model.common import Amount, Constituent, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import AverageDatasetMixin, BaseDeclaration, RefBase
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org
from openepd.model.resource import DatabaseResource, SoftwareResource
from openepd.model.validation.quantity import AmountMass
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
    name: str | None = pydantic.Field(
        max_length=200,
        description="Name. Recommended < 80 chars.",
        examples=["Aluminium profiles for windows, doors, and facades - anodized"],
        default=None,
    )
    id: UUID | None = pydantic.Field(  # type: ignore[assignment]
        description=(
            "Unique UUID for this dataset."
            "Use the UUID of the original source where possible, and put any other UUIDs in alt_ids."
        ),
        examples=["0197ad82-92cf-7978-a6c8-d4964c0a3624"],
        default=None,
    )
    kg_per_declared_unit: AmountMass | None = pydantic.Field(
        description="Mass of the product, in kilograms, per declared unit",
        examples=[Amount(qty=12.5, unit="kg").to_serializable(exclude_unset=True)],
        default=None,
    )
    reference_year: int | None = pydantic.Field(
        gt=2000,
        description=(
            "The year which the overall inventory represents best, considering the age/representativeness of the "
            "various specific and background data included.  May be used to calculate data quality indicators."
        ),
        default=None,
    )
    composition: list[Constituent] | None = pydantic.Field(
        max_length=255,
        description=(
            "List of constituent materials for use in making required declarations downstream, "
            "such as hazardous substances."
        ),
        default=None,
    )
    lci_databases: list[DatabaseResource] = pydantic.Field(
        description="LCI Database(s) and Version",
        default_factory=list,
        examples=[
            [
                {
                    "owner": {"web_domain": "ecoinvent.org"},
                    "name": "ecoinvent",
                    "version": "3.10",
                    "link": "https://support.ecoinvent.org/ecoinvent-version-3.10",
                },
                {
                    "owner": {"web_domain": "lcacommons.gov"},
                    "name": "ULSCI",
                    "version": "FY24.Q3.01",
                    "link": "https://www.lcacommons.gov/lca-collaboration/National_Renewable_Energy_Laboratory/USLCI_Database_Public/datasets",
                },
            ]
        ],
    )
    software_used: list[SoftwareResource] = pydantic.Field(
        description="List of software tool(s) and version(s) used for LCA and/or EPD generation.",
        default_factory=list,
        examples=[
            [
                {
                    "owner": {"web_domain": "greendelta.com"},
                    "primary_function": "LCA Analysis",
                    "name": "openLCA",
                    "version": "2.3.1",
                    "link": "https://share.greendelta.com/index.php/s/D1xa3haTiHJdhqt?path=%2F2.3.1",
                }
            ]
        ],
    )

    publisher: Org | None = pydantic.Field(description="Organization that published the LCA results.", default=None)
    reviewer: Org | None = pydantic.Field(description="Org that performed a critical review of the LCA.", default=None)
    reviewer_email: pydantic.EmailStr | None = pydantic.Field(
        description="Email address of the third party verifier",
        examples=["john.doe@example.com"],
        default=None,
    )
    owner: Org | None = pydantic.Field(description="Org who owns or publishes this dataset.", default=None)

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
