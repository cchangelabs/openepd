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
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMStr, TemperatureCStr, validate_unit_factory

from .enums import *

UnknownStrTypeHandleMe = str


class AsphaltV1(BaseOpenEpdHierarchicalSpec):
    """Asphalt performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    asphalt_aggregate_size_max: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    asphalt_rap: RatioFloat | None = pyd.Field(default=None, description="", example="0.5", ge=0, le=1)
    asphalt_ras: RatioFloat | None = pyd.Field(default=None, description="", example="0.5", ge=0, le=1)
    asphalt_ground_tire_rubber: RatioFloat | None = pyd.Field(default=None, description="", example="0.5", ge=0, le=1)
    asphalt_max_temperature: TemperatureCStr | None = pyd.Field(default=None, description="", example="1 °C")
    asphalt_min_temperature: TemperatureCStr | None = pyd.Field(default=None, description="", example="1 °C")
    asphalt_mix_type: AsphaltMixType | None = pyd.Field(default=None, description="", example="WMA")
    asphalt_gradation: AsphaltGradation | None = pyd.Field(default=None, description="", example="Gap-graded")
    asphalt_sbr: bool | None = pyd.Field(default=None, description="", example="True")
    asphalt_sbs: bool | None = pyd.Field(default=None, description="", example="True")
    asphalt_ppa: bool | None = pyd.Field(default=None, description="", example="True")
    asphalt_gtr: bool | None = pyd.Field(default=None, description="", example="True")
    asphalt_pmb: bool | None = pyd.Field(default=None, description="", example="True")

    _asphalt_aggregate_size_max_is_quantity_validator = pyd.validator("asphalt_aggregate_size_max", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _asphalt_max_temperature_is_quantity_validator = pyd.validator("asphalt_max_temperature", allow_reuse=True)(
        validate_unit_factory("°C")
    )
    _asphalt_min_temperature_is_quantity_validator = pyd.validator("asphalt_min_temperature", allow_reuse=True)(
        validate_unit_factory("°C")
    )
