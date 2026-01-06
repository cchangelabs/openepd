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
from openepd.model.specs.enums import FireProtectionPipingMaterial, PipingAnsiSchedule, PlumbingPipingMaterial
from openepd.model.validation.quantity import LengthMmStr, MassPerLengthStr


class BathtubsV1(BaseOpenEpdHierarchicalSpec):
    """Bathtubs."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Bathtubs",
        display_name="Bathtubs",
        historical_names=["Plumbing >> Plumbing fixtures >> Bathtubs"],
        description="Bathtubs.",
        masterformat="22 42 19 Bathtubs",
        declared_unit=Amount(qty=1, unit="item"),
    )


class FaucetsV1(BaseOpenEpdHierarchicalSpec):
    """Faucets."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Faucets",
        display_name="Faucets",
        historical_names=["Plumbing >> Plumbing fixtures >> Faucets"],
        description="Faucets.",
        masterformat="22 42 39 Commercial Faucets",
        declared_unit=Amount(qty=1, unit="item"),
    )


class OtherPlumbingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Other plumbing fixtures."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="OtherPlumbingFixtures",
        display_name="Other Plumbing Fixtures",
        short_name="Other",
        historical_names=["Plumbing >> Plumbing fixtures >> Other"],
        description="Other plumbing fixtures.",
        masterformat="22 40 00 Plumbing Fixtures",
        declared_unit=Amount(qty=1, unit="item"),
    )


class WaterClosetsV1(BaseOpenEpdHierarchicalSpec):
    """Water Closets."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WaterClosets",
        display_name="Water Closets",
        historical_names=["Plumbing >> Plumbing fixtures >> Water Closets"],
        description="Water Closets.",
        masterformat="22 42 13 Commercial Water Closets",
        declared_unit=Amount(qty=1, unit="item"),
    )


class FireProtectionPipingV1(BaseOpenEpdHierarchicalSpec):
    """System of pipes used to supply fire-suppression fluids to homes and/or businesses."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FireProtectionPiping",
        display_name="Fire Protection Piping",
        short_name="Piping",
        historical_names=["Plumbing >> Fire Suppression >> Piping"],
        description="System of pipes used to supply fire-suppression fluids to homes and/or businesses.",
        masterformat="21 11 00 Facility Fire-Suppression Water-Service Piping",
        declared_unit=Amount(qty=1, unit="m"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="FireSprinklers",
        display_name="Fire Sprinklers",
        historical_names=["Plumbing >> Fire Suppression >> Fire Sprinklers"],
        description="Fire sprinklers.",
        masterformat="21 13 00 Fire Sprinkler Systems",
        declared_unit=Amount(qty=1, unit="item"),
    )


class StorageTanksV1(BaseOpenEpdHierarchicalSpec):
    """Storage tanks."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="StorageTanks",
        display_name="Storage Tanks",
        historical_names=["Plumbing >> Plumbing Equipment >> Storage Tanks"],
        description="Storage tanks.",
        masterformat="22 12 00 Facility Potable-Water Storage Tanks",
        declared_unit=Amount(qty=1, unit="item"),
    )


class WaterHeatersV1(BaseOpenEpdHierarchicalSpec):
    """Water heaters."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="WaterHeaters",
        display_name="Water Heaters",
        historical_names=["Plumbing >> Plumbing Equipment >> Water Heaters"],
        description="Water heaters.",
        masterformat="22 34 00 Fuel-Fired Domestic Water Heaters",
        declared_unit=Amount(qty=1, unit="item"),
    )


class PlumbingFixturesV1(BaseOpenEpdHierarchicalSpec):
    """Residential and commercial water closets, urinals, lavatories, sinks, bathtubs, showers, faucets, etc."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PlumbingFixtures",
        display_name="Plumbing fixtures",
        historical_names=["Plumbing >> Plumbing fixtures"],
        description="Residential and commercial water closets, urinals, lavatories, sinks, bathtubs, showers, faucets, etc.",
        masterformat="22 40 00 Plumbing Fixtures",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    Bathtubs: BathtubsV1 | None = None
    Faucets: FaucetsV1 | None = None
    OtherPlumbingFixtures: OtherPlumbingFixturesV1 | None = None
    WaterClosets: WaterClosetsV1 | None = None


class FireSuppressionV1(BaseOpenEpdHierarchicalSpec):
    """Systems used to extinguish, control, or prevent fires."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="FireSuppression",
        display_name="Fire Suppression",
        historical_names=["Plumbing >> Fire Suppression"],
        description="Systems used to extinguish, control, or prevent fires.",
        masterformat="21 00 00 Fire Suppression",
        declared_unit=Amount(qty=1, unit="item"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="Piping",
        display_name="Plumbing Piping",
        short_name="Piping",
        historical_names=["OtherMaterials >> Piping", "Other Materials >> Piping"],
        description="System of pipes used to provide water and fuel, remove wastewater, allow venting of gases, or supply fire-suppression fluids to homes, businesses, or other facilities.",
        masterformat="22 10 00 Plumbing Piping Systems",
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="PlumbingEquipment",
        display_name="Plumbing Equipment",
        historical_names=["Plumbing >> Plumbing Equipment"],
        description="Water softeners, filtration equipment, water heaters, and other plumbing equipment.",
        masterformat="22 30 00 Plumbing Equipment",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    StorageTanks: StorageTanksV1 | None = None
    WaterHeaters: WaterHeatersV1 | None = None


class PlumbingV1(BaseOpenEpdHierarchicalSpec):
    """Residential and commercial plumbing equipment and fixtures."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Plumbing",
        display_name="Plumbing",
        description="Residential and commercial plumbing equipment and fixtures.",
        masterformat="22 00 00 Plumbing",
        declared_unit=Amount(qty=1, unit="item"),
    )

    # Nested specs:
    PlumbingFixtures: PlumbingFixturesV1 | None = None
    FireSuppression: FireSuppressionV1 | None = None
    Piping: PipingV1 | None = None
    PlumbingEquipment: PlumbingEquipmentV1 | None = None
