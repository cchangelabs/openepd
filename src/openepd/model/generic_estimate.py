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
__all__ = [
    "GenericEstimatePreviewV0",
    "GenericEstimatePreview",
    "GenericEstimateV0",
    "GenericEstimate",
    "GenericEstimateWithDepsV0",
    "GenericEstimateWithDeps",
    "GenericEstimateFactory",
    "GenericEstimateRef",
    "LicenseTerms",
]

import pydantic

from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes
from openepd.model.common import WithAltIdsMixin
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org
from openepd.model.specs.mixins import AverageDatasetMaterialSpecsMixin
from openepd.model.versioning import OpenEpdVersions, Version

from .light.generic_estimate import GenericEstimatePreviewV0 as GenericEstimatePreviewV0Light

# Import light versions here for compatibility reasons so they are available from the same import location
from .light.generic_estimate import GenericEstimateRef, LicenseTerms  # noqa: F401


class GenericEstimatePreviewV0(
    GenericEstimatePreviewV0Light,
    AverageDatasetMaterialSpecsMixin,
):
    """
    Generic Estimate preview, used in API list responses and where there is no need for a full object.

    Excludes LCIA data.
    """


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
