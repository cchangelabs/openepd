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
from openepd.model.common import Amount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class AcTransformersV1(BaseOpenEpdHierarchicalSpec):
    """Equipment for transforming between higher and lower voltage AC power."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AcTransformers",
        display_name="AC Transformers",
        short_name="Transformers",
        historical_names=["Transmission >> Transformers"],
        description="Equipment for transforming between higher and lower voltage AC power.",
        masterformat="33 73 00 Utility Transformers",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalInsulatorsV1(BaseOpenEpdHierarchicalSpec):
    """Passive electrical isolation."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalInsulators",
        display_name="ElectricalInsulators",
        short_name="Insulators",
        historical_names=["Transmission >> Insulators"],
        description="Passive electrical isolation.",
        masterformat="33 71 00 Electrical Utility Transmission and Distribution",
        declared_unit=Amount(qty=1, unit="item"),
    )


class ElectricalSubstationsV1(BaseOpenEpdHierarchicalSpec):
    """Electrical substations performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalSubstations",
        display_name="Electrical Substations",
        short_name="Substations",
        historical_names=["Transmission >> Substations"],
        description="Substations for electricity transmission and distribution.",
        masterformat="33 72 00 Utility Substations",
    )


class ElectricalSwitchgearV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for interrupting and controlling high-power electrical flows.

    Used for protection, isolation, or control of electrical equipment.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalSwitchgear",
        display_name="Electrical Switchgear",
        short_name="Switchgear",
        historical_names=["Transmission >> Switchgear"],
        description="Equipment for interrupting and controlling high-power electrical flows for protection, isolation, or control of electrical equipment.",
        masterformat="33 77 00 Medium-Voltage Utility Switchgear and Protection Devices",
    )


class PowerCablingV1(BaseOpenEpdHierarchicalSpec):
    """High-voltage electrical cabling."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="PowerCabling",
        display_name="PowerCabling",
        short_name="Cabling",
        historical_names=["Transmission >> Cabling"],
        description="High-voltage electrical cabling.",
        masterformat="33 71 00 Electrical Utility Transmission and Distribution",
        declared_unit=Amount(qty=1, unit="m"),
    )


class ElectricalTransmissionAndDistributionEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Electrical Transmission & Distribution Equipment."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="ElectricalTransmissionAndDistributionEquipment",
        display_name="Electrical Transmission & Distribution Equipment",
        short_name="Transmission",
        historical_names=["Transmission"],
        description="Electrical Transmission & Distribution Equipment.",
        masterformat="33 70 00 Electrical Utilities",
    )

    # Nested specs:
    AcTransformers: AcTransformersV1 | None = None
    ElectricalInsulators: ElectricalInsulatorsV1 | None = None
    ElectricalSubstations: ElectricalSubstationsV1 | None = None
    ElectricalSwitchgear: ElectricalSwitchgearV1 | None = None
    PowerCabling: PowerCablingV1 | None = None
