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
from enum import StrEnum

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.numbers import PositiveInt, RatioFloat
from openepd.model.validation.quantity import HeatConductanceUCIStr, LengthMmStr, PressureMPaStr, QuantityStr


class SolarHeatGainMixin(BaseOpenEpdSchema):
    """Solar heat gain mixin."""

    solar_heat_gain: RatioFloat | None = pyd.Field(
        default=None,
        description="Solar heat gain, measured at a certain level of Differential Pressure.",
        example=0.3,
        le=1,
        ge=0,
    )


class GlazingOptionsMixin(BaseOpenEpdSchema):
    """Glazing options mixin."""

    low_emissivity: bool | None = pyd.Field(default=None, description="Low Emissivity coatings")
    electrochromic: bool | None = pyd.Field(
        default=None, description="Glazing with an electrically controllable solar heat gain and/or other properties."
    )
    acid_etched: bool | None = pyd.Field(
        default=None, description="Flat glass that has undergone a chemical etching process."
    )
    tempered: bool | None = pyd.Field(
        default=None,
        description="Consists of a single pane that has been heat-treated "
        "to give the glass increased impact resistance. Standard typically used in North America.",
    )
    toughened: bool | None = pyd.Field(
        default=None,
        description="Consists of a single pane that has been specially heat-treated to give the glass increased "
        "impact resistance. Standard typically used in Europe.",
    )

    laminated: bool | None = pyd.Field(
        default=None,
        description="Consists of at least two glass panes lying one on top of the other, with one or several layers "
        "of a tear-resistant, viscoelastic film positioned between the panes, which consist of polyvinyl "
        "butyral (PVB)",
    )
    fire_resistant: bool | None = pyd.Field(default=None, description="Fire resistant")
    fire_protection: bool | None = pyd.Field(
        default=None,
        description="Specifically tested for its ability to block flames and smoke, but not radiant heat. Ranges"
        " from specialty tempered products rated for ~20 minutes to glass ceramics rated up to 3 hours.",
    )
    pyrolytic_coated: bool | None = pyd.Field(
        default=None,
        description="At least one coating is applied in a pyrolytic process, typically during float glass production.",
    )
    sputter_coat: bool | None = pyd.Field(
        default=None, description="At least one coating is applied using sputter (vacuum deposition) coating."
    )


class GlassPanesMixin(BaseOpenEpdSchema):
    """Glass panes mixin."""

    glass_panes: PositiveInt | None = pyd.Field(
        default=None,
        description="Number of panes, each separated by a cavity. A 3 pane unit has 2 cavities. example: 3",
        example=3,
    )


class DPRatingMixin(BaseOpenEpdSchema):
    """Differential pressure rating mixin."""

    dp_rating: PressureMPaStr | None = pyd.Field(
        default=None, description="Maximum Differential Pressure, a measure of wind tolerance.", example="75 psf"
    )


class AirInfiltrationMixin(BaseOpenEpdSchema):
    """Air infiltration mixin."""

    air_infiltration: QuantityStr | None = pyd.Field(
        default=None,
        description="Air infiltration, measured at a certain level of Differential Pressure.",
        example="0.3 m3/(sec * m2)",
    )


class AssemblyUFactorMixin(BaseOpenEpdSchema):
    """Assembly U factor mixin."""

    assembly_u_factor: HeatConductanceUCIStr | None = pyd.Field(
        default=None,
        description="Weighted average conductance of heat across assembly (including frame).",
        example="0.3 UCI",
    )


class GlassIntendedApplicationMixin(BaseOpenEpdSchema):
    """Glass intended application mixin."""

    glazing_intended_application_curtain_wall: bool | None = pyd.Field(
        default=None, description="Intended for curtain walls. Relevant for IGUs."
    )
    glazing_intended_application_r_windows: bool | None = pyd.Field(
        default=None,
        description="Intended for residential (NAFS 'R') and similar windows, doors, or skylights. Relevant for IGUs.",
    )
    glazing_intended_application_lc_windows: bool | None = pyd.Field(
        default=None, description="Intended for light commercial (NAFS 'LC') and similar windows. Relevant for IGUs."
    )
    glazing_intended_application_cw_windows: bool | None = pyd.Field(
        default=None, description="Intended for commercial (NAFS 'CW') and similar windows. Relevant for IGUs."
    )
    glazing_intended_application_aw_windows: bool | None = pyd.Field(
        default=None, description="Intended for architectural (NAFS 'AW') and similar windows. Relevant for IGUs."
    )
    glazing_intended_application_storefronts: bool | None = pyd.Field(
        default=None, description="Intended for Storefronts and similar applications. Relevant for IGUs."
    )
    glazing_intended_application_glazed_doors: bool | None = pyd.Field(
        default=None, description="Intended for Glazed Doors and similar applications. Relevant for IGUs."
    )
    glazing_intended_application_unit_skylights: bool | None = pyd.Field(
        default=None, description="Intended for Unit Skylights and similar applications. Relevant for IGUs."
    )
    glazing_intended_application_sloped_skylights: bool | None = pyd.Field(
        default=None,
        description="Intended for sloped glazing, and architectural skylights, and similar. Relevant for IGUs.",
    )
    glazing_intended_application_other: bool | None = pyd.Field(
        default=None, description="Intended for other application not listed. Relevant for IGUs."
    )


class ThermalSeparationEnum(StrEnum):
    """Thermal separation enum."""

    ALUMINIUM = "Aluminium"
    STEEL = "Steel"
    THERMALLY_IMPROVED_METAL = "Thermally Improved Metal"
    THERMALLY_BROKEN_METAL = "Thermally Broken Metal"
    NON_METAL = "Nonmetal"


class ThermalSeparationMixin(BaseOpenEpdSchema):
    """Thermal separation mixin."""

    thermal_separation: ThermalSeparationEnum | None = pyd.Field(default=None, description="Thermal separation.")


class HurricaneResistantMixin(BaseOpenEpdSchema):
    """Hurricane resistant mixin."""

    hurricane_resistant: bool | None = pyd.Field(
        default=None, description="The product has been designed to resist windborne debris."
    )


class NAFSPerformanceGrade(StrEnum):
    """NAFS Performance Grade enum."""

    GRADE_15_PSF = "15 psf"
    GRADE_20_PSF = "20 psf"
    GRADE_25_PSF = "25 psf"
    GRADE_30_PSF = "30 psf"
    GRADE_35_PSF = "35 psf"
    GRADE_40_PSF = "40 psf"
    GRADE_45_PSF = "45 psf"
    GRADE_50_PSF = "50 psf"
    GRADE_55_PSF = "55 psf"
    GRADE_60_PSF = "60 psf"
    GRADE_65_PSF = "65 psf"
    GRADE_70_PSF = "70 psf"
    GRADE_75_PSF = "75 psf"
    GRADE_80_PSF = "80 psf"
    GRADE_85_PSF = "85 psf"
    GRADE_90_PSF = "90 psf"
    GRADE_95_PSF = "95 psf"
    GRADE_100_PSF = "100 psf"
    GRADE_105_PSF = "105 psf"
    GRADE_110_PSF = "110 psf"
    GRADE_115_PSF = "115 psf"
    GRADE_120_PSF = "120 psf"
    GRADE_125_PSF = "125 psf"
    GRADE_130_PSF = "130 psf"
    GRADE_135_PSF = "135 psf"
    GRADE_140_PSF = "140 psf"
    GRADE_145_PSF = "145 psf"
    GRADE_150_PSF = "150 psf"
    GRADE_155_PSF = "155 psf"
    GRADE_160_PSF = "160 psf"
    GRADE_165_PSF = "165 psf"
    GRADE_170_PSF = "170 psf"
    GRADE_175_PSF = "175 psf"
    GRADE_180_PSF = "180 psf"
    GRADE_185_PSF = "185 psf"
    GRADE_190_PSF = "190 psf"
    GRADE_195_PSF = "195 psf"
    GRADE_200_PSF = "200 psf"
    GRADE_205_PSF = "205 psf"
    GRADE_210_PSF = "210 psf"


class SpacerEnum(StrEnum):
    """Spacer enum."""

    ALUMINIUM = "Aluminium"
    STAINLESS_STEEL = "Stainless steel"
    PLASTIC_AND_STAINLESS_STEEL = "Plastic and stainless steel"
    THERMOPLASTIC = "Thermoplastic"
    FOAM = "Foam"
    STAINLESS_STEEL_AND_TIN = "Stainless steel or tin plate U-channel"
    PLASTIC = "Plastic"


class FenestrationHardwareFunctionEnum(StrEnum):
    """Fenestration hardware function enum."""

    LOCK = "Lock"
    HINGE = "Hinge"
    HANDLE = "Handle"
    OPERATOR = "Operator"
    BALANCE = "Balance"
    OTHER = "Other"


class FrameMaterialEnum(StrEnum):
    """Framing material enum."""

    VINYL = "Vinyl"
    ALUMINIUM = "Aluminium"
    STEEL = "Steel"
    WOOD = "Wood"
    FIBERGLASS = "Fiberglass"
    COMPOSITE = "Composite"
    NONE = "None"
    OTHER = "Other"


class NAFSFenestrationV1(
    GlassPanesMixin,
    DPRatingMixin,
    AirInfiltrationMixin,
    SolarHeatGainMixin,
    AssemblyUFactorMixin,
    ThermalSeparationMixin,
    GlazingOptionsMixin,
    HurricaneResistantMixin,
    BaseOpenEpdHierarchicalSpec,
):
    """NAFS Fenestration V1 spec."""

    _EXT_VERSION = "1.0"
    nafs_performance_class_r: bool | None = pyd.Field(
        default=None, description="Residential; commonly used in one- and two-family dwellings."
    )
    nafs_performance_class_lc: bool | None = pyd.Field(
        default=None,
        description="Light Commercial: commonly used in low-rise and mid-rise multi-family dwellings and other "
        "buildings where larger sizes and higher loading requirements are expected.",
    )
    nafs_performance_class_cw: bool | None = pyd.Field(
        default=None,
        description="Commercial Window: commonly used in low-rise and mid-rise buildings where larger sizes, higher "
        "loading requirements, limits on deflection, and heavy use are expected.",
    )
    nafs_performance_class_aw: bool | None = pyd.Field(
        default=None,
        description="Architectural Window: commonly used in high-rise and mid-rise buildings to meet increased "
        "loading requirements and limits on deflection, and in buildings where frequent and extreme use "
        "of the fenestration products is expected.",
    )

    nafs_performance_grade: NAFSPerformanceGrade | None = pyd.Field(
        default=None,
        description="NAFS Performance Grade. The NAFS Performance Grade is a number that represents the performance "
        "of the glazing product. The higher the number, the better the performance. The NAFS Performance "
        "Grade is calculated using the NAFS Performance Class, the NAFS Performance Index, and the NAFS "
        "Performance Factor. While it is expressed as pressure, there are specific values which are "
        "allowed. The values are listed in the enum.",
    )


class InsulatingGlazingUnitsV1(
    GlassPanesMixin,
    DPRatingMixin,
    AirInfiltrationMixin,
    SolarHeatGainMixin,
    GlazingOptionsMixin,
    HurricaneResistantMixin,
    GlassIntendedApplicationMixin,
    BaseOpenEpdHierarchicalSpec,
):
    """Insulating glazing units V1 spec."""

    _EXT_VERSION = "1.0"

    cog_u_factor: HeatConductanceUCIStr | None = pyd.Field(
        default=None, description="Conductance of heat at center of glass.", example="0.3 UCI"
    )
    spacer: SpacerEnum | None = pyd.Field(default=None, description="Spacer material for Integrated Glass Unit.")


class FenestrationFramingV1(GlassIntendedApplicationMixin, BaseOpenEpdHierarchicalSpec):
    """Fenestration framing V1 spec."""

    _EXT_VERSION = "1.0"

    frame_material: FrameMaterialEnum | None = pyd.Field(default=None, description="Frame material.")


class FenestrationHardwareV1(BaseOpenEpdHierarchicalSpec):
    """Fenestration hardware V1 spec."""

    _EXT_VERSION = "1.0"

    hardware_function: FenestrationHardwareFunctionEnum | None = pyd.Field(
        default=None, description="Hardware function."
    )


class FenestrationPartsV1(GlassIntendedApplicationMixin, BaseOpenEpdHierarchicalSpec):
    """Fenestration parts V1 spec."""

    _EXT_VERSION = "1.0"

    FenestrationHardware: FenestrationHardwareV1 | None = pyd.Field(
        default=None, title="FenestrationHardwareV1", description="Fenestration hardware V1 spec."
    )
    FenestrationFraming: FenestrationFramingV1 | None = pyd.Field(
        default=None, title="FenestrationFramingV1", description="Fenestration framing V1 spec."
    )


class ProcessedNonInsulatedGlassPanesV1(
    GlassPanesMixin, SolarHeatGainMixin, GlazingOptionsMixin, BaseOpenEpdHierarchicalSpec
):
    """Processed non-insulated glass panes V1 spec."""

    _EXT_VERSION = "1.0"


class FlatGlassPanesV1(BaseOpenEpdHierarchicalSpec):
    """Flat glass panes."""

    _EXT_VERSION = "1.0"
    flat_glass_panes_thickness: LengthMmStr | None = pyd.Field(
        default=None, description="Thickness of the flat glass panes.", example="8 mm"
    )


class GlassPanesV1(BaseOpenEpdHierarchicalSpec):
    """Glass panes V1 spec."""

    _EXT_VERSION = "1.0"

    ProcessedNonInsulatedGlassPanes: ProcessedNonInsulatedGlassPanesV1 | None = pyd.Field(
        default=None,
        title="ProcessedNonInsulatedGlassPanesV1",
        description="Processed non-insulated glass panes V1 spec.",
    )
    FlatGlassPanes: FlatGlassPanesV1 | None = pyd.Field(
        default=None, title="FlatGlassPanes", description="Flat glass panes spec."
    )


class GlazingV1(BaseOpenEpdHierarchicalSpec):
    """Glazing V1 spec."""

    _EXT_VERSION = "1.0"
    thickness: str | None = pyd.Field(default=None, description="Thickness of the glazing.")
    GlassPanes: GlassPanesV1 | None = pyd.Field(default=None, title="GlassPanesV1", description="Glass panes V1 spec.")
    InsulatingGlazingUnits: InsulatingGlazingUnitsV1 | None = pyd.Field(
        default=None, title="InsulatingGlazingUnitsV1", description="Insulating glazing units V1 spec."
    )
    NAFSFenestration: NAFSFenestrationV1 | None = pyd.Field(
        default=None, title="NAFSFenestrationV1", description="NAFS Fenestration V1 spec."
    )
    FenestrationParts: FenestrationPartsV1 | None = pyd.Field(
        default=None, title="FenestrationPartsV1", description="Fenestration parts V1 spec."
    )
