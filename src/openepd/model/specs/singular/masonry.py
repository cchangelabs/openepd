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
from openepd.model.validation.quantity import (
    PressureMPaStr,
    ThermalConductivityStr,
)


class GMUV1(BaseOpenEpdHierarchicalSpec):
    """Glass masonry unit."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="GMU",
        display_name="Glass Masonry Unit",
        historical_names=["Masonry >> Glass Masonry Unit"],
        description="Glass masonry unit",
        masterformat="04 23 00 Glass Unit Masonry",
        declared_unit=Amount(qty=1, unit="t"),
    )


class AutoclavedAeratedConcreteV1(BaseOpenEpdHierarchicalSpec):
    """A lightweight, precast, foamed concrete masonry building material."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AutoclavedAeratedConcrete",
        display_name="Autoclaved Aerated Concrete",
        short_name="AAC",
        historical_names=["Masonry >> AAC"],
        description="A lightweight, precast, foamed concrete masonry building material",
        masterformat="04 22 26 Autoclaved Aerated Concrete Unit Masonry",
        declared_unit=Amount(qty=1, unit="m^3"),
    )

    # Own fields:
    strength_28d: PressureMPaStr | None = pydantic.Field(default=None, description="", examples=["1 MPa"])
    thermal_conductivity: ThermalConductivityStr | None = pydantic.Field(
        default=None, description="", examples=["1 W / (m * K)"]
    )
    white: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


class BrickV1(BaseOpenEpdHierarchicalSpec):
    """Solid masonry units made from clay or shale."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Brick",
        display_name="Brick",
        alt_names=["Concrete Masonry Unit", "Concrete Block", "Cinder Block"],
        description="Solid masonry units made from clay or shale",
        masterformat="04 21 00 Clay Unit Masonry",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    building: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    facing: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    floor: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    pedestrian: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    paving: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    other: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    chemical_resistant: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    glazed: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    tiles: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


class MasonryV1(BaseOpenEpdHierarchicalSpec):
    """Structural and/or enclosure system based on individual rigid units stacked and bound together with mortar."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Masonry",
        display_name="Masonry",
        description="Structural and/or enclosure system based on individual rigid units stacked and bound together with mortar",
        masterformat="04 20 00 Unit Masonry",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    white_cement: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )

    # Nested specs:
    GMU: GMUV1 | None = None
    AutoclavedAeratedConcrete: AutoclavedAeratedConcreteV1 | None = None
    Brick: BrickV1 | None = None
