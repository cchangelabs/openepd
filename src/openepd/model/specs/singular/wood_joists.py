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
from openepd.model.specs.enums import AllFabrication, AllTimberSpecies
from openepd.model.specs.singular.common import HasForestPracticesCertifiers


class WoodJoistsV1(BaseOpenEpdHierarchicalSpec, HasForestPracticesCertifiers):
    """
    Wood joists.

    Prefabricated I-shaped engineered wood structural members made primarily from one or more types of wood. Includes
    products made with metallic webbing. Excludes products where the wood is merely decorative.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    timber_species: AllTimberSpecies | None = pyd.Field(default=None, description="", example="Alaska Cedar")
    fabrication: AllFabrication | None = pyd.Field(default=None, description="", example="LVL")
    weather_exposed: bool | None = pyd.Field(default=None, description="", example=True)
    fire_retardant: bool | None = pyd.Field(default=None, description="", example=True)
    decay_resistant: bool | None = pyd.Field(default=None, description="", example=True)
