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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.enums import (
    CableTraysMaterial,
    CablingCategory,
    CablingFireRating,
    CablingJacketMaterial,
    FloorBoxCoverMaterial,
    FloorBoxFloorMaterial,
    FloorBoxMaterial,
    PduTechnology,
    RacewaysMaterial,
    RackType,
)
from openepd.model.validation.quantity import ElectricalCurrentStr, LengthMmStr, MassKgStr, validate_unit_factory


class PDUV1(BaseOpenEpdHierarchicalSpec):
    """Devices with multiple outputs designed to distribute power, often in a data center cabinet."""

    _EXT_VERSION = "1.0"

    # Own fields:
    amperage: ElectricalCurrentStr | None = pyd.Field(default=None, description="", example="1 A")
    outlet_level_metering: bool | None = pyd.Field(default=None, description="", example=True)
    outlet_level_switching: bool | None = pyd.Field(default=None, description="", example=True)
    pdu_technology: PduTechnology | None = pyd.Field(default=None, description="", example="Basic")
    pdu_outlets: int | None = pyd.Field(default=None, description="", example=3, le=200)

    _amperage_is_quantity_validator = pyd.validator("amperage", allow_reuse=True)(validate_unit_factory("A"))


class CabinetsRacksAndEnclosuresV1(BaseOpenEpdHierarchicalSpec):
    """Physical support upon which network equipment is mounted. Includes cabinets, racks, frames, and enclosures."""

    _EXT_VERSION = "1.0"

    # Own fields:
    static_load: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    total_racking_units: int | None = pyd.Field(default=None, description="", example=3)
    rack_type: RackType | None = pyd.Field(default=None, description="", example="Cabinet")


class DataCablingV1(BaseOpenEpdHierarchicalSpec):
    """Telecommunications cabling for buildings."""

    _EXT_VERSION = "1.0"

    # Own fields:
    outdoor: bool | None = pyd.Field(default=None, description="", example=True)
    cabling_category: CablingCategory | None = pyd.Field(default=None, description="", example="Cat7")
    fire_rating: CablingFireRating | None = pyd.Field(default=None, description="", example="CMP")
    jacket_material: CablingJacketMaterial | None = pyd.Field(default=None, description="", example="PVC")
    shielded: bool | None = pyd.Field(
        default=None, description="Foil or similar electromagnetic shielding", example=True
    )
    armored: bool | None = pyd.Field(default=None, description="Steel or similar physical armor jacket", example=True)
    rohs: bool | None = pyd.Field(default=None, description="Certified ROHS Compliant", example=True)
    reach: bool | None = pyd.Field(default=None, description="Certified REACH compliant", example=True)
    zwtl: bool | None = pyd.Field(default=None, description="Certified ZWTL compliant", example=True)
    connectorized: bool | None = pyd.Field(
        default=None,
        description="This cable is shipped as a specific length with integrated connectors. Impacts include the "
        "connectors for the specific cable length. Connectors add impact similar to 0.1-0.5 additional "
        "meters of cable",
        example=True,
    )
    thin_ethernet: bool | None = pyd.Field(
        default=None,
        description="At least part of this cable has a reduced outer diameter and thinner wires. Thin ethernet cables "
        "have handling advantages and tend to have a reduced impact, but also reduced channel length. "
        "See TIA 568.2-D Annex G.",
        example=True,
    )


class FloorBoxesAndAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical boxes that are installed in the floor.

    Used to provide power and/or data connections to devices in a room or space.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    painted: bool | None = pyd.Field(default=None, description="", example=True)
    fire_classified: bool | None = pyd.Field(
        default=None, description="Includes hardware to maintain fire rating of the floor", example=True
    )
    outdoor: bool | None = pyd.Field(default=None, description="Floor boxes installed in the ground", example=True)
    raised: bool | None = pyd.Field(default=None, description="Used in raised or computer style flooring", example=True)
    poke_through: bool | None = pyd.Field(
        default=None,
        description="Used primarily in retrofit or renovation and will maintain fire rating of the floor",
        example=True,
    )
    cover: bool | None = pyd.Field(
        default=None, description="Floor box cover or lid for use with a separate floor box", example=True
    )
    outlets: int | None = pyd.Field(
        default=None,
        description="Number of outlet ports from floor box, including power, data, video, and other connections",
        example=3,
        le=16,
    )
    material: FloorBoxMaterial | None = pyd.Field(default=None, description="", example="Metallic Box")
    cover_material: FloorBoxCoverMaterial | None = pyd.Field(default=None, description="", example="Brass")
    floor_material: FloorBoxFloorMaterial | None = pyd.Field(default=None, description="", example="Concrete")


class NetworkingCableTraysV1(BaseOpenEpdHierarchicalSpec):
    """
    Cable trays.

    Mechanical support systems that provide a rigid structural system for cables used for communication and
    power distribution.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    height: LengthMmStr | None = pyd.Field(default=None, description="", example="100 mm")
    width: LengthMmStr | None = pyd.Field(default=None, description="", example="100 mm")
    depth: LengthMmStr | None = pyd.Field(default=None, description="Depth of enclosure system", example="1 m")
    static_load: MassKgStr | None = pyd.Field(default=None, description="Mass that the unit can hold", example="1 kg")
    ventilated: bool | None = pyd.Field(
        default=None, description="At least 40% of the tray base is open to air flow", example=True
    )
    material: CableTraysMaterial | None = pyd.Field(default=None, description="", example="Stainless Steel")


class NetworkingRacewaysV1(BaseOpenEpdHierarchicalSpec):
    """
    Surface-mounted systems along the perimeter of walls to route, conceal, and protect cables.

    Often called trunking.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    width: LengthMmStr | None = pyd.Field(default=None, description="", example="100 mm")
    depth: LengthMmStr | None = pyd.Field(default=None, description="Depth of enclosure system", example="100 mm")
    painted: bool | None = pyd.Field(default=None, description="", example=True)
    divided: bool | None = pyd.Field(
        default=None,
        description="Dual service raceway for high and low voltage data and power applications",
        example=True,
    )
    raceways_material: RacewaysMaterial | None = pyd.Field(default=None, description="", example="Aluminum")


class NetworkInfrastructureV1(BaseOpenEpdHierarchicalSpec):
    """General category for network infrastructure products for data centers and commercial and residential buildings."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PDU: PDUV1 | None = None
    CabinetsRacksAndEnclosures: CabinetsRacksAndEnclosuresV1 | None = None
    DataCabling: DataCablingV1 | None = None
    FloorBoxesAndAccessories: FloorBoxesAndAccessoriesV1 | None = None
    NetworkingCableTrays: NetworkingCableTraysV1 | None = None
    NetworkingRaceways: NetworkingRacewaysV1 | None = None
