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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
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
from openepd.model.validation.quantity import LengthMStr, MassKgStr, validate_unit_factory


class PDUV1(BaseOpenEpdHierarchicalSpec):
    """P d u performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    amperage: str | None = pyd.Field(default=None, description="", example="1 A")
    outlet_level_metering: bool | None = pyd.Field(default=None, description="", example="True")
    outlet_level_switching: bool | None = pyd.Field(default=None, description="", example="True")
    pdu_technology: PduTechnology | None = pyd.Field(default=None, description="", example="Basic")
    pdu_outlets: int | None = pyd.Field(default=None, description="", example="3", le=200)

    _amperage_is_quantity_validator = pyd.validator("amperage", allow_reuse=True)(validate_unit_factory("A"))


class CabinetsRacksAndEnclosuresV1(BaseOpenEpdHierarchicalSpec):
    """Cabinets racks and enclosures performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    static_load: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    total_racking_units: int | None = pyd.Field(default=None, description="", example="3")
    rack_type: RackType | None = pyd.Field(default=None, description="", example="Cabinet")

    _static_load_is_quantity_validator = pyd.validator("static_load", allow_reuse=True)(validate_unit_factory("kg"))


class DataCablingV1(BaseOpenEpdHierarchicalSpec):
    """Data cabling performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    outdoor: bool | None = pyd.Field(default=None, description="", example="True")
    cabling_category: CablingCategory | None = pyd.Field(default=None, description="", example="Cat7")
    fire_rating: CablingFireRating | None = pyd.Field(default=None, description="", example="CMP")
    jacket_material: CablingJacketMaterial | None = pyd.Field(default=None, description="", example="PVC")
    shielded: bool | None = pyd.Field(default=None, description="", example="True")
    armored: bool | None = pyd.Field(default=None, description="", example="True")
    rohs: bool | None = pyd.Field(default=None, description="", example="True")
    reach: bool | None = pyd.Field(default=None, description="", example="True")
    zwtl: bool | None = pyd.Field(default=None, description="", example="True")
    connectorized: bool | None = pyd.Field(default=None, description="", example="True")
    thin_ethernet: bool | None = pyd.Field(default=None, description="", example="True")


class FloorBoxesAndAccessoriesV1(BaseOpenEpdHierarchicalSpec):
    """Floor boxes and accessories performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    painted: bool | None = pyd.Field(default=None, description="", example="True")
    fire_classified: bool | None = pyd.Field(default=None, description="", example="True")
    outdoor: bool | None = pyd.Field(default=None, description="", example="True")
    raised: bool | None = pyd.Field(default=None, description="", example="True")
    poke_through: bool | None = pyd.Field(default=None, description="", example="True")
    floor_box_cover: bool | None = pyd.Field(default=None, description="", example="True")
    floor_box_outlets: int | None = pyd.Field(default=None, description="", example="3", le=16)
    floor_box_material: FloorBoxMaterial | None = pyd.Field(default=None, description="", example="Metallic Box")
    floor_box_cover_material: FloorBoxCoverMaterial | None = pyd.Field(default=None, description="", example="Brass")
    floor_box_floor_material: FloorBoxFloorMaterial | None = pyd.Field(default=None, description="", example="Concrete")


class NetworkingCableTraysV1(BaseOpenEpdHierarchicalSpec):
    """Networking cable trays performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    height: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    width: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    depth: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    static_load: MassKgStr | None = pyd.Field(default=None, description="", example="1 kg")
    ventilated: bool | None = pyd.Field(default=None, description="", example="True")
    cable_trays_material: CableTraysMaterial | None = pyd.Field(default=None, description="", example="Stainless Steel")

    _height_is_quantity_validator = pyd.validator("height", allow_reuse=True)(validate_unit_factory("m"))
    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))
    _depth_is_quantity_validator = pyd.validator("depth", allow_reuse=True)(validate_unit_factory("m"))
    _static_load_is_quantity_validator = pyd.validator("static_load", allow_reuse=True)(validate_unit_factory("kg"))


class NetworkingRacewaysV1(BaseOpenEpdHierarchicalSpec):
    """Networking raceways performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    width: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    depth: LengthMStr | None = pyd.Field(default=None, description="", example="1 m")
    painted: bool | None = pyd.Field(default=None, description="", example="True")
    divided: bool | None = pyd.Field(default=None, description="", example="True")
    raceways_material: RacewaysMaterial | None = pyd.Field(default=None, description="", example="Aluminum")

    _width_is_quantity_validator = pyd.validator("width", allow_reuse=True)(validate_unit_factory("m"))
    _depth_is_quantity_validator = pyd.validator("depth", allow_reuse=True)(validate_unit_factory("m"))


class NetworkInfrastructureV1(BaseOpenEpdHierarchicalSpec):
    """Network infrastructure performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    PDU: PDUV1 | None = None
    CabinetsRacksAndEnclosures: CabinetsRacksAndEnclosuresV1 | None = None
    DataCabling: DataCablingV1 | None = None
    FloorBoxesAndAccessories: FloorBoxesAndAccessoriesV1 | None = None
    NetworkingCableTrays: NetworkingCableTraysV1 | None = None
    NetworkingRaceways: NetworkingRacewaysV1 | None = None
