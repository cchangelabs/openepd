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
    "IndustryEpdPreviewV0",
    "IndustryEpdPreview",
    "IndustryEpdV0",
    "IndustryEpd",
    "IndustryEpdWithDepsV0",
    "IndustryEpdWithDeps",
    "IndustryEpdFactory",
    "IndustryEpdRef",
    "SampleSize",
]

from openepd.model.base import BaseDocumentFactory, OpenEpdDoctypes
from openepd.model.common import WithAltIdsMixin
from openepd.model.lcia import WithLciaMixin
from openepd.model.specs.mixins import AverageDatasetMaterialSpecsMixin
from openepd.model.versioning import OpenEpdVersions, Version

from .light.industry_epd import IndustryEpdPreviewV0 as IndustryEpdPreviewV0Light

# Import light versions here for compatibility reasons so they are available from the same import location
from .light.industry_epd import IndustryEpdRef, SampleSize  # noqa: F401


class IndustryEpdPreviewV0(
    IndustryEpdPreviewV0Light,
    AverageDatasetMaterialSpecsMixin,
):
    """
    Industry EPD Preview object.

    Used in lists and other cases where full LCIA data is not required.
    """


IndustryEpdPreview = IndustryEpdPreviewV0


class IndustryEpdV0(IndustryEpdPreviewV0, WithLciaMixin, WithAltIdsMixin, title="Industry EPD (Full)"):
    """
    Full Industry EPD object.

    This is considered the most complete valid openEPD object for IndustryEpd. In addition to it, several related
    models are defined, either with fewer fields (to be used in APIs for list requests) or with more relaxed structure
    to support related entities matching.
    """


IndustryEpd = IndustryEpdV0


class IndustryEpdWithDepsV0(IndustryEpdV0, title="Industry EPD (with Dependencies)"):
    """
    Expanded version of the IndustryEpd.

    Contains related entities - orgs - with full fields, to support object matching in implementations.

    For now the implementation matches the above Industry Epd entity, but they will diverge as normal GE would have
    some required fields in Org (like web_domain), and WithDeps would not.

    """


IndustryEpdWithDeps = IndustryEpdWithDepsV0


class IndustryEpdFactory(BaseDocumentFactory[IndustryEpd]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = OpenEpdDoctypes.IndustryEpd
    VERSION_MAP: dict[Version, type[IndustryEpd]] = {OpenEpdVersions.Version0: IndustryEpdV0}
