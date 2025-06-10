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
    "CabinetsRacksAndEnclosuresRangeV1",
    "CommunicationsConduitRangeV1",
    "DataCablingRangeV1",
    "FloorBoxesAndAccessoriesRangeV1",
    "NetworkInfrastructureRangeV1",
    "NetworkingCableTraysRangeV1",
    "NetworkingRacewaysRangeV1",
    "PDURangeV1",
)

import pydantic

from openepd.model.common import RangeInt
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import (
    CableTraysMaterial,
    CablingCategory,
    CablingFireRating,
    CablingJacketMaterial,
    ConduitMaterial,
    FloorBoxCoverMaterial,
    FloorBoxFloorMaterial,
    FloorBoxMaterial,
    PduTechnology,
    RacewaysMaterial,
    RackType,
)
from openepd.model.validation.quantity import AmountRangeElectricalCurrent, AmountRangeLengthMm, AmountRangeMass

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


class PDURangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Devices with multiple outputs designed to distribute power, often in a data center cabinet.

    Range version.
    """

    _EXT_VERSION = "1.0"

    amperage: AmountRangeElectricalCurrent | None = pydantic.Field(default=None, description="")
    outlet_level_metering: bool | None = pydantic.Field(default=None, description="")
    outlet_level_switching: bool | None = pydantic.Field(default=None, description="")
    pdu_technology: list[PduTechnology] | None = pydantic.Field(default=None, description="")
    pdu_outlets: RangeInt | None = pydantic.Field(default=None, description="")


class CabinetsRacksAndEnclosuresRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Physical support upon which network equipment is mounted. Includes cabinets, racks, frames, and enclosures.

    Range version.
    """

    _EXT_VERSION = "1.0"

    static_load: AmountRangeMass | None = pydantic.Field(default=None, description="")
    total_racking_units: RangeInt | None = pydantic.Field(default=None, description="")
    rack_type: list[RackType] | None = pydantic.Field(default=None, description="")


class DataCablingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Telecommunications cabling for buildings.

    Range version.
    """

    _EXT_VERSION = "1.0"

    outdoor: bool | None = pydantic.Field(default=None, description="")
    cabling_category: list[CablingCategory] | None = pydantic.Field(default=None, description="")
    fire_rating: list[CablingFireRating] | None = pydantic.Field(default=None, description="")
    jacket_material: list[CablingJacketMaterial] | None = pydantic.Field(default=None, description="")
    shielded: bool | None = pydantic.Field(default=None, description="Foil or similar electromagnetic shielding")
    armored: bool | None = pydantic.Field(default=None, description="Steel or similar physical armor jacket")
    rohs: bool | None = pydantic.Field(default=None, description="Certified ROHS Compliant")
    reach: bool | None = pydantic.Field(default=None, description="Certified REACH compliant")
    zwtl: bool | None = pydantic.Field(default=None, description="Certified ZWTL compliant")
    connectorized: bool | None = pydantic.Field(
        default=None,
        description="This cable is shipped as a specific length with integrated connectors. Impacts include the connectors for the specific cable length. Connectors add impact similar to 0.1-0.5 additional meters of cable",
    )
    thin_ethernet: bool | None = pydantic.Field(
        default=None,
        description="At least part of this cable has a reduced outer diameter and thinner wires. Thin ethernet cables have handling advantages and tend to have a reduced impact, but also reduced channel length. See TIA 568.2-D Annex G.",
    )


class FloorBoxesAndAccessoriesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical boxes that are installed in the floor.

    Used to provide power and/or data connections to devices in a room or space.

    Range version.
    """

    _EXT_VERSION = "1.0"

    painted: bool | None = pydantic.Field(default=None, description="")
    fire_classified: bool | None = pydantic.Field(
        default=None,
        description="Includes hardware to maintain fire rating of the floor",
    )
    outdoor: bool | None = pydantic.Field(default=None, description="Floor boxes installed in the ground")
    raised: bool | None = pydantic.Field(default=None, description="Used in raised or computer style flooring")
    poke_through: bool | None = pydantic.Field(
        default=None,
        description="Used primarily in retrofit or renovation and will maintain fire rating of the floor",
    )
    cover: bool | None = pydantic.Field(
        default=None,
        description="Floor box cover or lid for use with a separate floor box",
    )
    outlets: RangeInt | None = pydantic.Field(
        default=None,
        description="Number of outlet ports from floor box, including power, data, video, and other connections",
    )
    material: list[FloorBoxMaterial] | None = pydantic.Field(default=None, description="")
    cover_material: list[FloorBoxCoverMaterial] | None = pydantic.Field(default=None, description="")
    floor_material: list[FloorBoxFloorMaterial] | None = pydantic.Field(default=None, description="")


class NetworkingCableTraysRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cable trays.

    Mechanical support systems that provide a rigid structural system for cables used for communication and
    power distribution.

    Range version.
    """

    _EXT_VERSION = "1.0"

    height: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    width: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    depth: AmountRangeLengthMm | None = pydantic.Field(default=None, description="Depth of enclosure system")
    static_load: AmountRangeMass | None = pydantic.Field(default=None, description="Mass that the unit can hold")
    ventilated: bool | None = pydantic.Field(
        default=None, description="At least 40% of the tray base is open to air flow"
    )
    material: list[CableTraysMaterial] | None = pydantic.Field(default=None, description="")


class NetworkingRacewaysRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Surface-mounted systems along the perimeter of walls to route, conceal, and protect cables.

    Often called trunking.

    Range version.
    """

    _EXT_VERSION = "1.0"

    width: AmountRangeLengthMm | None = pydantic.Field(default=None, description="")
    depth: AmountRangeLengthMm | None = pydantic.Field(default=None, description="Depth of enclosure system")
    painted: bool | None = pydantic.Field(default=None, description="")
    divided: bool | None = pydantic.Field(
        default=None,
        description="Dual service raceway for high and low voltage data and power applications",
    )
    raceways_material: list[RacewaysMaterial] | None = pydantic.Field(default=None, description="")


class CommunicationsConduitRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Tubing used to protect and route communications wiring in a building or structure.

    Range version.
    """

    _EXT_VERSION = "1.1"

    nominal_diameter: AmountRangeLengthMm | None = None
    outer_diameter: AmountRangeLengthMm | None = None
    inner_diameter: AmountRangeLengthMm | None = None
    wall_thickness: AmountRangeLengthMm | None = None
    material: list[ConduitMaterial] | None = None


class NetworkInfrastructureRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    General category for network infrastructure products for data centers and commercial and residential buildings.

    Range version.
    """

    _EXT_VERSION = "1.1"

    PDU: PDURangeV1 | None = None
    CabinetsRacksAndEnclosures: CabinetsRacksAndEnclosuresRangeV1 | None = None
    DataCabling: DataCablingRangeV1 | None = None
    FloorBoxesAndAccessories: FloorBoxesAndAccessoriesRangeV1 | None = None
    NetworkingCableTrays: NetworkingCableTraysRangeV1 | None = None
    NetworkingRaceways: NetworkingRacewaysRangeV1 | None = None
    CommunicationsConduit: CommunicationsConduitRangeV1 | None = None
