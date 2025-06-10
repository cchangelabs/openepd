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
from enum import StrEnum

import pydantic

from openepd.model.common import OpenEPDUnit
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import LengthMmStr, TemperatureCStr, validate_quantity_unit_factory


class AsphaltMixType(StrEnum):
    """Asphalt mix type enum."""

    HMA = "HMA"
    WMA = "WMA"


class AsphaltGradation(StrEnum):
    """Asphalt gradation enum."""

    Dense_graded = "Dense-graded"
    Open_graded = "Open-graded"
    Gap_graded = "Gap-graded"
    Permeable = "Permeable"
    Porous = "Porous"
    Other = "Other"


class AsphaltV1(BaseOpenEpdHierarchicalSpec):
    """Asphalt spec."""

    _EXT_VERSION = "1.1"

    asphalt_aggregate_size_max: LengthMmStr | None = pydantic.Field(
        default=None, examples=["5mm"], description="Max aggregate size"
    )

    asphalt_rap: float | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt pavement (RAP).",
        ge=0,
        le=1,
    )
    asphalt_ras: float | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt shingles (RAS).",
        ge=0,
        le=1,
    )
    asphalt_ground_tire_rubber: float | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by ground tire rubber (GTR).",
        ge=0,
        le=1,
    )

    asphalt_max_temperature: TemperatureCStr | None = pydantic.Field(
        default=None,
        description="The upper threshold temperature to which an asphalt "
        "binder can be heated preventing the asphalt mixture "
        "from rutting",
    )
    asphalt_min_temperature: TemperatureCStr | None = pydantic.Field(
        default=None,
        description="The lower threshold temperature for an asphalt "
        "binder to prevent thermal cracking of the asphalt"
        " mixture.",
    )

    asphalt_mix_type: AsphaltMixType | None = pydantic.Field(default=None, description="Asphalt mix type")
    asphalt_gradation: AsphaltGradation | None = pydantic.Field(default=None, description="Asphalt gradation")

    asphalt_sbr: bool | None = pydantic.Field(default=None, description="Styrene-butadiene rubber (SBR)")
    asphalt_sbs: bool | None = pydantic.Field(default=None, description="Styrene-butadiene-styrene (SBS)")
    asphalt_ppa: bool | None = pydantic.Field(default=None, description="Polyphosphoric acid (PPA)")
    asphalt_gtr: bool | None = pydantic.Field(default=None, description="Ground tire rubber (GTR)")
    asphalt_pmb: bool | None = pydantic.Field(default=None, description="Polymer modified bitumen (PMB)")

    @pydantic.field_validator("asphalt_aggregate_size_max", mode="before")
    def _aggregate_size_max_validator(cls, value):
        return validate_quantity_unit_factory(OpenEPDUnit.m)(cls, value)
