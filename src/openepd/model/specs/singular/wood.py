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

import pydantic

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

    fabrication: CompositeLumberFabrication | None = pydantic.Field(default=None, description="", examples=["LVL"])
    timber_species: EngineeredTimberSpecies | None = pydantic.Field(
        default=None, description="", examples=["Alaska Cedar"]
    )


class DimensionLumberV1(BaseOpenEpdHierarchicalSpec):
    """Dimension lumber for framing, decking, and other purposes."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    timber_species: SawnTimberSpecies | None = pydantic.Field(default=None, description="", examples=["Alaska Cedar"])
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

    fabrication: MassTimberFabrication | None = pydantic.Field(default=None, description="", examples=["CLT"])
    timber_species: EngineeredTimberSpecies | None = pydantic.Field(
        default=None, description="", examples=["Alaska Cedar"]
    )


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
    fabrication: SheathingPanelsFabrication | None = pydantic.Field(default=None, description="", examples=["Plywood"])
    wood_board_thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])
    timber_species: EngineeredTimberSpecies | None = pydantic.Field(
        default=None, description="", examples=["Alaska Cedar"]
    )


class UnfinishedWoodV1(BaseOpenEpdHierarchicalSpec):
    """Raw logs and other unfinished wood products."""

    _EXT_VERSION = "1.0"


class WoodV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """Structural Wood Products used in construction."""

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: AllTimberSpecies | None = pydantic.Field(
        default=None, description="Timber species", examples=["Alaska Cedar"]
    )
    fabrication: AllFabrication | None = pydantic.Field(
        default=None, description="Timber fabrication", examples=["LVL"]
    )
    weather_exposed: bool | None = pydantic.Field(
        default=None,
        description="Weather exposed",
        examples=[True],
    )
    fire_retardant: bool | None = pydantic.Field(
        default=None,
        description="Fire retardant",
        examples=[True],
    )
    decay_resistant: bool | None = pydantic.Field(
        default=None,
        description="Decay resistant",
        examples=[True],
    )
    fsc_certified: Annotated[float | None, CodegenSpec(override_type=float)] = pydantic.Field(
        default=None,
        description="Forest Stewardship Council certified proportion",
        examples=[0.3],
        ge=0,
        le=1,
    )
    fsc_certified_z: Annotated[float | None, CodegenSpec(override_type=float)] = pydantic.Field(
        default=None, description="", examples=[0.7]
    )

    recycled_content: Annotated[float | None, CodegenSpec(override_type=float)] = pydantic.Field(
        default=None, description="Recycled content", examples=[0.3], ge=0, le=1
    )
    recycled_content_z: Annotated[float | None, CodegenSpec(override_type=float)] = pydantic.Field(
        default=None, description="", examples=[0.7]
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
