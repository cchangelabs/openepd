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
from openepd.model.base import BaseDocumentFactory, RootDocument
from openepd.model.common import WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.epd import BaseDeclaration
from openepd.model.org import Org
from openepd.model.versioning import OpenEpdVersions, Version


class LicenseTerms(StrEnum):
    CC_BY = "CC-BY"
    ODbL = "ODbL"
    Government = "Government"
    Other = "Other"


# todo generate geography as a static list, change in code when it changes. This would help all static code generators and tooling
class Geography(StrEnum):
    US = "US-CA"


class GenericEstimateV0(WithAttachmentsMixin, WithAltIdsMixin, BaseDeclaration):
    """Represent a Generic Estimate."""

    _FORMAT_VERSION = OpenEpdVersions.Version0.as_str()

    doctype: str = pyd.Field(
        description='Describes the type and schema of the document. Must always be "openGenericEstimate"',
        default="openGenericEstimate",
    )

    name: str | None = pyd.Field(max_length=200, description="", default=None)
    description: str | None = pyd.Field(
        max_length=2000,
        description="1-paragraph description of the Generic Estimate. Supports plain text or github flavored markdown.",
    )

    publisher: Org | None = pyd.Field(description="Organization that published the LCA results.")
    reviewer_email: pyd.EmailStr | None = pyd.Field(
        description="Email address of the third party verifier", example="john.doe@example.com", default=None
    )
    reviewer: Org | None = pyd.Field(description="Org that performed a critical review of the LCA.")
    license_terms: list[LicenseTerms] | None = pyd.Field(description="The license terms for use of the data.")
    geography: list[Geography] | None = pyd.Field(
        "Jurisdiction(s) in which the LCA result is applicable.  An empty array, or absent properties, implies global applicability."
    )
    model_repository: pyd.AnyUrl | None = pyd.Field(
        default=None, description="A link to the shared git repository containing the LCA model used for this estimate."
    )


GenericEstimate = GenericEstimateV0


class GenericEstimateFactory(BaseDocumentFactory[GenericEstimate]):
    """Factory for EPD objects."""

    DOCTYPE_CONSTRAINT = "openGenericEstimate"
    VERSION_MAP: dict[Version, type[BaseDeclaration]] = {OpenEpdVersions.Version0: GenericEstimateV0}
