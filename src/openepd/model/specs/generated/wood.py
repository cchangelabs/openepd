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
from openepd.model.validation.quantity import LengthMStr, validate_unit_factory

from .enums import *

UnknownStrTypeHandleMe = str


class WoodDeckingV1(BaseOpenEpdHierarchicalSpec):
    """Wood decking performance specification."""

    _EXT_VERSION = "1.0"
    """Wood used for decking"""
    pass


class WoodFramingV1(BaseOpenEpdHierarchicalSpec):
    """Wood framing performance specification."""

    _EXT_VERSION = "1.0"
    """Lumber for framing, typically softwood"""
    pass


class PrefabricatedWoodInsulatedPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated wood insulated panels performance specification."""

    _EXT_VERSION = "1.0"

    pass


class PrefabricatedWoodTrussV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated wood truss performance specification."""

    _EXT_VERSION = "1.0"

    pass


class CompositeLumberV1(BaseOpenEpdHierarchicalSpec):
    """Composite lumber performance specification."""

    _EXT_VERSION = "1.0"

    pass


class DimensionLumberV1(BaseOpenEpdHierarchicalSpec):
    """Dimension lumber performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    WoodDecking: WoodDeckingV1 | None = None
    WoodFraming: WoodFramingV1 | None = None


class HeavyTimberV1(BaseOpenEpdHierarchicalSpec):
    """Heavy timber performance specification."""

    _EXT_VERSION = "1.0"
    """Large format natural timber"""
    pass


class MassTimberV1(BaseOpenEpdHierarchicalSpec):
    """Mass timber performance specification."""

    _EXT_VERSION = "1.0"
    """Manufactured structural wood elements, such a CLT and LVL"""
    pass


class NonStructuralWoodV1(BaseOpenEpdHierarchicalSpec):
    """Non structural wood performance specification."""

    _EXT_VERSION = "1.0"
    """Wood products that are not meant for structural use."""
    pass


class PrefabricatedWoodV1(BaseOpenEpdHierarchicalSpec):
    """Prefabricated wood performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PrefabricatedWoodInsulatedPanels: PrefabricatedWoodInsulatedPanelsV1 | None = None
    PrefabricatedWoodTruss: PrefabricatedWoodTrussV1 | None = None


class SheathingPanelsV1(BaseOpenEpdHierarchicalSpec):
    """Sheathing panels performance specification."""

    _EXT_VERSION = "1.0"
    """Structural Wood Panels"""

    # Own fields:
    wood_board_thickness: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")

    _wood_board_thickness_is_quantity_validator = pyd.validator("wood_board_thickness", allow_reuse=True)(
        validate_unit_factory("m")
    )


class UnfinishedWoodV1(BaseOpenEpdHierarchicalSpec):
    """Unfinished wood performance specification."""

    _EXT_VERSION = "1.0"
    """Unfinished or 'green' timber"""
    pass


class WoodV1(BaseOpenEpdHierarchicalSpec):
    """Wood performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: TimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")
    fabrication: Fabrication | None = pyd.Field(default=None, description="", example="LVL")
    rel_forest_practices_certifiers: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipFrom"
    )
    weather_exposed: bool | None = pyd.Field(default=None, description="", example="True")
    fire_retardant: bool | None = pyd.Field(default=None, description="", example="True")
    decay_resistant: bool | None = pyd.Field(default=None, description="", example="True")
    timber_strength_grade: str | None = pyd.Field(
        default=None, description="", example="test_valueValidatedStringProperty"
    )
    fsc_certified: float | None = pyd.Field(default=None, description="", example="2.3")
    fsc_certified_z: float | None = pyd.Field(default=None, description="", example="2.3")
    recycled_content_z: float | None = pyd.Field(default=None, description="", example="2.3")

    # Nested specs:
    CompositeLumber: CompositeLumberV1 | None = None
    DimensionLumber: DimensionLumberV1 | None = None
    HeavyTimber: HeavyTimberV1 | None = None
    MassTimber: MassTimberV1 | None = None
    NonStructuralWood: NonStructuralWoodV1 | None = None
    PrefabricatedWood: PrefabricatedWoodV1 | None = None
    SheathingPanels: SheathingPanelsV1 | None = None
    UnfinishedWood: UnfinishedWoodV1 | None = None
