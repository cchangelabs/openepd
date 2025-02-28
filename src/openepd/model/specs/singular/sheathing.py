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
import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import GypsumFacing, GypsumFireRating, GypsumThickness
from openepd.model.validation.quantity import LengthMmStr, RFactorStr, validate_quantity_unit_factory


class CementitiousSheathingBoardV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious sheathing board.

    Cementitious non-gypsum board used for sheathing exteriors, shaft walls, and interior walls/ceilings requiring
    moisture resistance.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    cement_board_thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])

    @pydantic.field_validator("cement_board_thickness", mode="before", check_fields=False)
    def _cement_board_thickness_is_quantity_validator(cls, v):
        return validate_quantity_unit_factory("m")(cls, v)


class GypsumSheathingBoardV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious sheathing board.

    Gypsum board used for sheathing exteriors, shaft walls, and interior walls/ceilings requiring moisture resistance.
    """

    _EXT_VERSION = "1.1"

    # Own fields:
    fire_rating: GypsumFireRating | None = pydantic.Field(default=None, description="", examples=["-"])
    thickness: GypsumThickness | None = pydantic.Field(default=None, description="", examples=["9 mm"])
    facing: GypsumFacing | None = pydantic.Field(default=None, description="", examples=["Paper"])

    r_factor: RFactorStr | None = pydantic.Field(default=None, description="", examples=["1 RSI"])

    flame_spread_astm_e84: int | None = pydantic.Field(default=None, description="", examples=[3])
    smoke_production_astm_e84: int | None = pydantic.Field(default=None, description="", examples=[3])
    surface_abrasion_d4977: int | None = pydantic.Field(default=None, description="", examples=[3])
    indentation_d5420: int | None = pydantic.Field(default=None, description="", examples=[3])
    soft_body_impact_e695: int | None = pydantic.Field(default=None, description="", examples=[3])
    hard_body_impact_c1929: int | None = pydantic.Field(default=None, description="", examples=[3])

    mold_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    foil_backing: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    moisture_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    abuse_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


@pydantic.field_validator("thickness")
def _gypsum_thickness_is_quantity_validator(cls, v):
    return validate_quantity_unit_factory("m")(cls, v)


@pydantic.field_validator("r_factor")
def _gypsum_r_factor_is_quantity_validator(cls, v):
    return validate_quantity_unit_factory("RSI")(cls, v)


class SheathingV1(BaseOpenEpdHierarchicalSpec):
    """
    Sheathing.

    Boards or panels used in floor, wall and roof assemblies as a surface onto which other materials can be applied.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    CementitiousSheathingBoard: CementitiousSheathingBoardV1 | None = None
    GypsumSheathingBoard: GypsumSheathingBoardV1 | None = None
