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
    "CompositeLumberRangeV1",
    "DimensionLumberRangeV1",
    "HeavyTimberRangeV1",
    "MassTimberRangeV1",
    "NonStructuralWoodRangeV1",
    "PrefabricatedWoodInsulatedPanelsRangeV1",
    "PrefabricatedWoodRangeV1",
    "PrefabricatedWoodTrussRangeV1",
    "SheathingPanelsRangeV1",
    "UnfinishedWoodRangeV1",
    "WoodDeckingRangeV1",
    "WoodFramingRangeV1",
    "WoodRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md

from openepd.compat.pydantic import pyd
from openepd.model.org import OrgRef
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    AllFabrication,
    AllTimberSpecies,
    CompositeLumberFabrication,
    EngineeredTimberSpecies,
    MassTimberFabrication,
    SawnTimberSpecies,
    SheathingPanelsFabrication,
)
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import AmountRangeLengthMm


class WoodDeckingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Dimensional boards for exterior decking.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WoodFramingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Dimension lumber for light framing.

    Includes solid and finger-jointed lumber. Standard shapes include 2x4, 2x6, and 2x8.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PrefabricatedWoodInsulatedPanelsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Structural insulated panels (SIPs).

    Consist of wood sheet layer(s) combined with (typically foam) insulation layer(s).

    Range version.
    """

    _EXT_VERSION = "1.0"


class PrefabricatedWoodTrussRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Shop-fabricated wood truss.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CompositeLumberRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Shop-fabricated structural Lumber.

    Includes Laminated Strand Lumber (LSL), Parallel Strand Lumber (PSL), and Laminated Veneer Lumber (LVL).

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabrication: list[CompositeLumberFabrication] | None = pyd.Field(default=None, description="")
    timber_species: list[EngineeredTimberSpecies] | None = pyd.Field(default=None, description="")


class DimensionLumberRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Dimension lumber for framing, decking, and other purposes.

    Range version.
    """

    _EXT_VERSION = "1.0"

    timber_species: list[SawnTimberSpecies] | None = pyd.Field(default=None, description="")
    WoodDecking: WoodDeckingRangeV1 | None = None
    WoodFraming: WoodFramingRangeV1 | None = None


class HeavyTimberRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Large format, unfinished natural timber.

    Range version.
    """

    _EXT_VERSION = "1.0"


class MassTimberRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Engineered heavy timber products.

    Includes glue laminated (glulam), cross-laminated timber (CLT), dowel laminated timber (DLT), and nail laminated
    timber (NLT).

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabrication: list[MassTimberFabrication] | None = pyd.Field(default=None, description="")
    timber_species: list[EngineeredTimberSpecies] | None = pyd.Field(default=None, description="")


class NonStructuralWoodRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Non-structural interior and exterior wood products for trim, cabinets, countertops, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PrefabricatedWoodRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Prefabricated wood structural members made primarily from one or more types of wood.

    Includes products made with metallic connectors, insulation, etc. Excludes products where the wood is merely
    decorative.

    Range version.
    """

    _EXT_VERSION = "1.0"

    PrefabricatedWoodInsulatedPanels: PrefabricatedWoodInsulatedPanelsRangeV1 | None = None
    PrefabricatedWoodTruss: PrefabricatedWoodTrussRangeV1 | None = None


class SheathingPanelsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wood sheets used for structural sheathing, including plywood and Oriented Strand Board.

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabrication: list[SheathingPanelsFabrication] | None = pyd.Field(default=None, description="")
    wood_board_thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    timber_species: list[EngineeredTimberSpecies] | None = pyd.Field(default=None, description="")


class UnfinishedWoodRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Raw logs and other unfinished wood products.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WoodRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Structural Wood Products used in construction.

    Range version.
    """

    _EXT_VERSION = "1.0"

    forest_practices_certifiers: list[OrgRef] | None = None
    timber_species: list[AllTimberSpecies] | None = pyd.Field(default=None, description="Timber species")
    fabrication: list[AllFabrication] | None = pyd.Field(default=None, description="Timber fabrication")
    weather_exposed: bool | None = pyd.Field(default=None, description="Weather exposed")
    fire_retardant: bool | None = pyd.Field(default=None, description="Fire retardant")
    decay_resistant: bool | None = pyd.Field(default=None, description="Decay resistant")
    fsc_certified: RatioFloat | None = pyd.Field(
        default=None, description="Forest Stewardship Council certified proportion"
    )
    fsc_certified_z: float | None = pyd.Field(default=None, description="")
    recycled_content: RatioFloat | None = pyd.Field(default=None, description="Recycled content")
    recycled_content_z: float | None = pyd.Field(default=None, description="")
    CompositeLumber: CompositeLumberRangeV1 | None = None
    DimensionLumber: DimensionLumberRangeV1 | None = None
    HeavyTimber: HeavyTimberRangeV1 | None = None
    MassTimber: MassTimberRangeV1 | None = None
    NonStructuralWood: NonStructuralWoodRangeV1 | None = None
    PrefabricatedWood: PrefabricatedWoodRangeV1 | None = None
    SheathingPanels: SheathingPanelsRangeV1 | None = None
    UnfinishedWood: UnfinishedWoodRangeV1 | None = None
