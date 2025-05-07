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
    "AuxiliariesRangeV1",
    "CleaningProductsRangeV1",
    "ClothingRangeV1",
    "CopperRangeV1",
    "EarthworkRangeV1",
    "ExteriorSunControlDevicesRangeV1",
    "FoodBeverageRangeV1",
    "GypsumFinishingCompoundsRangeV1",
    "OtherMaterialsRangeV1",
    "ProfilesRangeV1",
    "TransportationInfrastructureRangeV1",
    "UnknownRangeV1",
    "UnsupportedRangeV1",
    "ZincRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class AuxiliariesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Auxiliaries performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CleaningProductsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cleaning and disinfecting solutions.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ClothingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Clothing.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FoodBeverageRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Food Beverage and Tobacco Products.

    Range version.
    """

    _EXT_VERSION = "1.0"


class TransportationInfrastructureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    A broad category for unclassified materials focused on transportation infrastructure.

    Range version.
    """

    _EXT_VERSION = "1.0"

    Auxiliaries: AuxiliariesRangeV1 | None = None


class UnsupportedRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    A generic category for EPDs/Materials and categories that are explicitly not yet supported by EC3.

    Assume that any data in this subcategory is unreliable.

    Range version.
    """

    _EXT_VERSION = "1.0"

    CleaningProducts: CleaningProductsRangeV1 | None = None
    Clothing: ClothingRangeV1 | None = None
    FoodBeverage: FoodBeverageRangeV1 | None = None


class CopperRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Products made of copper.

    Range version.
    """

    _EXT_VERSION = "1.0"


class EarthworkRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Earthwork, including excavation, shoring, piles, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ExteriorSunControlDevicesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Sun control devices help to manage solar heat gain by redirecting sunlight.

    Range version.
    """

    _EXT_VERSION = "1.0"


class GypsumFinishingCompoundsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Plasters and the like for finishing Gypsum Sheet and Board.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ProfilesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Metal or polymer profiles used for producing or installing of Windows, Doors, Frames and Cladding.

    Range version.
    """

    _EXT_VERSION = "1.0"


class UnknownRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Materials with unknown category. Assume that any data in this subcategory is unreliable.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ZincRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Products made of zinc.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherMaterialsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Broad category of materials not yet classified.

    Range version.
    """

    _EXT_VERSION = "1.0"

    TransportationInfrastructure: TransportationInfrastructureRangeV1 | None = None
    Unsupported: UnsupportedRangeV1 | None = None
    Copper: CopperRangeV1 | None = None
    Earthwork: EarthworkRangeV1 | None = None
    ExteriorSunControlDevices: ExteriorSunControlDevicesRangeV1 | None = None
    GypsumFinishingCompounds: GypsumFinishingCompoundsRangeV1 | None = None
    Profiles: ProfilesRangeV1 | None = None
    Unknown: UnknownRangeV1 | None = None
    Zinc: ZincRangeV1 | None = None
