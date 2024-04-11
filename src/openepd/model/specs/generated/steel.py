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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, BaseOpenEpdSpec
from openepd.model.specs.generated.enums import SteelComposition, SteelRebarGrade
from openepd.model.specs.steel import SteelMakingRoute
from openepd.model.standard import Standard
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, PressureMPaStr, validate_unit_factory


class SteelFabricatedMixin(BaseOpenEpdSpec):
    """Class with fabricated property used in different parts of steel hierarchy."""

    fabricated: bool | None = pyd.Field(default=None, description="", example=True)


class ColdFormedFramingV1(BaseOpenEpdHierarchicalSpec):
    """Cold formed framing performance specification."""

    _EXT_VERSION = "1.0"


class DeckingSteelV1(BaseOpenEpdHierarchicalSpec):
    """Cold Formed Steel Decking."""

    _EXT_VERSION = "1.0"


class SteelSuspensionAssemblyV1(BaseOpenEpdHierarchicalSpec):
    """Steel suspension assembly performance specification."""

    _EXT_VERSION = "1.0"


class HollowSectionsV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Hollow sections performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:


class HotRolledSectionsV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Hot rolled sections performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:


class PlateSteelV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Plate Steels."""

    _EXT_VERSION = "1.0"

    # Own fields:


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
    """Cold Formed Structural Steel."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    ColdFormedFraming: ColdFormedFramingV1 | None = None
    DeckingSteel: DeckingSteelV1 | None = None
    SteelSuspensionAssembly: SteelSuspensionAssemblyV1 | None = None


class StructuralSteelV1(BaseOpenEpdHierarchicalSpec):
    """Structural Steel."""

    _EXT_VERSION = "1.0"

    # Own fields:
    modulus_of_elasticity: PressureMPaStr | None = pyd.Field(default=None, description="", example="1.0 MPa")
    thermal_expansion: str | None = pyd.Field(default=None, description="", example="1 / K")
    thermal_conductivity: str | None = pyd.Field(default=None, description="", example="1 W / (m * K)")

    _steel_modulus_of_elasticity_is_quantity_validator = pyd.validator("modulus_of_elasticity", allow_reuse=True)(
        validate_unit_factory("MPa")
    )
    _steel_thermal_expansion_is_quantity_validator = pyd.validator("thermal_expansion", allow_reuse=True)(
        validate_unit_factory("1 / K")
    )
    _steel_thermal_conductivity_is_quantity_validator = pyd.validator("thermal_conductivity", allow_reuse=True)(
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
    """Post-Tensioning Steels, per https://www.concretenetwork.com/post-tension/industry.html."""

    _EXT_VERSION = "1.0"


class RebarSteelV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Bar steels, such as rebar for concrete reinforcement."""

    _EXT_VERSION = "1.0"

    # Own fields:
    grade: SteelRebarGrade | None = pyd.Field(default=None, description="", example="60 ksi")
    diameter_min: LengthMmStr | None = pyd.Field(default=None, description="", example="8 mm")
    bending_pin_max: float | None = pyd.Field(default=None, description="", example=2.3)
    ts_ys_ratio_max: float | None = pyd.Field(default=None, description="", example=2.3)
    epoxy_coated: bool | None = pyd.Field(default=None, description="", example=True)

    _steel_rebar_diameter_min_is_quantity_validator = pyd.validator("diameter_min", allow_reuse=True)(
        validate_unit_factory("m")
    )


class WireMeshSteelV1(BaseOpenEpdHierarchicalSpec, SteelFabricatedMixin):
    """Mild steel wire for reinforcement, connections, and meshes."""

    _EXT_VERSION = "1.0"


class SteelV1(BaseOpenEpdHierarchicalSpec):
    """Steel performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    yield_tensile_str: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    bar_elongation: float | None = pyd.Field(default=None, description="", example=2.3)
    recycled_content: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)
    post_consumer_recycled_content: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)
    astm_marking: str | None = pyd.Field(default=None, description="")
    euro_marking: str | None = pyd.Field(default=None, description="")
    composition: SteelComposition | None = pyd.Field(default=None, description="", example="Carbon")
    cold_finished: bool | None = pyd.Field(default=None, description="", example=True)
    galvanized: bool | None = pyd.Field(default=None, description="", example=True)
    stainless: bool | None = pyd.Field(default=None, description="", example=True)
    making_route: SteelMakingRoute | None = pyd.Field(default=None)
    astm_standards: list[Standard] | None = pyd.Field(default=None, description="")
    sae_standards: list[Standard] | None = pyd.Field(default=None, description="")
    en_standards: list[Standard] | None = pyd.Field(default=None, description="")

    _steel_yield_tensile_str_is_quantity_validator = pyd.validator("yield_tensile_str", allow_reuse=True)(
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
