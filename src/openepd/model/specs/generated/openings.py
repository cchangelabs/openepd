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
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import (
    FlatGlassPanesThickness,
    FrameMaterial,
    HardwareFunction,
    NAFSPerformanceGrade,
    Spacer,
    ThermalSeparation,
)
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, PressureMPaStr, validate_unit_factory


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


class PanelDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Panel doors performance specification."""

    _EXT_VERSION = "1.0"


class PressureResistantDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Pressure resistant doors performance specification."""

    _EXT_VERSION = "1.0"


class SpecialFunctionDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Special function doors performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PanelDoors: PanelDoorsV1 | None = None
    PressureResistantDoors: PressureResistantDoorsV1 | None = None


class SlidingGlassDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Sliding glass doors performance specification."""

    _EXT_VERSION = "1.0"


class FenestrationAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Fenestration accessories performance specification."""

    _EXT_VERSION = "1.0"


class FenestrationFramingV1(BaseOpenEpdHierarchicalSpec):
    """Fenestration framing performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thermal_separation: ThermalSeparation | None = pyd.Field(default=None, description="", example="Aluminium")
    material: FrameMaterial | None = pyd.Field(default=None, description="", example="Vinyl")


class FenestrationHardwareV1(BaseOpenEpdHierarchicalSpec):
    """Fenestration hardware performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    function: HardwareFunction | None = pyd.Field(default=None, description="", example="Lock")


class FlatGlassPanesV1(BaseOpenEpdHierarchicalSpec):
    """Flat glass panes performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: FlatGlassPanesThickness | None = pyd.Field(default=None, description="", example="12 mm")

    _flat_glass_panes_thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class ProcessedNonInsulatingGlassPanesV1(BaseOpenEpdHierarchicalSpec):
    """Processed non insulating glass panes performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    low_emissivity: bool | None = pyd.Field(default=None, description="", example=True)
    electrochromic: bool | None = pyd.Field(default=None, description="", example=True)
    acid_etched: bool | None = pyd.Field(default=None, description="", example=True)
    tempered: bool | None = pyd.Field(default=None, description="", example=True)
    toughened: bool | None = pyd.Field(default=None, description="", example=True)
    laminated: bool | None = pyd.Field(default=None, description="", example=True)
    fire_resistant: bool | None = pyd.Field(default=None, description="", example=True)
    fire_protection: bool | None = pyd.Field(default=None, description="", example=True)
    pyrolytic_coated: bool | None = pyd.Field(default=None, description="", example=True)
    sputter_coat: bool | None = pyd.Field(default=None, description="", example=True)
    solar_heat_gain: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)


class GlazedDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Glazed doors performance specification."""

    _EXT_VERSION = "1.0"


class UnitSkylightsV1(BaseOpenEpdHierarchicalSpec):
    """Unit skylights performance specification."""

    _EXT_VERSION = "1.0"


class WindowsV1(BaseOpenEpdHierarchicalSpec):
    """Windows performance specification."""

    _EXT_VERSION = "1.0"


class IntegratedDoorsOpeningAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """Integrated doors opening assemblies performance specification."""

    _EXT_VERSION = "1.0"


class MetalDoorAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """Metal door and frames performance specification."""

    _EXT_VERSION = "1.0"


class SpecialtyDoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """Specialty doors and frames performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    SpecialFunctionDoors: SpecialFunctionDoorsV1 | None = None
    SlidingGlassDoors: SlidingGlassDoorsV1 | None = None


class WoodDoorsV1(BaseOpenEpdHierarchicalSpec):
    """Wood doors performance specification."""

    _EXT_VERSION = "1.0"


class FenestrationPartsV1(BaseOpenEpdHierarchicalSpec):
    """Fenestration parts performance specification."""

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
    """Glass panes performance specification."""

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


class NAFSFenestrationV1(BaseOpenEpdHierarchicalSpec):
    """NAFS fenestration performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    hurricane_resistant: bool | None = pyd.Field(default=None, description="", example=True)
    low_emissivity: bool | None = pyd.Field(default=None, description="", example=True)
    electrochromic: bool | None = pyd.Field(default=None, description="", example=True)
    acid_etched: bool | None = pyd.Field(default=None, description="", example=True)
    tempered: bool | None = pyd.Field(default=None, description="", example=True)
    toughened: bool | None = pyd.Field(default=None, description="", example=True)
    laminated: bool | None = pyd.Field(default=None, description="", example=True)
    fire_resistant: bool | None = pyd.Field(default=None, description="", example=True)
    fire_protection: bool | None = pyd.Field(default=None, description="", example=True)
    pyrolytic_coated: bool | None = pyd.Field(default=None, description="", example=True)
    sputter_coat: bool | None = pyd.Field(default=None, description="", example=True)
    thermal_separation: ThermalSeparation | None = pyd.Field(default=None, description="", example="Aluminium")
    assembly_u_factor: str | None = pyd.Field(default=None, description="", example="1 USI")
    solar_heat_gain: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)
    air_infiltration: str | None = pyd.Field(default=None, description="", example="1 m / s")
    dp_rating: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    glass_panes: int | None = pyd.Field(default=None, description="", example=3)

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
        validate_unit_factory("USI")
    )
    _air_infiltration_is_quantity_validator = pyd.validator("air_infiltration", allow_reuse=True)(
        validate_unit_factory("m / s")
    )
    _dp_rating_is_quantity_validator = pyd.validator("dp_rating", allow_reuse=True)(validate_unit_factory("MPa"))
    _nafs_performance_grade_is_quantity_validator = pyd.validator("performance_grade", allow_reuse=True)(
        validate_unit_factory("psf")
    )

    # Nested specs:
    GlazedDoors: GlazedDoorsV1 | None = None
    UnitSkylights: UnitSkylightsV1 | None = None
    Windows: WindowsV1 | None = None


class InsulatingGlazingUnitsV1(BaseOpenEpdHierarchicalSpec):
    """Insulating glazing units performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    intended_application: GlazingIntendedApplication | None = pyd.Field(
        default=None, description="Intended application for IGUs."
    )

    hurricane_resistant: bool | None = pyd.Field(default=None, description="", example=True)
    low_emissivity: bool | None = pyd.Field(default=None, description="", example=True)
    electrochromic: bool | None = pyd.Field(default=None, description="", example=True)
    acid_etched: bool | None = pyd.Field(default=None, description="", example=True)
    tempered: bool | None = pyd.Field(default=None, description="", example=True)
    toughened: bool | None = pyd.Field(default=None, description="", example=True)
    laminated: bool | None = pyd.Field(default=None, description="", example=True)
    fire_resistant: bool | None = pyd.Field(default=None, description="", example=True)
    fire_protection: bool | None = pyd.Field(default=None, description="", example=True)
    pyrolytic_coated: bool | None = pyd.Field(default=None, description="", example=True)
    sputter_coat: bool | None = pyd.Field(default=None, description="", example=True)
    solar_heat_gain: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)
    air_infiltration: str | None = pyd.Field(default=None, description="", example="1 m / s")
    dp_rating: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    glass_panes: int | None = pyd.Field(default=None, description="", example=3)
    cog_u_factor: str | None = pyd.Field(default=None, description="", example="1 USI")
    spacer: Spacer | None = pyd.Field(default=None, description="", example="Aluminium")

    _air_infiltration_is_quantity_validator = pyd.validator("air_infiltration", allow_reuse=True)(
        validate_unit_factory("m / s")
    )
    _dp_rating_is_quantity_validator = pyd.validator("dp_rating", allow_reuse=True)(validate_unit_factory("MPa"))
    _cog_u_factor_is_quantity_validator = pyd.validator("cog_u_factor", allow_reuse=True)(validate_unit_factory("USI"))


class CurtainWallsV1(BaseOpenEpdHierarchicalSpec):
    """Curtain walls performance specification."""

    _EXT_VERSION = "1.0"


class DoorsAndFramesV1(BaseOpenEpdHierarchicalSpec):
    """Doors and frames performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    height: LengthMmStr | None = pyd.Field(default=None, description="", example="1200 mm")
    width: LengthMmStr | None = pyd.Field(default=None, description="", example="600 mm")

    _height_is_quantity_validator = pyd.validator("height", allow_reuse=True)(validate_unit_factory("m"))
    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))

    # Nested specs:
    IntegratedDoorsOpeningAssemblies: IntegratedDoorsOpeningAssembliesV1 | None = None
    MetalDoorAndFrames: MetalDoorAndFramesV1 | None = None
    SpecialtyDoorsAndFrames: SpecialtyDoorsAndFramesV1 | None = None
    WoodDoors: WoodDoorsV1 | None = None


class EntrancesV1(BaseOpenEpdHierarchicalSpec):
    """Entrances performance specification."""

    _EXT_VERSION = "1.0"


class GlazingV1(BaseOpenEpdHierarchicalSpec):
    """Glazing performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    FenestrationParts: FenestrationPartsV1 | None = None
    GlassPanes: GlassPanesV1 | None = None
    NAFSFenestration: NAFSFenestrationV1 | None = None
    InsulatingGlazingUnits: InsulatingGlazingUnitsV1 | None = None


class StorefrontsV1(BaseOpenEpdHierarchicalSpec):
    """Storefronts performance specification."""

    _EXT_VERSION = "1.0"


class TranslucentWallAndRoofAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """Translucent wall and roof assemblies performance specification."""

    _EXT_VERSION = "1.0"


class WindowWallAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """Window wall assemblies performance specification."""

    _EXT_VERSION = "1.0"


class OpeningsV1(BaseOpenEpdHierarchicalSpec):
    """Openings performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="80 mm")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))

    # Nested specs:
    CurtainWalls: CurtainWallsV1 | None = None
    DoorsAndFrames: DoorsAndFramesV1 | None = None
    Entrances: EntrancesV1 | None = None
    Glazing: GlazingV1 | None = None
    Storefronts: StorefrontsV1 | None = None
    TranslucentWallAndRoofAssemblies: TranslucentWallAndRoofAssembliesV1 | None = None
    WindowWallAssemblies: WindowWallAssembliesV1 | None = None
