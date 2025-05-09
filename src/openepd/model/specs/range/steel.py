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
    "CoilSteelRangeV1",
    "ColdFormedFramingRangeV1",
    "ColdFormedSteelRangeV1",
    "CrudeSteelRangeV1",
    "DeckingSteelRangeV1",
    "HollowSectionsRangeV1",
    "HotRolledSectionsRangeV1",
    "MBQSteelRangeV1",
    "MetalRailingsRangeV1",
    "MetalStairsRangeV1",
    "MiscMetalFabricationRangeV1",
    "OpenWebMembranesRangeV1",
    "OtherSteelRangeV1",
    "PlateSteelRangeV1",
    "PostTensioningSteelRangeV1",
    "PrefabricatedSteelAssembliesRangeV1",
    "RebarSteelRangeV1",
    "SteelRangeV1",
    "SteelSuspensionAssemblyRangeV1",
    "StructuralSteelRangeV1",
    "WireMeshSteelRangeV1",
)


from openepd.compat.pydantic import pyd
from openepd.model.common import RangeFloat, RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import SteelComposition, SteelRebarGrade
from openepd.model.specs.singular.steel import SteelMakingRoute
from openepd.model.standard import Standard
from openepd.model.validation.quantity import (
    AmountRangeLengthMm,
    AmountRangePressureMpa,
    AmountRangeThermalConductivity,
    AmountRangeThermalExpansion,
)


class ColdFormedFramingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cold Formed Framing performance specification.

    Cold formed steel elements such as studs and framing, typically made from coil or sheet steel and used
    within walls and ceilings.

    Range version.
    """

    _EXT_VERSION = "1.0"


class DeckingSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Corrugated Decking made from cold-formed sheet steel. Often filled with concrete.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SteelSuspensionAssemblyRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Steel suspension assemblies for suspended (e.g. acoustical) ceiling systems.

    Range version.
    """

    _EXT_VERSION = "1.0"


class HollowSectionsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Hollow cross section steel shape, typically referred to as hollow structural section (HSS).

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabricated: bool | None = None


class HotRolledSectionsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Hot rolled sections performance specification.

    Steel shapes, such as angles, wide flange beams and I-beams, produced using a high temperature
    mill process.

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabricated: bool | None = None


class PlateSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Plate Steels.

    Flat hot-rolled steel, typically thicker than 'sheet', made by compressing multiple steel
    layers together into one.


    Range version.
    """

    _EXT_VERSION = "1.0"

    fabricated: bool | None = None


class MetalRailingsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Metal Railings including pipe and tube railings.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MetalStairsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Metal stairs.

    Includes: metal pan stairs, metal floor plate stairs, grating stairs, fire escapes,
    ladders, and walkways/catwalks/ramps/platforms.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MiscMetalFabricationRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Prefabricated steel assemblies not included in another category.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OpenWebMembranesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Open web membranes performance specification.

    Lightweight steel truss, typically made of parallel chords and a triangulated web system,
    "proportioned to span between bearing points.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MBQSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Merchant Bar Quality (MBQ) steel.

    Used as feedstock to steel construction products, but also includes rounds, angles, and light structural shapes.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CoilSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Sheet or strip steel, sold in rolls.

    Typically, coil steel is cold-formed into light gauge products.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ColdFormedSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cold Formed Steel Products.

    All types of cold formed steel products. These products are made from hot-rolled steel coils and
    sheets and are cold formed into products such as studs, decking, panels, and other accessories.

    Range version.
    """

    _EXT_VERSION = "1.0"

    ColdFormedFraming: ColdFormedFramingRangeV1 | None = None
    DeckingSteel: DeckingSteelRangeV1 | None = None
    SteelSuspensionAssembly: SteelSuspensionAssemblyRangeV1 | None = None


class StructuralSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Structural Steel.

    Hot rolled steel shapes, Hollow Sections, pipes, and similar hot-worked structural steels.

    Range version.
    """

    _EXT_VERSION = "1.0"

    modulus_of_elasticity: AmountRangePressureMpa | None = pyd.Field(
        default=None,
        description="Modulus of Elasticity, https://en.wikipedia.org/wiki/Elastic_modulus ",
    )
    thermal_expansion: AmountRangeThermalExpansion | None = pyd.Field(
        default=None,
        description="Thermal Expansion, https://en.wikipedia.org/wiki/Thermal_expansion",
    )
    thermal_conductivity: AmountRangeThermalConductivity | None = pyd.Field(
        default=None,
        description="Thermal Conductivity, https://en.wikipedia.org/wiki/Thermal_conductivity_and_resistivity",
    )
    HollowSections: HollowSectionsRangeV1 | None = None
    HotRolledSections: HotRolledSectionsRangeV1 | None = None
    PlateSteel: PlateSteelRangeV1 | None = None


class PrefabricatedSteelAssembliesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Prefabricated assemblies made primarily of steel.

    Range version.
    """

    _EXT_VERSION = "1.0"

    MetalRailings: MetalRailingsRangeV1 | None = None
    MetalStairs: MetalStairsRangeV1 | None = None
    MiscMetalFabrication: MiscMetalFabricationRangeV1 | None = None
    OpenWebMembranes: OpenWebMembranesRangeV1 | None = None


class PostTensioningSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Steel tensioning cables or tendons for compression of prestressed concrete.

    Range version.
    """

    _EXT_VERSION = "1.0"


class RebarSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Reinforcing bar used together with concrete.

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabricated: bool | None = None
    grade: list[SteelRebarGrade] | None = pyd.Field(default=None)
    diameter_min: AmountRangeLengthMm | None = pyd.Field(default=None, description="Minimal diameter")
    bending_pin_max: RangeFloat | None = pyd.Field(default=None)
    ts_ys_ratio_max: RangeFloat | None = pyd.Field(
        default=None,
        description="Max ratio of ultimate tensile to yield tensile strength",
    )
    epoxy_coated: bool | None = pyd.Field(default=None)


class WireMeshSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Mild steel wire for reinforcement, connections, and meshes.

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabricated: bool | None = None


class OtherSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """Steel products that do not fit into a defined subcategory."""

    _EXT_VERSION = "1.0"


class CrudeSteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """Crude steel products."""

    _EXT_VERSION = "1.0"


class SteelRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Broad category for construction materials made from steel and its alloys.

    Range version.
    """

    _EXT_VERSION = "1.2"

    yield_tensile_str: AmountRangePressureMpa | None = pyd.Field(
        default=None,
        description="Yield Tensile strength (Mpa) per unit area. Yield strength is the point at which a material begins to permanently deform or change shape due to applied stress.",
    )
    bar_elongation: RangeFloat | None = pyd.Field(
        default=None,
        description="Increase in length at break, in percent. Typically 10%-20%",
    )
    recycled_content: RangeRatioFloat | None = pyd.Field(default=None, description="")
    post_consumer_recycled_content: RangeRatioFloat | None = pyd.Field(
        default=None,
        description="Should be a number between zero and the Recycled Content (steel_recycled_content)",
    )
    astm_marking: str | None = pyd.Field(default=None, description="The marking to be expected on the product.")
    euro_marking: str | None = pyd.Field(default=None, description="The marking to be expected on the product.")
    composition: list[SteelComposition] | None = pyd.Field(default=None, description="Basic chemical composition")
    cold_finished: bool | None = pyd.Field(default=None)
    galvanized: bool | None = pyd.Field(default=None)
    stainless: bool | None = pyd.Field(default=None)
    making_route: SteelMakingRoute | None = pyd.Field(default=None)
    astm_standards: list[Standard] | None = pyd.Field(default=None, description="List of ASTM standards")
    sae_standards: list[Standard] | None = pyd.Field(default=None, description="List of SAE standards")
    en_standards: list[Standard] | None = pyd.Field(default=None, description="List of EN standards")
    MBQSteel: MBQSteelRangeV1 | None = None
    CoilSteel: CoilSteelRangeV1 | None = None
    ColdFormedSteel: ColdFormedSteelRangeV1 | None = None
    StructuralSteel: StructuralSteelRangeV1 | None = None
    PrefabricatedSteelAssemblies: PrefabricatedSteelAssembliesRangeV1 | None = None
    PostTensioningSteel: PostTensioningSteelRangeV1 | None = None
    RebarSteel: RebarSteelRangeV1 | None = None
    WireMeshSteel: WireMeshSteelRangeV1 | None = None
    OtherSteel: OtherSteelRangeV1 | None = None
    CrudeSteel: CrudeSteelRangeV1 | None = None
