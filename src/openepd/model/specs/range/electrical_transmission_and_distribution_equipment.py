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
    "AcTransformersRangeV1",
    "ElectricalInsulatorsRangeV1",
    "ElectricalSubstationsRangeV1",
    "ElectricalSwitchgearRangeV1",
    "ElectricalTransmissionAndDistributionEquipmentRangeV1",
    "PowerCablingRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class AcTransformersRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for transforming between higher and lower voltage AC power.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricalInsulatorsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Passive electrical isolation.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricalSubstationsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical substations performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricalSwitchgearRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Equipment for interrupting and controlling high-power electrical flows.

    Used for protection, isolation, or control of electrical equipment.

    Range version.
    """

    _EXT_VERSION = "1.0"


class PowerCablingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    High-voltage electrical cabling.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ElectricalTransmissionAndDistributionEquipmentRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical Transmission & Distribution Equipment.

    Range version.
    """

    _EXT_VERSION = "1.0"

    AcTransformers: AcTransformersRangeV1 | None = None
    ElectricalInsulators: ElectricalInsulatorsRangeV1 | None = None
    ElectricalSubstations: ElectricalSubstationsRangeV1 | None = None
    ElectricalSwitchgear: ElectricalSwitchgearRangeV1 | None = None
    PowerCabling: PowerCablingRangeV1 | None = None
