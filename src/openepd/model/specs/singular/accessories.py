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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class BlanketFacingV1(BaseOpenEpdHierarchicalSpec):
    """
    Facing materials for insulation products.

    Such as kraft, white vinyl sheeting, or aluminum foil, which can serve as air barrier, vapor barrier, radiant
    barrier, or flame resistive layer.
    """

    _EXT_VERSION = "1.0"


class DoorsHardwareV1(BaseOpenEpdHierarchicalSpec):
    """Door hardware, including automatic and security door hardware."""

    _EXT_VERSION = "1.0"


class FlooringAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Products used in flooring, other than the actual flooring product itself."""

    _EXT_VERSION = "1.0"


class MortarV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious paste used to bind building blocks such as stones, bricks, and concrete masonry."""

    _EXT_VERSION = "1.0"


class TileGroutV1(BaseOpenEpdHierarchicalSpec):
    """Water-cement-sand mixture for laying ceramic tile."""

    _EXT_VERSION = "1.0"


class AccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Materials that are used alongside other materials."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    BlanketFacing: BlanketFacingV1 | None = None
    DoorsHardware: DoorsHardwareV1 | None = None
    FlooringAccessories: FlooringAccessoriesV1 | None = None
    Mortar: MortarV1 | None = None
    TileGrout: TileGroutV1 | None = None
