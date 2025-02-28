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

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import FireProtectionPipingMaterial, PipingAnsiSchedule, PlumbingPipingMaterial
from openepd.model.validation.quantity import LengthMmStr, MassPerLengthStr


class BathtubsV1(BaseOpenEpdHierarchicalSpec):
    """Bathtubs."""

    _EXT_VERSION = "1.0"


class FaucetsV1(BaseOpenEpdHierarchicalSpec):
    """Faucets."""

    _EXT_VERSION = "1.0"


class OtherPlumbingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Other plumbing fixtures."""

    _EXT_VERSION = "1.0"


class WaterClosetsV1(BaseOpenEpdHierarchicalSpec):
    """Water Closets."""

    _EXT_VERSION = "1.0"


class FireProtectionPipingV1(BaseOpenEpdHierarchicalSpec):
    """System of pipes used to supply fire-suppression fluids to homes and/or businesses."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["6 mm"])
    piping_diameter: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["120 mm"])
    mass_per_unit_length: MassPerLengthStr | None = pydantic.Field(default=None, description="", examples=["1 kg / m"])
    piping_ansi_schedule: PipingAnsiSchedule | None = pydantic.Field(default=None, description="", examples=["5"])
    fire_protection_piping_material: FireProtectionPipingMaterial | None = pydantic.Field(
        default=None, description="", examples=["PVC"]
    )


class FireSprinklersV1(BaseOpenEpdHierarchicalSpec):
    """Fire sprinklers."""

    _EXT_VERSION = "1.0"


class StorageTanksV1(BaseOpenEpdHierarchicalSpec):
    """Storage tanks."""

    _EXT_VERSION = "1.0"


class WaterHeatersV1(BaseOpenEpdHierarchicalSpec):
    """Water heaters."""

    _EXT_VERSION = "1.0"


class PlumbingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Residential and commercial water closets, urinals, lavatories, sinks, bathtubs, showers, faucets, etc."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Bathtubs: BathtubsV1 | None = None
    Faucets: FaucetsV1 | None = None
    OtherPlumbingFixtures: OtherPlumbingFixturesV1 | None = None
    WaterClosets: WaterClosetsV1 | None = None


class FireSuppressionV1(BaseOpenEpdHierarchicalSpec):
    """Systems used to extinguish, control, or prevent fires."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    FireProtectionPiping: FireProtectionPipingV1 | None = None
    FireSprinklers: FireSprinklersV1 | None = None


class PipingV1(BaseOpenEpdHierarchicalSpec):
    """
    Piping.

    System of pipes used to provide water and fuel, remove wastewater, allow venting of gases, or supply
    fire-suppression fluids to homes, businesses, or other facilities.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["6 mm"])
    piping_diameter: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["120 mm"])
    mass_per_unit_length: MassPerLengthStr | None = pydantic.Field(default=None, description="", examples=["1 kg / m"])
    piping_ansi_schedule: PipingAnsiSchedule | None = pydantic.Field(default=None, description="", examples=["5"])
    plumbing_piping_material: PlumbingPipingMaterial | None = pydantic.Field(
        default=None, description="", examples=["PVC"]
    )


class PlumbingEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Water softeners, filtration equipment, water heaters, and other plumbing equipment."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    StorageTanks: StorageTanksV1 | None = None
    WaterHeaters: WaterHeatersV1 | None = None


class PlumbingV1(BaseOpenEpdHierarchicalSpec):
    """Residential and commercial plumbing equipment and fixtures."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PlumbingFixtures: PlumbingFixturesV1 | None = None
    FireSuppression: FireSuppressionV1 | None = None
    Piping: PipingV1 | None = None
    PlumbingEquipment: PlumbingEquipmentV1 | None = None
