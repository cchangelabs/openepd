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

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import (
    AccessFlooringCoreMaterial,
    AccessFlooringFinishMaterial,
    AccessFlooringSeismicRating,
    AccessFlooringStringers,
    AllFabrication,
    CarpetFormFactor,
    CarpetManufactureType,
    CarpetYarnType,
    CeilingPanelCoreMaterial,
    CeilingPanelFireRating,
    DeckingBoardMaterial,
    GypsumFacing,
    GypsumFireRating,
    IntendedApplication,
    ResilientFlooringFormFactor,
    ResilientFlooringMaterial,
    ResilientFlooringThickness,
    SawnTimberSpecies,
    SheetConstruction,
    WallBaseMaterial,
    WoodFlooringFabrication,
)
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import GwpKgCo2eStr, LengthMStr, PressureMPaStr, validate_unit_factory

UnknownStrTypeHandleMe = str


class AccessFlooringV1(BaseOpenEpdHierarchicalSpec):
    """Access flooring performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    access_flooring_core_material: AccessFlooringCoreMaterial | None = pyd.Field(
        default=None, description="", example="Cementitious"
    )
    access_flooring_finish_material: AccessFlooringFinishMaterial | None = pyd.Field(
        default=None, description="", example="Linoleum"
    )
    access_flooring_stringers: AccessFlooringStringers | None = pyd.Field(
        default=None, description="", example="Standard"
    )
    access_flooring_seismic_rating: AccessFlooringSeismicRating | None = pyd.Field(
        default=None, description="", example="Type 0"
    )
    access_flooring_magnetically_attached_finish: bool | None = pyd.Field(default=None, description="", example="True")
    access_flooring_permanent_finish: bool | None = pyd.Field(default=None, description="", example="True")
    access_flooring_drylay: bool | None = pyd.Field(default=None, description="", example="True")
    access_flooring_adjustable_height: bool | None = pyd.Field(default=None, description="", example="True")
    access_flooring_fixed_height: bool | None = pyd.Field(default=None, description="", example="True")
    access_flooring_finished_floor_height: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    access_flooring_panel_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    access_flooring_concentrated_load: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    access_flooring_uniform_load: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    access_flooring_rolling_load_10_pass: str | None = pyd.Field(default=None, description="", example="1 N")
    access_flooring_rolling_load_10000_pass: str | None = pyd.Field(default=None, description="", example="1 N")

    _access_flooring_finished_floor_height_is_quantity_validator = pyd.validator(
        "access_flooring_finished_floor_height", allow_reuse=True
    )(validate_unit_factory("m"))
    _access_flooring_panel_thickness_is_quantity_validator = pyd.validator(
        "access_flooring_panel_thickness", allow_reuse=True
    )(validate_unit_factory("m"))
    _access_flooring_concentrated_load_is_quantity_validator = pyd.validator(
        "access_flooring_concentrated_load", allow_reuse=True
    )(validate_unit_factory("MPa"))
    _access_flooring_uniform_load_is_quantity_validator = pyd.validator(
        "access_flooring_uniform_load", allow_reuse=True
    )(validate_unit_factory("MPa"))
    _access_flooring_rolling_load_10_pass_is_quantity_validator = pyd.validator(
        "access_flooring_rolling_load_10_pass", allow_reuse=True
    )(validate_unit_factory("N"))
    _access_flooring_rolling_load_10000_pass_is_quantity_validator = pyd.validator(
        "access_flooring_rolling_load_10000_pass", allow_reuse=True
    )(validate_unit_factory("N"))


class CarpetV1(BaseOpenEpdHierarchicalSpec):
    """Carpet performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    length: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    width: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    intended_application: list[IntendedApplication] | None = pyd.Field(default=None, description="", example="['Res']")
    manufacture_type: CarpetManufactureType | None = pyd.Field(default=None, description="", example="Tufted")
    form_factor: CarpetFormFactor | None = pyd.Field(default=None, description="", example="Tiles")
    yarn_weight: str | None = pyd.Field(default=None, description="", example="1 g / m2")
    yarn_type: CarpetYarnType | None = pyd.Field(default=None, description="", example="Nylon 6,6")
    yarn_material: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueAliasProperty"
    )
    fire_radiant_panel_rating_astme648: str | None = pyd.Field(
        default=None, description="", example="test_valueValidatedStringProperty"
    )
    fire_smoke_density_rating_astme648: str | None = pyd.Field(
        default=None, description="", example="test_valueValidatedStringProperty"
    )
    voc_emissions: str | None = pyd.Field(default=None, description="", example="test_valueValidatedStringProperty")
    cushioned: bool | None = pyd.Field(default=None, description="", example="True")
    bleachable: bool | None = pyd.Field(default=None, description="", example="True")
    gwp_factor_base: GwpKgCo2eStr | None = pyd.Field(default=None, description="", example="1 kgCO2e")
    gwp_factor_yarn: GwpKgCo2eStr | None = pyd.Field(default=None, description="", example="1 kgCO2e")
    rel_yarn: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipTo"
    )
    rel_backing: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipTo"
    )

    _length_is_quantity_validator = pyd.validator("length", allow_reuse=True)(validate_unit_factory("m"))
    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))
    _yarn_weight_is_quantity_validator = pyd.validator("yarn_weight", allow_reuse=True)(validate_unit_factory("g / m2"))
    _gwp_factor_base_is_quantity_validator = pyd.validator("gwp_factor_base", allow_reuse=True)(
        validate_unit_factory("kgCO2e")
    )
    _gwp_factor_yarn_is_quantity_validator = pyd.validator("gwp_factor_yarn", allow_reuse=True)(
        validate_unit_factory("kgCO2e")
    )


class LaminateV1(BaseOpenEpdHierarchicalSpec):
    """Laminate performance specification."""

    _EXT_VERSION = "1.0"


class OtherFlooringV1(BaseOpenEpdHierarchicalSpec):
    """Other flooring performance specification."""

    _EXT_VERSION = "1.0"


class ResilientFlooringV1(BaseOpenEpdHierarchicalSpec):
    """Resilient flooring performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    length: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    width: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    resilient_flooring_form_factor: ResilientFlooringFormFactor | None = pyd.Field(
        default=None, description="", example="Loose Lay"
    )
    resilient_flooring_material: ResilientFlooringMaterial | None = pyd.Field(
        default=None, description="", example="VCT"
    )
    sheet_construction: SheetConstruction | None = pyd.Field(default=None, description="", example="Homogeneous")
    resilient_flooring_wear_layer: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    resilient_flooring_delta_iic: float | None = pyd.Field(default=None, description="", example="2.3")
    resilient_flooring_thickness: ResilientFlooringThickness | None = pyd.Field(
        default=None, description="", example="≤ 2mm"
    )
    sport_flooring: bool | None = pyd.Field(default=None, description="", example="True")
    conductive_flooring: bool | None = pyd.Field(default=None, description="", example="True")
    zwtl: bool | None = pyd.Field(default=None, description="", example="True")
    floor_score: bool | None = pyd.Field(default=None, description="", example="True")
    nsf332: bool | None = pyd.Field(default=None, description="", example="True")

    _length_is_quantity_validator = pyd.validator("length", allow_reuse=True)(validate_unit_factory("m"))
    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))
    _resilient_flooring_wear_layer_is_quantity_validator = pyd.validator(
        "resilient_flooring_wear_layer", allow_reuse=True
    )(validate_unit_factory("m"))


class WallBaseV1(BaseOpenEpdHierarchicalSpec):
    """Wall base performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    wall_base_material: WallBaseMaterial | None = pyd.Field(default=None, description="", example="Rubber")


class WoodFlooringV1(BaseOpenEpdHierarchicalSpec):
    """Wood flooring performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    timber_species: SawnTimberSpecies | None = pyd.Field(default=None, description="", example="Oak")
    fabrication: WoodFlooringFabrication | None = pyd.Field(default=None, description="", example="Solid hardwood")
    rel_forest_practices_certifiers: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipFrom"
    )

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))


class AcousticalCeilingsV1(BaseOpenEpdHierarchicalSpec):
    """Acoustical ceilings performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))


class CeramicTileV1(BaseOpenEpdHierarchicalSpec):
    """Ceramic tile performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    porcelain: bool | None = pyd.Field(
        default=None, description="A dense and durable ceramic tile made from fine porcelain clay.", example="True"
    )
    quarry: bool | None = pyd.Field(
        default=None,
        description="A type of unglazed ceramic tile made from natural clay with a slightly rough texture.",
        example="True",
    )
    pressed_floor_tile: bool | None = pyd.Field(
        default=None,
        description="A durable and low-maintenance type of tile made by compressing clay or "
        "other materials at high pressure.",
        example="True",
    )
    wall_tile: bool | None = pyd.Field(
        default=None,
        description="A decorative tile designed for use on vertical surfaces such as walls or backsplashes.",
        example="True",
    )
    mosaic_tile: bool | None = pyd.Field(
        default=None,
        description="A small decorative tile made of glass, stone, or ceramic, arranged in a pattern "
        "to create a design.",
        example="True",
    )
    specialty: bool | None = pyd.Field(
        default=None,
        description="A unique and customized type of tile, often made from unconventional materials or with "
        "specialized designs or finishes.",
        example="True",
    )


class GaugedTileV1(BaseOpenEpdHierarchicalSpec):
    """Gauged tile performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    tile_panels: bool | None = pyd.Field(
        default=None,
        description="Large-format porcelain or natural stone tiles that are typically over 3 feet in length and width, "
        "designed for use in floor and wall installations to create a seamless and uninterrupted "
        "appearance.",
        example="True",
    )
    tile_pavers: bool | None = pyd.Field(
        default=None,
        description="Thick and durable porcelain or natural stone tiles that are commonly used in outdoor "
        "applications, such as patios, walkways, and driveways, due to their high resistance to weather "
        "and wear.",
        example="True",
    )


class GlassTileV1(BaseOpenEpdHierarchicalSpec):
    """Glass tile performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    regular: bool | None = pyd.Field(default=None, description="", example="True")
    glass_mosaic: bool | None = pyd.Field(default=None, description="", example="True")
    miniature_mosaic: bool | None = pyd.Field(default=None, description="", example="True")
    large_format: bool | None = pyd.Field(default=None, description="", example="True")


class GypsumSupportsV1(BaseOpenEpdHierarchicalSpec):
    """Gypsum supports performance specification."""

    _EXT_VERSION = "1.0"


class FlooringV1(BaseOpenEpdHierarchicalSpec):
    """Flooring performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AccessFlooring: AccessFlooringV1 | None = None
    Carpet: CarpetV1 | None = None
    Laminate: LaminateV1 | None = None
    OtherFlooring: OtherFlooringV1 | None = None
    ResilientFlooring: ResilientFlooringV1 | None = None
    WallBase: WallBaseV1 | None = None
    WoodFlooring: WoodFlooringV1 | None = None


class CeilingPanelV1(BaseOpenEpdHierarchicalSpec):
    """Ceiling panel performance specification."""

    _EXT_VERSION = "1.0"
    """Modular Ceiling Panels"""

    # Own fields:
    ceiling_panel_fire_rating: CeilingPanelFireRating | None = pyd.Field(
        default=None, description="", example="Class A"
    )
    ceiling_panel_core_material: CeilingPanelCoreMaterial | None = pyd.Field(
        default=None, description="", example="Fiberglass"
    )
    ceiling_panel_nrc: RatioFloat | None = pyd.Field(default=None, description="", example="0.5", ge=0, le=1)
    ceiling_panel_cac: int | None = pyd.Field(default=None, description="", example="3")

    # Nested specs:
    AcousticalCeilings: AcousticalCeilingsV1 | None = None


class BackingAndUnderlayV1(BaseOpenEpdHierarchicalSpec):
    """Backing and underlay performance specification."""

    _EXT_VERSION = "1.0"


class CementBoardV1(BaseOpenEpdHierarchicalSpec):
    """Cement board performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cement_board_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _cement_board_thickness_is_quantity_validator = pyd.validator("cement_board_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class TilingV1(BaseOpenEpdHierarchicalSpec):
    """Tiling performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    flooring: bool | None = pyd.Field(default=None, description="Tiling intended for walking.", example="True")
    wall_finish: bool | None = pyd.Field(
        default=None,
        description="A decorative tile designed for use on vertical surfaces such as walls or backsplashes.",
        example="True",
    )
    cladding: bool | None = pyd.Field(
        default=None,
        description="Tiling for exterior use, primarily used for the walls of buildings and structures, providing a "
        "protective and decorative layer that enhances the aesthetic appearance and weather resistance "
        "of the underlying structure.",
        example="True",
    )
    other: bool | None = pyd.Field(
        default=None, description="Tiling used as countertops, ceilings, furnishings, hardscapes etc.", example="True"
    )
    residential_only: bool | None = pyd.Field(
        default=None,
        description="All commercial tile can also be used in residential applications, but the opposite may not be "
        "true. This selection allows to filter out tiling that is not intended for commercial "
        "applications.",
        example="True",
    )
    reinforced: bool | None = pyd.Field(
        default=None,
        description="Steel-reinforced ceramic tiles or tiles with other special reinforcing technology.",
        example="True",
    )
    tiling_total_recycled_content: RatioFloat | None = pyd.Field(
        default=None,
        description="Proportion of this product that is sourced from recycled content. Pre-consumer recycling is "
        "given a 50% weighting, 100% for post-consumer, by mass.",
        example="0.5",
        ge=0,
        le=1,
    )
    tiling_post_consumer_recycled_content: RatioFloat | None = pyd.Field(
        default=None,
        description="Proportion of this product that is sourced from post-consumer recycled content, by mass.",
        example="0.5",
        ge=0,
        le=1,
    )

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))

    # Nested specs:
    CeramicTile: CeramicTileV1 | None = None
    GaugedTile: GaugedTileV1 | None = None
    GlassTile: GlassTileV1 | None = None


class DeckingBoardsV1(BaseOpenEpdHierarchicalSpec):
    """Decking boards performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: SawnTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")
    fabrication: AllFabrication | None = pyd.Field(default=None, description="", example="LVL")
    rel_forest_practices_certifiers: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipFrom"
    )
    weather_exposed: bool | None = pyd.Field(default=None, description="", example="True")
    fire_retardant: bool | None = pyd.Field(default=None, description="", example="True")
    decay_resistant: bool | None = pyd.Field(default=None, description="", example="True")
    decking_board_material: DeckingBoardMaterial | None = pyd.Field(default=None, description="", example="Wood")


class GlassFiberReinforcedGypsumFabricationsV1(BaseOpenEpdHierarchicalSpec):
    """Glass fiber reinforced gypsum fabrications performance specification."""

    _EXT_VERSION = "1.0"


class GypsumV1(BaseOpenEpdHierarchicalSpec):
    """Gypsum performance specification."""

    _EXT_VERSION = "1.0"
    """Gypsum Sheet and Board"""

    # Own fields:
    gypsum_fire_rating: GypsumFireRating | None = pyd.Field(default=None, description="", example="-")
    gypsum_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    gypsum_facing: GypsumFacing | None = pyd.Field(default=None, description="", example="Paper")
    gypsum_r_factor: str | None = pyd.Field(default=None, description="", example="1 RSI")
    gypsum_flame_spread_astm_e84: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_smoke_production_astm_e84: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_surface_abrasion_d4977: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_indentation_d5420: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_soft_body_impact_e695: int | None = pyd.Field(default=None, description="", example="3")
    gypsum_hard_body_impact_c1929: int | None = pyd.Field(default=None, description="", example="3")
    mold_resistant: bool | None = pyd.Field(default=None, description="", example="True")
    foil_backing: bool | None = pyd.Field(default=None, description="", example="True")
    moisture_resistant: bool | None = pyd.Field(default=None, description="", example="True")
    abuse_resistant: bool | None = pyd.Field(default=None, description="", example="True")

    _gypsum_thickness_is_quantity_validator = pyd.validator("gypsum_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _gypsum_r_factor_is_quantity_validator = pyd.validator("gypsum_r_factor", allow_reuse=True)(
        validate_unit_factory("RSI")
    )

    # Nested specs:
    GypsumSupports: GypsumSupportsV1 | None = None


class MirrorsV1(BaseOpenEpdHierarchicalSpec):
    """Mirrors performance specification."""

    _EXT_VERSION = "1.0"


class PaintingAndCoatingV1(BaseOpenEpdHierarchicalSpec):
    """Painting and coating performance specification."""

    _EXT_VERSION = "1.0"


class WallFinishesV1(BaseOpenEpdHierarchicalSpec):
    """Wall finishes performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))


class FinishesV1(BaseOpenEpdHierarchicalSpec):
    """Finishes performance specification."""

    _EXT_VERSION = "1.0"

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
