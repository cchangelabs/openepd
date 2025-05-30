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

from openepd.model.specs.base import BaseOpenEpdSpec
from openepd.model.specs.enums import (
    AccessFlooringCoreMaterial,
    AccessFlooringFinishMaterial,
    AccessFlooringSeismicRating,
    AccessFlooringStringers,
)
from openepd.model.validation.quantity import ForceNStr, LengthMmStr, PressureMPaStr, validate_quantity_unit_factory


class AccessFlooringMixin(BaseOpenEpdSpec):
    core_material: AccessFlooringCoreMaterial | None = pyd.Field(
        default=None, description="", examples=["Cementitious"]
    )
    finish_material: AccessFlooringFinishMaterial | None = pyd.Field(
        default=None, description="", examples=["Linoleum"]
    )
    stringers: AccessFlooringStringers | None = pyd.Field(default=None, description="", examples=["Standard"])
    seismic_rating: AccessFlooringSeismicRating | None = pyd.Field(default=None, description="", examples=["Type 0"])
    magnetically_attached_finish: bool | None = pyd.Field(default=None, description="", examples=[True])
    permanent_finish: bool | None = pyd.Field(default=None, description="", examples=[True])
    drylay: bool | None = pyd.Field(default=None, description="", examples=[True])
    adjustable_height: bool | None = pyd.Field(default=None, description="", examples=[True])
    fixed_height: bool | None = pyd.Field(default=None, description="", examples=[True])
    finished_floor_height: LengthMmStr | None = pyd.Field(default=None, description="", examples=["1 m"])
    panel_thickness: LengthMmStr | None = pyd.Field(default=None, description="", examples=["1 m"])
    concentrated_load: PressureMPaStr | None = pyd.Field(default=None, description="", examples=["1 MPa"])
    uniform_load: PressureMPaStr | None = pyd.Field(default=None, description="", examples=["1 MPa"])
    rolling_load_10_pass: ForceNStr | None = pyd.Field(default=None, description="", examples=["1 N"])
    rolling_load_10000_pass: ForceNStr | None = pyd.Field(default=None, description="", examples=["1 N"])

    @pyd.field_validator("rolling_load_10_pass", mode="before", check_fields=False)
    def _access_flooring_rolling_load_10_pass_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("N")(cls, value)

    @pyd.field_validator("rolling_load_10000_pass", mode="before", check_fields=False)
    def _access_flooring_rolling_load_10000_pass_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("N")(cls, value)
