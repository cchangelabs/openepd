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
from openepd.model.validation.quantity import PressureMPaStr, validate_unit_factory


class GMUV1(BaseOpenEpdHierarchicalSpec):
    """Glass Masonry Unit performance specification."""

    _EXT_VERSION = "1.0"


class AutoclavedAeratedConcreteV1(BaseOpenEpdHierarchicalSpec):
    """Autoclaved aerated concrete performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    strength_28d: PressureMPaStr | None = pyd.Field(default=None, description="", example="1 MPa")
    thermal_conductivity: str | None = pyd.Field(default=None, description="", example="1 W / (m * K)")
    white: bool | None = pyd.Field(default=None, description="", example=True)

    _concrete_compressive_strength_28d_is_quantity_validator = pyd.validator("strength_28d", allow_reuse=True)(
        validate_unit_factory("MPa")
    )
    _aac_thermal_conductivity_is_quantity_validator = pyd.validator("thermal_conductivity", allow_reuse=True)(
        validate_unit_factory("W / (m * K)")
    )


class BrickV1(BaseOpenEpdHierarchicalSpec):
    """Brick performance specification."""

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
    """Masonry performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    white_cement: bool | None = pyd.Field(default=None, description="", example=True)

    # Nested specs:
    GMU: GMUV1 | None = None
    AutoclavedAeratedConcrete: AutoclavedAeratedConcreteV1 | None = None
    Brick: BrickV1 | None = None
