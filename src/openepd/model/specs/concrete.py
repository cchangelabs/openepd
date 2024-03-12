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
from typing import Literal

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import OpenEPDUnit
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, BaseOpenEpdSpec
from openepd.model.validation.common import together_validator
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, PressureMPaStr, validate_unit_factory


class AciExposureClass(StrEnum):
    """
    American Concrete Institute concrete exposure classes.

      * `aci.F0` - Concrete not subjected to freezing-and-thawing cycles
      * `aci.F1` - Concrete experiences freezing-and-thawing cycles with limited exposure to water
      * `aci.F2` - Concrete exposed to freezing-and-thawing cycles with frequent exposure to water
      * `aci.F3` - Concrete exposed to freezing-and-thawing cycles with continual exposure to water
                    and exposure to deicing chemicals
      * `aci.S0` - Exposed to <150 ppm of SO4 in water and <0.1% SO4 in soil
      * `aci.S1` - Exposed to <1500 ppm of SO4 in water and <0.2% SO4 in soil
      * `aci.S2` - Exposed to <10000 ppm of SO4 in water and <2% SO4 in soil
      * `aci.S3` - Exposed to >10000 ppm of SO4 in water or >2% SO4 in soil

      * `aci.C1` - Concrete in contact with moisture, but the external source of chloride does not reach it.
      * `aci.C2` - Concrete subjected to moisture and an external source of chlorides such as deicing chemicals,
                    salt, brackish water, seawater, or spray from these sources.
      * `aci.W0` - Concrete dry in service
      * `aci.W1` - Concrete in contact with water, no requirement for low permeability
      * `aci.W2` - Concrete in contact with water where low permeability is required
    """

    F0 = "aci.F0"
    F1 = "aci.F1"
    F2 = "aci.F2"
    F3 = "aci.F3"
    S0 = "aci.S0"
    S1 = "aci.S1"
    S2 = "aci.S2"
    S3 = "aci.S3"
    C1 = "aci.C1"
    C2 = "aci.C2"
    W0 = "aci.W0"
    W1 = "aci.W1"
    W2 = "aci.W2"


class CsaExposureClass(StrEnum):
    """
    Canadian Standard Association concrete exposure classes.

      * `csa.C-XL` - Structurally reinforced concrete exposed to chlorides or other severe environment with or without
                     freezing and thawing conditions, with higher durability performance expectations than the C-1, A-1
                     or S-1 classes.

      * `csa.C-1` - Structurally reinforced concrete exposed to chlorides with or without freezing and thawing conditions.
                    Examples: bridge decks, parking decks and ramps, portions of marine structures located within the tidal
                    and splash zones, concrete exposed to seawater spray, and salt water pools.
      * `csa.C-2` - Non-structurally reinforced (i.e. plain) concrete exposed to chlorides and freezing and thawing.
                    Examples: garage floors, porches, steps, pavements, sidewalks curbs and gutters.
      * `csa.C-3` - Continuously submerged concrete exposed to chlorides but not to freezing and thawing.
                    Example: underwater portions of marine structures.
      * `csa.C-4` - Non-structurally reinforced concrete exposed to chlorides but not to freezing and thawing.
                    Examples: underground parking slabs on grade.

      * `csa.F-1` - Concrete exposed to freezing and thawing in a saturated condition but not to chlorides.
                    Examples: pool decks, patios, tennis courts, freshwater pools and fresh water control structures.
      * `csa.F-2` - Concrete in an unsaturated condition exposed to freezing and thawing but not to chlorides.
                    Examples: exterior walls and columns.

      * `csa.N` - Concrete not exposed to chlorides nor to freezing and thawing.
                  Examples: footings and interior slabs, walls and columns.

      * `csa.A-1` - Structurally reinforced concrete exposed to severe manure and/or silage gases, with or without
                    freeze-thaw exposure. Concrete exposed to the vapour above municipal sewage or industrial effluent,
                    where hydrogen sulphide gas may be generated.
                    Examples: reinforced beams, slabs, and columns over manure pits and silos, canals, and pig slats;
                    and access holes, enclosed chambers and pipes that are partially filled with effluents.
      * `csa.A-2` - Structurally reinforced concrete exposed to moderate to severe manure and/or silage gases and liquids,
                    with or without freeze-thaw exposure.
                    Examples: reinforced walls in exterior manure tanks, silos and feed bunkers, and exterior slabs.
      * `csa.A-3` - Structurally reinforced concrete exposed to moderate to severe manure and/or silage gases and liquids,
                    with or without freeze-thaw exposure in a continuously submerged condition. Concrete continuously
                    submerged in municipal or industrial effluents.
                    Examples: interior gutter walls, beams, slabs and columns; sewage pipes that are continuously full
                    (e.g. force mains); and submerged portions of sewage treatment structures.
      * `csa.A-4` - Non-structurally reinforced concrete exposed to moderate manure and/or silage gases and liquids, without
                    freeze-thaw exposure.
                    Examples: interior slabs on grade.

      * `csa.S-1` - Concrete subjected to very severe sulphate exposures.
                    Exposed to >10000 ppm of SO4 in water or >2% SO4 in soil
      * `csa.S-2` - Concrete subjected to severe sulphate exposure.
                    Exposed to <10000 ppm of SO4 in water and <2% SO4 in soil
      * `csa.S-3` - Concrete subjected to moderate sulphate exposure.
                    Exposed to <1500 ppm of SO4 in water and <0.2% SO4 in soil
    """

    C_XL = "csa.C-XL"
    C_1 = "csa.C-1"
    C_2 = "csa.C-2"
    C_3 = "csa.C-3"
    C_4 = "csa.C-4"
    F_1 = "csa.F-1"
    F2 = "csa.F-2"
    N = "csa.N"
    S_1 = "csa.S-1"
    S_2 = "csa.S-2"
    S_3 = "csa.S-3"
    A_1 = "csa.A-1"
    A_2 = "csa.A-2"
    A_3 = "csa.A-3"
    A_4 = "csa.A-4"


class EnExposureClass(StrEnum):
    """
    EN 206 Class (Europe).

    European Standard concrete exposure classes.

      * `en206.X0` - No risk of corrosion or attack.

      Corrosion induced by carbonation.

      * `en206.XC1` - Dry or permanently wet.
      * `en206.XC2` - Wet, rarely dry.
      * `en206.XC3` - Moderate humidity.
      * `en206.XC4` - Cyclic wet and dry.

      Corrosion induced by chlorides from sea water.

      * `en206.XS1` - Exposed to airborne salt but not in direct contact with sea water.
      * `en206.XS2` - Permanently submerged.
      * `en206.XS3` - Tidal, splash and spray zones.

      Corrosion induced by chlorides other than from sea water.

      * `en206.XD1` - Moderate humidity.
      * `en206.XD2` - Wet, rarely dry.
      * `en206.XD3` - Cyclic wet and dry.

      Freeze/thaw attack with or without de-icing agents.

      * `en206.XF1` - Moderate water saturation, without deicing agent.
      * `en206.XF2` - Moderate water saturation, with deicing agent.
      * `en206.XF3` - High water saturation, without de-icing agent.
      * `en206.XF4` - High water saturation, with de-icing agent or sea water.

      Chemical attack.

      * `en206.XA1` - Slightly aggressive chemical environment.
      * `en206.XA2` - Moderately aggressive chemical environment.
      * `en206.XA3` - Highly aggressive chemical environment.

    """

    en206_X0 = "en206.X0"
    en206_XC1 = "en206.XC1"
    en206_XC2 = "en206.XC2"
    en206_XC3 = "en206.XC3"
    en206_XC4 = "en206.XC4"
    en206_XS1 = "en206.XS1"
    en206_XS2 = "en206.XS2"
    en206_XS3 = "en206.XS3"
    en206_XD1 = "en206.XD1"
    en206_XD2 = "en206.XD2"
    en206_XD3 = "en206.XD3"
    en206_XF1 = "en206.XF1"
    en206_XF2 = "en206.XF2"
    en206_XF3 = "en206.XF3"
    en206_XF4 = "en206.XF4"
    en206_XA1 = "en206.XA1"
    en206_XA2 = "en206.XA2"
    en206_XA3 = "en206.XA3"


class CmuWeightClassification(StrEnum):
    """Concrete Masonry Unit weight classification."""

    Normal = "Normal"
    """Normal weight CMU has a density of 125 lbs/cu. ft."""
    Medium = "Medium"
    """Medium weight CMU has a density of 105-125 lbs/cu. ft."""
    Light = "Light"
    """Lightweight CMU has a density less than 105 lbs/cu. ft."""


class CmuOptions(BaseOpenEpdSchema):
    """Concrete Masonry Unit options."""

    load_bearing: bool | None = pyd.Field(
        description="Load-Bearing. CMUs intended to be loadbearing, rather than simply cosmetic",
        example=True,
        default=None,
    )
    aerated_concrete: bool | None = pyd.Field(
        description="AAC Aerated Concrete. Aerated Autoclaved Concrete, a foam concrete.", example=True, default=None
    )
    insulated: bool | None = pyd.Field(
        description="Insulated. CMUs with integral insulation", example=True, default=None
    )
    sound_absorbing: bool | None = pyd.Field(
        description="Sound Absorbing. CMUs structured for sound absorbtion", example=True, default=None
    )
    white: bool | None = pyd.Field(
        description="White. CMU using white cement and light-colored aggregate", example=True, default=None
    )
    recycled_aggregate: bool | None = pyd.Field(
        description="Recycled aggregate. CMU using primarily reycled aggregates", example=True, default=None
    )
    groundface: bool | None = pyd.Field(
        description="Ground Face. Ground or Honed facing, typically for improved appearance", example=True, default=None
    )
    splitface: bool | None = pyd.Field(
        description="Splitface. Rough surface texture via splitting; aggregate can be seen", example=True, default=None
    )
    smoothface: bool | None = pyd.Field(
        description="Smooth Face. Standard smooth-faced blocks", example=True, default=None
    )
    slumpstone: bool | None = pyd.Field(
        description="Slumpstone. A slightly rounded, random distortion with the look of rustic adobe.",
        example=True,
        default=None,
    )


class ConcreteTypicalApplication(BaseOpenEpdSpec):
    """Typical Application for Concrete."""

    fnd: bool | None = pyd.Field(
        description="Foundation. Typically used in direct contact with soil, e.g. footings, piles, mass concrete, "
        "mat foundations, and similar applications.",
        example=True,
        default=None,
    )
    sog: bool | None = pyd.Field(
        description="Slab on Grade. Typically used in continuously supported horizontal "
        "applications e.g. slab on grade, topping slabs, sidewalks, and roadways.",
        example=True,
        default=None,
    )
    hrz: bool | None = pyd.Field(
        description="Elevated Horizontal. Typically used in elevated horizontal applications, either on metal deck or "
        "where soffit formwork must be removed, e.g. post-tension plates, rebar plates, beams and slabs, "
        "waffle slabs.",
        example=True,
        default=None,
    )
    vrt_wall: bool | None = pyd.Field(description="Vertical Wall.", example=True, default=None)
    vrt_column: bool | None = pyd.Field(description="Vertical Column.", example=True, default=None)
    vrt_other: bool | None = pyd.Field(
        description="Vertical Other. Typically used in vertical applications other than "
        "walls or columns, e.g. sloped surfaces where formwork is required "
        "on multiple faces.",
        example=True,
        default=None,
    )
    sht: bool | None = pyd.Field(
        description="Shotcrete. Pneumatically applied, without formwork on all sides.", example=True, default=None
    )
    cdf: bool | None = pyd.Field(
        description="Flowable Fill (CDF). Typically used to fill voids, backfill retaining "
        "walls, as a sub-base, and similar applications. Also called Controlled "
        "Density Fill (CDF) or Controlled Low Strength Materials (CLSM).",
        example=True,
        default=None,
    )
    sac: bool | None = pyd.Field(
        description="Typically used in concrete sidewalks and barrier curbs.", example=True, default=None
    )
    pav: bool | None = pyd.Field(description="Typically used in pervious concrete", example=True, default=None)
    oil: bool | None = pyd.Field(
        description="Concretes for use in creation, maintenance, and decommissioning of "
        "petroleum extraction wells and similar applications. Includes foamed "
        "cement; often called cement in the drilling industry. Differs from "
        "flowable fill and grout in that it contains no sand or other aggregates.",
        example=True,
        default=None,
    )
    grt: bool | None = pyd.Field(
        description="Cement grouting is a slurry that is placed as a flowable liquid. It is "
        "an effective material for filling and strengthening granular soils, "
        "voids in rocks, foundation underpinnings, and other underground voids. "
        "Also called structural grout, these materials typically impart"
        " significant strength to the system",
        example=True,
        default=None,
    )
    ota: bool | None = pyd.Field(
        description="Typical application not covered by other values.", example=True, default=None
    )


class CmuSpec(BaseOpenEpdSpec):
    """Standardized Concrete Masonry Unit-specific extension for OpenEPD."""

    strength: str = pyd.Field(description="Compressive strength", example="4000 psi")
    options: CmuOptions = pyd.Field(
        description="Options for CMU. List of true/false properties", default_factory=CmuOptions
    )


class Cementitious(BaseOpenEpdSchema):
    """List of cementitious materials, and proportion by mass."""

    opc: RatioFloat | None = pyd.Field(default=None, description="Ordinary Gray Portland Cement")
    wht: RatioFloat | None = pyd.Field(default=None, description="White Portland Cement")
    ggbs: RatioFloat | None = pyd.Field(default=None, description="Ground Granulated Blast Furnace Slag")
    flyAsh: RatioFloat | None = pyd.Field(default=None, description="Fly Ash, including types F, CL, and CH")
    siFume: RatioFloat | None = pyd.Field(default=None, description="Silica Fume")
    gg45: RatioFloat | None = pyd.Field(default=None, description="Ground Glass, 45um or smaller")
    natPoz: RatioFloat | None = pyd.Field(default=None, description="Natural pozzolan")
    mk: RatioFloat | None = pyd.Field(default=None, description="Metakaolin")
    CaCO3: RatioFloat | None = pyd.Field(default=None, description="Limestone")
    other: RatioFloat | None = pyd.Field(default=None, description="Other SCMs")


class TypicalApplication(BaseOpenEpdSchema):
    """Concrete typical application."""

    fnd: bool | None = pyd.Field(description="Foundation", default=None)
    sog: bool | None = pyd.Field(description="Slab on Grade", default=None)
    hrz: bool | None = pyd.Field(description="Elevated Horizontal", default=None)
    vrt_wall: bool | None = pyd.Field(description="Vertical Wall", default=None)
    vrt_column: bool | None = pyd.Field(description="Vertical Column", default=None)
    vrt_other: bool | None = pyd.Field(description="Vertical Other", default=None)
    sht: bool | None = pyd.Field(description="Shotcrete", default=None)
    cdf: bool | None = pyd.Field(description="Flowable Fill (CDF,default=None)", default=None)
    sac: bool | None = pyd.Field(description="Sidewalk and Curb", default=None)
    pav: bool | None = pyd.Field(description="Paving", default=None)
    oil: bool | None = pyd.Field(description="Oil Patch", default=None)
    grt: bool | None = pyd.Field(description="Cement Grout", default=None)
    ota: bool | None = pyd.Field(description="Other", default=None)


class ConcreteV1Options(BaseOpenEpdSchema):
    """Concrete options."""

    lightweight: bool | None = pyd.Field(description="Lightweight", default=None)
    plc: bool | None = pyd.Field(description="Portland Limestone Cement", default=None)
    scc: bool | None = pyd.Field(description="Self Compacting", default=None)
    finishable: bool | None = pyd.Field(description="Finishable", default=None)
    air: bool | None = pyd.Field(description="Air Entrainment", default=None)
    co2: bool | None = pyd.Field(description="CO2 Curing", default=None)
    white: bool | None = pyd.Field(description="White Cement", default=None)
    fiber_reinforced: bool | None = pyd.Field(description="Fiber reinforced", default=None)


class ReadyMixV1(BaseOpenEpdHierarchicalSpec):
    """Concretes to be mixed and then poured on-site."""

    _EXT_VERSION = "1.0"


class FlowableFillV1(BaseOpenEpdHierarchicalSpec):
    """
    Flowable fill is a slurry that is placed as a flowable liquid (high slump) and sets with no compaction.

    It is often used in tight or restricted access areas where placing and compacting
    fill is difficult. Applications include filling large voids such as abandoned underground storage
    tanks, basements, tunnels, mines, and sewers. It can also be used as paving sub-base, bridge
    abutment, and retaining wall backfill. Also called Controlled Density Fill (CDF) or Controlled
    Low Strength Materials (CLSMs). These materials typically have compressive strengths
    under 1200 psi.
    """

    _EXT_VERSION = "1.0"


class OilPatchV1(BaseOpenEpdHierarchicalSpec):
    """
    Concretes for use in petroleum extraction wells and similar applications.

    Includes foamed cement; often called cement in the drilling industry. Differs from
    flowable fill and grout in that it contains no sand or other aggregates.
    """

    _EXT_VERSION = "1.0"


class ConcretePavingV1(BaseOpenEpdHierarchicalSpec):
    """Concrete paving."""

    _EXT_VERSION = "1.0"


class ShotcreteV1(BaseOpenEpdHierarchicalSpec):
    """Concretes sprayed on a target."""

    _EXT_VERSION = "1.0"


class CementGroutV1(BaseOpenEpdHierarchicalSpec):
    """
    Cement grouting is a slurry that is placed as a flowable liquid.

    It is an effective material for filling and
    strengthening granular soils, voids in rocks, foundation underpinnings, and other underground voids. Also called
    structural grout, these materials typically impart significant compressive strength to the system.

    """

    _EXT_VERSION = "1.0"


class ConcreteV1(BaseOpenEpdHierarchicalSpec):
    """Concrete spec."""

    _EXT_VERSION = "1.0"

    strength_28d: PressureMPaStr | None = pyd.Field(
        default=None, example="30 MPa", description="Concrete strength after 28 days"
    )
    strength_early: PressureMPaStr | None = pyd.Field(
        default=None,
        example="30 MPa",
        description="A strength spec which is to be reached earlier than 28 days (e.g. 3d)",
    )
    strength_early_d: Literal[3, 7, 14] | None = pyd.Field(default=None, description="Test Day for the Early Strength")
    strength_late: PressureMPaStr | None = pyd.Field(
        default=None,
        example="30 MPa",
        description="A strength spec which is to be reached later than 28 days (e.g. 42d)",
    )
    strength_late_d: Literal[42, 56, 72, 96, 120] | None = pyd.Field(
        default=None, description="Test Day for the Late Strength"
    )
    slump: LengthMmStr | None = pyd.Field(description="Minimum test slump", example="40 mm", default=None)
    w_c_ratio: RatioFloat | None = pyd.Field(description="Ratio of water to cement", example=0.3, default=None)
    aci_exposure_classes: list[AciExposureClass] = pyd.Field(
        description=(AciExposureClass.__doc__ or "").lstrip(), default_factory=list
    )
    csa_exposure_classes: list[CsaExposureClass] = pyd.Field(
        description=(CsaExposureClass.__doc__ or "").lstrip(), default_factory=list
    )
    en_exposure_classes: list[EnExposureClass] = pyd.Field(
        description=(EnExposureClass.__doc__ or "").lstrip(), default_factory=list
    )
    cementitious: Cementitious | None = pyd.Field(
        default=None,
        description="List of cementitious materials, and proportion by mass. Each field is 0 to 1.",
    )
    application: TypicalApplication | None = pyd.Field(description="Typical Application", default=None)
    options: ConcreteV1Options | None = pyd.Field(description="Concrete options", default=None)

    # Nested specs
    ReadyMix: ReadyMixV1 | None = None
    FlowableFill: FlowableFillV1 | None = None
    OilPatch: OilPatchV1 | None = None
    ConcretePaving: ConcretePavingV1 | None = None
    Shotcrete: ShotcreteV1 | None = None
    CementGrout: CementGroutV1 | None = None

    _compressive_strength_unit_validator = pyd.validator("strength_28d", allow_reuse=True, check_fields=False)(
        validate_unit_factory(OpenEPDUnit.MPa)
    )
    _strength_early_unit_validator = pyd.validator("strength_early", allow_reuse=True)(
        validate_unit_factory(OpenEPDUnit.MPa)
    )
    _strength_late_unit_validator = pyd.validator("strength_late", allow_reuse=True)(
        validate_unit_factory(OpenEPDUnit.MPa)
    )

    @pyd.root_validator
    def _late_validator(cls, values):
        together_validator("strength_late", "strength_late_d", values)
        return values

    @pyd.root_validator
    def _early_validator(cls, values):
        together_validator("strength_early", "strength_early_d", values)
        return values


class PrecastConcreteV1(BaseOpenEpdHierarchicalSpec):
    """Precast Concrete spec."""

    _EXT_VERSION = "1.0"

    strength_28d: PressureMPaStr | None = pyd.Field(
        default=None, example="30 MPa", description="Concrete strength after 28 days"
    )

    lightweight: bool | None = pyd.Field(description="Lightweight", default=None)
    steel_mass_percentage: RatioFloat | None = pyd.Field(
        default=None,
        description="Percent of total mass that is steel reinforcement. Steel reinforcement "
        "substantially changes functional performance and usually adds substantial GWP "
        "per declared unit.",
    )

    insulated: bool | None = pyd.Field(description="Insulated", default=None)
    gfrc: bool | None = pyd.Field(description="Glass Fiber Reinforced Concrete", default=None)

    _compressive_strength_unit_validator = pyd.validator("strength_28d", allow_reuse=True)(
        validate_unit_factory(OpenEPDUnit.MPa)
    )
