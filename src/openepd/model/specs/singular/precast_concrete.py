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
import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, BaseOpenEpdSpec
from openepd.model.validation.quantity import PressureMPaStr


class StructuralPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Structural Precast Concrete."""

    wall: bool | None = pydantic.Field(
        description="Precast solid wall elements, including thin shell",
        examples=[True],
        default=None,
    )
    solid_slab: bool | None = pydantic.Field(
        description="Precast slabs used for floor or roof applications",
        examples=[True],
        default=None,
    )
    hollowcore: bool | None = pydantic.Field(
        description="Precast slabs with tubular voids, typically used flooring applications",
        examples=[True],
        default=None,
    )
    beam: bool | None = pydantic.Field(
        description="Precast structural beams for carrying or transferring loads; includes girders",
        examples=[True],
        default=None,
    )
    column: bool | None = pydantic.Field(
        description="Precast structural columns for carrying or transferring loads",
        examples=[True],
        default=None,
    )
    stairs: bool | None = pydantic.Field(
        description="Staircases made of precast concrete components",
        examples=[True],
        default=None,
    )
    balcony: bool | None = pydantic.Field(
        description="Balcony slabs made from precast concrete",
        examples=[True],
        default=None,
    )
    pile: bool | None = pydantic.Field(
        description="Precast concrete structural foundation elements used to support offshore structures such as bridges, oil rigs, and floating airports",
        examples=[True],
        default=None,
    )


class UtilityPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Utility Underground Precast Concrete."""

    manhole: bool | None = pydantic.Field(
        description="Precast barrel-shaped chambers used for wastewater management and access management",
        examples=[True],
        default=None,
    )
    retaining_wall: bool | None = pydantic.Field(
        description="Precast concrete structures for retaining soil",
        examples=[True],
        default=None,
    )
    box_culvert: bool | None = pydantic.Field(
        description="A precast concrete structure commonly used to channel water, primarily as part of a drainage system",
        examples=[True],
        default=None,
    )


class ArchitecturalPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Architectural Precast Concrete."""

    wall: bool | None = pydantic.Field(
        description="Precast solid wall elements, including thin shell",
        examples=[True],
        default=None,
    )


class CivilPrecastElementType(BaseOpenEpdSpec):
    """Precast element types for Civil Precast Concrete."""

    beam: bool | None = pydantic.Field(
        description="Precast structural beams for carrying or transferring loads; includes girders",
        examples=[True],
        default=None,
    )
    manhole: bool | None = pydantic.Field(
        description="Precast barrel-shaped chambers used for wastewater management and access management",
        examples=[True],
        default=None,
    )
    retaining_wall: bool | None = pydantic.Field(
        description="Precast concrete structures for retaining soil",
        examples=[True],
        default=None,
    )
    rail_sleeper: bool | None = pydantic.Field(
        description="Rectangular supports for the rails on railroad tracks, which transfer loads to the track ballast and subgrade and keep the rails spaced to the correct gauge. Also called railroad ties",
        examples=[True],
        default=None,
    )
    box_culvert: bool | None = pydantic.Field(
        description="A precast concrete structure commonly used to channel water, primarily as part of a drainage system",
        examples=[True],
        default=None,
    )
    pile: bool | None = pydantic.Field(
        description="Precast concrete structural foundation elements used to support offshore structures such as bridges, oil rigs, and floating airports",
        examples=[True],
        default=None,
    )
    road_barriers: bool | None = pydantic.Field(
        description="Precast Vehicle and Traffic Barriers",
        examples=[True],
        default=None,
    )


class ArchitecturalPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete cladding used for architectural purposes."""

    _EXT_VERSION = "1.1"

    element_type: ArchitecturalPrecastElementType | None = pydantic.Field(
        default=None,
        description="Precast element type used for architectural applications.",
    )


class StructuralPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete used for structural purposes."""

    _EXT_VERSION = "1.1"

    element_type: StructuralPrecastElementType | None = pydantic.Field(
        default=None,
        description="Precast element type used for structural applications.",
    )


class UtilityUndergroundPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete for utility vaults, manhole, drain inlets. Excludes piping."""

    _EXT_VERSION = "1.1"

    element_type: UtilityPrecastElementType | None = pydantic.Field(
        default=None,
        description="Precast element type used for utility underground applications.",
    )


class CivilPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete used for civil engineering applications including bridges, highways, and railroads."""

    _EXT_VERSION = "1.0"

    element_type: CivilPrecastElementType | None = pydantic.Field(
        default=None,
        description="Precast element type used as civil engineering components.",
    )


class PrecastConcreteV1(BaseOpenEpdHierarchicalSpec):
    """General category for precast concrete components."""

    _EXT_VERSION = "1.1"

    # Own fields:
    lightweight: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    concrete_compressive_strength_28d: PressureMPaStr | None = pydantic.Field(
        default=None, description="", examples=["1 MPa"]
    )
    insulated: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    gfrc: bool | None = pydantic.Field(
        default=None,
        description="Glass Fiber Reinforced Concrete is fiber-reinforced concrete sometimes used in "
        "architectural panels",
        examples=[True],
    )
    steel_mass_percentage: float | None = pydantic.Field(default=None, description="", examples=[0.5], ge=0, le=1)

    # Nested specs:
    ArchitecturalPrecast: ArchitecturalPrecastV1 | None = None
    StructuralPrecast: StructuralPrecastV1 | None = None
    UtilityUndergroundPrecast: UtilityUndergroundPrecastV1 | None = None
    CivilPrecast: CivilPrecastV1 | None = None
