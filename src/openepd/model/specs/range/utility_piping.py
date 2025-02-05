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
    "BuildingHeatingPipingRangeV1",
    "BuriedPipingRangeV1",
    "UtilityPipingRangeV1",
)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.common import RangeAmount
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import BuriedPipingType, PipingAnsiSchedule, UtilityPipingMaterial
from openepd.model.validation.quantity import AmountRangeLengthMm


class BuildingHeatingPipingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Heating piping.

    System of pipes used to supply heated fluids (liquids or steam) for purposes of controlling temperature inside a
    home, business, or other building facility.

    Range version.
    """

    _EXT_VERSION = "1.0"


class BuriedPipingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    System of pipes used to provide or transport fluids (liquids and gases) underground.

    Range version.
    """

    _EXT_VERSION = "1.0"

    buried_piping_type: list[BuriedPipingType] | None = pyd.Field(default=None, description="")


class UtilityPipingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Utility piping.

    System of pipes used to convey fluids (liquids and gases) from one location to another. Piping can be metal,
    plastic, concrete, fiberglass, or other materials.

    Range version.
    """

    _EXT_VERSION = "1.0"

    thickness: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    piping_diameter: AmountRangeLengthMm | None = pyd.Field(default=None, description="")
    mass_per_unit_length: RangeAmount | None = pyd.Field(default=None, description="")
    piping_ansi_schedule: list[PipingAnsiSchedule] | None = pyd.Field(default=None, description="")
    utility_piping_material: list[UtilityPipingMaterial] | None = pyd.Field(default=None, description="")
    BuildingHeatingPiping: BuildingHeatingPipingRangeV1 | None = None
    BuriedPiping: BuriedPipingRangeV1 | None = None
