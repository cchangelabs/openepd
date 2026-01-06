#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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
import pydantic

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import AluminiumAlloy


class AluminiumBilletsV1(BaseOpenEpdHierarchicalSpec):
    """Cast Aluminium ingots or billets for use in manufacturing more finished products."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AluminiumBillets",
        display_name="Aluminium Billets",
        short_name="Billets",
        historical_names=["Aluminium >> Billets"],
        description="Cast Aluminium ingots or billets for use in manufacturing more finished products.",
        masterformat="05 00 00 METALS",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class AluminiumExtrusionsV1(BaseOpenEpdHierarchicalSpec):
    """
    Extruded aluminum products used in construction.

    Includes range of finish options including mill finish, painted, and anodized.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AluminiumExtrusions",
        display_name="Aluminium Extrusions",
        short_name="Extrusions",
        historical_names=["Aluminium >> Extrusions"],
        description="Extruded aluminum products used in construction with of a range of finish options including mill finish, painted, and anodized.",
        masterformat="05 00 00 METALS",
        declared_unit=Amount(qty=1, unit="kg"),
    )

    # Own fields:
    thermally_improved: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


class AluminiumSheetGoodsV1(BaseOpenEpdHierarchicalSpec):
    """Rolled and/or Stamped Aluminium coil or sheets, often used in flashing, trim, panels, and deck."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AluminiumSheetGoods",
        display_name="Aluminium Sheet Goods",
        short_name="Sheet",
        historical_names=["Aluminium >> Sheet"],
        description="Rolled and/or Stamped Aluminium coil or sheets, often used in flashing, trim, panels, and deck.",
        masterformat="05 00 00 METALS",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class AluminiumSuspensionAssemblyV1(BaseOpenEpdHierarchicalSpec):
    """Aluminum suspension assemblies for acoustical ceiling systems."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AluminiumSuspensionAssembly",
        display_name="Aluminium Suspension Assemblies",
        alt_names=["Aluminum Suspension Assemblies"],
        historical_names=["Aluminium >> Aluminium Suspension Assemblies"],
        description="Aluminum suspension assemblies for acoustical ceiling systems",
        masterformat="09 53 00 Suspension Assemblies",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class AluminiumV1(BaseOpenEpdHierarchicalSpec):
    """Broad category for construction materials made primarily from Aluminium and its alloys."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Aluminium",
        display_name="Aluminium",
        alt_names=["Aluminum", "Al", "Alluminio"],
        description="Broad category for construction materials made primarily from Aluminium and its alloys",
        masterformat="05 00 00 METALS",
        declared_unit=Amount(qty=1, unit="kg"),
    )

    # Own fields:
    alloy: AluminiumAlloy | None = pydantic.Field(
        default=None, description="", examples=[str(AluminiumAlloy.ALLOY_1XXX)]
    )
    anodized: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    painted: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )

    # Nested specs:
    AluminiumBillets: AluminiumBilletsV1 | None = None
    AluminiumExtrusions: AluminiumExtrusionsV1 | None = None
    AluminiumSheetGoods: AluminiumSheetGoodsV1 | None = None
    AluminiumSuspensionAssembly: AluminiumSuspensionAssemblyV1 | None = None
