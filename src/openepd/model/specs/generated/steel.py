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
from openepd.model.specs.generated.enums import SteelComposition, SteelRebarGrade
from openepd.model.standard import Standard
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMStr, PressureMPaStr, validate_unit_factory


class ColdFormedFramingV1(BaseOpenEpdHierarchicalSpec):
    """Cold formed framing performance specification."""

    _EXT_VERSION = "1.0"


class DeckingSteelV1(BaseOpenEpdHierarchicalSpec):
    """Decking steel performance specification."""

    _EXT_VERSION = "1.0"
    """Cold Formed Steel Decking"""


class SteelSuspensionAssemblyV1(BaseOpenEpdHierarchicalSpec):
    """Steel suspension assembly performance specification."""

    _EXT_VERSION = "1.0"


class HollowSectionsV1(BaseOpenEpdHierarchicalSpec):
    """Hollow sections performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    steel_fabricated: bool | None = pyd.Field(default=None, description="", example="True")


class HotRolledSectionsV1(BaseOpenEpdHierarchicalSpec):
    """Hot rolled sections performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    steel_fabricated: bool | None = pyd.Field(default=None, description="", example="True")


class PlateSteelV1(BaseOpenEpdHierarchicalSpec):
    """Plate steel performance specification."""

    _EXT_VERSION = "1.0"
    """Plate Steels"""

    # Own fields:
    steel_fabricated: bool | None = pyd.Field(default=None, description="", example="True")


class MetalRailingsV1(BaseOpenEpdHierarchicalSpec):
    """Metal railings performance specification."""

    _EXT_VERSION = "1.0"


class MetalStairsV1(BaseOpenEpdHierarchicalSpec):
    """Metal stairs performance specification."""

    _EXT_VERSION = "1.0"


class MiscMetalFabricationV1(BaseOpenEpdHierarchicalSpec):
    """Misc metal fabrication performance specification."""

    _EXT_VERSION = "1.0"


class OpenWebMembranesV1(BaseOpenEpdHierarchicalSpec):
    """Open web membranes performance specification."""

    _EXT_VERSION = "1.0"


class MBQSteelV1(BaseOpenEpdHierarchicalSpec):
    """M b q steel performance specification."""

    _EXT_VERSION = "1.0"


class CoilSteelV1(BaseOpenEpdHierarchicalSpec):
    """Coil steel performance specification."""

    _EXT_VERSION = "1.0"


class ColdFormedSteelV1(BaseOpenEpdHierarchicalSpec):
    """Cold formed steel performance specification."""

    _EXT_VERSION = "1.0"
    """Cold Formed Structural Steel"""

    # Nested specs:
    ColdFormedFraming: ColdFormedFramingV1 | None = None
    DeckingSteel: DeckingSteelV1 | None = None
    SteelSuspensionAssembly: SteelSuspensionAssemblyV1 | None = None


class StructuralSteelV1(BaseOpenEpdHierarchicalSpec):
    """Structural steel performance specification."""

    _EXT_VERSION = "1.0"
    """Structural Steel"""

    # Own fields:
    steel_modulus_of_elasticity: PressureMPaStr | None = pyd.Field(default=None, description="", example="1.0 MPa")
    steel_thermal_expansion: str | None = pyd.Field(default=None, description="", example="1 / K")
    steel_thermal_conductivity: str | None = pyd.Field(default=None, description="", example="1 W / (m * K)")

    _steel_modulus_of_elasticity_is_quantity_validator = pyd.validator("steel_modulus_of_elasticity", allow_reuse=True)(
        validate_unit_factory("MPa")
    )
    _steel_thermal_expansion_is_quantity_validator = pyd.validator("steel_thermal_expansion", allow_reuse=True)(
        validate_unit_factory("1 / K")
    )
    _steel_thermal_conductivity_is_quantity_validator = pyd.validator("steel_thermal_conductivity", allow_reuse=True)(
        validate_unit_factory("W / (m * K)")
    )

    # Nested specs:
    HollowSections: HollowSectionsV1 | None = None
    HotRolledSections: HotRolledSectionsV1 | None = None
    PlateSteel: PlateSteelV1 | None = None


class PrefabricatedSteelAssembliesV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated steel assemblies performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    MetalRailings: MetalRailingsV1 | None = None
    MetalStairs: MetalStairsV1 | None = None
    MiscMetalFabrication: MiscMetalFabricationV1 | None = None
    OpenWebMembranes: OpenWebMembranesV1 | None = None


class PostTensioningSteelV1(BaseOpenEpdHierarchicalSpec):
    """Post tensioning steel performance specification."""

    _EXT_VERSION = "1.0"
    """Post-Tensioning Steels, per https://www.concretenetwork.com/post-tension/industry.html"""


class RebarSteelV1(BaseOpenEpdHierarchicalSpec):
    """Rebar steel performance specification."""

    _EXT_VERSION = "1.0"
    """Bar steels, such as rebar for concrete reinforcement"""

    # Own fields:
    steel_fabricated: bool | None = pyd.Field(default=None, description="", example="True")
    steel_rebar_grade: SteelRebarGrade | None = pyd.Field(default=None, description="", example="60 ksi")
    steel_rebar_diameter_min: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    steel_rebar_bending_pin_max: float | None = pyd.Field(default=None, description="", example="2.3")
    steel_rebar_ts_ys_ratio_max: float | None = pyd.Field(default=None, description="", example="2.3")
    epoxy_coated: bool | None = pyd.Field(default=None, description="", example="True")

    _steel_rebar_diameter_min_is_quantity_validator = pyd.validator("steel_rebar_diameter_min", allow_reuse=True)(
        validate_unit_factory("m")
    )


class WireMeshSteelV1(BaseOpenEpdHierarchicalSpec):
    """Wire mesh steel performance specification."""

    _EXT_VERSION = "1.0"
    """Mild steel wire for reinforcement, connections, and meshes"""

    # Own fields:
    steel_fabricated: bool | None = pyd.Field(default=None, description="", example="True")


class SteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    steel_yield_tensile_str: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    steel_bar_elongation: float | None = pyd.Field(default=None, description="", example="2.3")
    steel_recycled_content: RatioFloat | None = pyd.Field(default=None, description="", example="0.5", ge=0, le=1)
    steel_post_consumer_recycled_content: RatioFloat | None = pyd.Field(
        default=None, description="", example="0.5", ge=0, le=1
    )
    steel_astm_marking: str | None = pyd.Field(
        default=None, description="", example="test_valueValidatedStringProperty"
    )
    steel_euro_marking: str | None = pyd.Field(
        default=None, description="", example="test_valueValidatedStringProperty"
    )
    steel_composition: SteelComposition | None = pyd.Field(default=None, description="", example="Carbon")
    cold_finished: bool | None = pyd.Field(default=None, description="", example="True")
    galvanized: bool | None = pyd.Field(default=None, description="", example="True")
    stainless: bool | None = pyd.Field(default=None, description="", example="True")
    steel_making_route_bof: bool | None = pyd.Field(default=None, description="", example="True")
    steel_making_route_eaf: bool | None = pyd.Field(default=None, description="", example="True")
    steel_making_route_ohf: bool | None = pyd.Field(default=None, description="", example="True")
    astm_standards: list[Standard] | None = pyd.Field(default=None, description="")
    sae_standards: list[Standard] | None = pyd.Field(default=None, description="")
    en_standards: list[Standard] | None = pyd.Field(default=None, description="")

    _steel_yield_tensile_str_is_quantity_validator = pyd.validator("steel_yield_tensile_str", allow_reuse=True)(
        validate_unit_factory("MPa")
    )

    # Nested specs:
    MBQSteel: MBQSteelV1 | None = None
    CoilSteel: CoilSteelV1 | None = None
    ColdFormedSteel: ColdFormedSteelV1 | None = None
    StructuralSteel: StructuralSteelV1 | None = None
    PrefabricatedSteelAssemblies: PrefabricatedSteelAssembliesV1 | None = None
    PostTensioningSteel: PostTensioningSteelV1 | None = None
    RebarSteel: RebarSteelV1 | None = None
    WireMeshSteel: WireMeshSteelV1 | None = None
