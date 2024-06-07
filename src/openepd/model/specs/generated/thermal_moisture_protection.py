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
from openepd.model.validation.quantity import LengthMmStr, PressureMPaStr


class BituminousRoofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Bituminous roofing.

    Premanufactured membrane roofing sheets consisting of asphalt, reinforcing layers, and in some cases a surfacing.
    """

    _EXT_VERSION = "1.0"


class SinglePlyEPDMV1(BaseOpenEpdHierarchicalSpec):
    """Ethylene propylene diene monomer (EPDM) rubber membrane."""

    _EXT_VERSION = "1.0"


class SinglePlyKEEV1(BaseOpenEpdHierarchicalSpec):
    """
    Ketone Ethylene Ester (KEE) roof membranes.

    Consist of PVC resin and KEE plasticizer, with KEE exceeding 50% of the polymer content by weight.
    """

    _EXT_VERSION = "1.0"


class SinglePlyOtherV1(BaseOpenEpdHierarchicalSpec):
    """Single ply other performance specification."""

    _EXT_VERSION = "1.0"


class SinglePlyPolyurethaneV1(BaseOpenEpdHierarchicalSpec):
    """Polyurethane liquid for flat roof waterproofing."""

    _EXT_VERSION = "1.0"


class SinglePlyPVCV1(BaseOpenEpdHierarchicalSpec):
    """Polyvinyl chloride (PVC) thermoplastic membrane."""

    _EXT_VERSION = "1.0"


class SinglePlyTPOV1(BaseOpenEpdHierarchicalSpec):
    """Thermoplastic Polyolefin (TPO) membrane."""

    _EXT_VERSION = "1.0"


class BlanketInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Non-rigid insulation batts, blankets, and rolls."""

    _EXT_VERSION = "1.0"


class BlownInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Loose-fill insulation for blow-in or closed cavity applications."""

    _EXT_VERSION = "1.0"


class BoardInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Rigid insulation products including rigid foams, wood fiberboard insulation, and rigid mineral wool boards."""

    _EXT_VERSION = "1.0"

    # Own fields:
    compressive_strength: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")


class FoamedInPlaceV1(BaseOpenEpdHierarchicalSpec):
    """Open and closed cell spray foam insulation."""

    _EXT_VERSION = "1.0"

    # Own fields:
    foam_type: FoamType | None = pyd.Field(default=None, description="", example="Open-Cell")


class SprayedInsulationV1(BaseOpenEpdHierarchicalSpec):
    """
    Spray-on insulation, such as spray-on cellulose.

    Foaming sprays are categorized separately under foamed-in-place.
    """

    _EXT_VERSION = "1.0"


class AirBarriersV1(BaseOpenEpdHierarchicalSpec):
    """Air Infiltration Barrier."""

    _EXT_VERSION = "1.0"


class MembraneRoofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Membrane roofing.

    Built-up bituminous, modified bituminous, elastomeric, thermoplastic, fluid-applied, and hot-applied rubberized
    asphalt membrane roofing.
    """

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

    # Nested specs:
    BituminousRoofing: BituminousRoofingV1 | None = None
    SinglePlyEPDM: SinglePlyEPDMV1 | None = None
    SinglePlyKEE: SinglePlyKEEV1 | None = None
    SinglePlyOther: SinglePlyOtherV1 | None = None
    SinglePlyPolyurethane: SinglePlyPolyurethaneV1 | None = None
    SinglePlyPVC: SinglePlyPVCV1 | None = None
    SinglePlyTPO: SinglePlyTPOV1 | None = None


class InsulationV1(BaseOpenEpdHierarchicalSpec):
    """Thermal insulation materials for use in construction."""

    _EXT_VERSION = "1.0"

    # Own fields:
    r_value: float | None = pyd.Field(default=None, description="", example=2.3)
    material: InsulatingMaterial | None = pyd.Field(default=None, description="", example="Mineral Wool")
    intended_application: list[InsulationIntendedApplication] | None = pyd.Field(
        default=None, description="", example=["Wall & General"]
    )
    thickness_per_declared_unit: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")

    # Nested specs:
    BlanketInsulation: BlanketInsulationV1 | None = None
    BlownInsulation: BlownInsulationV1 | None = None
    BoardInsulation: BoardInsulationV1 | None = None
    FoamedInPlace: FoamedInPlaceV1 | None = None
    SprayedInsulation: SprayedInsulationV1 | None = None


class DampproofingAndWaterproofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Dampproofing and waterproofing.

    Dampproofing, and built-up bituminous, sheet, fluid-applied, cementitious, reactive, and bentonite waterproofing.
    """

    _EXT_VERSION = "1.0"


class FlashingAndSheetMetalV1(BaseOpenEpdHierarchicalSpec):
    """Exposed sheet metal items, typically for drainage."""

    _EXT_VERSION = "1.0"


class JointProtectionV1(BaseOpenEpdHierarchicalSpec):
    """Preformed joint seals and sealants, expansion control joint cover assemblies."""

    _EXT_VERSION = "1.0"


class RoofCoverBoardsV1(BaseOpenEpdHierarchicalSpec):
    """
    Boards installed between the insulation and membrane layers on a roof system.

    It provides additional durability, fire protection, thermal, and vapor performance to a roof system, especially
    in low-slope, high foot traffic applications.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    material: RoofCoverBoardsMaterial | None = pyd.Field(default=None, description="", example="Gypsum Fiber")
    facing: list[RoofCoverBoardsFacing] | None = pyd.Field(default=None, description="", example=["Paper"])
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="1 m")


class SteepSlopeRoofingV1(BaseOpenEpdHierarchicalSpec):
    """Roofing materials typically for slopes of 3:12 and greater."""

    _EXT_VERSION = "1.0"


class WeatherBarriersV1(BaseOpenEpdHierarchicalSpec):
    """Vapor retarders and sheet or membrane air barriers."""

    _EXT_VERSION = "1.0"


class ThermalMoistureProtectionV1(BaseOpenEpdHierarchicalSpec):
    """
    Thermal moisture protection.

    Broad category of materials whose function is to provide moisture and thermal protection between spaces (e.g.,
    between the exterior and interior of a building).
    """

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
