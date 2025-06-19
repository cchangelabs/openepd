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

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    FlatGlassPanesThickness,
    FrameMaterial,
    HardwareFunction,
    NAFSPerformanceGrade,
    Spacer,
    ThermalSeparation,
)
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import (
    LengthMmStr,
    PressureMPaStr,
    SpeedStr,
    UFactorStr,
    validate_quantity_unit_factory,
)


class GlazingIntendedApplication(BaseOpenEpdSchema):
    """Glass intended application mixin."""

    curtain_wall: bool | None = pyd.Field(default=None, description="Intended for curtain walls. Relevant for IGUs.")
    r_windows: bool | None = pyd.Field(
        default=None,
        description="Intended for residential (NAFS 'R') and similar windows, doors, or skylights. Relevant for IGUs.",
    )
    lc_windows: bool | None = pyd.Field(
        default=None, description="Intended for light commercial (NAFS 'LC') and similar windows. Relevant for IGUs."
    )
    cw_windows: bool | None = pyd.Field(
        default=None, description="Intended for commercial (NAFS 'CW') and similar windows. Relevant for IGUs."
    )
    aw_windows: bool | None = pyd.Field(
        default=None, description="Intended for architectural (NAFS 'AW') and similar windows. Relevant for IGUs."
    )
    storefronts: bool | None = pyd.Field(
        default=None, description="Intended for Storefronts and similar applications. Relevant for IGUs."
    )
    glazed_doors: bool | None = pyd.Field(
        default=None, description="Intended for Glazed Doors and similar applications. Relevant for IGUs."
    )
    unit_skylights: bool | None = pyd.Field(
        default=None, description="Intended for Unit Skylights and similar applications. Relevant for IGUs."
    )
    sloped_skylights: bool | None = pyd.Field(
        default=None,
        description="Intended for sloped glazing, and architectural skylights, and similar. Relevant for IGUs.",
    )
    other: bool | None = pyd.Field(
        default=None, description="Intended for other application not listed. Relevant for IGUs."
    )


class GlazingOptionsMixin(BaseOpenEpdSchema):
    """Common glazing options."""

    low_emissivity: bool | None = pyd.Field(default=None, description="Low Emissivity coatings", example=True)
    electrochromic: bool | None = pyd.Field(
        default=None,
        description="Glazing with an electrically controllable solar heat gain and/or other properties.",
        example=True,
    )
    acid_etched: bool | None = pyd.Field(
        default=None, description="Flat glass that has undergone a chemical etching process.", example=True
    )
    tempered: bool | None = pyd.Field(
        default=None,
        description="Consists of a single pane that has been heat-treated to give the glass increased impact "
        "resistance. Standard typically used in North America.",
        example=True,
    )
    toughened: bool | None = pyd.Field(
        default=None,
        description="Consists of a single pane that has been specially heat-treated to give the glass increased impact "
        "resistance. Standard typically used in Europe.",
        example=True,
    )
    laminated: bool | None = pyd.Field(
        default=None,
        description="Consists of at least two glass panes lying one on top of the other, with one or several layers of "
        "a tear-resistant, viscoelastic film positioned between the panes, which consist of polyvinyl "
        "butyral (PVB)",
        example=True,
    )
    fire_resistant: bool | None = pyd.Field(default=None, example=True)
    fire_protection: bool | None = pyd.Field(
        default=None,
        description="Specifically tested for its ability to block flames and smoke, but not radiant heat. Ranges from"
        " specialty tempered products rated for ~20 minutes to glass ceramics rated up to 3 hours.",
        example=True,
    )
    pyrolytic_coated: bool | None = pyd.Field(
        default=None,
        description="At least one coating is applied in a pyrolytic process, typically during float glass production.",
        example=True,
    )
    sputter_coat: bool | None = pyd.Field(
        default=None,
        description="At least one coating is applied using sputter (vacuum deposition) coating.",
        example=True,
    )
    solar_heat_gain: RatioFloat | None = pyd.Field(
        default=None,
        description="Solar heat gain, measured at a certain level of Differential Pressure. Range is 0 to 1.",
        example=0.5,
        ge=0,
        le=1,
    )


class PanelDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Panel doors performance specification."""

    _EXT_VERSION = "1.0"


class PressureResistantDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Pressure-Resistant Doors."""

    _EXT_VERSION = "1.0"


class SpecialFunctionDoorsV1(BaseOpenEpdHierarchicalSpec):
    """
    Special function doors.

    Includes doors for e.g., cold storage, hangars, lightproof applications,
    security, sound control, vaults, etc.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    PanelDoors: PanelDoorsV1 | None = None
    PressureResistantDoors: PressureResistantDoorsV1 | None = None


class SlidingGlassDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Sliding glass doors performance specification."""

    _EXT_VERSION = "1.0"


class FenestrationAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """
    Fenestration accessories.

    Gaskets, seals, fasteners, and other low-mass items which may be useful in calculating the impact of a
    fenestration system.
    """

    _EXT_VERSION = "1.0"


class FenestrationFramingV1(BaseOpenEpdHierarchicalSpec):
    """
    Fenestration Framing.

    Lineal elements ("sticks") for use in fenestration, including frames, sashes, and mullions.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    thermal_separation: ThermalSeparation | None = pyd.Field(default=None, example="Aluminium")
    material: FrameMaterial | None = pyd.Field(default=None, example="Vinyl")


class FenestrationHardwareV1(BaseOpenEpdHierarchicalSpec):
    """Locks, operation hardware, and other substantial items declared on a per-piece basis."""

    _EXT_VERSION = "1.0"

    # Own fields:
    function: HardwareFunction | None = pyd.Field(default=None, description="", example="Lock")


class FlatGlassPanesV1(BaseOpenEpdHierarchicalSpec):
    """Monolithic, uncoated flat glass panes that are not substantially processed."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: FlatGlassPanesThickness | None = pyd.Field(default=None, example="12 mm")

    _flat_glass_panes_thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(
        validate_quantity_unit_factory("m")
    )


class ProcessedNonInsulatingGlassPanesV1(BaseOpenEpdHierarchicalSpec, GlazingOptionsMixin):
    """
    Solid glass panes without internal gaps which have been heat-treated or otherwise substantially processed.

    Includes:
    1. Coatings including low-e and other coatings (see PCR)
    2. laminating (fire-rated, glass clad polycarbonate, interlayers
    3. Heat treated (heat strengthened, tempered, fire-rated)
    4. Mechanically or chemically processed or fabricated
    (edging, bending, etching, drilling, notching, cutting, polishing, etc)
    5. combined products of processing in 1-5.
    """

    _EXT_VERSION = "1.0"


class GlazedDoorsV1(BaseOpenEpdHierarchicalSpec):
    """
    Factory assembled door which is at least 50% glass by area.

    Includes sliding patio doors and hinged doors.
    """

    _EXT_VERSION = "1.0"


class UnitSkylightsV1(BaseOpenEpdHierarchicalSpec):
    """
    Unit skylights performance specification.

    A factory assembled fenestration unit for installation on the roof of a structure to provide interior
    building spaces with natural daylight, warmth, and ventilation; generally not operable
    by hand (cf. roof window). Includes frame(s) and possibly operating hardware.
    """

    _EXT_VERSION = "1.1"

    roof_window: bool | None = pyd.Field(
        default=None,
        description=(
            "Similar to a skylight but has an outward opening that extends from a roof, and is therefore not fixed"
        ),
        example=True,
    )


class WindowsV1(BaseOpenEpdHierarchicalSpec):
    """Windows including glazing and frame material."""

    _EXT_VERSION = "1.0"


class IntegratedDoorsOpeningAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """Pre-installed unit that includes door, frame, and hardware."""

    _EXT_VERSION = "1.0"


class MetalDoorAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """Metal doors and frames."""

    _EXT_VERSION = "1.0"


class SpecialtyDoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """
    Specialty doors and frames.

    Includes e.g., access doors and panels, sliding glass doors, coiling doors, special function doors,
    folding doors, etc.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    SpecialFunctionDoors: SpecialFunctionDoorsV1 | None = None
    SlidingGlassDoors: SlidingGlassDoorsV1 | None = None


class WoodDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Wood doors performance specification."""

    _EXT_VERSION = "1.0"


class FenestrationPartsV1(BaseOpenEpdHierarchicalSpec):
    """
    Fenestration Parts.

    Parts and assemblies for integration into building fenestration such as windows, curtain walls,
    and storefronts.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    intended_application: GlazingIntendedApplication | None = pyd.Field(
        default=None, description="Intended application."
    )

    # Nested specs:
    FenestrationAccessories: FenestrationAccessoriesV1 | None = None
    FenestrationFraming: FenestrationFramingV1 | None = None
    FenestrationHardware: FenestrationHardwareV1 | None = None


class GlassPanesV1(BaseOpenEpdHierarchicalSpec):
    """Flat glass panes."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    FlatGlassPanes: FlatGlassPanesV1 | None = None
    ProcessedNonInsulatingGlassPanes: ProcessedNonInsulatingGlassPanesV1 | None = None


class NAFSPerformanceClass(BaseOpenEpdSchema):
    """NAFS Performance class."""

    r: bool | None = pyd.Field(
        default=None, description="Residential; commonly used in one- and two-family dwellings.", example=True
    )
    lc: bool | None = pyd.Field(
        default=None,
        description="Light Commercial: commonly used in low-rise and mid-rise multi-family dwellings and other "
        "buildings where larger sizes and higher loading requirements are expected.",
        example=True,
    )
    cw: bool | None = pyd.Field(
        default=None,
        description="Commercial Window: commonly used in low-rise and mid-rise buildings where larger sizes, higher "
        "loading requirements, limits on deflection, and heavy use are expected.",
        example=True,
    )
    aw: bool | None = pyd.Field(
        default=None,
        description="Architectural Window: commonly used in high-rise and mid-rise buildings to meet increased "
        "loading requirements and limits on deflection, and in buildings where frequent and extreme use "
        "of the fenestration products is expected.",
        example=True,
    )


class NAFSFenestrationV1(BaseOpenEpdHierarchicalSpec, GlazingOptionsMixin):
    """Factory assembled fenestration units compliant to the North American Fenestration Standard."""

    _EXT_VERSION = "1.0"

    # Own fields:
    hurricane_resistant: bool | None = pyd.Field(
        default=None, description="The product has been designed to resist windborne debris.", example=True
    )

    assembly_u_factor: UFactorStr | None = pyd.Field(
        default=None,
        description="Weighted average conductance of heat across assembly (including frame).",
        example="1 USI",
    )
    air_infiltration: SpeedStr | None = pyd.Field(
        default=None,
        description="Air infiltration, measured at a certain level of Differential Pressure.",
        example="1 m3 / m2 / s",
    )

    thermal_separation: ThermalSeparation | None = pyd.Field(default=None, example="Aluminium")
    dp_rating: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    glass_panes: int | None = pyd.Field(
        default=None,
        description="Number of panes, each separated by a cavity. A 3 pane unit has 2 cavities. example: 3",
        example=3,
    )

    performance_class: NAFSPerformanceClass | None = pyd.Field(
        default=None, description="Performance class according to NAFS."
    )

    performance_grade: NAFSPerformanceGrade | None = pyd.Field(
        default=None,
        description="NAFS Performance Grade. The NAFS Performance Grade is a number that represents the performance "
        "of the glazing product. The higher the number, the better the performance. The NAFS Performance "
        "Grade is calculated using the NAFS Performance Class, the NAFS Performance Index, and the NAFS "
        "Performance Factor. While it is expressed as pressure, there are specific values which are "
        "allowed. The values are listed in the enum.",
        example="95 psf",
    )

    _assembly_u_factor_is_quantity_validator = pyd.validator("assembly_u_factor", allow_reuse=True)(
        validate_quantity_unit_factory("USI")
    )
    _nafs_performance_grade_is_quantity_validator = pyd.validator("performance_grade", allow_reuse=True)(
        validate_quantity_unit_factory("psf")
    )

    # Nested specs:
    GlazedDoors: GlazedDoorsV1 | None = None
    UnitSkylights: UnitSkylightsV1 | None = None
    Windows: WindowsV1 | None = None


class InsulatingGlazingUnitsV1(BaseOpenEpdHierarchicalSpec, GlazingOptionsMixin):
    """Insulating glazing units performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    intended_application: GlazingIntendedApplication | None = pyd.Field(
        default=None, description="Intended application for IGUs."
    )

    hurricane_resistant: bool | None = pyd.Field(default=None, example=True)

    dp_rating: PressureMPaStr | None = pyd.Field(
        default=None, description="Maximum Differential Pressure, a measure of wind tolerance.", example="1 MPa"
    )
    air_infiltration: SpeedStr | None = pyd.Field(
        default=None,
        description="Air infiltration, measured at a certain level of Differential Pressure.",
        example="1 m3 / m2 / s",
    )
    glass_panes: int | None = pyd.Field(
        default=None,
        description="Number of panes, each separated by a cavity. A 3 pane unit has 2 cavities. example: 3",
        example=3,
    )
    cog_u_factor: UFactorStr | None = pyd.Field(
        default=None, description="Conductance of heat at center of glass.", example="1 USI"
    )
    spacer: Spacer | None = pyd.Field(
        default=None, description="Spacer material for Integrated Glass Unit.", example="Aluminium"
    )

    _dp_rating_is_quantity_validator = pyd.validator("dp_rating", allow_reuse=True)(
        validate_quantity_unit_factory("MPa")
    )
    _cog_u_factor_is_quantity_validator = pyd.validator("cog_u_factor", allow_reuse=True)(
        validate_quantity_unit_factory("USI")
    )


class CurtainWallsV1(BaseOpenEpdHierarchicalSpec):
    """
    Curtain Walls.

    Exterior skin of building where walls are non-structural and are outboard of the floor slabs,
    often as system of aluminum framing with vision glass and opaque panels of glass, metal, or other
    materials.

    Can be 'unitized' (prefabricated off-site) or 'stick' (fabricated on site).
    """

    _EXT_VERSION = "1.0"


class DoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """Doors (the operable part) and frames (what holds the door proper)."""

    _EXT_VERSION = "1.0"

    # Own fields:
    height: LengthMmStr | None = pyd.Field(default=None, example="1200 mm")
    width: LengthMmStr | None = pyd.Field(default=None, example="600 mm")

    # Nested specs:
    IntegratedDoorsOpeningAssemblies: IntegratedDoorsOpeningAssembliesV1 | None = None
    MetalDoorAndFrames: MetalDoorAndFramesV1 | None = None
    SpecialtyDoorsAndFrames: SpecialtyDoorsAndFramesV1 | None = None
    WoodDoors: WoodDoorsV1 | None = None


class EntrancesV1(BaseOpenEpdHierarchicalSpec):
    """Building entrances (distinct from the door proper)."""

    _EXT_VERSION = "1.0"


class GlazingV1(BaseOpenEpdHierarchicalSpec):
    """
    Glazing performance specification.

    Broad category of glass-based products, accessories, and assemblies ranging from
    glass panes and framing to curtain walls.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    FenestrationParts: FenestrationPartsV1 | None = None
    GlassPanes: GlassPanesV1 | None = None
    NAFSFenestration: NAFSFenestrationV1 | None = None
    InsulatingGlazingUnits: InsulatingGlazingUnitsV1 | None = None


class StorefrontsV1(BaseOpenEpdHierarchicalSpec):
    """
    Storefronts.

    Fabricated building facades commonly used in retail applications, typically one or two stories
    tall and using metal framing and glass.
    """

    _EXT_VERSION = "1.0"


class TranslucentWallAndRoofAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """
    Translucent wall and roof assemblies.

    Includes structured polycarbonate panel and fiberglass sandwich panel assemblies.
    """

    _EXT_VERSION = "1.0"


class WindowWallAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """
    Window Wall Assemblies.

    Exterior skin of building where walls are non-structural and sit between floor slabs, often as
    system of aluminum framing with vision glass and opaque panels of glass, metal,
    or other materials.
    """

    _EXT_VERSION = "1.0"


class OpeningsV1(BaseOpenEpdHierarchicalSpec):
    """
    Openings performance specification.

    General category that includes windows, storefronts, window walls, curtain walls,
    doors, entrances, etc.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, example="80 mm")

    # Nested specs:
    CurtainWalls: CurtainWallsV1 | None = None
    DoorsAndFrames: DoorsAndFramesV1 | None = None
    Entrances: EntrancesV1 | None = None
    Glazing: GlazingV1 | None = None
    Storefronts: StorefrontsV1 | None = None
    TranslucentWallAndRoofAssemblies: TranslucentWallAndRoofAssembliesV1 | None = None
    WindowWallAssemblies: WindowWallAssembliesV1 | None = None
