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
    "CementitiousSheathingBoardRangeV1",
    "GypsumSheathingBoardRangeV1",
    "SheathingRangeV1",
)

import pydantic

from openepd.model.common import RangeInt
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import GypsumFacing, GypsumFireRating, GypsumThickness
from openepd.model.validation.quantity import AmountRangeLengthMm, AmountRangeRFactor

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class CementitiousSheathingBoardRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious sheathing board.

    Cementitious non-gypsum board used for sheathing exteriors, shaft walls, and interior walls/ceilings requiring
    moisture resistance.

    Range version.
    """

    _EXT_VERSION = "1.0"

    cement_board_thickness: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")


class GypsumSheathingBoardRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious sheathing board.

    Gypsum board used for sheathing exteriors, shaft walls, and interior walls/ceilings requiring moisture resistance.

    Range version.
    """

    _EXT_VERSION = "1.1"

    fire_rating: list[GypsumFireRating] | None = pydantic.Field(default=None, description="")
    thickness: list[GypsumThickness] | None = pydantic.Field(default=None, description="")
    facing: list[GypsumFacing] | None = pydantic.Field(default=None, description="")
    r_factor: AmountRangeRFactor | None = pydantic.Field(default=None, description="")
    flame_spread_astm_e84: RangeInt | None = pydantic.Field(default=None, description="")
    smoke_production_astm_e84: RangeInt | None = pydantic.Field(default=None, description="")
    surface_abrasion_d4977: RangeInt | None = pydantic.Field(default=None, description="")
    indentation_d5420: RangeInt | None = pydantic.Field(default=None, description="")
    soft_body_impact_e695: RangeInt | None = pydantic.Field(default=None, description="")
    hard_body_impact_c1929: RangeInt | None = pydantic.Field(default=None, description="")
    mold_resistant: bool | None = pydantic.Field(default=None, description="")
    foil_backing: bool | None = pydantic.Field(default=None, description="")
    moisture_resistant: bool | None = pydantic.Field(default=None, description="")
    abuse_resistant: bool | None = pydantic.Field(default=None, description="")


class SheathingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Sheathing.

    Boards or panels used in floor, wall and roof assemblies as a surface onto which other materials can be applied.

    Range version.
    """

    _EXT_VERSION = "1.0"

    CementitiousSheathingBoard: CementitiousSheathingBoardRangeV1 | None = None
    GypsumSheathingBoard: GypsumSheathingBoardRangeV1 | None = None
