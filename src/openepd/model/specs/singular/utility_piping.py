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
from openepd.model.specs.enums import BuriedPipingType, PipingAnsiSchedule, UtilityPipingMaterial
from openepd.model.validation.quantity import LengthMmStr, MassPerLengthStr


class BuildingHeatingPipingV1(BaseOpenEpdHierarchicalSpec):
    """
    Heating piping.

    System of pipes used to supply heated fluids (liquids or steam) for purposes of controlling temperature inside a
    home, business, or other building facility.
    """

    _EXT_VERSION = "1.0"


class BuriedPipingV1(BaseOpenEpdHierarchicalSpec):
    """System of pipes used to provide or transport fluids (liquids and gases) underground."""

    _EXT_VERSION = "1.0"

    # Own fields:
    buried_piping_type: list[BuriedPipingType] | None = pyd.Field(
        default=None, description="", example=["Water Utilities"]
    )


class UtilityPipingV1(BaseOpenEpdHierarchicalSpec):
    """
    Utility piping.

    System of pipes used to convey fluids (liquids and gases) from one location to another. Piping can be metal,
    plastic, concrete, fiberglass, or other materials.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="6 m")
    piping_diameter: LengthMmStr | None = pyd.Field(default=None, description="", example="200 mm")
    mass_per_unit_length: MassPerLengthStr | None = pyd.Field(default=None, description="", example="1 kg / m")
    piping_ansi_schedule: PipingAnsiSchedule | None = pyd.Field(default=None, description="", example="5")
    utility_piping_material: UtilityPipingMaterial | None = pyd.Field(default=None, description="", example="PVC")

    # Nested specs:
    BuildingHeatingPiping: BuildingHeatingPipingV1 | None = None
    BuriedPiping: BuriedPipingV1 | None = None
