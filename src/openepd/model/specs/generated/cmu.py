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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import CmuBlockType, CmuWeightClassification
from openepd.model.validation.quantity import GwpKgCo2eStr, PressureMPaStr


class CMUV1(BaseOpenEpdHierarchicalSpec):
    """Pre-manufactured concrete masonry blocks."""

    _EXT_VERSION = "1.0"

    # Own fields:
    white_cement: bool | None = pyd.Field(default=None, description="", example=True)
    strength_28d: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    weight_classification: CmuWeightClassification | None = pyd.Field(default=None, description="", example="Normal")
    block_type: CmuBlockType | None = pyd.Field(default=None, description="", example="Gray")
    insulated: bool | None = pyd.Field(default=None, description="", example=True)
    sound_performance: bool | None = pyd.Field(default=None, description="", example=True)
    b1_recarbonation: GwpKgCo2eStr | None = pyd.Field(default=None, description="", example="1 kgCO2e")
    b1_recarbonation_z: float | None = pyd.Field(default=None, description="", example=2.3)
