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
__all__ = (
    "ExteriorSpecialtiesRangeV1",
    "FireplacesStovesRangeV1",
    "InformationSpecialtiesRangeV1",
    "InteriorSpecialtiesRangeV1",
    "OtherSpecialtiesRangeV1",
    "ProtectiveRailsGuardsRangeV1",
    "ProtectiveSurfaceCoveringsRangeV1",
    "SafetySpecialtiesRangeV1",
    "SpecialtiesRangeV1",
    "StorageSpecialtiesRangeV1",
    "WallDoorProtectionRangeV1",
)


from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class ProtectiveRailsGuardsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Linear handrails, guards, and protective strips for interior areas where extra protection is needed.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ProtectiveSurfaceCoveringsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Protective wall panels for interior areas where extra protection is needed.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WallDoorProtectionRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Items for protection of walls and doors from wear, traffic, or impact.

    Range version.
    """

    _EXT_VERSION = "1.0"

    ProtectiveRailsGuards: ProtectiveRailsGuardsRangeV1 | None = None
    ProtectiveSurfaceCoverings: ProtectiveSurfaceCoveringsRangeV1 | None = None


class InformationSpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Information specialties.

    Range version.
    """

    _EXT_VERSION = "1.0"


class InteriorSpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Interior specialties.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FireplacesStovesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fireplaces and stoves.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SafetySpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Safety specialties.

    Range version.
    """

    _EXT_VERSION = "1.0"


class StorageSpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Storage specialties.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ExteriorSpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Specialties that add to building aesthetics and weather protection.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherSpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other specialties.

    Range version.
    """

    _EXT_VERSION = "1.0"


class SpecialtiesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Construction specialties.

    Range version.
    """

    _EXT_VERSION = "1.0"

    WallDoorProtection: WallDoorProtectionRangeV1 | None = None
    InformationSpecialties: InformationSpecialtiesRangeV1 | None = None
    InteriorSpecialties: InteriorSpecialtiesRangeV1 | None = None
    FireplacesStoves: FireplacesStovesRangeV1 | None = None
    SafetySpecialties: SafetySpecialtiesRangeV1 | None = None
    StorageSpecialties: StorageSpecialtiesRangeV1 | None = None
    ExteriorSpecialties: ExteriorSpecialtiesRangeV1 | None = None
    OtherSpecialties: OtherSpecialtiesRangeV1 | None = None
