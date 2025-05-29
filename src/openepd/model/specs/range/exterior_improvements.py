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
import pydantic as pyd

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import AmountRangePressureMpa


class ConcretePaversRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Segmental units of concrete of standardized sizes and shapes for use in paving applications.

    Includes pavers and paving slabs.
    """

    _EXT_VERSION = "1.0"

    compressive_strength: AmountRangePressureMpa | None = pyd.Field(
        default=None,
        description=(
            "Unit strength in MPa, ksi, or psi. "
            "This is the net compressive strength, also known as unit strength, as opposed to f′ₘ (f prime m) which is "
            "the strength of the completed wall module."
        ),
    )
    white_cement: bool | None = pyd.Field(default=None, description="CMU using some portion of white cement")


class ExteriorImprovementsRangeV1(BaseOpenEpdHierarchicalSpec):
    """Products that alter the exterior appearance of a lot or its structures."""

    _EXT_VERSION = "1.0"

    ConcretePavers: ConcretePaversRangeV1 | None = None
