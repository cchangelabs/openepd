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
__all__ = (
    "IntumescentFireproofingRangeV1",
    "SprayFireproofingRangeV1",
    "AppliedFireproofingRangeV1",
    "FirestoppingRangeV1",
    "FireAndSmokeProtectionRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    IntumescentFireproofingMaterialType,
    SprayFireproofingDensity,
    SprayFireproofingMaterialType,
)
from openepd.model.validation.quantity import AmountRangeLengthMm


class IntumescentFireproofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fireproofing material applied to structural materials, which swells as a result of heat exposure.

    As a result it increases in volume and decreasing in density.

    Range version.
    """

    _EXT_VERSION = "1.0"

    material_type: list[IntumescentFireproofingMaterialType] | None = pyd.Field(default=None, description="")


class SprayFireproofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Spray fireproofing.

    A passive fire protection system that reduces the rate of temperature increase in concrete or steel during a fire.

    Range version.
    """

    _EXT_VERSION = "1.0"

    material_type: list[SprayFireproofingMaterialType] | None = pyd.Field(default=None, description="")
    density: list[SprayFireproofingDensity] | None = pyd.Field(default=None, description="")


class AppliedFireproofingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fireproofing material applied to structural materials.

    Materials include: cement aggregate, cementitious, magnesium-oxychloride, intumescent, magnesium cement, mineral
    fiber, and mineral fiber fireproofing products.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    IntumescentFireproofing: IntumescentFireproofingRangeV1 | None = None
    SprayFireproofing: SprayFireproofingRangeV1 | None = None


class FirestoppingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Seals and protects openings and joints in fire rate assemblies.

    Typically sealants, sprays, and caulks.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FireAndSmokeProtectionRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fire and smoke protection.

    General category of materials whose function is to provide protection of materials, spaces, and occupants from
    fire and smoke damage.

    Range version.
    """

    _EXT_VERSION = "1.0"

    AppliedFireproofing: AppliedFireproofingRangeV1 | None = None
    Firestopping: FirestoppingRangeV1 | None = None
