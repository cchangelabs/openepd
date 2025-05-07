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
    "ArchitecturalPrecastRangeV1",
    "CivilPrecastRangeV1",
    "PrecastConcreteRangeV1",
    "StructuralPrecastRangeV1",
    "UtilityUndergroundPrecastRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.common import RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.singular.precast_concrete import (
    ArchitecturalPrecastElementType,
    CivilPrecastElementType,
    StructuralPrecastElementType,
    UtilityPrecastElementType,
)
from openepd.model.validation.quantity import AmountRangePressureMpa


class ArchitecturalPrecastRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Precast concrete cladding used for architectural purposes.

    Range version.
    """

    _EXT_VERSION = "1.1"

    element_type: ArchitecturalPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used for architectural applications."
    )


class StructuralPrecastRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Precast concrete used for structural purposes.

    Range version.
    """

    _EXT_VERSION = "1.1"

    element_type: StructuralPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used for structural applications."
    )


class UtilityUndergroundPrecastRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Precast concrete for utility vaults, manhole, drain inlets. Excludes piping.

    Range version.
    """

    _EXT_VERSION = "1.1"

    element_type: UtilityPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used for utility underground applications."
    )


class CivilPrecastRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Precast concrete used for civil engineering applications including bridges, highways, and railroads.

    Range version.
    """

    _EXT_VERSION = "1.0"

    element_type: CivilPrecastElementType | None = pyd.Field(
        default=None, description="Precast element type used as civil engineering components."
    )


class PrecastConcreteRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    General category for precast concrete components.

    Range version.
    """

    _EXT_VERSION = "1.1"

    lightweight: bool | None = pyd.Field(default=None, description="")
    concrete_compressive_strength_28d: AmountRangePressureMpa | None = pyd.Field(default=None, description="")
    insulated: bool | None = pyd.Field(default=None, description="")
    gfrc: bool | None = pyd.Field(
        default=None,
        description="Glass Fiber Reinforced Concrete is fiber-reinforced concrete sometimes used in architectural panels",
    )
    steel_mass_percentage: RangeRatioFloat | None = pyd.Field(default=None, description="")
    ArchitecturalPrecast: ArchitecturalPrecastRangeV1 | None = None
    StructuralPrecast: StructuralPrecastRangeV1 | None = None
    UtilityUndergroundPrecast: UtilityUndergroundPrecastRangeV1 | None = None
    CivilPrecast: CivilPrecastRangeV1 | None = None
