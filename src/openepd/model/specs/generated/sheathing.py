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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import GypsumFacing, GypsumFireRating
from openepd.model.validation.quantity import LengthMStr, validate_unit_factory


class CementitiousSheathingBoardV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious sheathing board performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cement_board_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _cement_board_thickness_is_quantity_validator = pyd.validator("cement_board_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class GypsumSheathingBoardV1(BaseOpenEpdHierarchicalSpec):
    """Gypsum sheathing board performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    gypsum_fire_rating: GypsumFireRating | None = pyd.Field(default=None, description="", example="-")
    gypsum_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    gypsum_facing: GypsumFacing | None = pyd.Field(default=None, description="", example="Paper")
    gypsum_r_factor: str | None = pyd.Field(default=None, description="", example="1 RSI")
    gypsum_flame_spread_astm_e84: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_smoke_production_astm_e84: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_surface_abrasion_d4977: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_indentation_d5420: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_soft_body_impact_e695: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_hard_body_impact_c1929: int | None = pyd.Field(default=None, description="", example="3")
    mold_resistant: bool | None = pyd.Field(default=None, description="", example="True")
    foil_backing: bool | None = pyd.Field(default=None, description="", example="True")
    moisture_resistant: bool | None = pyd.Field(default=None, description="", example="True")
    abuse_resistant: bool | None = pyd.Field(default=None, description="", example="True")

    _gypsum_thickness_is_quantity_validator = pyd.validator("gypsum_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _gypsum_r_factor_is_quantity_validator = pyd.validator("gypsum_r_factor", allow_reuse=True)(
        validate_unit_factory("RSI")
    )


class SheathingV1(BaseOpenEpdHierarchicalSpec):
    """Sheathing performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    CementitiousSheathingBoard: CementitiousSheathingBoardV1 | None = None
    GypsumSheathingBoard: GypsumSheathingBoardV1 | None = None
