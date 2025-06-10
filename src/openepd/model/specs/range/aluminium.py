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
__all__ = (
    "AluminiumBilletsRangeV1",
    "AluminiumExtrusionsRangeV1",
    "AluminiumRangeV1",
    "AluminiumSheetGoodsRangeV1",
    "AluminiumSuspensionAssemblyRangeV1",
)

import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import AluminiumAlloy

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class AluminiumBilletsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cast Aluminium ingots or billets for use in manufacturing more finished products.

    Range version.
    """

    _EXT_VERSION = "1.0"


class AluminiumExtrusionsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Extruded aluminum products used in construction.

    Includes range of finish options including mill finish, painted, and anodized.


    Range version.
    """

    _EXT_VERSION = "1.0"

    thermally_improved: bool | None = pydantic.Field(default=None, description="")


class AluminiumSheetGoodsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Rolled and/or Stamped Aluminium coil or sheets, often used in flashing, trim, panels, and deck.

    Range version.
    """

    _EXT_VERSION = "1.0"


class AluminiumSuspensionAssemblyRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Aluminum suspension assemblies for acoustical ceiling systems.

    Range version.
    """

    _EXT_VERSION = "1.0"


class AluminiumRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Broad category for construction materials made primarily from Aluminium and its alloys.

    Range version.
    """

    _EXT_VERSION = "1.0"

    alloy: list[AluminiumAlloy] | None = pydantic.Field(default=None, description="")
    anodized: bool | None = pydantic.Field(default=None, description="")
    painted: bool | None = pydantic.Field(default=None, description="")
    AluminiumBillets: AluminiumBilletsRangeV1 | None = None
    AluminiumExtrusions: AluminiumExtrusionsRangeV1 | None = None
    AluminiumSheetGoods: AluminiumSheetGoodsRangeV1 | None = None
    AluminiumSuspensionAssembly: AluminiumSuspensionAssemblyRangeV1 | None = None
