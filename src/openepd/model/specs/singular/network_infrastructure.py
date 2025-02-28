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
from openepd.model.specs.enums import (
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
from openepd.model.specs.singular.mixins.conduit_mixin import ConduitMixin
from openepd.model.validation.quantity import (
    ElectricalCurrentStr,
    LengthMmStr,
    MassKgStr,
    validate_quantity_unit_factory,
)


class PDUV1(BaseOpenEpdHierarchicalSpec):
    """Devices with multiple outputs designed to distribute power, often in a data center cabinet."""

    _EXT_VERSION = "1.0"

    # Own fields:
    amperage: ElectricalCurrentStr | None = pydantic.Field(default=None, description="", examples=["1 A"])
    outlet_level_metering: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    outlet_level_switching: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    pdu_technology: PduTechnology | None = pydantic.Field(default=None, description="", examples=["Basic"])
    pdu_outlets: int | None = pydantic.Field(default=None, description="", examples=[3], le=200)

    @pydantic.field_validator("amperage", mode="before", check_fields=False)
    def _validate_amperage(cls, value):
        return validate_quantity_unit_factory("A")(cls, value)


class CabinetsRacksAndEnclosuresV1(BaseOpenEpdHierarchicalSpec):
    """Physical support upon which network equipment is mounted. Includes cabinets, racks, frames, and enclosures."""

    _EXT_VERSION = "1.0"

    # Own fields:
    static_load: MassKgStr | None = pydantic.Field(default=None, description="", examples=["1 kg"])
    total_racking_units: int | None = pydantic.Field(default=None, description="", examples=[3])
    rack_type: RackType | None = pydantic.Field(default=None, description="", examples=["Cabinet"])


class DataCablingV1(BaseOpenEpdHierarchicalSpec):
    """Telecommunications cabling for buildings."""

    _EXT_VERSION = "1.0"

    # Own fields:
    outdoor: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    cabling_category: CablingCategory | None = pydantic.Field(default=None, description="", examples=["Cat7"])
    fire_rating: CablingFireRating | None = pydantic.Field(default=None, description="", examples=["CMP"])
    jacket_material: CablingJacketMaterial | None = pydantic.Field(default=None, description="", examples=["PVC"])
    shielded: bool | None = pydantic.Field(
        default=None,
        description="Foil or similar electromagnetic shielding",
        examples=[True],
    )
    armored: bool | None = pydantic.Field(
        default=None,
        description="Steel or similar physical armor jacket",
        examples=[True],
    )
    rohs: bool | None = pydantic.Field(
        default=None,
        description="Certified ROHS Compliant",
        examples=[True],
    )
    reach: bool | None = pydantic.Field(
        default=None,
        description="Certified REACH compliant",
        examples=[True],
    )
    zwtl: bool | None = pydantic.Field(
        default=None,
        description="Certified ZWTL compliant",
        examples=[True],
    )
    connectorized: bool | None = pydantic.Field(
        default=None,
        description="This cable is shipped as a specific length with integrated connectors. Impacts include the "
        "connectors for the specific cable length. Connectors add impact similar to 0.1-0.5 additional "
        "meters of cable",
        examples=[True],
    )
    thin_ethernet: bool | None = pydantic.Field(
        default=None,
        description="At least part of this cable has a reduced outer diameter and thinner wires. Thin ethernet cables "
        "have handling advantages and tend to have a reduced impact, but also reduced channel length. "
        "See TIA 568.2-D Annex G.",
        examples=[True],
    )


class FloorBoxesAndAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """
    Electrical boxes that are installed in the floor.

    Used to provide power and/or data connections to devices in a room or space.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    painted: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    fire_classified: bool | None = pydantic.Field(
        default=None,
        description="Includes hardware to maintain fire rating of the floor",
        examples=[True],
    )
    outdoor: bool | None = pydantic.Field(
        default=None,
        description="Floor boxes installed in the ground",
        examples=[True],
    )
    raised: bool | None = pydantic.Field(
        default=None,
        description="Used in raised or computer style flooring",
        examples=[True],
    )
    poke_through: bool | None = pydantic.Field(
        default=None,
        description="Used primarily in retrofit or renovation and will maintain fire rating of the floor",
        examples=[True],
    )
    cover: bool | None = pydantic.Field(
        default=None,
        description="Floor box cover or lid for use with a separate floor box",
        examples=[True],
    )
    outlets: int | None = pydantic.Field(
        default=None,
        description="Number of outlet ports from floor box, including power, data, video, and other connections",
        examples=[3],
        le=16,
    )
    material: FloorBoxMaterial | None = pydantic.Field(default=None, description="", examples=["Metallic Box"])
    cover_material: FloorBoxCoverMaterial | None = pydantic.Field(default=None, description="", examples=["Brass"])
    floor_material: FloorBoxFloorMaterial | None = pydantic.Field(default=None, description="", examples=["Concrete"])


class NetworkingCableTraysV1(BaseOpenEpdHierarchicalSpec):
    """
    Cable trays.

    Mechanical support systems that provide a rigid structural system for cables used for communication and
    power distribution.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    height: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    width: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    depth: LengthMmStr | None = pydantic.Field(default=None, description="Depth of enclosure system", examples=["1 m"])
    static_load: MassKgStr | None = pydantic.Field(
        default=None, description="Mass that the unit can hold", examples=["1 kg"]
    )
    ventilated: bool | None = pydantic.Field(
        default=None,
        description="At least 40% of the tray base is open to air flow",
        examples=[True],
    )
    material: CableTraysMaterial | None = pydantic.Field(default=None, description="", examples=["Stainless Steel"])


class NetworkingRacewaysV1(BaseOpenEpdHierarchicalSpec):
    """
    Surface-mounted systems along the perimeter of walls to route, conceal, and protect cables.

    Often called trunking.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    width: LengthMmStr | None = pydantic.Field(default=None, description="", examples=["100 mm"])
    depth: LengthMmStr | None = pydantic.Field(
        default=None, description="Depth of enclosure system", examples=["100 mm"]
    )
    painted: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    divided: bool | None = pydantic.Field(
        default=None,
        description="Dual service raceway for high and low voltage data and power applications",
        examples=[True],
    )
    raceways_material: RacewaysMaterial | None = pydantic.Field(default=None, description="", examples=["Aluminum"])


class CommunicationsConduitV1(BaseOpenEpdHierarchicalSpec, ConduitMixin):
    """Tubing used to protect and route communications wiring in a building or structure."""

    _EXT_VERSION = "1.1"


class NetworkInfrastructureV1(BaseOpenEpdHierarchicalSpec):
    """General category for network infrastructure products for data centers and commercial and residential buildings."""

    _EXT_VERSION = "1.1"

    # Nested specs:
    PDU: PDUV1 | None = None
    CabinetsRacksAndEnclosures: CabinetsRacksAndEnclosuresV1 | None = None
    DataCabling: DataCablingV1 | None = None
    FloorBoxesAndAccessories: FloorBoxesAndAccessoriesV1 | None = None
    NetworkingCableTrays: NetworkingCableTraysV1 | None = None
    NetworkingRaceways: NetworkingRacewaysV1 | None = None
    CommunicationsConduit: CommunicationsConduitV1 | None = None
