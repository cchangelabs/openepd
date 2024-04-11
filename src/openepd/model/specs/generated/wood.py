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
from openepd.model.org import OrgRef
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.common import HasForestPracticesCertifiers
from openepd.model.specs.generated.enums import (
    AllFabrication,
    AllTimberSpecies,
    CompositeLumberFabrication,
    EngineeredTimberSpecies,
    MassTimberFabrication,
    SawnTimberSpecies,
    SheathingPanelsFabrication,
)
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import LengthMmStr, validate_unit_factory


class WoodDeckingV1(BaseOpenEpdHierarchicalSpec):
    """Wood used for decking."""

    _EXT_VERSION = "1.0"


class WoodFramingV1(BaseOpenEpdHierarchicalSpec):
    """Lumber for framing, typically softwood."""

    _EXT_VERSION = "1.0"


class PrefabricatedWoodInsulatedPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated wood insulated panels performance specification."""

    _EXT_VERSION = "1.0"


class PrefabricatedWoodTrussV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated wood truss performance specification."""

    _EXT_VERSION = "1.0"


class CompositeLumberV1(BaseOpenEpdHierarchicalSpec):
    """Composite lumber performance specification."""

    _EXT_VERSION = "1.0"

    fabrication: CompositeLumberFabrication | None = pyd.Field(default=None, description="", example="LVL")
    timber_species: EngineeredTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")


class DimensionLumberV1(BaseOpenEpdHierarchicalSpec):
    """Dimension lumber performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    timber_species: SawnTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")
    WoodDecking: WoodDeckingV1 | None = None
    WoodFraming: WoodFramingV1 | None = None


class HeavyTimberV1(BaseOpenEpdHierarchicalSpec):
    """Large format natural timber."""

    _EXT_VERSION = "1.0"


class MassTimberV1(BaseOpenEpdHierarchicalSpec):
    """Manufactured structural wood elements, such a CLT and LVL."""

    _EXT_VERSION = "1.0"

    fabrication: MassTimberFabrication | None = pyd.Field(default=None, description="", example="CLT")
    timber_species: EngineeredTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")


class NonStructuralWoodV1(BaseOpenEpdHierarchicalSpec):
    """Wood products that are not meant for structural use."""

    _EXT_VERSION = "1.0"


class PrefabricatedWoodV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated wood performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PrefabricatedWoodInsulatedPanels: PrefabricatedWoodInsulatedPanelsV1 | None = None
    PrefabricatedWoodTruss: PrefabricatedWoodTrussV1 | None = None


class SheathingPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Structural Wood Panels."""

    _EXT_VERSION = "1.0"

    # Own fields:
    fabrication: SheathingPanelsFabrication | None = pyd.Field(default=None, description="", example="Plywood")
    wood_board_thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")
    timber_species: EngineeredTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")

    _wood_board_thickness_is_quantity_validator = pyd.validator("wood_board_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class UnfinishedWoodV1(BaseOpenEpdHierarchicalSpec):
    """Unfinished or 'green' timber."""

    _EXT_VERSION = "1.0"


class WoodV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """Wood performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: AllTimberSpecies | None = pyd.Field(
        default=None, description="Timber species", example="Alaska Cedar"
    )
    fabrication: AllFabrication | None = pyd.Field(default=None, description="Timber fabrication", example="LVL")
    forest_practices_certifiers: list[OrgRef] | None = pyd.Field(
        default=None, description="List of organizations that certify forest practices."
    )
    weather_exposed: bool | None = pyd.Field(default=None, description="Weather exposed", example=True)
    fire_retardant: bool | None = pyd.Field(default=None, description="Fire retardant", example=True)
    decay_resistant: bool | None = pyd.Field(default=None, description="Decay resistant", example=True)
    fsc_certified: RatioFloat | None = pyd.Field(
        default=None, description="Forest Stewardship Council certified proportion", example=0.3, ge=0, le=1
    )
    fsc_certified_z: float | None = pyd.Field(default=None, description="", example=0.7)

    recycled_content: RatioFloat | None = pyd.Field(
        default=None, description="Recycled content", example=0.3, ge=0, le=1
    )
    recycled_content_z: float | None = pyd.Field(default=None, description="", example=0.7)

    # Nested specs:
    CompositeLumber: CompositeLumberV1 | None = None
    DimensionLumber: DimensionLumberV1 | None = None
    HeavyTimber: HeavyTimberV1 | None = None
    MassTimber: MassTimberV1 | None = None
    NonStructuralWood: NonStructuralWoodV1 | None = None
    PrefabricatedWood: PrefabricatedWoodV1 | None = None
    SheathingPanels: SheathingPanelsV1 | None = None
    UnfinishedWood: UnfinishedWoodV1 | None = None
