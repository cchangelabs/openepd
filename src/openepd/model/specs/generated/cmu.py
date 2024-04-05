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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import CmuBlockType, CmuWeightClassification
from openepd.model.validation.quantity import GwpKgCo2eStr, PressureMPaStr, validate_unit_factory


class CMUV1(BaseOpenEpdHierarchicalSpec):
    """CMU performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    white_cement: bool | None = pyd.Field(default=None, description="", example="True")
    concrete_compressive_strength_28d: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    cmu_weight_classification: CmuWeightClassification | None = pyd.Field(
        default=None, description="", example="Normal"
    )
    cmu_block_type: CmuBlockType | None = pyd.Field(default=None, description="", example="Gray")
    cmu_insulated: bool | None = pyd.Field(default=None, description="", example="True")
    cmu_sound_performance: bool | None = pyd.Field(default=None, description="", example="True")
    b1_recarbonation: GwpKgCo2eStr | None = pyd.Field(default=None, description="", example="1 kgCO2e")
    b1_recarbonation_z: float | None = pyd.Field(default=None, description="", example="2.3")

    _concrete_compressive_strength_28d_is_quantity_validator = pyd.validator(
        "concrete_compressive_strength_28d", allow_reuse=True
    )(validate_unit_factory("MPa"))
    _b1_recarbonation_is_quantity_validator = pyd.validator("b1_recarbonation", allow_reuse=True)(
        validate_unit_factory("kgCO2e")
    )