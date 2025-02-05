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

from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, CodegenSpec
from openepd.model.specs.enums import AsphaltGradation, AsphaltMixType
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, TemperatureCStr


class AsphaltV1(BaseOpenEpdHierarchicalSpec):
    """General category for asphalt mixtures."""

    _EXT_VERSION = "1.0"

    # Own fields:
    aggregate_size_max: LengthMmStr | None = pyd.Field(default=None, description="Max aggregate size", example="20 mm")
    rap: RatioFloat | None = pyd.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt pavement (RAP).",
        example=0.5,
        ge=0,
        le=1,
    )
    ras: RatioFloat | None = pyd.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt shingles (RAS).",
        example=0.5,
        ge=0,
        le=1,
    )
    ground_tire_rubber: RatioFloat | None = pyd.Field(
        default=None,
        description="Percent of mixture that has been replaced by ground tire rubber (GTR).",
        example=0.5,
        ge=0,
        le=1,
    )
    max_temperature: Annotated[TemperatureCStr | None, CodegenSpec(override_type=TemperatureCStr)] = pyd.Field(
        default=None,
        description="The upper threshold temperature to which an asphalt "
        "binder can be heated preventing the asphalt mixture "
        "from rutting",
        example="90 °C",
    )
    min_temperature: Annotated[TemperatureCStr | None, CodegenSpec(override_type=TemperatureCStr)] = pyd.Field(
        default=None,
        description="The lower threshold temperature for an asphalt "
        "binder to prevent thermal cracking of the asphalt"
        " mixture.",
        example="-20 °C",
    )
    mix_type: AsphaltMixType | None = pyd.Field(default=None, description="Asphalt mix type", example="WMA")
    gradation: AsphaltGradation | None = pyd.Field(default=None, description="Asphalt gradation", example="Gap-graded")

    sbr: bool | None = pyd.Field(default=None, description="Styrene-butadiene rubber (SBR)", example=True)
    sbs: bool | None = pyd.Field(default=None, description="Styrene-butadiene-styrene (SBS)", example=True)
    ppa: bool | None = pyd.Field(default=None, description="Polyphosphoric acid (PPA)", example=True)
    gtr: bool | None = pyd.Field(default=None, description="Ground tire rubber (GTR)", example=True)
    pmb: bool | None = pyd.Field(default=None, description="Polymer modified bitumen (PMB)", example=True)
