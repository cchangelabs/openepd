#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
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
    _CATEGORY_META = CategoryMeta(
        unique_name="IntumescentFireproofing",
        display_name="Intumescent Fire Resistive Material",
        short_name="Intumescent",
        historical_names=["Fire and Smoke Protection >> Applied Fireproofing >> Intumescent"],
        description="Fireproofing material applied to structural materials, which swells as a result of heat exposure, thus increasing in volume and decreasing in density.",
        masterformat="07 81 20 Intumescent Fireproofing",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    material_type: IntumescentFireproofingMaterialType | None = pydantic.Field(
        default=None, description="", examples=["Epoxy"]
    )


class SprayFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Spray fireproofing.

    A passive fire protection system that reduces the rate of temperature increase in concrete or steel during a fire.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SprayFireproofing",
        display_name="Spray-Applied Fire Resistive Material",
        short_name="Spray-Applied",
        historical_names=["Fire and Smoke Protection >> Applied Fireproofing >> Spray-Applied"],
        description="A passive fire protection system that reduces the rate of temperature increase in concrete or steel during a fire",
        masterformat="07 81 10 Spray-Applied Fireproofing",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    material_type: SprayFireproofingMaterialType | None = pydantic.Field(
        default=None, description="", examples=["Gypsum-based"]
    )
    density: SprayFireproofingDensity | None = pydantic.Field(default=None, description="", examples=["Standard"])


class AppliedFireproofingV1(BaseOpenEpdHierarchicalSpec):
    """
    Fireproofing material applied to structural materials.

    Materials include: cement aggregate, cementitious, magnesium-oxychloride, intumescent, magnesium cement, mineral
    fiber, and mineral fiber fireproofing products.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AppliedFireproofing",
        display_name="Applied Fireproofing",
        historical_names=["Fire and Smoke Protection >> Applied Fireproofing"],
        description="Fireproofing material applied to structural materials including: cement aggregate, cementitious, magnesium-oxychloride, intumescent, magnesium cement, mineral fiber, and mineral fiber fireproofing products.",
        masterformat="07 81 00 Applied Fireproofing",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["10 mm"])

    # Nested specs:
    IntumescentFireproofing: IntumescentFireproofingV1 | None = None
    SprayFireproofing: SprayFireproofingV1 | None = None


class FirestoppingV1(BaseOpenEpdHierarchicalSpec):
    """
    Seals and protects openings and joints in fire rate assemblies.

    Typically sealants, sprays, and caulks.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Firestopping",
        display_name="Firestopping",
        historical_names=["Fire and Smoke Protection >> Firestopping"],
        description="Seals and protects openings and joints in fire rate assemblies - typically sealants, sprays, and caulks",
        masterformat="07 84 00 Firestopping",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class FireAndSmokeProtectionV1(BaseOpenEpdHierarchicalSpec):
    """
    Fire and smoke protection.

    General category of materials whose function is to provide protection of materials, spaces, and occupants from
    fire and smoke damage.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FireAndSmokeProtection",
        display_name="Fire and Smoke Protection",
        description="General category of materials whose function is to provide protection of materials, spaces, and occupants from fire and smoke damage ",
        masterformat="07 80 00 Fire and Smoke Protection",
        declared_unit=Amount(qty=1, unit="kg"),
    )

    # Nested specs:
    AppliedFireproofing: AppliedFireproofingV1 | None = None
    Firestopping: FirestoppingV1 | None = None
