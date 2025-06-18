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
    "CurtainWallsRangeV1",
    "DoorsAndFramesRangeV1",
    "EntrancesRangeV1",
    "FenestrationAccessoriesRangeV1",
    "FenestrationFramingRangeV1",
    "FenestrationHardwareRangeV1",
    "FenestrationPartsRangeV1",
    "FlatGlassPanesRangeV1",
    "GlassPanesRangeV1",
    "GlazedDoorsRangeV1",
    "GlazingRangeV1",
    "InsulatingGlazingUnitsRangeV1",
    "IntegratedDoorsOpeningAssembliesRangeV1",
    "MetalDoorAndFramesRangeV1",
    "NAFSFenestrationRangeV1",
    "OpeningsRangeV1",
    "PanelDoorsRangeV1",
    "PressureResistantDoorsRangeV1",
    "ProcessedNonInsulatingGlassPanesRangeV1",
    "SlidingGlassDoorsRangeV1",
    "SpecialFunctionDoorsRangeV1",
    "SpecialtyDoorsAndFramesRangeV1",
    "StorefrontsRangeV1",
    "TranslucentWallAndRoofAssembliesRangeV1",
    "UnitSkylightsRangeV1",
    "WindowWallAssembliesRangeV1",
    "WindowsRangeV1",
    "WoodDoorsRangeV1",
)

import pydantic

from openepd.model.common import RangeInt, RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    FlatGlassPanesThickness,
    FrameMaterial,
    HardwareFunction,
    NAFSPerformanceGrade,
    Spacer,
    ThermalSeparation,
)
from openepd.model.specs.singular.openings import GlazingIntendedApplication, NAFSPerformanceClass
from openepd.model.validation.quantity import (
    AmountRangeLengthMm,
    AmountRangePressureMpa,
    AmountRangeSpeed,
    AmountRangeUFactor,
)


class PanelDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Panel doors performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PressureResistantDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Pressure-Resistant Doors.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SpecialFunctionDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Special function doors.

    Includes doors for e.g., cold storage, hangars, lightproof applications,
    security, sound control, vaults, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    PanelDoors: PanelDoorsRangeV1 | None = None
    PressureResistantDoors: PressureResistantDoorsRangeV1 | None = None


class SlidingGlassDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Sliding glass doors performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FenestrationAccessoriesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fenestration accessories.

    Gaskets, seals, fasteners, and other low-mass items which may be useful in calculating the impact of a
    fenestration system.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FenestrationFramingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fenestration Framing.

    Lineal elements ("sticks") for use in fenestration, including frames, sashes, and mullions.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thermal_separation: list[ThermalSeparation] | None = pydantic.Field(default=None)
    material: list[FrameMaterial] | None = pydantic.Field(default=None)


class FenestrationHardwareRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Locks, operation hardware, and other substantial items declared on a per-piece basis.

    Range version.
    """

    _EXT_VERSION = "1.0"

    function: list[HardwareFunction] | None = pydantic.Field(default=None, description="")


class FlatGlassPanesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Monolithic, uncoated flat glass panes that are not substantially processed.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: list[FlatGlassPanesThickness] | None = pydantic.Field(default=None)


class ProcessedNonInsulatingGlassPanesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Solid glass panes without internal gaps which have been heat-treated or otherwise substantially processed.

    Includes:
    1. Coatings including low-e and other coatings (see PCR)
    2. laminating (fire-rated, glass clad polycarbonate, interlayers
    3. Heat treated (heat strengthened, tempered, fire-rated)
    4. Mechanically or chemically processed or fabricated
    (edging, bending, etching, drilling, notching, cutting, polishing, etc)
    5. combined products of processing in 1-5.

    Range version.
    """

    _EXT_VERSION = "1.0"

    low_emissivity: bool | None = None
    electrochromic: bool | None = None
    acid_etched: bool | None = None
    tempered: bool | None = None
    toughened: bool | None = None
    laminated: bool | None = None
    fire_resistant: bool | None = None
    fire_protection: bool | None = None
    pyrolytic_coated: bool | None = None
    sputter_coat: bool | None = None
    solar_heat_gain: RangeRatioFloat | None = None


class GlazedDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Factory assembled door which is at least 50% glass by area.

    Includes sliding patio doors and hinged doors.

    Range version.
    """

    _EXT_VERSION = "1.0"


class UnitSkylightsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Unit skylights performance specification.

    A factory assembled fenestration unit for installation on the roof of a structure to provide interior
    building spaces with natural daylight, warmth, and ventilation; generally not operable
    by hand (cf. roof window). Includes frame(s) and possibly operating hardware.

    Range version.
    """

    _EXT_VERSION = "1.1"

    roof_window: bool | None = pydantic.Field(
        default=None,
        description=(
            "Similar to a skylight but has an outward opening that extends from a roof, and is therefore not fixed"
        ),
        examples=[True],
    )


class WindowsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Windows including glazing and frame material.

    Range version.
    """

    _EXT_VERSION = "1.0"


class IntegratedDoorsOpeningAssembliesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Pre-installed unit that includes door, frame, and hardware.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MetalDoorAndFramesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Metal doors and frames.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SpecialtyDoorsAndFramesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Specialty doors and frames.

    Includes e.g., access doors and panels, sliding glass doors, coiling doors, special function doors,
    folding doors, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    SpecialFunctionDoors: SpecialFunctionDoorsRangeV1 | None = None
    SlidingGlassDoors: SlidingGlassDoorsRangeV1 | None = None


class WoodDoorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wood doors performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FenestrationPartsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fenestration Parts.

    Parts and assemblies for integration into building fenestration such as windows, curtain walls,
    and storefronts.

    Range version.
    """

    _EXT_VERSION = "1.0"

    intended_application: GlazingIntendedApplication | None = pydantic.Field(
        default=None, description="Intended application."
    )
    FenestrationAccessories: FenestrationAccessoriesRangeV1 | None = None
    FenestrationFraming: FenestrationFramingRangeV1 | None = None
    FenestrationHardware: FenestrationHardwareRangeV1 | None = None


class GlassPanesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Flat glass panes.

    Range version.
    """

    _EXT_VERSION = "1.0"

    FlatGlassPanes: FlatGlassPanesRangeV1 | None = None
    ProcessedNonInsulatingGlassPanes: ProcessedNonInsulatingGlassPanesRangeV1 | None = None


class NAFSFenestrationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Factory assembled fenestration units compliant to the North American Fenestration Standard.

    Range version.
    """

    _EXT_VERSION = "1.0"

    low_emissivity: bool | None = None
    electrochromic: bool | None = None
    acid_etched: bool | None = None
    tempered: bool | None = None
    toughened: bool | None = None
    laminated: bool | None = None
    fire_resistant: bool | None = None
    fire_protection: bool | None = None
    pyrolytic_coated: bool | None = None
    sputter_coat: bool | None = None
    solar_heat_gain: RangeRatioFloat | None = None
    hurricane_resistant: bool | None = pydantic.Field(
        default=None,
        description="The product has been designed to resist windborne debris.",
    )
    assembly_u_factor: AmountRangeUFactor | None = pydantic.Field(
        default=None,
        description="Weighted average conductance of heat across assembly (including frame).",
    )
    air_infiltration: AmountRangeSpeed | None = pydantic.Field(
        default=None,
        description="Air infiltration, measured at a certain level of Differential Pressure.",
    )
    thermal_separation: list[ThermalSeparation] | None = pydantic.Field(default=None)
    dp_rating: AmountRangePressureMpa | None = pydantic.Field(default=None, description="")
    glass_panes: RangeInt | None = pydantic.Field(
        default=None,
        description="Number of panes, each separated by a cavity. A 3 pane unit has 2 cavities. example: 3",
    )
    performance_class: NAFSPerformanceClass | None = pydantic.Field(
        default=None, description="Performance class according to NAFS."
    )
    performance_grade: list[NAFSPerformanceGrade] | None = pydantic.Field(
        default=None,
        description="NAFS Performance Grade. The NAFS Performance Grade is a number that represents the performance of the glazing product. The higher the number, the better the performance. The NAFS Performance Grade is calculated using the NAFS Performance Class, the NAFS Performance Index, and the NAFS Performance Factor. While it is expressed as pressure, there are specific values which are allowed. The values are listed in the enum.",
    )
    GlazedDoors: GlazedDoorsRangeV1 | None = None
    UnitSkylights: UnitSkylightsRangeV1 | None = None
    Windows: WindowsRangeV1 | None = None


class InsulatingGlazingUnitsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Insulating glazing units performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

    low_emissivity: bool | None = None
    electrochromic: bool | None = None
    acid_etched: bool | None = None
    tempered: bool | None = None
    toughened: bool | None = None
    laminated: bool | None = None
    fire_resistant: bool | None = None
    fire_protection: bool | None = None
    pyrolytic_coated: bool | None = None
    sputter_coat: bool | None = None
    solar_heat_gain: RangeRatioFloat | None = None
    intended_application: GlazingIntendedApplication | None = pydantic.Field(
        default=None, description="Intended application for IGUs."
    )
    hurricane_resistant: bool | None = pydantic.Field(default=None)
    dp_rating: AmountRangePressureMpa | None = pydantic.Field(
        default=None,
        description="Maximum Differential Pressure, a measure of wind tolerance.",
    )
    air_infiltration: AmountRangeSpeed | None = pydantic.Field(
        default=None,
        description="Air infiltration, measured at a certain level of Differential Pressure.",
    )
    glass_panes: RangeInt | None = pydantic.Field(
        default=None,
        description="Number of panes, each separated by a cavity. A 3 pane unit has 2 cavities. example: 3",
    )
    cog_u_factor: AmountRangeUFactor | None = pydantic.Field(
        default=None, description="Conductance of heat at center of glass."
    )
    spacer: list[Spacer] | None = pydantic.Field(default=None, description="Spacer material for Integrated Glass Unit.")


class CurtainWallsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Curtain Walls.

    Exterior skin of building where walls are non-structural and are outboard of the floor slabs,
    often as system of aluminum framing with vision glass and opaque panels of glass, metal, or other
    materials.

    Can be 'unitized' (prefabricated off-site) or 'stick' (fabricated on site).

    Range version.
    """

    _EXT_VERSION = "1.0"


class DoorsAndFramesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Doors (the operable part) and frames (what holds the door proper).

    Range version.
    """

    _EXT_VERSION = "1.0"

    height: AmountRangeLengthMm | None = pydantic.Field(default=None)
    width: AmountRangeLengthMm | None = pydantic.Field(default=None)
    IntegratedDoorsOpeningAssemblies: IntegratedDoorsOpeningAssembliesRangeV1 | None = None
    MetalDoorAndFrames: MetalDoorAndFramesRangeV1 | None = None
    SpecialtyDoorsAndFrames: SpecialtyDoorsAndFramesRangeV1 | None = None
    WoodDoors: WoodDoorsRangeV1 | None = None


class EntrancesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Building entrances (distinct from the door proper).

    Range version.
    """

    _EXT_VERSION = "1.0"


class GlazingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Glazing performance specification.

    Broad category of glass-based products, accessories, and assemblies ranging from
    glass panes and framing to curtain walls.

    Range version.
    """

    _EXT_VERSION = "1.0"

    FenestrationParts: FenestrationPartsRangeV1 | None = None
    GlassPanes: GlassPanesRangeV1 | None = None
    NAFSFenestration: NAFSFenestrationRangeV1 | None = None
    InsulatingGlazingUnits: InsulatingGlazingUnitsRangeV1 | None = None


class StorefrontsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Storefronts.

    Fabricated building facades commonly used in retail applications, typically one or two stories
    tall and using metal framing and glass.

    Range version.
    """

    _EXT_VERSION = "1.0"


class TranslucentWallAndRoofAssembliesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Translucent wall and roof assemblies.

    Includes structured polycarbonate panel and fiberglass sandwich panel assemblies.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WindowWallAssembliesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Window Wall Assemblies.

    Exterior skin of building where walls are non-structural and sit between floor slabs, often as
    system of aluminum framing with vision glass and opaque panels of glass, metal,
    or other materials.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OpeningsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Openings performance specification.

    General category that includes windows, storefronts, window walls, curtain walls,
    doors, entrances, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pydantic.Field(default=None)
    CurtainWalls: CurtainWallsRangeV1 | None = None
    DoorsAndFrames: DoorsAndFramesRangeV1 | None = None
    Entrances: EntrancesRangeV1 | None = None
    Glazing: GlazingRangeV1 | None = None
    Storefronts: StorefrontsRangeV1 | None = None
    TranslucentWallAndRoofAssemblies: TranslucentWallAndRoofAssembliesRangeV1 | None = None
    WindowWallAssemblies: WindowWallAssembliesRangeV1 | None = None
