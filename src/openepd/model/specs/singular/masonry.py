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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import (
    PressureMPaStr,
    ThermalConductivityStr,
    validate_quantity_ge_factory,
    validate_quantity_unit_factory,
)


class GMUV1(BaseOpenEpdHierarchicalSpec):
    """Glass masonry unit."""

    _EXT_VERSION = "1.0"


class AutoclavedAeratedConcreteV1(BaseOpenEpdHierarchicalSpec):
    """A lightweight, precast, foamed concrete masonry building material."""

    _EXT_VERSION = "1.0"

    # Own fields:
    strength_28d: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    thermal_conductivity: ThermalConductivityStr | None = pyd.Field(
        default=None, description="", example="1 W / (m * K)"
    )
    white: bool | None = pyd.Field(default=None, description="", example=True)

    _aac_thermal_conductivity_is_quantity_validator = pyd.validator("thermal_conductivity", allow_reuse=True)(
        validate_quantity_unit_factory("W / (m * K)")
    )

    _aac_thermal_conductivity_min_validator = pyd.validator("thermal_conductivity", allow_reuse=True)(
        validate_quantity_ge_factory("0 W / (m * K)")
    )


class BrickV1(BaseOpenEpdHierarchicalSpec):
    """Solid masonry units made from clay or shale."""

    _EXT_VERSION = "1.0"

    # Own fields:
    building: bool | None = pyd.Field(default=None, description="", example=True)
    facing: bool | None = pyd.Field(default=None, description="", example=True)
    floor: bool | None = pyd.Field(default=None, description="", example=True)
    pedestrian: bool | None = pyd.Field(default=None, description="", example=True)
    paving: bool | None = pyd.Field(default=None, description="", example=True)
    other: bool | None = pyd.Field(default=None, description="", example=True)
    chemical_resistant: bool | None = pyd.Field(default=None, description="", example=True)
    glazed: bool | None = pyd.Field(default=None, description="", example=True)
    tiles: bool | None = pyd.Field(default=None, description="", example=True)


class MasonryV1(BaseOpenEpdHierarchicalSpec):
    """Structural and/or enclosure system based on individual rigid units stacked and bound together with mortar."""

    _EXT_VERSION = "1.0"

    # Own fields:
    white_cement: bool | None = pyd.Field(default=None, description="", example=True)

    # Nested specs:
    GMU: GMUV1 | None = None
    AutoclavedAeratedConcrete: AutoclavedAeratedConcreteV1 | None = None
    Brick: BrickV1 | None = None
