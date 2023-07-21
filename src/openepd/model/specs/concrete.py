#
#  Copyright 2023 by C Change Labs Inc. www.c-change-labs.com
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

from openepd.model.base import BaseOpenEpdSpec


class CmuWeightClassification(StrEnum):
    """Concrete Masonry Unit weight classification."""

    Normal = "Normal"
    """Normal weight CMU has a density of 125 lbs/cu. ft."""
    Medium = "Medium"
    """Medium weight CMU has a density of 105-125 lbs/cu. ft."""
    Light = "Light"
    """Lightweight CMU has a density less than 105 lbs/cu. ft."""


class CmuOptions(BaseOpenEpdSpec):
    """Concrete Masonry Unit options."""

    load_bearing: bool | None = pyd.Field(
        description="Load-Bearing. CMUs intended to be loadbearing, rather than simply cosmetic",
        default=None,
        json_schema_extra={"example": True},
    )
    aerated_concrete: bool | None = pyd.Field(
        description="AAC Aerated Concrete. Aerated Autoclaved Concrete, a foam concrete.",
        default=None,
        json_schema_extra={"example": True},
    )
    insulated: bool | None = pyd.Field(
        description="Insulated. CMUs with integral insulation",
        default=None,
    )
    sound_absorbing: bool | None = pyd.Field(
        description="Sound Absorbing. CMUs structured for sound absorbtion",
        default=None,
    )
    white: bool | None = pyd.Field(
        description="White. CMU using white cement and light-colored aggregate",
        default=None,
    )
    recycled_aggregate: bool | None = pyd.Field(
        description="Recycled aggregate. CMU using primarily reycled aggregates",
        default=None,
    )
    groundface: bool | None = pyd.Field(
        description="Ground Face. Ground or Honed facing, typically for improved appearance", default=None
    )
    splitface: bool | None = pyd.Field(
        description="Splitface. Rough surface texture via splitting; aggregate can be seen", default=None
    )
    smoothface: bool | None = pyd.Field(description="Smooth Face. Standard smooth-faced blocks", default=None)
    slumpstone: bool | None = pyd.Field(
        description="Slumpstone. A slightly rounded, random distortion with the look of rustic adobe.",
        default=None,
    )


class CmuSpec(BaseOpenEpdSpec):
    """Standardized Concrete Masonry Unit-specific extension for OpenEPD."""

    strength: str = pyd.Field(
        description="Compressive strength",
        json_schema_extra=dict(example="4000 psi"),
    )
    options: CmuOptions = pyd.Field(
        description="Options for CMU. List of true/false properties", default_factory=CmuOptions
    )
