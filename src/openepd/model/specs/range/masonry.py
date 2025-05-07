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
    "AutoclavedAeratedConcreteRangeV1",
    "BrickRangeV1",
    "GMURangeV1",
    "MasonryRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.validation.quantity import AmountRangePressureMpa, AmountRangeThermalConductivity


class GMURangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Glass masonry unit.

    Range version.
    """

    _EXT_VERSION = "1.0"


class AutoclavedAeratedConcreteRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    A lightweight, precast, foamed concrete masonry building material.

    Range version.
    """

    _EXT_VERSION = "1.0"

    strength_28d: AmountRangePressureMpa | None = pyd.Field(default=None, description="")
    thermal_conductivity: AmountRangeThermalConductivity | None = pyd.Field(default=None, description="")
    white: bool | None = pyd.Field(default=None, description="")


class BrickRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Solid masonry units made from clay or shale.

    Range version.
    """

    _EXT_VERSION = "1.0"

    building: bool | None = pyd.Field(default=None, description="")
    facing: bool | None = pyd.Field(default=None, description="")
    floor: bool | None = pyd.Field(default=None, description="")
    pedestrian: bool | None = pyd.Field(default=None, description="")
    paving: bool | None = pyd.Field(default=None, description="")
    other: bool | None = pyd.Field(default=None, description="")
    chemical_resistant: bool | None = pyd.Field(default=None, description="")
    glazed: bool | None = pyd.Field(default=None, description="")
    tiles: bool | None = pyd.Field(default=None, description="")


class MasonryRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Structural and/or enclosure system based on individual rigid units stacked and bound together with mortar.

    Range version.
    """

    _EXT_VERSION = "1.0"

    white_cement: bool | None = pyd.Field(default=None, description="")
    GMU: GMURangeV1 | None = None
    AutoclavedAeratedConcrete: AutoclavedAeratedConcreteRangeV1 | None = None
    Brick: BrickRangeV1 | None = None
