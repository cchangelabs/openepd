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
    "AccessFlooringRangeV1",
    "AcousticalCeilingsRangeV1",
    "BackingAndUnderlayRangeV1",
    "CarpetRangeV1",
    "CeilingPanelRangeV1",
    "CementBoardRangeV1",
    "CeramicTileRangeV1",
    "DeckingBoardsRangeV1",
    "FinishesRangeV1",
    "FlooringRangeV1",
    "GaugedTileRangeV1",
    "GlassFiberReinforcedGypsumFabricationsRangeV1",
    "GlassTileRangeV1",
    "GypsumRangeV1",
    "GypsumSupportsRangeV1",
    "LaminateRangeV1",
    "MirrorsRangeV1",
    "OtherFlooringRangeV1",
    "PaintByAreaRangeV1",
    "PaintByMassRangeV1",
    "PaintByVolumeRangeV1",
    "PaintingAndCoatingRangeV1",
    "PlasterRangeV1",
    "ResilientFlooringRangeV1",
    "TilingRangeV1",
    "WallBaseRangeV1",
    "WallFinishesRangeV1",
    "WoodFlooringRangeV1",
)


from openepd.compat.pydantic import pyd
from openepd.model.common import RangeAmount, RangeFloat, RangeInt, RangeRatioFloat
from openepd.model.org import OrgRef
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    AllFabrication,
    CarpetFormFactor,
    CarpetIntendedApplication,
    CarpetManufactureType,
    CarpetYarnType,
    CeilingPanelCoreMaterial,
    CeilingPanelFireRating,
    CementBoardThickness,
    DeckingBoardMaterial,
    GypsumFacing,
    GypsumFireRating,
    GypsumThickness,
    PlasterComposition,
    ResilientFlooringFormFactor,
    ResilientFlooringMaterial,
    ResilientFlooringThickness,
    SawnTimberSpecies,
    VinylSheetConstruction,
    WallBaseMaterial,
    WoodFlooringFabrication,
    WoodFlooringTimberSpecies,
)
from openepd.model.specs.range.mixins.access_flooring_mixin import AccessFlooringRangeMixin
from openepd.model.validation.quantity import (
    AmountRangeGWP,
    AmountRangeLengthMm,
    AmountRangeRFactor,
    AmountRangeYarnWeight,
)


class AccessFlooringRangeV1(BaseOpenEpdHierarchicalSpec, AccessFlooringRangeMixin):
    """
    Elevated floor system built on top of concrete slab surface.

    It thereby creates a hidden void between the two floors that is used for the passage of mechanical and electrical
    services. The system consists of panels, stringers, and pedestals.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CarpetRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Textile Floor Coverings.

    Range version.
    """

    _EXT_VERSION = "1.0"

    length: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    width: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    intended_application: list[CarpetIntendedApplication] | None = pyd.Field(default=None, description="")
    manufacture_type: list[CarpetManufactureType] | None = pyd.Field(default=None, description="")
    form_factor: list[CarpetFormFactor] | None = pyd.Field(default=None, description="")
    yarn_weight: AmountRangeYarnWeight | None = pyd.Field(default=None, description="")
    yarn_type: list[CarpetYarnType] | None = pyd.Field(default=None, description="")
    fire_radiant_panel_rating_astme648: str | None = pyd.Field(default=None, description="")
    fire_smoke_density_rating_astme648: str | None = pyd.Field(default=None, description="")
    voc_emissions: str | None = pyd.Field(default=None, description="")
    cushioned: bool | None = pyd.Field(default=None, description="")
    bleachable: bool | None = pyd.Field(default=None, description="")
    gwp_factor_base: AmountRangeGWP | None = pyd.Field(default=None, description="")
    gwp_factor_yarn: AmountRangeGWP | None = pyd.Field(default=None, description="")


class LaminateRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Laminate flooring.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherFlooringRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other not yet classified kinds of flooring.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ResilientFlooringRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Resilient floor products.

    Includes vinyl, rubber, linoleum, composition cork, etc. in modular square or rectangle shapes.

    Range version.
    """

    _EXT_VERSION = "1.0"

    length: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    width: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    form_factor: list[ResilientFlooringFormFactor] | None = pyd.Field(default=None, description="")
    material: list[ResilientFlooringMaterial] | None = pyd.Field(default=None, description="")
    sheet_construction: list[VinylSheetConstruction] | None = pyd.Field(default=None, description="")
    wear_layer: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    delta_iic: RangeFloat | None = pyd.Field(default=None, description="")
    thickness: list[ResilientFlooringThickness] | None = pyd.Field(default=None, description="")
    sport_flooring: bool | None = pyd.Field(default=None, description="")
    conductive_flooring: bool | None = pyd.Field(default=None, description="")
    zwtl: bool | None = pyd.Field(default=None, description="")
    floor_score: bool | None = pyd.Field(default=None, description="")
    nsf332: bool | None = pyd.Field(default=None, description="")


class WallBaseRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wall base made to help cover gaps between wall and vinyl, rubber, wood, or tile flooring.

    Range version.
    """

    _EXT_VERSION = "1.0"

    wall_base_material: list[WallBaseMaterial] | None = pyd.Field(default=None, description="")


class WoodFlooringRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wood flooring for interior applications.

    Includes hardwood strip and plank flooring, engineered hardwood flooring, wood parquet flooring, coordinated
    transitions, and molding pieces.

    Range version.
    """

    _EXT_VERSION = "1.0"

    forest_practices_certifiers: list[OrgRef] | None = None
    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    timber_species: list[WoodFlooringTimberSpecies] | None = pyd.Field(default=None, description="")
    fabrication: list[WoodFlooringFabrication] | None = pyd.Field(default=None, description="")


class AcousticalCeilingsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Acoustical ceiling panels.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")


class CeramicTileRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Ceramic tiles, including porcelain, quarry, pressed floor tile, wall tile, mosaic tile, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    porcelain: bool | None = pyd.Field(
        default=None, description="A dense and durable ceramic tile made from fine porcelain clay."
    )
    quarry: bool | None = pyd.Field(
        default=None,
        description="A type of unglazed ceramic tile made from natural clay with a slightly rough texture.",
    )
    pressed_floor_tile: bool | None = pyd.Field(
        default=None,
        description="A durable and low-maintenance type of tile made by compressing clay or other materials at high pressure.",
    )
    wall_tile: bool | None = pyd.Field(
        default=None,
        description="A decorative tile designed for use on vertical surfaces such as walls or backsplashes.",
    )
    mosaic_tile: bool | None = pyd.Field(
        default=None,
        description="A small decorative tile made of glass, stone, or ceramic, arranged in a pattern to create a design.",
    )
    specialty: bool | None = pyd.Field(
        default=None,
        description="A unique and customized type of tile, often made from unconventional materials or with specialized designs or finishes.",
    )


class GaugedTileRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Specially manufactured porcelain tile with extra-large panels/slabs.

    Manufactured to a specific thickness ranging from 2-20 mm.

    Range version.
    """

    _EXT_VERSION = "1.0"

    tile_panels: bool | None = pyd.Field(
        default=None,
        description="Large-format porcelain or natural stone tiles that are typically over 3 feet in length and width, designed for use in floor and wall installations to create a seamless and uninterrupted appearance.",
    )
    tile_pavers: bool | None = pyd.Field(
        default=None,
        description="Thick and durable porcelain or natural stone tiles that are commonly used in outdoor applications, such as patios, walkways, and driveways, due to their high resistance to weather and wear.",
    )


class GlassTileRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Glass Tiles.

    Range version.
    """

    _EXT_VERSION = "1.0"

    regular: bool | None = pyd.Field(
        default=None,
        description="Glass tile that is typically square or rectangular in shape, and used for a variety of decorative applications, such as kitchen backsplashes, shower walls, and accent borders.",
    )
    glass_mosaic: bool | None = pyd.Field(
        default=None,
        description="A small, decorative glass tile made in a variety of shapes and colors, used for intricate designs and patterns on walls, floors, and other surfaces.",
    )
    miniature_mosaic: bool | None = pyd.Field(
        default=None,
        description="Glass mosaic tile that is smaller in size than regular glass mosaic tile, often used for intricate details and designs in backsplashes, shower walls, and decorative accents.",
    )
    large_format: bool | None = pyd.Field(
        default=None,
        description="Glass tile that is larger in size than regular glass tile, often used to create a dramatic and modern effect in commercial and residential spaces.",
    )


class GypsumSupportsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Supports for suspended and furred gypsum wall and ceiling assemblies.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FlooringRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    General category - finishes for floors.

    Range version.
    """

    _EXT_VERSION = "1.0"

    AccessFlooring: AccessFlooringRangeV1 | None = None
    Carpet: CarpetRangeV1 | None = None
    Laminate: LaminateRangeV1 | None = None
    OtherFlooring: OtherFlooringRangeV1 | None = None
    ResilientFlooring: ResilientFlooringRangeV1 | None = None
    WallBase: WallBaseRangeV1 | None = None
    WoodFlooring: WoodFlooringRangeV1 | None = None


class CeilingPanelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Acoustical and other specialty ceiling panels.

    Range version.
    """

    _EXT_VERSION = "1.0"

    fire_rating: list[CeilingPanelFireRating] | None = pyd.Field(default=None, description="")
    core_material: list[CeilingPanelCoreMaterial] | None = pyd.Field(default=None, description="")
    nrc: RangeRatioFloat | None = pyd.Field(
        default=None, description="Noise Reduction Coefficient (NRC) or Sound Absorbtion Average (SAA) per ASTM C423"
    )
    cac: RangeInt | None = pyd.Field(default=None, description="Ceiling Attenuation Class (CAC) per ASTM E1414")
    AcousticalCeilings: AcousticalCeilingsRangeV1 | None = None


class BackingAndUnderlayRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious, glass-mat faced gypsum, and fibered gypsum backing boards to support finish materials.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CementBoardRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Hard cementitious boards, typically used as a tile backer.

    Range version.
    """

    _EXT_VERSION = "1.1"

    thickness: list[CementBoardThickness] | None = pyd.Field(default=None, description="")


class TilingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Decorative building materials that includes a variety of ceramic, porcelain, and glass tiles.

    Used for covering and enhancing surfaces such as floors, walls, and countertops.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    flooring: bool | None = pyd.Field(default=None, description="Tiling intended for walking.")
    wall_finish: bool | None = pyd.Field(
        default=None,
        description="A decorative tile designed for use on vertical surfaces such as walls or backsplashes.",
    )
    cladding: bool | None = pyd.Field(
        default=None,
        description="Tiling for exterior use, primarily used for the walls of buildings and structures, providing a protective and decorative layer that enhances the aesthetic appearance and weather resistance of the underlying structure.",
    )
    other: bool | None = pyd.Field(
        default=None, description="Tiling used as countertops, ceilings, furnishings, hardscapes etc."
    )
    residential_only: bool | None = pyd.Field(
        default=None,
        description="All commercial tile can also be used in residential applications, but the opposite may not be true. This selection allows to filter out tiling that is not intended for commercial applications.",
    )
    reinforced: bool | None = pyd.Field(
        default=None, description="Steel-reinforced ceramic tiles or tiles with other special reinforcing technology."
    )
    total_recycled_content: RangeRatioFloat | None = pyd.Field(
        default=None,
        description="Proportion of this product that is sourced from recycled content. Pre-consumer recycling is given a 50% weighting, 100% for post-consumer, by mass.",
    )
    post_consumer_recycled_content: RangeRatioFloat | None = pyd.Field(
        default=None,
        description="Proportion of this product that is sourced from post-consumer recycled content, by mass.",
    )
    CeramicTile: CeramicTileRangeV1 | None = None
    GaugedTile: GaugedTileRangeV1 | None = None
    GlassTile: GlassTileRangeV1 | None = None


class DeckingBoardsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Decking boards provide the finished surface of a deck and support the weight of people and furniture.

    Range version.
    """

    _EXT_VERSION = "1.0"

    forest_practices_certifiers: list[OrgRef] | None = None
    timber_species: list[SawnTimberSpecies] | None = pyd.Field(default=None, description="")
    fabrication: list[AllFabrication] | None = pyd.Field(default=None, description="")
    weather_exposed: bool | None = pyd.Field(default=None, description="")
    fire_retardant: bool | None = pyd.Field(default=None, description="")
    decay_resistant: bool | None = pyd.Field(default=None, description="")
    material: list[DeckingBoardMaterial] | None = pyd.Field(default=None, description="")


class GlassFiberReinforcedGypsumFabricationsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Gypsum with integrated glass fiber reinforcement, which may be fabricated in complex shapes or as a board.

    Range version.
    """

    _EXT_VERSION = "1.0"


class GypsumRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Gypsum board used for interior walls, ceilings, and similar applications.

    Range version.
    """

    _EXT_VERSION = "1.1"

    fire_rating: list[GypsumFireRating] | None = pyd.Field(default=None, description="")
    thickness: list[GypsumThickness] | None = pyd.Field(default=None, description="")
    facing: list[GypsumFacing] | None = pyd.Field(default=None, description="")
    r_factor: AmountRangeRFactor | None = pyd.Field(default=None, description="")
    flame_spread_astm_e84: RangeInt | None = pyd.Field(default=None, description="")
    smoke_production_astm_e84: RangeInt | None = pyd.Field(default=None, description="")
    surface_abrasion_d4977: RangeInt | None = pyd.Field(default=None, description="")
    indentation_d5420: RangeInt | None = pyd.Field(default=None, description="")
    soft_body_impact_e695: RangeInt | None = pyd.Field(default=None, description="")
    hard_body_impact_c1929: RangeInt | None = pyd.Field(default=None, description="")
    mold_resistant: bool | None = pyd.Field(default=None, description="")
    foil_backing: bool | None = pyd.Field(default=None, description="")
    moisture_resistant: bool | None = pyd.Field(default=None, description="")
    abuse_resistant: bool | None = pyd.Field(default=None, description="")
    GypsumSupports: GypsumSupportsRangeV1 | None = None


class MirrorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Mirrors.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PaintByMassRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings by mass.

    Expected declared unit for products is mass of ready to use product.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PaintByVolumeRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings by volume.

    Expecting declared unit for products is volume of ready to use product.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PaintByAreaRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings by area.

    Expected declared unit is area of host surface covered by the product.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PaintingAndCoatingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings.

    Range version.
    """

    _EXT_VERSION = "1.1"

    PaintByMass: PaintByMassRangeV1 | None = None
    PaintByVolume: PaintByVolumeRangeV1 | None = None
    PaintByArea: PaintByAreaRangeV1 | None = None


class WallFinishesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Interior wall coverings including fabric, textile, wood, stone, and metal products.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")


class PlasterRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Plaster, Stucco, & Render.

    Used for the protective or decorative coating of walls and ceilings and for
    moulding and casting decorative elements. These are typically gypsum-, lime-,
    or cement-based. Products in this category refer to dry mix.

    Range version.
    """

    _EXT_VERSION = "1.0"

    composition: list[PlasterComposition] | None = pyd.Field(default=None, description="")
    application_rate: RangeAmount | None = pyd.Field(
        default=None, description="Typical or reference amount of material covering a unit of a host surface."
    )


class FinishesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    General category - finishes for interior ceilings, floors, walls.

    Range version.
    """

    _EXT_VERSION = "1.1"

    Flooring: FlooringRangeV1 | None = None
    CeilingPanel: CeilingPanelRangeV1 | None = None
    BackingAndUnderlay: BackingAndUnderlayRangeV1 | None = None
    CementBoard: CementBoardRangeV1 | None = None
    Tiling: TilingRangeV1 | None = None
    DeckingBoards: DeckingBoardsRangeV1 | None = None
    GlassFiberReinforcedGypsumFabrications: GlassFiberReinforcedGypsumFabricationsRangeV1 | None = None
    Gypsum: GypsumRangeV1 | None = None
    Mirrors: MirrorsRangeV1 | None = None
    PaintingAndCoating: PaintingAndCoatingRangeV1 | None = None
    WallFinishes: WallFinishesRangeV1 | None = None
    Plaster: PlasterRangeV1 | None = None
