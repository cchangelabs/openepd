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
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import PressureMPaStr


class ArchitecturalPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete cladding used for architectural purposes."""

    _EXT_VERSION = "1.0"


class StructuralPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete used for structural purposes."""

    _EXT_VERSION = "1.0"


class UtilityUndergroundPrecastV1(BaseOpenEpdHierarchicalSpec):
    """Precast concrete for utility vaults, manhole, drain inlets. Excludes piping."""

    _EXT_VERSION = "1.0"


class PrecastConcreteV1(BaseOpenEpdHierarchicalSpec):
    """General category for precast concrete components."""

    _EXT_VERSION = "1.0"

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
