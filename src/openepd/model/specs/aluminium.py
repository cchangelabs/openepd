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

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.numbers import RatioFloat


class AluminiumAlloy(StrEnum):
    """Aluminium alloy enum."""

    ALLOY_1xxx = ("1xxx",)
    ALLOY_2xxx = ("2xxx",)
    ALLOY_3xxx = ("3xxx",)
    ALLOY_4xxx = ("4xxx",)
    ALLOY_5xxx = ("5xxx",)
    ALLOY_6xxx = ("6xxx",)
    ALLOY_7xxx = ("7xxx",)
    ALLOY_8xxx = ("8xxx",)
    ALLOY_1xx_x = ("1xx.x",)
    ALLOY_2xx_x = ("2xx.x",)
    ALLOY_3xx_x = ("3xx.x",)
    ALLOY_4xx_x = ("4xx.x",)
    ALLOY_5xx_x = ("5xx.x",)
    ALLOY_7xx_x = ("7xx.x",)
    ALLOY_8xx_x = ("8xx.x",)
    ALLOY_9xx_x = ("9xx.x",)


class AluminiumExtrusionsV1(BaseOpenEpdHierarchicalSpec):
    """Aluminium extrusions V1 spec."""

    _EXT_VERSION = "1.0"

    """Aluminium extrusions V1 spec."""
    thermally_improved: bool | None = pyd.Field(default=None, description="Thermally improved")


class AluminiumV1(BaseOpenEpdHierarchicalSpec):
    """Aluminium V1 spec."""

    _EXT_VERSION = "1.0"
    recycled_content: RatioFloat | None = pyd.Field(default=None, description="Recycled content")

    alloy: AluminiumAlloy | None = pyd.Field(default=None, description="Alloy")
    anodized: bool | None = None
    painted: bool | None = None

    AluminiumExtrusions: AluminiumExtrusionsV1 | None = pyd.Field(title="AluminiumExtrusionsV1", default=None)
