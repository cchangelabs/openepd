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
    "BathtubsRangeV1",
    "FaucetsRangeV1",
    "FireProtectionPipingRangeV1",
    "FireSprinklersRangeV1",
    "FireSuppressionRangeV1",
    "OtherPlumbingFixturesRangeV1",
    "PipingRangeV1",
    "PlumbingEquipmentRangeV1",
    "PlumbingFixturesRangeV1",
    "PlumbingRangeV1",
    "StorageTanksRangeV1",
    "WaterClosetsRangeV1",
    "WaterHeatersRangeV1",
)

import pydantic

from openepd.model.common import RangeAmount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import FireProtectionPipingMaterial, PipingAnsiSchedule, PlumbingPipingMaterial
from openepd.model.validation.quantity import AmountRangeLengthMm

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class BathtubsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Bathtubs.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FaucetsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Faucets.

    Range version.
    """

    _EXT_VERSION = "1.0"


class OtherPlumbingFixturesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Other plumbing fixtures.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WaterClosetsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Water Closets.

    Range version.
    """

    _EXT_VERSION = "1.0"


class FireProtectionPipingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    System of pipes used to supply fire-suppression fluids to homes and/or businesses.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    piping_diameter: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    mass_per_unit_length: RangeAmount | None = pydantic.Field(default=None, description="")
    piping_ansi_schedule: list[PipingAnsiSchedule] | None = pydantic.Field(default=None, description="")
    fire_protection_piping_material: list[FireProtectionPipingMaterial] | None = pydantic.Field(
        default=None, description=""
    )


class FireSprinklersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fire sprinklers.

    Range version.
    """

    _EXT_VERSION = "1.0"


class StorageTanksRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Storage tanks.

    Range version.
    """

    _EXT_VERSION = "1.0"


class WaterHeatersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Water heaters.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PlumbingFixturesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Residential and commercial water closets, urinals, lavatories, sinks, bathtubs, showers, faucets, etc.

    Range version.
    """

    _EXT_VERSION = "1.0"

    Bathtubs: BathtubsRangeV1 | None = None
    Faucets: FaucetsRangeV1 | None = None
    OtherPlumbingFixtures: OtherPlumbingFixturesRangeV1 | None = None
    WaterClosets: WaterClosetsRangeV1 | None = None


class FireSuppressionRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Systems used to extinguish, control, or prevent fires.

    Range version.
    """

    _EXT_VERSION = "1.0"

    FireProtectionPiping: FireProtectionPipingRangeV1 | None = None
    FireSprinklers: FireSprinklersRangeV1 | None = None


class PipingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Piping.

    System of pipes used to provide water and fuel, remove wastewater, allow venting of gases, or supply
    fire-suppression fluids to homes, businesses, or other facilities.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    piping_diameter: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    mass_per_unit_length: RangeAmount | None = pydantic.Field(default=None, description="")
    piping_ansi_schedule: list[PipingAnsiSchedule] | None = pydantic.Field(default=None, description="")
    plumbing_piping_material: list[PlumbingPipingMaterial] | None = pydantic.Field(default=None, description="")


class PlumbingEquipmentRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Water softeners, filtration equipment, water heaters, and other plumbing equipment.

    Range version.
    """

    _EXT_VERSION = "1.0"

    StorageTanks: StorageTanksRangeV1 | None = None
    WaterHeaters: WaterHeatersRangeV1 | None = None


class PlumbingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Residential and commercial plumbing equipment and fixtures.

    Range version.
    """

    _EXT_VERSION = "1.0"

    PlumbingFixtures: PlumbingFixturesRangeV1 | None = None
    FireSuppression: FireSuppressionRangeV1 | None = None
    Piping: PipingRangeV1 | None = None
    PlumbingEquipment: PlumbingEquipmentRangeV1 | None = None
