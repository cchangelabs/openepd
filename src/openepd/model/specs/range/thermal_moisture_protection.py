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
    "AirBarriersRangeV1",
    "BituminousRoofingRangeV1",
    "BlanketInsulationRangeV1",
    "BlownInsulationRangeV1",
    "BoardInsulationRangeV1",
    "DampproofingAndWaterproofingRangeV1",
    "FlashingAndSheetMetalRangeV1",
    "FoamedInPlaceRangeV1",
    "InsulationRangeV1",
    "JointProtectionRangeV1",
    "MembraneRoofingRangeV1",
    "RoofCoverBoardsRangeV1",
    "SinglePlyEPDMRangeV1",
    "SinglePlyKEERangeV1",
    "SinglePlyOtherRangeV1",
    "SinglePlyPVCRangeV1",
    "SinglePlyPolyurethaneRangeV1",
    "SinglePlyTPORangeV1",
    "SprayedInsulationRangeV1",
    "SteepSlopeRoofingRangeV1",
    "ThermalMoistureProtectionRangeV1",
    "WeatherBarriersRangeV1",
)

import pydantic

from openepd.model.common import RangeFloat, RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    FoamType,
    InsulatingMaterial,
    InsulationIntendedApplication,
    MembraneRoofingReinforcement,
    RoofCoverBoardsFacing,
    RoofCoverBoardsMaterial,
)
from openepd.model.validation.quantity import AmountRangeLengthMm, AmountRangePressureMpa

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class BituminousRoofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Bituminous roofing.

    Premanufactured membrane roofing sheets consisting of asphalt, reinforcing layers, and in some cases a surfacing.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SinglePlyEPDMRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Ethylene propylene diene monomer (EPDM) rubber membrane.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SinglePlyKEERangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Ketone Ethylene Ester (KEE) roof membranes.

    Consist of PVC resin and KEE plasticizer, with KEE exceeding 50% of the polymer content by weight.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SinglePlyOtherRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Single ply other performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SinglePlyPolyurethaneRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Polyurethane liquid for flat roof waterproofing.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SinglePlyPVCRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Polyvinyl chloride (PVC) thermoplastic membrane.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SinglePlyTPORangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Thermoplastic Polyolefin (TPO) membrane.

    Range version.
    """

    _EXT_VERSION = "1.0"


class BlanketInsulationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Non-rigid insulation batts, blankets, and rolls.

    Range version.
    """

    _EXT_VERSION = "1.0"


class BlownInsulationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Loose-fill insulation for blow-in or closed cavity applications.

    Range version.
    """

    _EXT_VERSION = "1.0"


class BoardInsulationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Rigid insulation products including rigid foams, wood fiberboard insulation, and rigid mineral wool boards.

    Range version.
    """

    _EXT_VERSION = "1.0"

    compressive_strength: AmountRangePressureMpa | None = pydantic.Field(default=None, description="")


class FoamedInPlaceRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Open and closed cell spray foam insulation.

    Range version.
    """

    _EXT_VERSION = "1.0"

    foam_type: list[FoamType] | None = pydantic.Field(default=None, description="")


class SprayedInsulationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Spray-on insulation, such as spray-on cellulose.

    Foaming sprays are categorized separately under foamed-in-place.

    Range version.
    """

    _EXT_VERSION = "1.0"


class AirBarriersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Air Infiltration Barrier.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MembraneRoofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Membrane roofing.

    Built-up bituminous, modified bituminous, elastomeric, thermoplastic, fluid-applied, and hot-applied rubberized
    asphalt membrane roofing.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    sri: RangeFloat | None = pydantic.Field(default=None, description="")
    total_recycled_content: RangeRatioFloat | None = pydantic.Field(default=None, description="")
    post_consumer_recycled_content: RangeRatioFloat | None = pydantic.Field(default=None, description="")
    reinforcement: list[MembraneRoofingReinforcement] | None = pydantic.Field(default=None, description="")
    felt_backing: bool | None = pydantic.Field(default=None, description="")
    nsf347: bool | None = pydantic.Field(default=None, description="")
    vantage_vinyl: bool | None = pydantic.Field(default=None, description="")
    BituminousRoofing: BituminousRoofingRangeV1 | None = None
    SinglePlyEPDM: SinglePlyEPDMRangeV1 | None = None
    SinglePlyKEE: SinglePlyKEERangeV1 | None = None
    SinglePlyOther: SinglePlyOtherRangeV1 | None = None
    SinglePlyPolyurethane: SinglePlyPolyurethaneRangeV1 | None = None
    SinglePlyPVC: SinglePlyPVCRangeV1 | None = None
    SinglePlyTPO: SinglePlyTPORangeV1 | None = None


class InsulationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Thermal insulation materials for use in construction.

    Range version.
    """

    _EXT_VERSION = "1.0"

    r_value: RangeFloat | None = pydantic.Field(default=None, description="")
    material: list[InsulatingMaterial] | None = pydantic.Field(default=None, description="")
    intended_application: list[InsulationIntendedApplication] | None = pydantic.Field(default=None, description="")
    thickness_per_declared_unit: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    BlanketInsulation: BlanketInsulationRangeV1 | None = None
    BlownInsulation: BlownInsulationRangeV1 | None = None
    BoardInsulation: BoardInsulationRangeV1 | None = None
    FoamedInPlace: FoamedInPlaceRangeV1 | None = None
    SprayedInsulation: SprayedInsulationRangeV1 | None = None


class DampproofingAndWaterproofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Dampproofing and waterproofing.

    Dampproofing, and built-up bituminous, sheet, fluid-applied, cementitious, reactive, and bentonite waterproofing.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FlashingAndSheetMetalRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Exposed sheet metal items, typically for drainage.

    Range version.
    """

    _EXT_VERSION = "1.0"


class JointProtectionRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Preformed joint seals and sealants, expansion control joint cover assemblies.

    Range version.
    """

    _EXT_VERSION = "1.0"


class RoofCoverBoardsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Boards installed between the insulation and membrane layers on a roof system.

    It provides additional durability, fire protection, thermal, and vapor performance to a roof system, especially
    in low-slope, high foot traffic applications.

    Range version.
    """

    _EXT_VERSION = "1.0"

    material: list[RoofCoverBoardsMaterial] | None = pydantic.Field(default=None, description="")
    facing: list[RoofCoverBoardsFacing] | None = pydantic.Field(default=None, description="")
    thickness: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")


class SteepSlopeRoofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Roofing materials typically for slopes of 3:12 and greater.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WeatherBarriersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Vapor retarders and sheet or membrane air barriers.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ThermalMoistureProtectionRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Thermal moisture protection.

    Broad category of materials whose function is to provide moisture and thermal protection between spaces (e.g.,
    between the exterior and interior of a building).

    Range version.
    """

    _EXT_VERSION = "1.0"

    AirBarriers: AirBarriersRangeV1 | None = None
    MembraneRoofing: MembraneRoofingRangeV1 | None = None
    Insulation: InsulationRangeV1 | None = None
    DampproofingAndWaterproofing: DampproofingAndWaterproofingRangeV1 | None = None
    FlashingAndSheetMetal: FlashingAndSheetMetalRangeV1 | None = None
    JointProtection: JointProtectionRangeV1 | None = None
    RoofCoverBoards: RoofCoverBoardsRangeV1 | None = None
    SteepSlopeRoofing: SteepSlopeRoofingRangeV1 | None = None
    WeatherBarriers: WeatherBarriersRangeV1 | None = None
