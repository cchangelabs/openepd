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
from openepd.model.specs.enums import AsphaltGradation, AsphaltMixType
from openepd.model.validation.quantity import LengthMmStr, TemperatureCStr


class AsphaltV1(BaseOpenEpdHierarchicalSpec):
    """General category for asphalt mixtures."""

    _EXT_VERSION = "1.0"

    # Own fields:
    aggregate_size_max: LengthMmStr | None = pydantic.Field(
        default=None, description="Max aggregate size", examples=["20 mm"]
    )
    rap: float | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt pavement (RAP).",
        examples=[0.5],
        ge=0,
        le=1,
    )
    ras: float | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt shingles (RAS).",
        examples=[0.5],
        ge=0,
        le=1,
    )
    ground_tire_rubber: float | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by ground tire rubber (GTR).",
        examples=[0.5],
        ge=0,
        le=1,
    )
    max_temperature: Annotated[TemperatureCStr | None, CodegenSpec(override_type=TemperatureCStr)] = pydantic.Field(
        default=None,
        description="The upper threshold temperature to which an asphalt "
        "binder can be heated preventing the asphalt mixture "
        "from rutting",
        examples=["90 °C"],
    )
    min_temperature: Annotated[TemperatureCStr | None, CodegenSpec(override_type=TemperatureCStr)] = pydantic.Field(
        default=None,
        description="The lower threshold temperature for an asphalt "
        "binder to prevent thermal cracking of the asphalt"
        " mixture.",
        examples=["-20 °C"],
    )
    mix_type: AsphaltMixType | None = pydantic.Field(default=None, description="Asphalt mix type", examples=["WMA"])
    gradation: AsphaltGradation | None = pydantic.Field(
        default=None, description="Asphalt gradation", examples=["Gap-graded"]
    )

    sbr: bool | None = pydantic.Field(
        default=None,
        description="Styrene-butadiene rubber (SBR)",
        examples=[True],
    )
    sbs: bool | None = pydantic.Field(
        default=None,
        description="Styrene-butadiene-styrene (SBS)",
        examples=[True],
    )
    ppa: bool | None = pydantic.Field(
        default=None,
        description="Polyphosphoric acid (PPA)",
        examples=[True],
    )
    gtr: bool | None = pydantic.Field(
        default=None,
        description="Ground tire rubber (GTR)",
        examples=[True],
    )
    pmb: bool | None = pydantic.Field(
        default=None,
        description="Polymer modified bitumen (PMB)",
        examples=[True],
    )
