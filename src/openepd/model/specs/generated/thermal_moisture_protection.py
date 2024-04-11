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
from openepd.model.specs.generated.enums import (
    FoamType,
    InsulatingMaterial,
    InsulationIntendedApplication,
    MembraneRoofingReinforcement,
    RoofCoverBoardsFacing,
    RoofCoverBoardsMaterial,
)
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, PressureMPaStr, validate_unit_factory


class BituminousRoofingV1(BaseOpenEpdHierarchicalSpec):
    """Bituminous roofing performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyEPDMV1(BaseOpenEpdHierarchicalSpec):
    """Single ply e p d m performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyKEEV1(BaseOpenEpdHierarchicalSpec):
    """Single ply k e e performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyOtherV1(BaseOpenEpdHierarchicalSpec):
    """Single ply other performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyPolyurethaneV1(BaseOpenEpdHierarchicalSpec):
    """Single ply polyurethane performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyPVCV1(BaseOpenEpdHierarchicalSpec):
    """Single ply p v c performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyTPOV1(BaseOpenEpdHierarchicalSpec):
    """Single ply t p o performance specification."""

    _EXT_VERSION = "1.0"


class BlanketInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Blanket insulation performance specification."""

    _EXT_VERSION = "1.0"


class BlownInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Blown insulation performance specification."""

    _EXT_VERSION = "1.0"


class BoardInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Board insulation performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    compressive_strength: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")

    _compressive_strength_is_quantity_validator = pyd.validator("compressive_strength", allow_reuse=True)(
        validate_unit_factory("MPa")
    )


class FoamedInPlaceV1(BaseOpenEpdHierarchicalSpec):
    """Foamed in place performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    foam_type: FoamType | None = pyd.Field(default=None, description="", example="Open-Cell")


class SprayedInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Sprayed insulation performance specification."""

    _EXT_VERSION = "1.0"


class AirBarriersV1(BaseOpenEpdHierarchicalSpec):
    """Air barriers performance specification."""

    _EXT_VERSION = "1.0"


class MembraneRoofingV1(BaseOpenEpdHierarchicalSpec):
    """Membrane roofing performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")
    sri: float | None = pyd.Field(default=None, description="", example=2.3)
    total_recycled_content: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)
    post_consumer_recycled_content: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)
    reinforcement: MembraneRoofingReinforcement | None = pyd.Field(default=None, description="", example="Polyester")
    felt_backing: bool | None = pyd.Field(default=None, description="", example=True)
    nsf347: bool | None = pyd.Field(default=None, description="", example=True)
    vantage_vinyl: bool | None = pyd.Field(default=None, description="", example=True)

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))

    # Nested specs:
    BituminousRoofing: BituminousRoofingV1 | None = None
    SinglePlyEPDM: SinglePlyEPDMV1 | None = None
    SinglePlyKEE: SinglePlyKEEV1 | None = None
    SinglePlyOther: SinglePlyOtherV1 | None = None
    SinglePlyPolyurethane: SinglePlyPolyurethaneV1 | None = None
    SinglePlyPVC: SinglePlyPVCV1 | None = None
    SinglePlyTPO: SinglePlyTPOV1 | None = None


class InsulationV1(BaseOpenEpdHierarchicalSpec):
    """Insulation performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    r_value: float | None = pyd.Field(default=None, description="", example=2.3)
    material: InsulatingMaterial | None = pyd.Field(default=None, description="", example="Mineral Wool")
    intended_application: list[InsulationIntendedApplication] | None = pyd.Field(
        default=None, description="", example=["Wall & General"]
    )
    thickness_per_declared_unit: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")

    _thickness_per_declared_unit_is_quantity_validator = pyd.validator("thickness_per_declared_unit", allow_reuse=True)(
        validate_unit_factory("m")
    )

    # Nested specs:
    BlanketInsulation: BlanketInsulationV1 | None = None
    BlownInsulation: BlownInsulationV1 | None = None
    BoardInsulation: BoardInsulationV1 | None = None
    FoamedInPlace: FoamedInPlaceV1 | None = None
    SprayedInsulation: SprayedInsulationV1 | None = None


class DampproofingAndWaterproofingV1(BaseOpenEpdHierarchicalSpec):
    """Dampproofing and waterproofing performance specification."""

    _EXT_VERSION = "1.0"


class FlashingAndSheetMetalV1(BaseOpenEpdHierarchicalSpec):
    """Flashing and sheet metal performance specification."""

    _EXT_VERSION = "1.0"


class JointProtectionV1(BaseOpenEpdHierarchicalSpec):
    """Joint protection performance specification."""

    _EXT_VERSION = "1.0"


class RoofCoverBoardsV1(BaseOpenEpdHierarchicalSpec):
    """Roof cover boards performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    material: RoofCoverBoardsMaterial | None = pyd.Field(default=None, description="", example="Gypsum Fiber")
    facing: list[RoofCoverBoardsFacing] | None = pyd.Field(default=None, description="", example=["Paper"])
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="1 m")

    _roof_cover_boards_thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class SteepSlopeRoofingV1(BaseOpenEpdHierarchicalSpec):
    """Steep slope roofing performance specification."""

    _EXT_VERSION = "1.0"


class WeatherBarriersV1(BaseOpenEpdHierarchicalSpec):
    """Weather barriers performance specification."""

    _EXT_VERSION = "1.0"


class ThermalMoistureProtectionV1(BaseOpenEpdHierarchicalSpec):
    """Thermal moisture protection performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AirBarriers: AirBarriersV1 | None = None
    MembraneRoofing: MembraneRoofingV1 | None = None
    Insulation: InsulationV1 | None = None
    DampproofingAndWaterproofing: DampproofingAndWaterproofingV1 | None = None
    FlashingAndSheetMetal: FlashingAndSheetMetalV1 | None = None
    JointProtection: JointProtectionV1 | None = None
    RoofCoverBoards: RoofCoverBoardsV1 | None = None
    SteepSlopeRoofing: SteepSlopeRoofingV1 | None = None
    WeatherBarriers: WeatherBarriersV1 | None = None
