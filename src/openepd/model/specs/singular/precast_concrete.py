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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, BaseOpenEpdSpec
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import PressureMPaStr


class StructuralPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Structural Precast Concrete."""

    wall: bool | None = pyd.Field(
        description="Precast solid wall elements, including thin shell",
        example=True,
        default=None,
    )
    solid_slab: bool | None = pyd.Field(
        description="Precast slabs used for floor or roof applications",
        example=True,
        default=None,
    )
    hollowcore: bool | None = pyd.Field(
        description="Precast slabs with tubular voids, typically used flooring applications",
        example=True,
        default=None,
    )
    beam: bool | None = pyd.Field(
        description="Precast structural beams for carrying or transferring loads; includes girders",
        example=True,
        default=None,
    )
    column: bool | None = pyd.Field(
        description="Precast structural columns for carrying or transferring loads",
        example=True,
        default=None,
    )
    stairs: bool | None = pyd.Field(
        description="Staircases made of precast concrete components",
        example=True,
        default=None,
    )
    balcony: bool | None = pyd.Field(
        description="Balcony slabs made from precast concrete",
        example=True,
        default=None,
    )
    pile: bool | None = pyd.Field(
        description="Precast concrete structural foundation elements used to support offshore structures such as bridges, oil rigs, and floating airports",
        example=True,
        default=None,
    )


class UtilityPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Utility Underground Precast Concrete."""

    manhole: bool | None = pyd.Field(
        description="Precast barrel-shaped chambers used for wastewater management and access management",
        example=True,
        default=None,
    )
    retaining_wall: bool | None = pyd.Field(
        description="Precast concrete structures for retaining soil",
        example=True,
        default=None,
    )
    box_culvert: bool | None = pyd.Field(
        description="A precast concrete structure commonly used to channel water, primarily as part of a drainage system",
        example=True,
        default=None,
    )


class ArchitecturalPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Architectural Precast Concrete."""

    wall: bool | None = pyd.Field(
        description="Precast solid wall elements, including thin shell",
        example=True,
        default=None,
    )


class CivilPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Civil Precast Concrete."""

    beam: bool | None = pyd.Field(
        description="Precast structural beams for carrying or transferring loads; includes girders",
        example=True,
        default=None,
    )
    manhole: bool | None = pyd.Field(
        description="Precast barrel-shaped chambers used for wastewater management and access management",
        example=True,
        default=None,
    )
    retaining_wall: bool | None = pyd.Field(
        description="Precast concrete structures for retaining soil",
        example=True,
        default=None,
    )
    rail_sleeper: bool | None = pyd.Field(
        description="Rectangular supports for the rails on railroad tracks, which transfer loads to the track ballast and subgrade and keep the rails spaced to the correct gauge. Also called railroad ties",
        example=True,
        default=None,
    )
    box_culvert: bool | None = pyd.Field(
        description="A precast concrete structure commonly used to channel water, primarily as part of a drainage system",
        example=True,
        default=None,
    )
    pile: bool | None = pyd.Field(
        description="Precast concrete structural foundation elements used to support offshore structures such as bridges, oil rigs, and floating airports",
        example=True,
        default=None,
    )
    road_barriers: bool | None = pyd.Field(
        description="Precast Vehicle and Traffic Barriers",
        example=True,
        default=None,
    )


class ArchitecturalPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete cladding used for architectural purposes."""

    _EXT_VERSION = "1.1"

    element_type: ArchitecturalPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used for architectural applications."
    )


class StructuralPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete used for structural purposes."""

    _EXT_VERSION = "1.1"

    element_type: StructuralPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used for structural applications."
    )


class UtilityUndergroundPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete for utility vaults, manhole, drain inlets. Excludes piping."""

    _EXT_VERSION = "1.1"

    element_type: UtilityPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used for utility underground applications."
    )


class CivilPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete used for civil engineering applications including bridges, highways, and railroads."""

    _EXT_VERSION = "1.0"

    element_type: CivilPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used as civil engineering components."
    )


class PrecastConcreteV1(BaseOpenEpdHierarchicalSpec):
    """General category for precast concrete components."""

    _EXT_VERSION = "1.1"

    # Own fields:
    lightweight: bool | None = pyd.Field(default=None, description="", example=True)
    concrete_compressive_strength_28d: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    insulated: bool | None = pyd.Field(default=None, description="", example=True)
    gfrc: bool | None = pyd.Field(
        default=None,
        description="Glass Fiber Reinforced Concrete is fiber-reinforced concrete sometimes used in "
        "architectural panels",
        example=True,
    )
    steel_mass_percentage: RatioFloat | None = pyd.Field(default=None, description="", example=0.5, ge=0, le=1)

    # Nested specs:
    ArchitecturalPrecast: ArchitecturalPrecastV1 | None = None
    StructuralPrecast: StructuralPrecastV1 | None = None
    UtilityUndergroundPrecast: UtilityUndergroundPrecastV1 | None = None
    CivilPrecast: CivilPrecastV1 | None = None
