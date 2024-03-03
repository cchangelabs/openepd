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
from enum import StrEnum

import pydantic as pyd

from openepd.model.common import OpenEPDUnit
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, TemperatureCStr, validate_unit_factory


class AsphaltMixType(StrEnum):
    """Asphalt mix type enum."""

    HMA = "HMA"
    WMA = "WMA"


class AsphaltGradation(StrEnum):
    """Asphalt gradation enum."""

    Dense_graded = "Dense-graded"
    Open_graded = "Open-graded"
    Gap_graded = "Gap-graded"


class AsphaltV1(BaseOpenEpdHierarchicalSpec):
    """Asphalt spec."""

    _EXT_VERSION = "1.0"

    asphalt_aggregate_size_max: LengthMmStr | None = pyd.Field(
        default=None, example="5mm", description="Max aggregate size"
    )

    asphalt_rap: RatioFloat | None = pyd.Field(
        default=None, description="Percent of mixture that has been replaced by recycled " "asphalt pavement (RAP)."
    )
    asphalt_ras: RatioFloat | None = pyd.Field(
        default=None, description="Percent of mixture that has been replaced by recycled " "asphalt shingles (RAS)."
    )
    asphalt_ground_tire_rubber: RatioFloat | None = pyd.Field(
        default=None, description="Percent of mixture that has been replaced " "by ground tire rubber (GTR)."
    )

    asphalt_max_temperature: TemperatureCStr | None = pyd.Field(
        default=None,
        description="The upper threshold temperature to which an asphalt "
        "binder can be heated preventing the asphalt mixture "
        "from rutting",
    )
    asphalt_min_temperature: TemperatureCStr | None = pyd.Field(
        default=None,
        description="The lower threshold temperature for an asphalt "
        "binder to prevent thermal cracking of the asphalt"
        " mixture.",
    )

    asphalt_mix_type: AsphaltMixType | None = pyd.Field(default=None, description="Asphalt mix type")
    asphalt_gradation: AsphaltGradation | None = pyd.Field(default=None, description="Asphalt gradation")

    asphalt_sbr: bool | None = pyd.Field(default=None, description="Styrene-butadiene rubber (SBR)")
    asphalt_sbs: bool | None = pyd.Field(default=None, description="Styrene-butadiene-styrene (SBS)")
    asphalt_ppa: bool | None = pyd.Field(default=None, description="Polyphosphoric acid (PPA)")
    asphalt_gtr: bool | None = pyd.Field(default=None, description="Ground tire rubber (GTR)")
    asphalt_pmb: bool | None = pyd.Field(default=None, description="Polymer modified bitumen (PMB)")

    _aggregate_size_max_validator = pyd.validator("asphalt_aggregate_size_max", allow_reuse=True)(
        validate_unit_factory(OpenEPDUnit.m)
    )
