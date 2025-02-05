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
from typing import Annotated

from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, CodegenSpec
from openepd.model.specs.enums import (
    AllFabrication,
    AllTimberSpecies,
    CompositeLumberFabrication,
    EngineeredTimberSpecies,
    MassTimberFabrication,
    SawnTimberSpecies,
    SheathingPanelsFabrication,
)
from openepd.model.specs.singular.common import HasForestPracticesCertifiers
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr


class WoodDeckingV1(BaseOpenEpdHierarchicalSpec):
    """Dimensional boards for exterior decking."""

    _EXT_VERSION = "1.0"


class WoodFramingV1(BaseOpenEpdHierarchicalSpec):
    """
    Dimension lumber for light framing.

    Includes solid and finger-jointed lumber. Standard shapes include 2x4, 2x6, and 2x8.
    """

    _EXT_VERSION = "1.0"


class PrefabricatedWoodInsulatedPanelsV1(BaseOpenEpdHierarchicalSpec):
    """
    Structural insulated panels (SIPs).

    Consist of wood sheet layer(s) combined with (typically foam) insulation layer(s).
    """

    _EXT_VERSION = "1.0"


class PrefabricatedWoodTrussV1(BaseOpenEpdHierarchicalSpec):
    """Shop-fabricated wood truss."""

    _EXT_VERSION = "1.0"


class CompositeLumberV1(BaseOpenEpdHierarchicalSpec):
    """
    Shop-fabricated structural Lumber.

    Includes Laminated Strand Lumber (LSL), Parallel Strand Lumber (PSL), and Laminated Veneer Lumber (LVL).
    """

    _EXT_VERSION = "1.0"

    fabrication: CompositeLumberFabrication | None = pyd.Field(default=None, description="", example="LVL")
    timber_species: EngineeredTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")


class DimensionLumberV1(BaseOpenEpdHierarchicalSpec):
    """Dimension lumber for framing, decking, and other purposes."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    timber_species: SawnTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")
    WoodDecking: WoodDeckingV1 | None = None
    WoodFraming: WoodFramingV1 | None = None


class HeavyTimberV1(BaseOpenEpdHierarchicalSpec):
    """Large format, unfinished natural timber."""

    _EXT_VERSION = "1.0"


class MassTimberV1(BaseOpenEpdHierarchicalSpec):
    """
    Engineered heavy timber products.

    Includes glue laminated (glulam), cross-laminated timber (CLT), dowel laminated timber (DLT), and nail laminated
    timber (NLT).
    """

    _EXT_VERSION = "1.0"

    fabrication: MassTimberFabrication | None = pyd.Field(default=None, description="", example="CLT")
    timber_species: EngineeredTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")


class NonStructuralWoodV1(BaseOpenEpdHierarchicalSpec):
    """Non-structural interior and exterior wood products for trim, cabinets, countertops, etc."""

    _EXT_VERSION = "1.0"


class PrefabricatedWoodV1(BaseOpenEpdHierarchicalSpec):
    """
    Prefabricated wood structural members made primarily from one or more types of wood.

    Includes products made with metallic connectors, insulation, etc. Excludes products where the wood is merely
    decorative.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    PrefabricatedWoodInsulatedPanels: PrefabricatedWoodInsulatedPanelsV1 | None = None
    PrefabricatedWoodTruss: PrefabricatedWoodTrussV1 | None = None


class SheathingPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Wood sheets used for structural sheathing, including plywood and Oriented Strand Board."""

    _EXT_VERSION = "1.0"

    # Own fields:
    fabrication: SheathingPanelsFabrication | None = pyd.Field(default=None, description="", example="Plywood")
    wood_board_thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")
    timber_species: EngineeredTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")


class UnfinishedWoodV1(BaseOpenEpdHierarchicalSpec):
    """Raw logs and other unfinished wood products."""

    _EXT_VERSION = "1.0"


class WoodV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """Structural Wood Products used in construction."""

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: AllTimberSpecies | None = pyd.Field(
        default=None, description="Timber species", example="Alaska Cedar"
    )
    fabrication: AllFabrication | None = pyd.Field(default=None, description="Timber fabrication", example="LVL")
    weather_exposed: bool | None = pyd.Field(default=None, description="Weather exposed", example=True)
    fire_retardant: bool | None = pyd.Field(default=None, description="Fire retardant", example=True)
    decay_resistant: bool | None = pyd.Field(default=None, description="Decay resistant", example=True)
    fsc_certified: Annotated[RatioFloat | None, CodegenSpec(override_type=RatioFloat)] = pyd.Field(
        default=None, description="Forest Stewardship Council certified proportion", example=0.3, ge=0, le=1
    )
    fsc_certified_z: Annotated[float | None, CodegenSpec(override_type=float)] = pyd.Field(
        default=None, description="", example=0.7
    )

    recycled_content: Annotated[RatioFloat | None, CodegenSpec(override_type=RatioFloat)] = pyd.Field(
        default=None, description="Recycled content", example=0.3, ge=0, le=1
    )
    recycled_content_z: Annotated[float | None, CodegenSpec(override_type=float)] = pyd.Field(
        default=None, description="", example=0.7
    )

    # Nested specs:
    CompositeLumber: CompositeLumberV1 | None = None
    DimensionLumber: DimensionLumberV1 | None = None
    HeavyTimber: HeavyTimberV1 | None = None
    MassTimber: MassTimberV1 | None = None
    NonStructuralWood: NonStructuralWoodV1 | None = None
    PrefabricatedWood: PrefabricatedWoodV1 | None = None
    SheathingPanels: SheathingPanelsV1 | None = None
    UnfinishedWood: UnfinishedWoodV1 | None = None
