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
from typing import Literal

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseDocumentFactory, BaseOpenEpdSchema, OpenEpdDoctypes
from openepd.model.common import WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.declaration import (
    AverageDatasetMixin,
    BaseDeclaration,
    RefBase,
    WithEpdDeveloperMixin,
    WithProgramOperatorMixin,
    WithVerifierMixin,
)
from openepd.model.lcia import WithLciaMixin
from openepd.model.org import Org
from openepd.model.versioning import OpenEpdVersions, Version


class SampleSize(BaseOpenEpdSchema):
    """Sample size."""

    products: pyd.NonNegativeInt | None = pyd.Field(
        default=None,
        description="Count of separate products or results that were included in this industry EPD, "
        "and over which the standard deviation was calculated",
    )
    plants: pyd.NonNegativeInt | None = pyd.Field(
        default=None, description="Count of unique manufacturing plants that submitted data for this Industry EPD"
    )
    manufacturers: pyd.NonNegativeInt | None = pyd.Field(
        default=None, description="Count of unique manufacturing companies that submitted data for this Industry EPD"
    )


class IndustryEpdRef(RefBase, title="Industry EPD (Ref)"):
    """Reference (short) version of Industry average EPD object."""


class IndustryEpdPreviewV0(
    WithAttachmentsMixin,
    AverageDatasetMixin,
    WithEpdDeveloperMixin,
    WithVerifierMixin,
    WithProgramOperatorMixin,
    IndustryEpdRef,
    BaseDeclaration,
    title="Industry EPD (preview)",
):
    """
    Industry EPD Preview object.

    Used in lists and other cases where full LCIA data is not required.
    """

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    doctype: Literal["openIndustryEpd"] = pyd.Field(
        description='Describes the type and schema of the document. Must always be "openIndustryEpd"',
        default="openIndustryEpd",
    )

    sample_size: SampleSize | None = None

    publishers: list[Org] | None = pyd.Field(description="")
    manufacturers: list[Org] | None = pyd.Field(description="Participating manufacturers")


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
