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
from openepd.model.org import OrgRef
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.common import HasForestPracticesCertifiers
from openepd.model.specs.generated.enums import AllFabrication, AllTimberSpecies


class WoodJoistsV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """Wood joists performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: AllTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")
    fabrication: AllFabrication | None = pyd.Field(default=None, description="", example="LVL")
    forest_practices_certifiers: list[OrgRef] | None = pyd.Field(default=None, description="")
    weather_exposed: bool | None = pyd.Field(default=None, description="", example=True)
    fire_retardant: bool | None = pyd.Field(default=None, description="", example=True)
    decay_resistant: bool | None = pyd.Field(default=None, description="", example=True)
