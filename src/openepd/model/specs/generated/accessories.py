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


class BlanketFacingV1(BaseOpenEpdHierarchicalSpec):
    """Blanket facing performance specification."""

    _EXT_VERSION = "1.0"


class DoorsHardwareV1(BaseOpenEpdHierarchicalSpec):
    """Doors hardware performance specification."""

    _EXT_VERSION = "1.0"


class FlooringAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Flooring accessories performance specification."""

    _EXT_VERSION = "1.0"


class MortarV1(BaseOpenEpdHierarchicalSpec):
    """Mortar performance specification."""

    _EXT_VERSION = "1.0"


class TileGroutV1(BaseOpenEpdHierarchicalSpec):
    """Tile grout performance specification."""

    _EXT_VERSION = "1.0"


class AccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Accessories performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    BlanketFacing: BlanketFacingV1 | None = None
    DoorsHardware: DoorsHardwareV1 | None = None
    FlooringAccessories: FlooringAccessoriesV1 | None = None
    Mortar: MortarV1 | None = None
    TileGrout: TileGroutV1 | None = None
