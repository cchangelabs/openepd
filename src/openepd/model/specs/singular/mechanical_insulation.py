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
from openepd.model.specs.enums import InsulatingMaterial, InsulationIntendedApplication
from openepd.model.validation.quantity import LengthMmStr


class MechanicalInsulationV1(BaseOpenEpdHierarchicalSpec):
    """
    Insulation products whose primary purpose is for mechanical systems rather than for building envelope.

    Includes HVAC, plumbing, and acoustic insulations.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    r_value: float | None = pyd.Field(default=None, description="", example=2.3)
    material: InsulatingMaterial | None = pyd.Field(default=None, description="", example="Mineral Wool")
    intended_application: list[InsulationIntendedApplication] | None = pyd.Field(
        default=None, description="", example=["Wall & General"]
    )
    thickness_per_declared_unit: LengthMmStr | None = pyd.Field(default=None, description="", example="20 mm")
