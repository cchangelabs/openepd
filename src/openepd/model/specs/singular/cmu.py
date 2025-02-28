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
from typing import Annotated

import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, CodegenSpec
from openepd.model.specs.enums import CmuBlockType, CmuWeightClassification
from openepd.model.validation.quantity import GwpKgCo2eStr, PressureMPaStr


class CMUV1(BaseOpenEpdHierarchicalSpec):
    """Pre-manufactured concrete masonry blocks."""

    _EXT_VERSION = "1.0"

    # Own fields:
    white_cement: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    strength_28d: PressureMPaStr | None = pydantic.Field(default=None, description="", examples=["1 MPa"])
    weight_classification: CmuWeightClassification | None = pydantic.Field(
        default=None, description="", examples=["Normal"]
    )
    block_type: CmuBlockType | None = pydantic.Field(default=None, description="", examples=["Gray"])
    insulated: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    sound_performance: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    b1_recarbonation: Annotated[GwpKgCo2eStr | None, CodegenSpec(override_type=GwpKgCo2eStr)] = pydantic.Field(
        default=None, description="", examples=["1 kgCO2e"]
    )
    b1_recarbonation_z: Annotated[float | None, CodegenSpec(override_type=float)] = pydantic.Field(
        default=None, description="", examples=[2.3]
    )
