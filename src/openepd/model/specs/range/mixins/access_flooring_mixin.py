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
from openepd.model.validation.quantity import AmountRangeForce, AmountRangeLengthMm, AmountRangePressureMpa


class AccessFlooringRangeMixin(BaseOpenEpdSpec):
    core_material: list[AccessFlooringCoreMaterial] | None = pyd.Field(default=None, description="")
    finish_material: list[AccessFlooringFinishMaterial] | None = pyd.Field(default=None, description="")
    stringers: list[AccessFlooringStringers] | None = pyd.Field(default=None, description="")
    seismic_rating: list[AccessFlooringSeismicRating] | None = pyd.Field(default=None, description="")
    magnetically_attached_finish: bool | None = pyd.Field(default=None, description="")
    permanent_finish: bool | None = pyd.Field(default=None, description="")
    drylay: bool | None = pyd.Field(default=None, description="")
    adjustable_height: bool | None = pyd.Field(default=None, description="")
    fixed_height: bool | None = pyd.Field(default=None, description="")
    finished_floor_height: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    panel_thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    concentrated_load: AmountRangePressureMpa | None = pyd.Field(default=None, description="")
    uniform_load: AmountRangePressureMpa | None = pyd.Field(default=None, description="")
    rolling_load_10_pass: AmountRangeForce | None = pyd.Field(default=None, description="")
    rolling_load_10000_pass: AmountRangeForce | None = pyd.Field(default=None, description="")
