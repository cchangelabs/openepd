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
from openepd.model.specs.singular.common import HasForestPracticesCertifiers
from openepd.model.specs.singular.mixins.access_flooring_mixin import AccessFlooringMixin
from openepd.model.validation.quantity import (
    AreaPerVolumeStr,
    GwpKgCo2eStr,
    LengthMmStr,
    LengthMStr,
    RFactorStr,
    YarnWeightStr,
    validate_quantity_ge_factory,
    validate_quantity_le_factory,
    validate_quantity_unit_factory,
)


class AccessFlooringV1(BaseOpenEpdHierarchicalSpec, AccessFlooringMixin):
    """
    Elevated floor system built on top of concrete slab surface.

    It thereby creates a hidden void between the two floors that is used for the passage of mechanical and electrical
    services. The system consists of panels, stringers, and pedestals.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AccessFlooring",
        display_name="Access Flooring",
        historical_names=["Finishes >> Flooring >> Access Flooring"],
        description="Elevated floor system built on top of concrete slab surface, thereby creating a hidden void between the two floors that is used for the passage of mechanical and electrical services. The system consists of panels, stringers, and pedestals.",
        masterformat="09 69 00 Access Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class CarpetV1(BaseOpenEpdHierarchicalSpec):
    """Textile Floor Coverings."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Carpet",
        display_name="Carpet",
        alt_names=["Carpeting", "Textile Flooring"],
        description="Textile Floor Coverings",
        masterformat="09 68 00 Carpeting",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    length: LengthMStr | None = pydantic.Field(default=None, description="", examples=["1 m"])
    width: LengthMStr | None = pydantic.Field(default=None, description="", examples=["1 m"])
    intended_application: list[CarpetIntendedApplication] | None = pydantic.Field(
        default=None, description="", examples=[["Res"]]
    )
    manufacture_type: CarpetManufactureType | None = pydantic.Field(default=None, description="", examples=["Tufted"])
    form_factor: CarpetFormFactor | None = pydantic.Field(default=None, description="", examples=["Tiles"])
    yarn_weight: YarnWeightStr | None = pydantic.Field(default=None, description="", examples=["1 g / m2"])
    yarn_type: CarpetYarnType | None = pydantic.Field(default=None, description="", examples=["Nylon 6,6"])
    fire_radiant_panel_rating_astme648: str | None = pydantic.Field(default=None, description="")
    fire_smoke_density_rating_astme648: str | None = pydantic.Field(default=None, description="")
    voc_emissions: str | None = pydantic.Field(
        default=None, description="", examples=["test_valueValidatedStringProperty"]
    )
    cushioned: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    bleachable: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    gwp_factor_base: GwpKgCo2eStr | None = pydantic.Field(default=None, description="", examples=["1 kgCO2e"])
    gwp_factor_yarn: GwpKgCo2eStr | None = pydantic.Field(default=None, description="", examples=["1 kgCO2e"])

    @pydantic.field_validator("yarn_weight", mode="before", check_fields=False)
    def _yarn_weight_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("g / m2")(cls, value)

    @pydantic.field_validator("yarn_weight", mode="before", check_fields=False)
    def _yarn_weight_ge_validator(cls, value):
        return validate_quantity_ge_factory("0 g / m2")(cls, value)


class LaminateV1(BaseOpenEpdHierarchicalSpec):
    """Laminate flooring."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Laminate",
        display_name="Laminate",
        alt_names=["Laminates"],
        description="Laminate flooring",
        masterformat="09 62 19 Laminate Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class OtherFlooringV1(BaseOpenEpdHierarchicalSpec):
    """Other not yet classified kinds of flooring."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherFlooring",
        display_name="Other Flooring",
        historical_names=["Finishes >> Flooring >> Other Flooring"],
        description="Other not yet classified kinds of flooring",
        masterformat="09 60 00 Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class ResilientFlooringV1(BaseOpenEpdHierarchicalSpec):
    """
    Resilient floor products.

    Includes vinyl, rubber, linoleum, composition cork, etc. in modular square or rectangle shapes.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ResilientFlooring",
        display_name="Resilient Flooring",
        alt_names=["Vinyl Flooring", "Cork Flooring", "Linoleum"],
        historical_names=["Finishes >> Flooring >> Resilient Flooring"],
        description="Resilient floor products (including vinyl, rubber, linoleum, composition cork, etc.) in modular square or rectangle shapes",
        masterformat="09 65 00 Resilient Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    length: LengthMStr | None = pydantic.Field(default=None, description="", examples=["1 m"])
    width: LengthMStr | None = pydantic.Field(default=None, description="", examples=["1 m"])
    form_factor: ResilientFlooringFormFactor | None = pydantic.Field(
        default=None, description="", examples=["Loose Lay"]
    )
    material: ResilientFlooringMaterial | None = pydantic.Field(default=None, description="", examples=["VCT"])
    sheet_construction: VinylSheetConstruction | None = pydantic.Field(
        default=None, description="", examples=["Homogeneous"]
    )
    wear_layer: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["1 m"])
    delta_iic: float | None = pydantic.Field(default=None, description="", examples=[2.3])
    thickness: ResilientFlooringThickness | None = pydantic.Field(default=None, description="", examples=["≤ 2mm"])
    sport_flooring: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    conductive_flooring: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    zwtl: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    floor_score: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    nsf332: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


class WallBaseV1(BaseOpenEpdHierarchicalSpec):
    """Wall base made to help cover gaps between wall and vinyl, rubber, wood, or tile flooring."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WallBase",
        display_name="Wall Base",
        historical_names=["Finishes >> Flooring >> Wall Base"],
        description="Wall base made to help cover gaps between wall and vinyl, rubber, wood, or tile flooring.",
        masterformat="09 65 13 Resilient Base and Accessories",
        declared_unit=Amount(qty=1, unit="m"),
    )

    # Own fields:
    wall_base_material: WallBaseMaterial | None = pydantic.Field(default=None, description="", examples=["Rubber"])


class WoodFlooringV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """
    Wood flooring for interior applications.

    Includes hardwood strip and plank flooring, engineered hardwood flooring, wood parquet flooring, coordinated
    transitions, and molding pieces.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WoodFlooring",
        display_name="Wood Flooring",
        historical_names=["Finishes >> Flooring >> Wood Flooring"],
        description="Wood flooring for interior applications including hardwood strip and plank flooring, engineered hardwood flooring, wood parquet flooring, coordinated transitions, and molding pieces.",
        masterformat="09 64 00 Wood Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])
    timber_species: WoodFlooringTimberSpecies | None = pydantic.Field(default=None, description="", examples=["Oak"])
    fabrication: WoodFlooringFabrication | None = pydantic.Field(
        default=None, description="", examples=["Solid hardwood"]
    )


class AcousticalCeilingsV1(BaseOpenEpdHierarchicalSpec):
    """Acoustical ceiling panels."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AcousticalCeilings",
        display_name="Acoustical Ceilings",
        alt_names=["Acoustical Panels"],
        historical_names=["Finishes >> Ceiling Panels >> Acoustical Ceilings"],
        description="Acoustical ceiling panels",
        masterformat="09 51 00 Acoustical Ceilings",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])


class CeramicTileV1(BaseOpenEpdHierarchicalSpec):
    """Ceramic tiles, including porcelain, quarry, pressed floor tile, wall tile, mosaic tile, etc."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CeramicTile",
        display_name="Ceramic Tile",
        short_name="Ceramic",
        historical_names=["Finishes >> Tiling >> Ceramic"],
        description="Ceramic tiles, including porcelain, quarry, pressed floor tile, wall tile, mosaic tile, etc.",
        masterformat="09 31 00 Ceramic Tile",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    porcelain: bool | None = pydantic.Field(
        default=None,
        description="A dense and durable ceramic tile made from fine porcelain clay.",
        examples=[True],
    )
    quarry: bool | None = pydantic.Field(
        default=None,
        description="A type of unglazed ceramic tile made from natural clay with a slightly rough texture.",
        examples=[True],
    )
    pressed_floor_tile: bool | None = pydantic.Field(
        default=None,
        description="A durable and low-maintenance type of tile made by compressing clay or "
        "other materials at high pressure.",
        examples=[True],
    )
    wall_tile: bool | None = pydantic.Field(
        default=None,
        description="A decorative tile designed for use on vertical surfaces such as walls or backsplashes.",
        examples=[True],
    )
    mosaic_tile: bool | None = pydantic.Field(
        default=None,
        description="A small decorative tile made of glass, stone, or ceramic, arranged in a pattern "
        "to create a design.",
        examples=[True],
    )
    specialty: bool | None = pydantic.Field(
        default=None,
        description="A unique and customized type of tile, often made from unconventional materials or with "
        "specialized designs or finishes.",
        examples=[True],
    )


class GaugedTileV1(BaseOpenEpdHierarchicalSpec):
    """
    Specially manufactured porcelain tile with extra-large panels/slabs.

    Manufactured to a specific thickness ranging from 2-20 mm.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="GaugedTile",
        display_name="Gauged Tile",
        short_name="Gauged",
        historical_names=["Finishes >> Tiling >> Gauged"],
        description="Specially manufactured porcelain tile with extra-large panels/slabs manufactured to a specific thickness ranging from 2-20 mm",
        masterformat="09 31 00 Ceramic Tile",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    tile_panels: bool | None = pydantic.Field(
        default=None,
        description="Large-format porcelain or natural stone tiles that are typically over 3 feet in length and width, "
        "designed for use in floor and wall installations to create a seamless and uninterrupted "
        "appearance.",
        examples=[True],
    )
    tile_pavers: bool | None = pydantic.Field(
        default=None,
        description="Thick and durable porcelain or natural stone tiles that are commonly used in outdoor "
        "applications, such as patios, walkways, and driveways, due to their high resistance to weather "
        "and wear.",
        examples=[True],
    )


class GlassTileV1(BaseOpenEpdHierarchicalSpec):
    """Glass Tiles."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="GlassTile",
        display_name="Glass Tile",
        short_name="Glass",
        historical_names=["Finishes >> Tiling >> Glass"],
        description="Glass Tiles",
        masterformat="09 35 00 Glass Mosaic Tile",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    regular: bool | None = pydantic.Field(
        default=None,
        description="Glass tile that is typically square or rectangular in shape, and used for a variety of "
        "decorative applications, such as kitchen backsplashes, shower walls, and accent borders.",
        examples=[True],
    )
    glass_mosaic: bool | None = pydantic.Field(
        default=None,
        description="A small, decorative glass tile made in a variety of shapes and colors, used for intricate "
        "designs and patterns on walls, floors, and other surfaces.",
        examples=[True],
    )
    miniature_mosaic: bool | None = pydantic.Field(
        default=None,
        description="Glass mosaic tile that is smaller in size than regular glass mosaic tile, often used for "
        "intricate details and designs in backsplashes, shower walls, and decorative accents.",
        examples=[True],
    )
    large_format: bool | None = pydantic.Field(
        default=None,
        description="Glass tile that is larger in size than regular glass tile, often used to create a dramatic and "
        "modern effect in commercial and residential spaces.",
        examples=[True],
    )


class GypsumSupportsV1(BaseOpenEpdHierarchicalSpec):
    """Supports for suspended and furred gypsum wall and ceiling assemblies."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="GypsumSupports",
        display_name="Gypsum Supports",
        historical_names=["Finishes >> Gypsum Board >> Gypsum Supports"],
        description="Supports for suspended and furred gypsum wall and ceiling assemblies",
        masterformat="09 22 00 Supports for Plaster and Gypsum Board",
        declared_unit=Amount(qty=1000, unit="sqft"),
    )


class FlooringV1(BaseOpenEpdHierarchicalSpec):
    """General category - finishes for floors."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Flooring",
        display_name="Flooring",
        description="General category - finishes for floors",
        masterformat="09 60 00 Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Nested specs:
    AccessFlooring: AccessFlooringV1 | None = None
    Carpet: CarpetV1 | None = None
    Laminate: LaminateV1 | None = None
    OtherFlooring: OtherFlooringV1 | None = None
    ResilientFlooring: ResilientFlooringV1 | None = None
    WallBase: WallBaseV1 | None = None
    WoodFlooring: WoodFlooringV1 | None = None


class CeilingPanelV1(BaseOpenEpdHierarchicalSpec):
    """Acoustical and other specialty ceiling panels."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CeilingPanel",
        display_name="Ceiling Panels",
        alt_names=["Hung Ceiling", "Ceiling Tile"],
        historical_names=["Finishes >> Ceiling Panels"],
        description="Acoustical and other specialty ceiling panels",
        masterformat="09 50 00 Ceilings",
        declared_unit=Amount(qty=1, unit="m^2"),
    )
    """Modular Ceiling Panels"""

    # Own fields:
    fire_rating: CeilingPanelFireRating | None = pydantic.Field(default=None, description="", examples=["Class A"])
    core_material: CeilingPanelCoreMaterial | None = pydantic.Field(
        default=None, description="", examples=["Fiberglass"]
    )
    nrc: float | None = pydantic.Field(
        default=None,
        description="Noise Reduction Coefficient (NRC) or Sound Absorbtion Average (SAA) per ASTM C423",
        examples=[0.5],
        ge=0,
        le=1,
    )
    cac: int | None = pydantic.Field(
        default=None,
        description="Ceiling Attenuation Class (CAC) per ASTM E1414",
        examples=[13],
        ge=10,
        le=50,
    )

    # Nested specs:
    AcousticalCeilings: AcousticalCeilingsV1 | None = None


class BackingAndUnderlayV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious, glass-mat faced gypsum, and fibered gypsum backing boards to support finish materials."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="BackingAndUnderlay",
        display_name="Backing&Underlay",
        alt_names=["Subfloor"],
        historical_names=["Finishes >> Backing&Underlay"],
        description="Cementitious, glass-mat faced gypsum, and fibered gypsum backing boards to support finish materials",
        masterformat="09 28 00 Backing Boards and Underlayments",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class CementBoardV1(BaseOpenEpdHierarchicalSpec):
    """Hard cementitious boards, typically used as a tile backer."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="CementBoard",
        display_name="Cement Board",
        historical_names=["Finishes >> Cement Board"],
        description="Hard cementitious boards, typically used as a tile backer.",
        masterformat="09 28 13 Cementitious Backing Board",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: CementBoardThickness | None = pydantic.Field(
        default=None, description="", examples=[str(CementBoardThickness.INCH_1_2)]
    )

    @pydantic.field_validator("thickness")
    def _cement_board_thickness_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("m")(cls, value)


class TilingV1(BaseOpenEpdHierarchicalSpec):
    """
    Decorative building materials that includes a variety of ceramic, porcelain, and glass tiles.

    Used for covering and enhancing surfaces such as floors, walls, and countertops.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Tiling",
        display_name="Tiling",
        description="Decorative building materials that includes a variety of ceramic, porcelain, and glass tiles, used for covering and enhancing surfaces such as floors, walls, and countertops.",
        masterformat="09 30 00 Tiling",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["9 mm"])
    flooring: bool | None = pydantic.Field(
        default=None,
        description="Tiling intended for walking.",
        examples=[True],
    )
    wall_finish: bool | None = pydantic.Field(
        default=None,
        description="A decorative tile designed for use on vertical surfaces such as walls or backsplashes.",
        examples=[True],
    )
    cladding: bool | None = pydantic.Field(
        default=None,
        description="Tiling for exterior use, primarily used for the walls of buildings and structures, providing a "
        "protective and decorative layer that enhances the aesthetic appearance and weather resistance "
        "of the underlying structure.",
        examples=[True],
    )
    other: bool | None = pydantic.Field(
        default=None,
        description="Tiling used as countertops, ceilings, furnishings, hardscapes etc.",
        examples=[True],
    )
    residential_only: bool | None = pydantic.Field(
        default=None,
        description="All commercial tile can also be used in residential applications, but the opposite may not be "
        "true. This selection allows to filter out tiling that is not intended for commercial "
        "applications.",
        examples=[True],
    )
    reinforced: bool | None = pydantic.Field(
        default=None,
        description="Steel-reinforced ceramic tiles or tiles with other special reinforcing technology.",
        examples=[True],
    )
    total_recycled_content: float | None = pydantic.Field(
        default=None,
        description="Proportion of this product that is sourced from recycled content. Pre-consumer recycling is "
        "given a 50% weighting, 100% for post-consumer, by mass.",
        examples=[0.5],
        ge=0,
        le=1,
    )
    post_consumer_recycled_content: float | None = pydantic.Field(
        default=None,
        description="Proportion of this product that is sourced from post-consumer recycled content, by mass.",
        examples=[0.5],
        ge=0,
        le=1,
    )

    @pydantic.field_validator("thickness", mode="before")
    def _thickness_max_validator(cls, value):
        return validate_quantity_le_factory("50 mm")(cls, value)

    # Nested specs:
    CeramicTile: CeramicTileV1 | None = None
    GaugedTile: GaugedTileV1 | None = None
    GlassTile: GlassTileV1 | None = None


class DeckingBoardsV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """Decking boards provide the finished surface of a deck and support the weight of people and furniture."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="DeckingBoards",
        display_name="Decking Boards",
        historical_names=["Finishes >> Decking Boards"],
        description="Decking boards provide the finished surface of a deck and support the weight of people and furniture.",
        masterformat="06 00 00 Wood, Plastics & Composites",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    timber_species: SawnTimberSpecies | None = pydantic.Field(default=None, description="", examples=["Alaska Cedar"])
    fabrication: AllFabrication | None = pydantic.Field(default=None, description="", examples=["LVL"])
    weather_exposed: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    fire_retardant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    decay_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    material: DeckingBoardMaterial | None = pydantic.Field(default=None, description="", examples=["Wood"])


class GlassFiberReinforcedGypsumFabricationsV1(BaseOpenEpdHierarchicalSpec):
    """Gypsum with integrated glass fiber reinforcement, which may be fabricated in complex shapes or as a board."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="GlassFiberReinforcedGypsumFabrications",
        display_name="Glass Fiber Reinforced Gypsum Fabrications",
        short_name="GFRG Fabrications",
        historical_names=["Finishes >> GFRG Fabrications"],
        description="Gypsum with integrated glass fiber reinforcement, which may be fabricated in complex shapes or as a board.",
        masterformat="09 27 13 Glass-Fiber-Reinforced Gypsum Fabrications",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class GypsumV1(BaseOpenEpdHierarchicalSpec):
    """Gypsum board used for interior walls, ceilings, and similar applications."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="Gypsum",
        display_name="Gypsum Board",
        alt_names=["Drywall", "Gyp board", "gypsum board"],
        historical_names=["Finishes >> Gypsum Board"],
        description="Gypsum board used for interior walls, ceilings, and similar applications.",
        masterformat="09 29 00 Gypsum Board",
        declared_unit=Amount(qty=1000, unit="sqft"),
    )

    # Own fields:
    fire_rating: GypsumFireRating | None = pydantic.Field(default=None, description="", examples=["-"])
    thickness: GypsumThickness | None = pydantic.Field(default=None, description="", examples=["1 m"])
    facing: GypsumFacing | None = pydantic.Field(default=None, description="", examples=["Paper"])
    r_factor: RFactorStr | None = pydantic.Field(default=None, description="", examples=["1 RSI"])
    flame_spread_astm_e84: int | None = pydantic.Field(default=None, description="", examples=[3])
    smoke_production_astm_e84: int | None = pydantic.Field(default=None, description="", examples=[3])
    surface_abrasion_d4977: int | None = pydantic.Field(default=None, description="", examples=[3])
    indentation_d5420: int | None = pydantic.Field(default=None, description="", examples=[3])
    soft_body_impact_e695: int | None = pydantic.Field(default=None, description="", examples=[3])
    hard_body_impact_c1929: int | None = pydantic.Field(default=None, description="", examples=[3])
    mold_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    foil_backing: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    moisture_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    abuse_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )

    @pydantic.field_validator("r_factor")
    def _gypsum_r_factor_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("RSI")(cls, value)

    # Nested specs:
    GypsumSupports: GypsumSupportsV1 | None = None


class MirrorsV1(BaseOpenEpdHierarchicalSpec):
    """Mirrors."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Mirrors",
        display_name="Mirrors",
        alt_names=["Mirror"],
        description="Mirrors",
        masterformat="08 83 00 Mirrors",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class PaintByMassV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings by mass.

    Expected declared unit for products is mass of ready to use product.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PaintByMass",
        display_name="Paint By Mass",
        short_name="By Mass",
        historical_names=["Finishes >> Painting and Coating >> By Mass"],
        description="Paintings and coatings measured by mass of ready-to-use product.",
        masterformat="09 90 00 Painting and Coating",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class PaintByVolumeV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings by volume.

    Expecting declared unit for products is volume of ready to use product.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PaintByVolume",
        display_name="Paint By Volume",
        short_name="By Volume",
        historical_names=["Finishes >> Painting and Coating >> By Volume"],
        description="Paintings and coatings measured by volume of ready-to-use product.",
        masterformat="09 90 00 Painting and Coating",
        declared_unit=Amount(qty=1, unit="m^3"),
    )


class PaintByAreaV1(BaseOpenEpdHierarchicalSpec):
    """
    Paintings and coatings by area.

    Expected declared unit is area of host surface covered by the product.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PaintByArea",
        display_name="Paint By Area",
        short_name="By Area",
        historical_names=["Finishes >> Painting and Coating >> By Area"],
        description="Paintings and coatings measured by area of host surface covered by the ready-to-use product.",
        masterformat="09 90 00 Painting and Coating",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class PaintingAndCoatingV1(BaseOpenEpdHierarchicalSpec):
    """Paintings and coatings."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="PaintingAndCoating",
        display_name="Painting and Coating",
        historical_names=["Finishes >> Painting and Coating"],
        description="Paintings and coatings",
        masterformat="09 90 00 Painting and Coating",
    )

    PaintByMass: PaintByMassV1 | None = None
    PaintByVolume: PaintByVolumeV1 | None = None
    PaintByArea: PaintByAreaV1 | None = None


class WallFinishesV1(BaseOpenEpdHierarchicalSpec):
    """Interior wall coverings including fabric, textile, wood, stone, and metal products."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WallFinishes",
        display_name="Wall Finishes",
        historical_names=["Finishes >> Wall Finishes"],
        description="Interior wall coverings including fabric, textile, wood, stone, and metal products ",
        masterformat="09 70 00 Wall Finishes",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])


class PlasterV1(BaseOpenEpdHierarchicalSpec):
    """
    Plaster, Stucco, & Render.

    Used for the protective or decorative coating of walls and ceilings and for
    moulding and casting decorative elements. These are typically gypsum-, lime-,
    or cement-based. Products in this category refer to dry mix.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Plaster",
        display_name="Plaster, Stucco, & Render",
        short_name="Plaster",
        description="Used for the protective or decorative coating of walls and ceilings and for moulding and casting decorative elements. These are typically gypsum-, lime-, or cement-based. Products in this category refer to dry mix.",
        masterformat="09 24 00 Cement Plastering",
        declared_unit=Amount(qty=1, unit="kg"),
    )

    # Own fields:
    composition: PlasterComposition | None = pydantic.Field(default=None, description="", examples=["Cement"])
    application_rate: AreaPerVolumeStr | None = pydantic.Field(
        default=None,
        description="Typical or reference amount of material covering a unit of a host surface.",
        examples=["10 m2/l"],
    )


class FinishesV1(BaseOpenEpdHierarchicalSpec):
    """General category - finishes for interior ceilings, floors, walls."""

    _EXT_VERSION = "1.1"
    _CATEGORY_META = CategoryMeta(
        unique_name="Finishes",
        display_name="Finishes",
        description="General category - finishes for interior ceilings, floors, walls",
        masterformat="09 00 00 Finishes",
    )

    # Nested specs:
    Flooring: FlooringV1 | None = None
    CeilingPanel: CeilingPanelV1 | None = None
    BackingAndUnderlay: BackingAndUnderlayV1 | None = None
    CementBoard: CementBoardV1 | None = None
    Tiling: TilingV1 | None = None
    DeckingBoards: DeckingBoardsV1 | None = None
    GlassFiberReinforcedGypsumFabrications: GlassFiberReinforcedGypsumFabricationsV1 | None = None
    Gypsum: GypsumV1 | None = None
    Mirrors: MirrorsV1 | None = None
    PaintingAndCoating: PaintingAndCoatingV1 | None = None
    WallFinishes: WallFinishesV1 | None = None
    Plaster: PlasterV1 | None = None
