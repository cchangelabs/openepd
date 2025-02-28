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
__all__ = ("AsphaltRangeV1",)

import pydantic

from openepd.model.common import RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import AsphaltGradation, AsphaltMixType
from openepd.model.validation.quantity import AmountRangeLengthMm, TemperatureCStr

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class AsphaltRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    General category for asphalt mixtures.

    Range version.
    """

    _EXT_VERSION = "1.0"

    aggregate_size_max: AmountRangeLengthMm | None = pydantic.Field(default=None, description="Max aggregate size")
    rap: RangeRatioFloat | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt pavement (RAP).",
    )
    ras: RangeRatioFloat | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by recycled asphalt shingles (RAS).",
    )
    ground_tire_rubber: RangeRatioFloat | None = pydantic.Field(
        default=None,
        description="Percent of mixture that has been replaced by ground tire rubber (GTR).",
    )
    max_temperature: TemperatureCStr | None = pydantic.Field(
        default=None,
        description="The upper threshold temperature to which an asphalt binder can be heated preventing the asphalt mixture from rutting",
    )
    min_temperature: TemperatureCStr | None = pydantic.Field(
        default=None,
        description="The lower threshold temperature for an asphalt binder to prevent thermal cracking of the asphalt mixture.",
    )
    mix_type: list[AsphaltMixType] | None = pydantic.Field(default=None, description="Asphalt mix type")
    gradation: list[AsphaltGradation] | None = pydantic.Field(default=None, description="Asphalt gradation")
    sbr: bool | None = pydantic.Field(default=None, description="Styrene-butadiene rubber (SBR)")
    sbs: bool | None = pydantic.Field(default=None, description="Styrene-butadiene-styrene (SBS)")
    ppa: bool | None = pydantic.Field(default=None, description="Polyphosphoric acid (PPA)")
    gtr: bool | None = pydantic.Field(default=None, description="Ground tire rubber (GTR)")
    pmb: bool | None = pydantic.Field(default=None, description="Polymer modified bitumen (PMB)")
