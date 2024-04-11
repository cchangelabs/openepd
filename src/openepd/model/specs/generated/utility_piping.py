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
from openepd.model.specs.generated.enums import BuriedPipingType, PipingAnsiSchedule, UtilityPipingMaterial
from openepd.model.validation.quantity import LengthMmStr, validate_unit_factory


class BuildingHeatingPipingV1(BaseOpenEpdHierarchicalSpec):
    """Building heating piping performance specification."""

    _EXT_VERSION = "1.0"


class BuriedPipingV1(BaseOpenEpdHierarchicalSpec):
    """Buried piping performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    buried_piping_type: list[BuriedPipingType] | None = pyd.Field(
        default=None, description="", example=["Water Utilities"]
    )


class UtilityPipingV1(BaseOpenEpdHierarchicalSpec):
    """Utility piping performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    thickness: LengthMmStr | None = pyd.Field(default=None, description="", example="6 m")
    piping_diameter: LengthMmStr | None = pyd.Field(default=None, description="", example="200 mm")
    mass_per_unit_length: str | None = pyd.Field(default=None, description="", example="1 kg / m")
    piping_ansi_schedule: PipingAnsiSchedule | None = pyd.Field(default=None, description="", example="5")
    utility_piping_material: UtilityPipingMaterial | None = pyd.Field(default=None, description="", example="PVC")

    _thickness_is_quantity_validator = pyd.validator("thickness", allow_reuse=True)(validate_unit_factory("m"))
    _piping_diameter_is_quantity_validator = pyd.validator("piping_diameter", allow_reuse=True)(
        validate_unit_factory("m")
    )
    _mass_per_unit_length_is_quantity_validator = pyd.validator("mass_per_unit_length", allow_reuse=True)(
        validate_unit_factory("kg / m")
    )

    # Nested specs:
    BuildingHeatingPiping: BuildingHeatingPipingV1 | None = None
    BuriedPiping: BuriedPipingV1 | None = None
