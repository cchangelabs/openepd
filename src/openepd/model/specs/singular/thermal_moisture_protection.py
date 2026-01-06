#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    FoamType,
    InsulatingMaterial,
    InsulationIntendedApplication,
    MembraneRoofingReinforcement,
    RoofCoverBoardsFacing,
    RoofCoverBoardsMaterial,
)
from openepd.model.validation.quantity import LengthMmStr, PressureMPaStr


class BituminousRoofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Bituminous roofing.

    Premanufactured membrane roofing sheets consisting of asphalt, reinforcing layers, and in some cases a surfacing.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="BituminousRoofing",
        display_name="Bituminous Roofing",
        short_name="Bituminous",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> Bituminous"],
        description="Premanufactured membrane roofing sheets consisting of asphalt, reinforcing layers, and in some cases a surfacing.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SinglePlyEPDMV1(BaseOpenEpdHierarchicalSpec):
    """Ethylene propylene diene monomer (EPDM) rubber membrane."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SinglePlyEPDM",
        display_name="Single-Ply EPDM",
        short_name="EPDM",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> EPDM"],
        description="Ethylene propylene diene monomer (EPDM) rubber membrane.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SinglePlyKEEV1(BaseOpenEpdHierarchicalSpec):
    """
    Ketone Ethylene Ester (KEE) roof membranes.

    Consist of PVC resin and KEE plasticizer, with KEE exceeding 50% of the polymer content by weight.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SinglePlyKEE",
        display_name="Single-Ply KEE",
        short_name="KEE",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> KEE"],
        description="Ketone Ethylene Ester (KEE) roof membranes consist of PVC resin and KEE plasticizer, with KEE exceeding 50% of the polymer content by weight.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SinglePlyOtherV1(BaseOpenEpdHierarchicalSpec):
    """Single ply other performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SinglePlyOther",
        display_name="Other Membranes",
        short_name="Other",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> Other"],
        description="Other types of membrane roofing materials.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SinglePlyPolyurethaneV1(BaseOpenEpdHierarchicalSpec):
    """Polyurethane liquid for flat roof waterproofing."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SinglePlyPolyurethane",
        display_name="Single-Ply Polyurethane",
        short_name="Polyurethane",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> Polyurethane"],
        description="Polyurethane liquid for flat roof waterproofing.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SinglePlyPVCV1(BaseOpenEpdHierarchicalSpec):
    """Polyvinyl chloride (PVC) thermoplastic membrane."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SinglePlyPVC",
        display_name="Single-Ply PVC",
        short_name="PVC",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> PVC"],
        description="Polyvinyl chloride (PVC) thermoplastic membrane.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class SinglePlyTPOV1(BaseOpenEpdHierarchicalSpec):
    """Thermoplastic Polyolefin (TPO) membrane."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SinglePlyTPO",
        display_name="Single-Ply TPO",
        short_name="TPO",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing >> TPO"],
        description="Thermoplastic Polyolefin (TPO) membrane.",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class BlanketInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Non-rigid insulation batts, blankets, and rolls."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="BlanketInsulation",
        display_name="Blanket",
        alt_names=["Roll Insulation"],
        historical_names=["Thermal/Moisture Prot. >> Insulation >> Blanket"],
        description="Non-rigid insulation batts, blankets, and rolls",
        masterformat="07 21 16 Blanket Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class BlownInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Loose-fill insulation for blow-in or closed cavity applications."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="BlownInsulation",
        display_name="Blown",
        historical_names=["Thermal/Moisture Prot. >> Insulation >> Blown"],
        description="Loose-fill insulation for blow-in or closed cavity applications",
        masterformat="07 21 26 Blown Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class BoardInsulationV1(BaseOpenEpdHierarchicalSpec):
    """Rigid insulation products including rigid foams, wood fiberboard insulation, and rigid mineral wool boards."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="BoardInsulation",
        display_name="Board",
        historical_names=["Thermal/Moisture Prot. >> Insulation >> Board"],
        description="Rigid insulation products including rigid foams, wood fiberboard insulation, and rigid mineral wool boards",
        masterformat="07 21 13 Board Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    compressive_strength: PressureMPaStr | None = pydantic.Field(default=None, description="", examples=["1 MPa"])


class FoamedInPlaceV1(BaseOpenEpdHierarchicalSpec):
    """Open and closed cell spray foam insulation."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FoamedInPlace",
        display_name="Foamed-In-Place",
        historical_names=["Thermal/Moisture Prot. >> Insulation >> Foamed-In-Place"],
        description="Open and closed cell spray foam insulation",
        masterformat="07 21 19 Foamed-In-Place Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    foam_type: FoamType | None = pydantic.Field(default=None, description="", examples=["Open-Cell"])


class SprayedInsulationV1(BaseOpenEpdHierarchicalSpec):
    """
    Spray-on insulation, such as spray-on cellulose.

    Foaming sprays are categorized separately under foamed-in-place.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SprayedInsulation",
        display_name="Sprayed",
        historical_names=["Thermal/Moisture Prot. >> Insulation >> Sprayed"],
        description="Spray-on insulation, such as spray-on cellulose.  Foaming sprays are categorized separately under foamed-in-place.",
        masterformat="07 21 29 Sprayed Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class AirBarriersV1(BaseOpenEpdHierarchicalSpec):
    """Air Infiltration Barrier."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AirBarriers",
        display_name="Air Barriers",
        alt_names=["Air Infiltration Barrier"],
        historical_names=["Thermal/Moisture Prot. >> Air Barriers"],
        description="Air Infiltration Barrier",
        masterformat="07 27 00 Air Barriers",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class MembraneRoofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Membrane roofing.

    Built-up bituminous, modified bituminous, elastomeric, thermoplastic, fluid-applied, and hot-applied rubberized
    asphalt membrane roofing.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MembraneRoofing",
        display_name="Membrane Roofing",
        historical_names=["Thermal/Moisture Prot. >> Membrane Roofing"],
        description="Built-up bituminous, modified bituminous, elastomeric, thermoplastic, fluid-applied, and hot-applied rubberized asphalt membrane roofing  ",
        masterformat="07 50 00 Membrane Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])
    sri: float | None = pydantic.Field(default=None, description="", examples=[2.3])
    total_recycled_content: float | None = pydantic.Field(default=None, description="", examples=[0.5], ge=0, le=1)
    post_consumer_recycled_content: float | None = pydantic.Field(
        default=None, description="", examples=[0.5], ge=0, le=1
    )
    reinforcement: MembraneRoofingReinforcement | None = pydantic.Field(
        default=None, description="", examples=["Polyester"]
    )
    felt_backing: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    nsf347: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    vantage_vinyl: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="Insulation",
        display_name="Insulation",
        historical_names=["Thermal/Moisture Prot. >> Insulation"],
        description="Thermal insulation materials for use in construction",
        masterformat="07 21 00 Thermal Insulation",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    r_value: float | None = pydantic.Field(default=None, description="", examples=[2.3])
    material: InsulatingMaterial | None = pydantic.Field(default=None, description="", examples=["Mineral Wool"])
    intended_application: list[InsulationIntendedApplication] | None = pydantic.Field(
        default=None, description="", examples=[["Wall & General"]]
    )
    thickness_per_declared_unit: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])

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
    _CATEGORY_META = CategoryMeta(
        unique_name="DampproofingAndWaterproofing",
        display_name="Dampproofing And Waterproofing",
        historical_names=["Thermal/Moisture Prot. >> Dampproofing And Waterproofing"],
        description="Dampproofing, and built-up bituminous, sheet, fluid-applied, cementitious, reactive, and bentonite waterproofing ",
        masterformat="07 10 00 Dampproofing and Waterproofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class FlashingAndSheetMetalV1(BaseOpenEpdHierarchicalSpec):
    """Exposed sheet metal items, typically for drainage."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FlashingAndSheetMetal",
        display_name="Flashing and Sheet Metal",
        historical_names=["Thermal/Moisture Prot. >> Flashing and Sheet Metal"],
        description="Exposed sheet metal items, typically for drainage",
        masterformat="07 60 00 Flashing and Sheet Metal",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class JointProtectionV1(BaseOpenEpdHierarchicalSpec):
    """Preformed joint seals and sealants, expansion control joint cover assemblies."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="JointProtection",
        display_name="Joint Protection",
        historical_names=["Thermal/Moisture Prot. >> Joint Protection"],
        description="Preformed joint seals and sealants, expansion control joint cover assemblies",
        masterformat="07 90 00 Joint Protection",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class RoofCoverBoardsV1(BaseOpenEpdHierarchicalSpec):
    """
    Boards installed between the insulation and membrane layers on a roof system.

    It provides additional durability, fire protection, thermal, and vapor performance to a roof system, especially
    in low-slope, high foot traffic applications.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="RoofCoverBoards",
        display_name="Roof Cover Boards",
        alt_names=["Low Slope Roofing Cover Board"],
        historical_names=["Thermal/Moisture Prot. >> Roof Cover Boards"],
        description="Boards installed between the insulation and membrane layers on a roof system. It provides additional durability, fire protection, thermal, and vapor performance to a roof system, especially in low-slope, high foot traffic applications.",
        masterformat="07 22 17 Low Slope Roofing Cover Board",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    material: RoofCoverBoardsMaterial | None = pydantic.Field(default=None, description="", examples=["Gypsum Fiber"])
    facing: list[RoofCoverBoardsFacing] | None = pydantic.Field(default=None, description="", examples=[["Paper"]])
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["1 m"])


class SteepSlopeRoofingV1(BaseOpenEpdHierarchicalSpec):
    """Roofing materials typically for slopes of 3:12 and greater."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SteepSlopeRoofing",
        display_name="Steep Slope Roofing",
        historical_names=["Thermal/Moisture Prot. >> Steep Slope Roofing"],
        description="Roofing materials typically for slopes of 3:12 and greater",
        masterformat="07 30 00 Steep Slope Roofing",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class WeatherBarriersV1(BaseOpenEpdHierarchicalSpec):
    """Vapor retarders and sheet or membrane air barriers."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WeatherBarriers",
        display_name="Weather Barriers",
        historical_names=["Thermal/Moisture Prot. >> Weather Barriers"],
        description="Vapor retarders and sheet or membrane air barriers",
        masterformat="07 25 00 Weather Barriers",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class ThermalMoistureProtectionV1(BaseOpenEpdHierarchicalSpec):
    """
    Thermal moisture protection.

    Broad category of materials whose function is to provide moisture and thermal protection between spaces (e.g.,
    between the exterior and interior of a building).
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ThermalMoistureProtection",
        display_name="Thermal/Moisture Prot.",
        alt_names=["Thermal and Moisture Protection"],
        description="Broad category of materials whose function is to provide moisture and thermal protection between spaces (e.g., between the exterior and interior of a building)",
        masterformat="07 00 00 Thermal and Moisture",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

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
