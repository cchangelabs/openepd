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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdSpec
from openepd.model.specs.enums import (
    AccessFlooringCoreMaterial,
    AccessFlooringFinishMaterial,
    AccessFlooringSeismicRating,
    AccessFlooringStringers,
)
from openepd.model.validation.quantity import ForceNStr, LengthMmStr, PressureMPaStr, validate_quantity_unit_factory


class AccessFlooringMixin(BaseOpenEpdSpec):
    core_material: AccessFlooringCoreMaterial | None = pyd.Field(default=None, description="", example="Cementitious")
    finish_material: AccessFlooringFinishMaterial | None = pyd.Field(default=None, description="", example="Linoleum")
    stringers: AccessFlooringStringers | None = pyd.Field(default=None, description="", example="Standard")
    seismic_rating: AccessFlooringSeismicRating | None = pyd.Field(default=None, description="", example="Type 0")
    magnetically_attached_finish: bool | None = pyd.Field(default=None, description="", example=True)
    permanent_finish: bool | None = pyd.Field(default=None, description="", example=True)
    drylay: bool | None = pyd.Field(default=None, description="", example=True)
    adjustable_height: bool | None = pyd.Field(default=None, description="", example=True)
    fixed_height: bool | None = pyd.Field(default=None, description="", example=True)
    finished_floor_height: LengthMmStr | None = pyd.Field(default=None, description="", example="1 m")
    panel_thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="1 m")
    concentrated_load: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    uniform_load: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    rolling_load_10_pass: ForceNStr | None = pyd.Field(default=None, description="", example="1 N")
    rolling_load_10000_pass: ForceNStr | None = pyd.Field(default=None, description="", example="1 N")

    _access_flooring_rolling_load_10_pass_is_quantity_validator = pyd.validator(
        "rolling_load_10_pass", allow_reuse=True
    )(validate_quantity_unit_factory("N"))
    _access_flooring_rolling_load_10000_pass_is_quantity_validator = pyd.validator(
        "rolling_load_10000_pass", allow_reuse=True
    )(validate_quantity_unit_factory("N"))
