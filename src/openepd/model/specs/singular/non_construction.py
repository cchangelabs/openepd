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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class ChemicalsV1(BaseOpenEpdHierarchicalSpec):
    """Products of the Chemical or Allied Industries.  Includes most products in WCO HS Section VI."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Chemicals",
        display_name="Chemical Products",
        description="Products of the Chemical or Allied Industries.  Includes most products in WCO HS Section VI.",
    )


class ElectricityAndFuelV1(BaseOpenEpdHierarchicalSpec):
    """Energy carriers including fuels, electricity, and steam."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricityAndFuel",
        display_name="Electricity, Steam and Fuels",
        description="Energy carriers including fuels, electricity, and steam.",
    )


class VehiclesV1(BaseOpenEpdHierarchicalSpec):
    """Machinery for moving people and goods.  Includes most products in WCO HS Section XVII."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Vehicles",
        display_name="Vehicles & Transport Equipment",
        short_name="Vehicles",
        description="Machinery for moving people and goods. Includes most products in WCO HS Section XVII.",
    )


class MachineryAndEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Machinery other than for installation in a building."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MachineryAndEquipment",
        display_name="Machinery & Equipment",
        description="Machinery other than for installation in a building. ",
    )


class ServicesV1(BaseOpenEpdHierarchicalSpec):
    """Services, including digital and professional services."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Services",
        display_name="Services",
        description="Services, including digital and professional services.",
    )


class ConsumerGoodsV1(BaseOpenEpdHierarchicalSpec):
    """Nonperishable products intended for use by individual consumers."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ConsumerGoods",
        display_name="Consumer Goods",
        description="Nonperishable products intended for use by individual consumers.",
    )
