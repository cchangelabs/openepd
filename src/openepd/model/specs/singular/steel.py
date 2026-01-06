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
from typing import Annotated

import pydantic

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, BaseOpenEpdSpec, CodegenSpec
from openepd.model.specs.enums import SteelComposition, SteelRebarGrade
from openepd.model.standard import Standard
from openepd.model.validation.quantity import (
    LengthMmStr,
    PressureMPaStr,
    ThermalConductivityStr,
    ThermalExpansionStr,
    validate_quantity_unit_factory,
)


class SteelMakingRoute(BaseOpenEpdSchema):
    """Steel making route."""

    bof: bool | None = pydantic.Field(default=None, description="Basic oxygen furnace")
    eaf: bool | None = pydantic.Field(default=None, description="Electric arc furnace")
    ohf: bool | None = pydantic.Field(default=None, description="Open hearth furnace")


class SteelFabricatedMixin(BaseOpenEpdSpec):
    """Class with fabricated property used in different parts of steel hierarchy."""

    fabricated: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


class ColdFormedFramingV1(BaseOpenEpdHierarchicalSpec):
    """
    Cold Formed Framing performance specification.

    Cold formed steel elements such as studs and framing, typically made from coil or sheet steel and used
    within walls and ceilings.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ColdFormedFraming",
        display_name="Cold Formed Framing",
        short_name="Framing",
        historical_names=["Steel >> Cold Formed >> Framing"],
        description="Cold formed steel elements such as studs and framing, typically made from coil or sheet steel and used within walls and ceilings.",
        masterformat="05 40 00 COLD-FORMED METAL FRAMING",
        declared_unit=Amount(qty=1, unit="t"),
    )


class DeckingSteelV1(BaseOpenEpdHierarchicalSpec):
    """Corrugated Decking made from cold-formed sheet steel. Often filled with concrete."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="DeckingSteel",
        display_name="Composite and Form Decks",
        short_name="Decking",
        alt_names=["Metal Decking", "Steel Decking", "Corrugated Steel Deck"],
        historical_names=["Steel >> Cold Formed >> Decking", "Steel >> DeckingSteel", "Steel >> Decking"],
        description="Corrugated Decking made from cold-formed sheet steel. Often filled with concrete.",
        masterformat="05 31 00 Steel Decking",
        declared_unit=Amount(qty=1, unit="t"),
    )


class SteelSuspensionAssemblyV1(BaseOpenEpdHierarchicalSpec):
    """Steel suspension assemblies for suspended (e.g. acoustical) ceiling systems."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SteelSuspensionAssembly",
        display_name="Steel Suspension Assemblies",
        short_name="Suspension Assemblies",
        historical_names=[
            "Steel >> Cold Formed >> Suspension Assemblies",
            "Steel >> SteelSuspensionAssembly",
            "Steel >> Steel Suspension Assemblies",
        ],
        description="Steel suspension assemblies for suspended (e.g. acoustical) ceiling systems",
        masterformat="09 53 00 Suspension Assemblies",
        declared_unit=Amount(qty=1, unit="t"),
    )


class HollowSectionsV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Hollow cross section steel shape, typically referred to as hollow structural section (HSS)."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HollowSections",
        display_name="Hollow Sections",
        masterformat="05 12 00 Structural Steel Framing",
        description="Hollow cross section steel shape, typically referred to as hollow structural section (HSS)",
        declared_unit=Amount(qty=1, unit="t"),
    )


class HotRolledSectionsV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """
    Hot rolled sections performance specification.

    Steel shapes, such as angles, wide flange beams and I-beams, produced using a high temperature
    mill process.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="HotRolledSections",
        display_name="Hot-Rolled Sections",
        historical_names=["Steel >> Structural Steel >> Hot-Rolled Sections"],
        description="Steel shapes, such as angles, wide flange beams and I-beams, produced using a high temperature mill process.",
        masterformat="05 12 00 Structural Steel Framing",
        declared_unit=Amount(qty=1, unit="t"),
    )


class PlateSteelV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """
    Plate Steels.

    Flat hot-rolled steel, typically thicker than 'sheet', made by compressing multiple steel
    layers together into one.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PlateSteel",
        display_name="Plate Steel",
        short_name="Plate",
        masterformat="05 12 00 STRUCTURAL STEEL FRAMING",
        description=(
            "Flat hot-rolled steel, typically thicker than 'sheet', "
            "made by compressing multiple steel layers together into one"
        ),
        declared_unit=Amount(qty=1, unit="t"),
    )
    # Own fields:


class MetalRailingsV1(BaseOpenEpdHierarchicalSpec):
    """Metal Railings including pipe and tube railings."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MetalRailings",
        display_name="Metal Railings",
        short_name="Railings",
        historical_names=["Steel >> Prefab Assemb. >> Railings"],
        description="Metal Railings including pipe and tube railings",
        masterformat="05 52 00 Metal Railings",
        declared_unit=Amount(qty=1, unit="t"),
    )


class MetalStairsV1(BaseOpenEpdHierarchicalSpec):
    """
    Metal stairs.

    Includes: metal pan stairs, metal floor plate stairs, grating stairs, fire escapes,
    ladders, and walkways/catwalks/ramps/platforms.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MetalStairs",
        display_name="Metal Stairs",
        short_name="Stairs",
        historical_names=["Steel >> Prefab Assemb. >> Stairs"],
        description="Metal stairs including: metal pan stairs, metal floor plate stairs, grating stairs, fire escapes, ladders, and walkways/catwalks/ramps/platforms",
        masterformat="05 51 00 Metal Stairs",
        declared_unit=Amount(qty=1, unit="t"),
    )


class MiscMetalFabricationV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated steel assemblies not included in another category."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MiscMetalFabrication",
        display_name="Misc. Metal Fabrications",
        short_name="Misc.",
        historical_names=["Steel >> Prefab Assemb. >> Misc."],
        description="Prefabricated steel assemblies not included in another category.",
        masterformat="05 50 00 Misc. Metal Fabrications",
        declared_unit=Amount(qty=1, unit="t"),
    )


class OpenWebMembranesV1(BaseOpenEpdHierarchicalSpec):
    """
    Open web membranes performance specification.

    Lightweight steel truss, typically made of parallel chords and a triangulated web system,
    "proportioned to span between bearing points.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OpenWebMembranes",
        display_name="Open Web Steel Joists",
        short_name="Open Web",
        historical_names=["Steel >> Prefab Assemb. >> Open Web"],
        description="Lightweight steel truss, typically made of parallel chords and a triangulated web system, proportioned to span between bearing points",
        masterformat="05 21 19 Open Web Steel Joist Framing",
        declared_unit=Amount(qty=1, unit="t"),
    )


class MBQSteelV1(BaseOpenEpdHierarchicalSpec):
    """
    Merchant Bar Quality (MBQ) steel.

    Used as feedstock to steel construction products, but also includes rounds, angles, and light structural shapes.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="MBQSteel",
        display_name="Merchant Bar (MBQ)",
        short_name="Merchant Bar",
        alt_names=["MBQ"],
        historical_names=["Steel >> Merchant Bar"],
        description="Merchant Bar Quality (MBQ) steel is used as feedstock to steel construction products, but also includes rounds, angles, and light structural shapes.",
        masterformat="05 00 00 Metals",
        declared_unit=Amount(qty=1, unit="t"),
    )


class CoilSteelV1(BaseOpenEpdHierarchicalSpec):
    """
    Sheet or strip steel, sold in rolls.

    Typically, coil steel is cold-formed into light gauge products.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CoilSteel",
        display_name="Coil Steel",
        short_name="Coil",
        historical_names=["Steel >> Coil"],
        description="Sheet or strip steel, sold in rolls. Typically, coil steel is cold-formed into light gauge products.",
        masterformat="05 00 00 Metals",
        declared_unit=Amount(qty=1, unit="t"),
    )


class ColdFormedSteelV1(BaseOpenEpdHierarchicalSpec):
    """
    Cold Formed Steel Products.

    All types of cold formed steel products. These products are made from hot-rolled steel coils and
    sheets and are cold formed into products such as studs, decking, panels, and other accessories.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ColdFormedSteel",
        display_name="Cold Formed Steel",
        description="All types of cold formed steel products. These products are made from hot-rolled steel coils and sheets and are cold formed into products such as studs, decking, panels, and other accessories.",
        masterformat="05 40 00 Cold-Formed Metal Framing",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Nested specs:
    ColdFormedFraming: ColdFormedFramingV1 | None = None
    DeckingSteel: DeckingSteelV1 | None = None
    SteelSuspensionAssembly: SteelSuspensionAssemblyV1 | None = None


class StructuralSteelV1(BaseOpenEpdHierarchicalSpec):
    """
    Structural Steel.

    Hot rolled steel shapes, Hollow Sections, pipes, and similar hot-worked structural steels.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="StructuralSteel",
        display_name="Structural Steel",
        masterformat="05 12 00 Structural Steel Framing",
        description="Hot rolled steel shapes, Hollow Sections, pipes, and similar hot-worked structural steels",
        declared_unit=Amount(qty=1, unit="t"),
    )
    # Own fields:
    modulus_of_elasticity: PressureMPaStr | None = pydantic.Field(
        default=None,
        description="Modulus of Elasticity, https://en.wikipedia.org/wiki/Elastic_modulus ",
        examples=["193 GPa"],
    )
    thermal_expansion: ThermalExpansionStr | None = pydantic.Field(
        default=None,
        description="Thermal Expansion, https://en.wikipedia.org/wiki/Thermal_expansion",
        examples=["1.11E-5 / K"],
    )
    thermal_conductivity: ThermalConductivityStr | None = pydantic.Field(
        default=None,
        description="Thermal Conductivity, https://en.wikipedia.org/wiki/Thermal_conductivity_and_resistivity",
        examples=["1.45E-5 W / m / K)"],
    )

    @pydantic.field_validator("thermal_expansion")
    def _steel_thermal_expansion_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("1 / K")(cls, value)

    @pydantic.field_validator("thermal_conductivity")
    def _steel_thermal_conductivity_is_quantity_validator(cls, value):
        return validate_quantity_unit_factory("W / (m * K)")(cls, value)

    # Nested specs:
    HollowSections: HollowSectionsV1 | None = None
    HotRolledSections: HotRolledSectionsV1 | None = None
    PlateSteel: PlateSteelV1 | None = None


class PrefabricatedSteelAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated assemblies made primarily of steel."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PrefabricatedSteelAssemblies",
        display_name="Prefabricated Steel Assemblies",
        short_name="Prefab Assemb.",
        historical_names=["Steel >> Prefab Assemb."],
        description="Prefabricated assemblies made primarily of steel.",
        masterformat="05 00 00 Metals",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Nested specs:
    MetalRailings: MetalRailingsV1 | None = None
    MetalStairs: MetalStairsV1 | None = None
    MiscMetalFabrication: MiscMetalFabricationV1 | None = None
    OpenWebMembranes: OpenWebMembranesV1 | None = None


class PostTensioningSteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel tensioning cables or tendons for compression of prestressed concrete."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PostTensioningSteel",
        display_name="Post-Tensioning Steel",
        short_name="Post-Tensioning",
        alt_names=["Post-Tension Steel", "PT Tendons", "PT Steel"],
        historical_names=["Steel >> Post-Tensioning"],
        description="Steel tensioning cables or tendons for compression of prestressed concrete",
        masterformat="03 23 00 Stressed Tendon Reinforcing",
        declared_unit=Amount(qty=1, unit="t"),
    )


class RebarSteelV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Reinforcing bar used together with concrete."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="RebarSteel",
        display_name="Reinforcing Bar",
        short_name="Rebar",
        alt_names=["Concrete Reinforcing", "Concrete Reinforcement"],
        historical_names=["Steel >> Rebar"],
        description="Reinforcing bar used together with concrete.",
        masterformat="03 21 00 Reinforcement Bars",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    grade: SteelRebarGrade | None = pydantic.Field(default=None, examples=["60 ksi"])
    diameter_min: LengthMmStr | None = pydantic.Field(default=None, description="Minimal diameter", examples=["8 mm"])
    bending_pin_max: float | None = pydantic.Field(default=None, examples=[2.3])
    ts_ys_ratio_max: float | None = pydantic.Field(
        default=None,
        description="Max ratio of ultimate tensile to yield tensile strength",
        examples=[2.3],
    )
    epoxy_coated: bool | None = pydantic.Field(
        default=None,
        examples=[True],
    )


class WireMeshSteelV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Mild steel wire for reinforcement, connections, and meshes."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WireMeshSteel",
        display_name="Reinforcing Wire and Mesh",
        short_name="Wire & Mesh",
        alt_names=["Wire Rod", "Wire Mesh", "Structural Welded Wire", "WWF", "Welded Wire Fabric"],
        historical_names=["Steel >> Wire & Mesh"],
        description="Mild steel wire for reinforcement, connections, and meshes",
        masterformat="03 22 00 Fabric and Grid Reinforcing",
        declared_unit=Amount(qty=1, unit="t"),
    )


class OtherSteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel products that do not fit into a defined subcategory."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherSteel",
        display_name="Other Steel Products",
        short_name="Other",
        alt_names=["OtherSteelProducts"],
        historical_names=["Steel >> Other"],
        description="Steel products that do not fit into a defined subcategory",
        masterformat="05 00 00 Metals",
        declared_unit=Amount(qty=1, unit="t"),
    )


class CrudeSteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel ingots, billets, blooms, and slabs for use in manufacturing steel products."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CrudeSteel",
        display_name="Crude Steel",
        short_name="Crude",
        historical_names=["Steel >> Crude"],
        description="Steel ingots, billets, blooms, and slabs for use in manufacturing steel products.",
        masterformat="05 00 00 Metals",
        declared_unit=Amount(qty=1, unit="t"),
    )


class SteelV1(BaseOpenEpdHierarchicalSpec):
    """Broad category for construction materials made from steel and its alloys."""

    _EXT_VERSION = "1.2"
    _CATEGORY_META = CategoryMeta(
        unique_name="Steel",
        display_name="Steel",
        masterformat="05 00 00 Metals",
        description="Broad category for construction materials made from steel and its alloys",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    yield_tensile_str: PressureMPaStr | None = pydantic.Field(
        default=None,
        description="Yield Tensile strength (Mpa) per unit area. Yield strength is the point at which a material "
        "begins to permanently deform or change shape due to applied stress.",
        examples=["100 MPa"],
    )
    bar_elongation: float | None = pydantic.Field(
        default=None,
        description="Increase in length at break, in percent. Typically 10%-20%",
        examples=[0.2],
    )
    recycled_content: float | None = pydantic.Field(default=None, description="", examples=[0.5], ge=0, le=1)
    post_consumer_recycled_content: float | None = pydantic.Field(
        default=None,
        description="Should be a number between zero and the Recycled Content (steel_recycled_content)",
        examples=[0.5],
        ge=0,
        le=1,
    )
    astm_marking: str | None = pydantic.Field(
        default=None,
        description="The marking to be expected on the product.",
        examples=["S4S60"],
    )
    euro_marking: str | None = pydantic.Field(
        default=None,
        description="The marking to be expected on the product.",
        examples=["S4S60"],
    )
    composition: SteelComposition | None = pydantic.Field(
        default=None, description="Basic chemical composition", examples=["Carbon"]
    )
    cold_finished: bool | None = pydantic.Field(
        default=None,
        examples=[True],
    )
    galvanized: bool | None = pydantic.Field(
        default=None,
        examples=[True],
    )
    stainless: bool | None = pydantic.Field(
        default=None,
        examples=[True],
    )
    making_route: Annotated[SteelMakingRoute | None, CodegenSpec(override_type=SteelMakingRoute)] = pydantic.Field(
        default=None
    )
    astm_standards: list[Standard] | None = pydantic.Field(default=None, description="List of ASTM standards")
    sae_standards: list[Standard] | None = pydantic.Field(default=None, description="List of SAE standards")
    en_standards: list[Standard] | None = pydantic.Field(default=None, description="List of EN standards")

    # Nested specs:
    MBQSteel: MBQSteelV1 | None = None
    CoilSteel: CoilSteelV1 | None = None
    ColdFormedSteel: ColdFormedSteelV1 | None = None
    StructuralSteel: StructuralSteelV1 | None = None
    PrefabricatedSteelAssemblies: PrefabricatedSteelAssembliesV1 | None = None
    PostTensioningSteel: PostTensioningSteelV1 | None = None
    RebarSteel: RebarSteelV1 | None = None
    WireMeshSteel: WireMeshSteelV1 | None = None
    OtherSteel: OtherSteelV1 | None = None
    CrudeSteel: CrudeSteelV1 | None = None
