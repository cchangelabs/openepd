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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class AuxiliariesV1(BaseOpenEpdHierarchicalSpec):
    """Auxiliaries performance specification."""

    _EXT_VERSION = "1.0"


class CleaningProductsV1(BaseOpenEpdHierarchicalSpec):
    """Cleaning products performance specification."""

    _EXT_VERSION = "1.0"


class ClothingV1(BaseOpenEpdHierarchicalSpec):
    """Clothing performance specification."""

    _EXT_VERSION = "1.0"


class FoodBeverageV1(BaseOpenEpdHierarchicalSpec):
    """Food beverage performance specification."""

    _EXT_VERSION = "1.0"


class TransportationInfrastructureV1(BaseOpenEpdHierarchicalSpec):
    """Transportation infrastructure performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Auxiliaries: AuxiliariesV1 | None = None


class UnsupportedV1(BaseOpenEpdHierarchicalSpec):
    """Unsupported performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    CleaningProducts: CleaningProductsV1 | None = None
    Clothing: ClothingV1 | None = None
    FoodBeverage: FoodBeverageV1 | None = None


class CopperV1(BaseOpenEpdHierarchicalSpec):
    """Copper performance specification."""

    _EXT_VERSION = "1.0"


class EarthworkV1(BaseOpenEpdHierarchicalSpec):
    """Earthwork performance specification."""

    _EXT_VERSION = "1.0"


class ExteriorSunControlDevicesV1(BaseOpenEpdHierarchicalSpec):
    """Exterior sun control devices performance specification."""

    _EXT_VERSION = "1.0"


class GypsumFinishingCompoundsV1(BaseOpenEpdHierarchicalSpec):
    """Plasters and the like for finishing Gypsum Sheet and Board."""

    _EXT_VERSION = "1.0"


class ProfilesV1(BaseOpenEpdHierarchicalSpec):
    """Profiles performance specification."""

    _EXT_VERSION = "1.0"


class UnknownV1(BaseOpenEpdHierarchicalSpec):
    """Unknown performance specification."""

    _EXT_VERSION = "1.0"


class ZincV1(BaseOpenEpdHierarchicalSpec):
    """Zinc performance specification."""

    _EXT_VERSION = "1.0"


class OtherMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Other materials performance specification."""

    _EXT_VERSION = "1.0"

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
