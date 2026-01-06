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
from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class BlanketFacingV1(BaseOpenEpdHierarchicalSpec):
    """
    Facing materials for insulation products.

    Such as kraft, white vinyl sheeting, or aluminum foil, which can serve as air barrier, vapor barrier, radiant
    barrier, or flame resistive layer.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="BlanketFacing",
        display_name="Blanket Facing",
        historical_names=["Accessories >> Blanket Facing"],
        description="Facing materials for insulation products, such as kraft, white vinyl sheeting, or aluminum foil, which can serve as air barrier, vapor barrier, radiant barrier, or flame resistive layer.",
        masterformat="07 21 16 Blanket Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class DoorsHardwareV1(BaseOpenEpdHierarchicalSpec):
    """Door hardware, including automatic and security door hardware."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="DoorsHardware",
        display_name="Doors Hardware",
        historical_names=["Accessories >> Doors Hardware"],
        description="Door hardware, including automatic and security door hardware",
        masterformat="08 70 00 Doors Hardware",
        declared_unit=Amount(qty=1, unit="item"),
    )


class FlooringAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Products used in flooring, other than the actual flooring product itself."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FlooringAccessories",
        display_name="Flooring Accessories",
        historical_names=["Accessories >> Flooring Accessories"],
        description="Products used in flooring, other than the actual flooring product itself.",
        masterformat="09 60 00 Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class MortarV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious paste used to bind building blocks such as stones, bricks, and concrete masonry."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Mortar",
        display_name="Mortar",
        alt_names=["Mortars", "mørtel"],
        description="Cementitious paste used to bind building blocks such as stones, bricks, and concrete masonry.",
        masterformat="04 05 13 Masonry Mortaring",
        declared_unit=Amount(qty=1, unit="t"),
    )


class TileGroutV1(BaseOpenEpdHierarchicalSpec):
    """Water-cement-sand mixture for laying ceramic tile."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="TileGrout",
        display_name="Tile Grout",
        historical_names=["Accessories >> Tile Grout"],
        description="Water-cement-sand mixture for laying ceramic tile",
        masterformat="09 30 60 Tile Adhesives, Mortars and Grouts",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class AccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Materials that are used alongside other materials."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Accessories",
        display_name="Accessories",
        description="Materials that are used alongside other materials",
    )

    # Nested specs:
    BlanketFacing: BlanketFacingV1 | None = None
    DoorsHardware: DoorsHardwareV1 | None = None
    FlooringAccessories: FlooringAccessoriesV1 | None = None
    Mortar: MortarV1 | None = None
    TileGrout: TileGroutV1 | None = None
