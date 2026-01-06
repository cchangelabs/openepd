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


class AuxiliariesV1(BaseOpenEpdHierarchicalSpec):
    """Auxiliaries performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Auxiliaries",
        display_name="Auxiliaries",
        historical_names=["Other Materials >> Transportation Infrastructure >> Auxiliaries"],
        description="Auxiliary equipment for transportation",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class CleaningProductsV1(BaseOpenEpdHierarchicalSpec):
    """Cleaning and disinfecting solutions."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CleaningProducts",
        display_name="Cleaning Products",
        historical_names=["Other Materials >> Unsupported >> Cleaning Products"],
        description="Cleaning and disinfecting solutions",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class ClothingV1(BaseOpenEpdHierarchicalSpec):
    """Clothing."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Clothing",
        display_name="Clothing",
        historical_names=[
            "Textile Products >> Clothing",
            "OtherMaterials >> Unsupported >> Clothing",
            "Other Materials >> Unsupported >> Clothing",
        ],
        description="Clothing",
        declared_unit=Amount(qty=1, unit="item"),
    )


class FoodBeverageV1(BaseOpenEpdHierarchicalSpec):
    """Food Beverage and Tobacco Products."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FoodBeverage",
        display_name="Foods & Beverages",
        historical_names=[
            "OtherMaterials >> Unsupported >> FoodBeverage",
            "Other Materials >> Unsupported >> Foods & Beverages",
        ],
        description="Foods, beverages, tobacco, other human consumables, and specific ingredients for them. Includes most products in WCO HS Section I, II and IV. Excludes pharmaceuticals.",
    )


class TransportationInfrastructureV1(BaseOpenEpdHierarchicalSpec):
    """A broad category for unclassified materials focused on transportation infrastructure."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="TransportationInfrastructure",
        display_name="Transportation Infrastructure",
        historical_names=["Other Materials >> Transportation Infrastructure"],
        description="A broad category for unclassified materials focused on transportation infrastructure",
        declared_unit=Amount(qty=1, unit="kg"),
    )

    # Nested specs:
    Auxiliaries: AuxiliariesV1 | None = None


class UnsupportedV1(BaseOpenEpdHierarchicalSpec):
    """
    A generic category for EPDs/Materials and categories that are explicitly not yet supported by EC3.

    Assume that any data in this subcategory is unreliable.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Unsupported",
        display_name="Unsupported",
        historical_names=["Other Materials >> Unsupported"],
        description="A generic category for EPDs/Materials and categories that are explicitly not yet supported by EC3. Assume that any data in this subcategory is unreliable.",
    )

    # Nested specs:
    CleaningProducts: CleaningProductsV1 | None = None

    Clothing: ClothingV1 | None = pydantic.Field(
        default=None,
        json_schema_extra={
            "deprecated": True,
        },
        description="UnsupportedV1.Clothing is deprecated. Use TextileProductsV1.Clothing instead.",
    )
    """
    UnsupportedV1.Clothing is deprecated. Use TextileProductsV1.Clothing instead.
    """
    FoodBeverage: FoodBeverageV1 | None = pydantic.Field(
        default=None,
        json_schema_extra={
            "deprecated": True,
        },
        description="UnsupportedV1.FoodBeverage is deprecated. Use Specs.FoodBeverage instead.",
    )
    """
    UnsupportedV1.FoodBeverage is deprecated. Use TextileProductsV1.FoodBeverage instead.
    """


class TextileProductsV1(BaseOpenEpdHierarchicalSpec):
    """Products to be worn by humans, and materials intended to manufacture them. Includes most of WS HS Sections XI, XII."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="TextileProducts",
        display_name="Textiles, Footwear, and Apparel",
        short_name="Textile Products",
        historical_names=["Textile Products"],
        description="Products to be worn by humans, and materials intended to manufacture them. Includes most of WCO HS Sections XI, XII.",
    )

    Clothing: ClothingV1 | None = None


class CopperV1(BaseOpenEpdHierarchicalSpec):
    """Products made of copper."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Copper",
        display_name="Copper",
        historical_names=["Other Materials >> Copper"],
        description="Products made of copper",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class EarthworkV1(BaseOpenEpdHierarchicalSpec):
    """Earthwork, including excavation, shoring, piles, etc."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Earthwork",
        display_name="Earthwork",
        historical_names=["Other Materials >> Earthwork"],
        description="Earthwork, including excavation, shoring, piles, etc.",
        masterformat="31 00 00 Earthwork",
        declared_unit=Amount(qty=1, unit="t"),
    )


class ExteriorSunControlDevicesV1(BaseOpenEpdHierarchicalSpec):
    """Sun control devices help to manage solar heat gain by redirecting sunlight."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ExteriorSunControlDevices",
        display_name="Exterior Sun Control Devices",
        alt_names=["Sun Control Systems"],
        historical_names=["Other Materials >> Exterior Sun Control Devices"],
        description="Sun control devices help to manage solar heat gain by redirecting sunlight.",
        masterformat="10 71 13 Exterior Sun Control Devices",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class GypsumFinishingCompoundsV1(BaseOpenEpdHierarchicalSpec):
    """Plasters and the like for finishing Gypsum Sheet and Board."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="GypsumFinishingCompounds",
        display_name="Gypsum Finishing Compounds",
        historical_names=["Other Materials >> Gypsum Finishing Compounds"],
        description="Plasters and the like for finishing Gypsum Sheet and Board",
        declared_unit=Amount(qty=1000, unit="sqft"),
    )


class ProfilesV1(BaseOpenEpdHierarchicalSpec):
    """Metal or polymer profiles used for producing or installing of Windows, Doors, Frames and Cladding."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Profiles",
        display_name="Profiles",
        historical_names=["Other Materials >> Profiles"],
        description="Metal or polymer profiles used for producing or installing of Windows, Doors, Frames and Cladding",
        declared_unit=Amount(qty=1, unit="m"),
    )


class UnknownV1(BaseOpenEpdHierarchicalSpec):
    """Materials with unknown category. Assume that any data in this subcategory is unreliable."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Unknown",
        display_name="Unknown",
        historical_names=["Other Materials >> Unknown"],
        description="Materials with unknown category. Assume that any data in this subcategory is unreliable.",
    )


class ZincV1(BaseOpenEpdHierarchicalSpec):
    """Products made of zinc."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Zinc",
        display_name="Zinc",
        historical_names=["Other Materials >> Zinc"],
        description="Products made of zinc.",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class OtherPaperPlasticV1(BaseOpenEpdHierarchicalSpec):
    """Other products primarily made of plastic or paper. Includes WCO HS sections VII and X."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherPaperPlastic",
        display_name="Paper & Plastics",
        historical_names=["Other Materials >> Paper & Plastics"],
        description="Other products primarily made of plastic or paper. Includes WCO HS sections VII and X",
    )


class OtherMineralMetalV1(BaseOpenEpdHierarchicalSpec):
    """Base minerals, metals, materials, and products made primarily of them not otherwise classified.  Includes most of WCO HS Section XV."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherMineralMetal",
        display_name="Metals, Minerals, and Glass",
        short_name="Metal, Mineral, Glass",
        historical_names=["Other Materials >> Metal, Mineral, Glass"],
        description="Base minerals, metals, materials, and products made primarily of them not otherwise classified.  Includes most of WCO HS Section XV.",
    )


class OtherMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Broad category of materials not yet classified."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherMaterials",
        display_name="Other Materials",
        alt_names=["Unclassified", "Misc", "Others"],
        description="Broad category of materials not yet classified",
    )

    # Nested specs:
    TransportationInfrastructure: TransportationInfrastructureV1 | None = None
    Unsupported: UnsupportedV1 | None = None
    Copper: CopperV1 | None = None
    Earthwork: EarthworkV1 | None = None
    ExteriorSunControlDevices: ExteriorSunControlDevicesV1 | None = None
    GypsumFinishingCompounds: GypsumFinishingCompoundsV1 | None = None
    Profiles: ProfilesV1 | None = None
    Unknown: UnknownV1 | None = None
    Zinc: ZincV1 | None = None
    OtherPaperPlastic: OtherPaperPlasticV1 | None = None
    OtherMineralMetal: OtherMineralMetalV1 | None = None
