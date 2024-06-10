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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class AcTransformersV1(BaseOpenEpdHierarchicalSpec):
    """Equipment for transforming between higher and lower voltage AC power."""

    _EXT_VERSION = "1.0"


class ElectricalInsulatorsV1(BaseOpenEpdHierarchicalSpec):
    """Passive electrical isolation."""

    _EXT_VERSION = "1.0"


class ElectricalSubstationsV1(BaseOpenEpdHierarchicalSpec):
    """Electrical substations performance specification."""

    _EXT_VERSION = "1.0"


class ElectricalSwitchgearV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for interrupting and controlling high-power electrical flows.

    Used for protection, isolation, or control of electrical equipment.
    """

    _EXT_VERSION = "1.0"


class PowerCablingV1(BaseOpenEpdHierarchicalSpec):
    """High-voltage electrical cabling."""

    _EXT_VERSION = "1.0"


class ElectricalTransmissionAndDistributionEquipmentV1(BaseOpenEpdHierarchicalSpec):
    """Electrical Transmission & Distribution Equipment."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AcTransformers: AcTransformersV1 | None = None
    ElectricalInsulators: ElectricalInsulatorsV1 | None = None
    ElectricalSubstations: ElectricalSubstationsV1 | None = None
    ElectricalSwitchgear: ElectricalSwitchgearV1 | None = None
    PowerCabling: PowerCablingV1 | None = None
