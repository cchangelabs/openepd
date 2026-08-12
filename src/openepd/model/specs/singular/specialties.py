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
from openepd.model.category import CategoryMeta
from openepd.model.common import NonNegativeAmount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class ProtectiveRailsGuardsV1(BaseOpenEpdHierarchicalSpec):
    """Linear handrails, guards, and protective strips for interior areas where extra protection is needed."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ProtectiveRailsGuards",
        display_name="Wall & Door Protective Rails & Guards",
        short_name="Rails & Guards",
        description=(
            "Linear handrails, guards, and protective strips for interior areas where extra protection is needed "
            "against wear, traffic, or impact."
        ),
        masterformat="10 26 00 Wall and Door Protection",
        declared_unit=NonNegativeAmount(qty=1, unit="m"),
    )


class ProtectiveSurfaceCoveringsV1(BaseOpenEpdHierarchicalSpec):
    """Protective wall panels for interior areas where extra protection is needed."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ProtectiveSurfaceCoverings",
        display_name="Wall & Door Protective Coverings",
        short_name="Coverings",
        description=(
            "Protective wall panels for interior areas where extra protection is needed against wear, traffic, "
            "or impact."
        ),
        masterformat="10 26 00 Wall and Door Protection",
        declared_unit=NonNegativeAmount(qty=1, unit="m^2"),
    )


class WallDoorProtectionV1(BaseOpenEpdHierarchicalSpec):
    """Items for protection of walls and doors from wear, traffic, or impact."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WallDoorProtection",
        display_name="Wall & Door Protection",
        short_name="Wall & Door Protection",
        description="Items for protection of walls and doors from wear, traffic, or impact.",
        masterformat="10 26 00 Wall and Door Protection",
    )

    # Nested specs:
    ProtectiveRailsGuards: ProtectiveRailsGuardsV1 | None = None
    ProtectiveSurfaceCoverings: ProtectiveSurfaceCoveringsV1 | None = None


class InformationSpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Information specialties."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="InformationSpecialties",
        display_name="Information Specialties",
        short_name="Information",
        masterformat="10 10 00 Information Specialties",
    )


class InteriorSpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Interior specialties."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="InteriorSpecialties",
        display_name="Interior Specialties",
        short_name="Interior",
        masterformat="10 20 00 Interior Specialties",
    )


class FireplacesStovesV1(BaseOpenEpdHierarchicalSpec):
    """Fireplaces and stoves."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FireplacesStoves",
        display_name="Fireplaces and Stoves",
        short_name="Fireplaces & Stoves",
        masterformat="10 30 00 Fireplaces and Stoves",
    )


class SafetySpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Safety specialties."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SafetySpecialties",
        display_name="Safety Specialties",
        short_name="Safety",
        masterformat="10 40 00 Safety Specialties",
    )


class StorageSpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Storage specialties."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="StorageSpecialties",
        display_name="Storage Specialties",
        short_name="Storage",
        masterformat="10 50 00 Storage Specialties",
    )


class ExteriorSpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Specialties that add to building aesthetics and weather protection."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ExteriorSpecialties",
        display_name="Exterior Specialties",
        short_name="Exterior",
        description=(
            "Specialties add to the aesthetics of the building, protect people and the building from the weather, "
            "and flag poles."
        ),
        masterformat="10 70 00 Exterior Specialties",
    )


class OtherSpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Other specialties."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherSpecialties",
        display_name="Other Specialties",
        short_name="Other",
        masterformat="10 80 00 Other Specialties",
    )


class SpecialtiesV1(BaseOpenEpdHierarchicalSpec):
    """Construction specialties."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Specialties",
        display_name="Construction Specialties",
        short_name="Specialties",
        description="Construction Specialties",
        masterformat="10 00 00 Specialties",
    )

    # Nested specs:
    WallDoorProtection: WallDoorProtectionV1 | None = None
    InformationSpecialties: InformationSpecialtiesV1 | None = None
    InteriorSpecialties: InteriorSpecialtiesV1 | None = None
    FireplacesStoves: FireplacesStovesV1 | None = None
    SafetySpecialties: SafetySpecialtiesV1 | None = None
    StorageSpecialties: StorageSpecialtiesV1 | None = None
    ExteriorSpecialties: ExteriorSpecialtiesV1 | None = None
    OtherSpecialties: OtherSpecialtiesV1 | None = None
