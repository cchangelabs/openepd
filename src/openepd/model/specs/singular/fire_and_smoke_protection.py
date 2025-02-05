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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    IntumescentFireproofingMaterialType,
    SprayFireproofingDensity,
    SprayFireproofingMaterialType,
)
from openepd.model.validation.quantity import LengthMmStr


class IntumescentFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Fireproofing material applied to structural materials, which swells as a result of heat exposure.

    As a result it increases in volume and decreasing in density.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    material_type: IntumescentFireproofingMaterialType | None = pyd.Field(default=None, description="", example="Epoxy")


class SprayFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Spray fireproofing.

    A passive fire protection system that reduces the rate of temperature increase in concrete or steel during a fire.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    material_type: SprayFireproofingMaterialType | None = pyd.Field(
        default=None, description="", example="Gypsum-based"
    )
    density: SprayFireproofingDensity | None = pyd.Field(default=None, description="", example="Standard")


class AppliedFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Fireproofing material applied to structural materials.

    Materials include: cement aggregate, cementitious, magnesium-oxychloride, intumescent, magnesium cement, mineral
    fiber, and mineral fiber fireproofing products.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="10 mm")

    # Nested specs:
    IntumescentFireproofing: IntumescentFireproofingV1 | None = None
    SprayFireproofing: SprayFireproofingV1 | None = None


class FirestoppingV1(BaseOpenEpdHierarchicalSpec):
    """
    Seals and protects openings and joints in fire rate assemblies.

    Typically sealants, sprays, and caulks.
    """

    _EXT_VERSION = "1.0"


class FireAndSmokeProtectionV1(BaseOpenEpdHierarchicalSpec):
    """
    Fire and smoke protection.

    General category of materials whose function is to provide protection of materials, spaces, and occupants from
    fire and smoke damage.
    """

    _EXT_VERSION = "1.0"

    # Nested specs:
    AppliedFireproofing: AppliedFireproofingV1 | None = None
    Firestopping: FirestoppingV1 | None = None
