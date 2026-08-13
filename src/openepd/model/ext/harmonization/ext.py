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

import pydantic as pyd

from openepd.model.base import OpenEpdExtension
from openepd.model.ext.harmonization.coproducts import CoproductsHarmonizationFactor
from openepd.model.ext.harmonization.custom import CustomHarmonizationFactor
from openepd.model.ext.harmonization.eac import EacHarmonizationFactor
from openepd.model.ext.harmonization.mbvfa import MbvfaHarmonizationFactor
from openepd.model.ext.harmonization.offsets import OffsetsHarmonizationFactor


class HarmonizationEpdExtension(OpenEpdExtension):
    """OpenEPD extension payload for harmonization factors."""

    model_config = pyd.ConfigDict(extra="allow")
    __pydantic_extra__: dict[str, CustomHarmonizationFactor] = pyd.Field(init=False)

    coproducts: CoproductsHarmonizationFactor | None = pyd.Field(
        default=None,
        description=(
            "Documents allocation of impact burdens to products other than the primary product. "
            "These factors can be used to harmonize across allocation methodologies."
        ),
    )
    eac: EacHarmonizationFactor | None = pyd.Field(
        default=None,
        description=(
            "Documents the use and effects of Energy Attribute Certificates, "
            "including RECs and Guarantees of Origin, rather than grid emissions."
        ),
    )
    mbvfa: MbvfaHarmonizationFactor | None = pyd.Field(
        default=None,
        description=(
            "Documents the use and effects of Mass Balanced Virtual Feedstock Allocation, "
            "including book-and-claim and related accounting approaches."
        ),
    )
    offsets: OffsetsHarmonizationFactor | None = pyd.Field(
        default=None,
        description="Documents the use and effects of offsets, including registry standards and retirement coverage.",
    )

    @classmethod
    def get_extension_name(cls) -> str:
        """
        Return the OpenEPD extension namespace segment.

        :returns: The extension name used under ``ext.<name>``.
        """
        return "harmonization"
