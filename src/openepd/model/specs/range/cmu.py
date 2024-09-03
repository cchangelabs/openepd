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
__all__ = ("CMURangeV1",)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.common import RangeFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import CmuBlockType, CmuWeightClassification
from openepd.model.validation.quantity import AmountRangeGWP, AmountRangePressureMpa


class CMURangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Pre-manufactured concrete masonry blocks.

    Range version.
    """

    _EXT_VERSION = "1.0"

    white_cement: bool | None = pyd.Field(default=None, description="")
    strength_28d: AmountRangePressureMpa | None = pyd.Field(default=None, description="")
    weight_classification: list[CmuWeightClassification] | None = pyd.Field(default=None, description="")
    block_type: list[CmuBlockType] | None = pyd.Field(default=None, description="")
    insulated: bool | None = pyd.Field(default=None, description="")
    sound_performance: bool | None = pyd.Field(default=None, description="")
    b1_recarbonation: AmountRangeGWP | None = pyd.Field(default=None, description="")
    b1_recarbonation_z: RangeFloat | None = pyd.Field(default=None, description="")
