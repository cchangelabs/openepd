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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import AluminiumAlloy


class AluminiumBilletsV1(BaseOpenEpdHierarchicalSpec):
    """Cast Aluminium ingots or billets for use in manufacturing more finished products."""

    _EXT_VERSION = "1.0"


class AluminiumExtrusionsV1(BaseOpenEpdHierarchicalSpec):
    """Extruded aluminum products used in construction.

    Includes range of finish options including mill finish, painted, and anodized.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    thermally_improved: bool | None = pyd.Field(default=None, description="", example=True)


class AluminiumSheetGoodsV1(BaseOpenEpdHierarchicalSpec):
    """Rolled and/or Stamped Aluminium coil or sheets, often used in flashing, trim, panels, and deck."""

    _EXT_VERSION = "1.0"


class AluminiumSuspensionAssemblyV1(BaseOpenEpdHierarchicalSpec):
    """Aluminum suspension assemblies for acoustical ceiling systems."""

    _EXT_VERSION = "1.0"


class AluminiumV1(BaseOpenEpdHierarchicalSpec):
    """Broad category for construction materials made primarily from Aluminium and its alloys."""

    _EXT_VERSION = "1.0"

    # Own fields:
    alloy: AluminiumAlloy | None = pyd.Field(default=None, description="", example=str(AluminiumAlloy.ALLOY_1XXX))
    anodized: bool | None = pyd.Field(default=None, description="", example=True)
    painted: bool | None = pyd.Field(default=None, description="", example=True)

    # Nested specs:
    AluminiumBillets: AluminiumBilletsV1 | None = None
    AluminiumExtrusions: AluminiumExtrusionsV1 | None = None
    AluminiumSheetGoods: AluminiumSheetGoodsV1 | None = None
    AluminiumSuspensionAssembly: AluminiumSuspensionAssemblyV1 | None = None
