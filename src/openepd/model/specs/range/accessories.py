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
    "AccessoriesRangeV1",
    "BlanketFacingRangeV1",
    "DoorsHardwareRangeV1",
    "FlooringAccessoriesRangeV1",
    "MortarRangeV1",
    "TileGroutRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class BlanketFacingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Facing materials for insulation products.

    Such as kraft, white vinyl sheeting, or aluminum foil, which can serve as air barrier, vapor barrier, radiant
    barrier, or flame resistive layer.

    Range version.
    """

    _EXT_VERSION = "1.0"


class DoorsHardwareRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Door hardware, including automatic and security door hardware.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FlooringAccessoriesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Products used in flooring, other than the actual flooring product itself.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MortarRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious paste used to bind building blocks such as stones, bricks, and concrete masonry.

    Range version.
    """

    _EXT_VERSION = "1.0"


class TileGroutRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Water-cement-sand mixture for laying ceramic tile.

    Range version.
    """

    _EXT_VERSION = "1.0"


class AccessoriesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Materials that are used alongside other materials.

    Range version.
    """

    _EXT_VERSION = "1.0"

    BlanketFacing: BlanketFacingRangeV1 | None = None
    DoorsHardware: DoorsHardwareRangeV1 | None = None
    FlooringAccessories: FlooringAccessoriesRangeV1 | None = None
    Mortar: MortarRangeV1 | None = None
    TileGrout: TileGroutRangeV1 | None = None
