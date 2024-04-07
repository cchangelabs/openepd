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
from openepd.model.specs.generated.enums import (
    IntumescentFireproofingMaterialType,
    SprayFireproofingDensity,
    SprayFireproofingMaterialType,
)
from openepd.model.validation.quantity import LengthMmStr, validate_unit_factory


class IntumescentFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """Intumescent fireproofing performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    material_type: IntumescentFireproofingMaterialType | None = pyd.Field(default=None, description="", example="Epoxy")


class SprayFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """Spray fireproofing performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    material_type: SprayFireproofingMaterialType | None = pyd.Field(
        default=None, description="", example="Gypsum-based"
    )
    density: SprayFireproofingDensity | None = pyd.Field(default=None, description="", example="Standard")


class AppliedFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """Applied fireproofing performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))

    # Nested specs:
    IntumescentFireproofing: IntumescentFireproofingV1 | None = None
    SprayFireproofing: SprayFireproofingV1 | None = None


class FirestoppingV1(BaseOpenEpdHierarchicalSpec):
    """Firestopping performance specification."""

    _EXT_VERSION = "1.0"


class FireAndSmokeProtectionV1(BaseOpenEpdHierarchicalSpec):
    """Fire and smoke protection performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AppliedFireproofing: AppliedFireproofingV1 | None = None
    Firestopping: FirestoppingV1 | None = None
