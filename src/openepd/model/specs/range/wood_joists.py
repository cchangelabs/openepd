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
__all__ = ("WoodJoistsRangeV1",)

# NB! This is a generated code. Do not edit it manually. Please see src/openepd/model/specs/README.md


from openepd.compat.pydantic import pyd
from openepd.model.org import OrgRef
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.enums import AllFabrication, AllTimberSpecies


class WoodJoistsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Wood joists.

    Prefabricated I-shaped engineered wood structural members made primarily from one or more types of wood. Includes
    products made with metallic webbing. Excludes products where the wood is merely decorative.

    Range version.
    """

    _EXT_VERSION = "1.0"

    forest_practices_certifiers: list[OrgRef] | None = None
    timber_species: list[AllTimberSpecies] | None = pyd.Field(default=None, description="")
    fabrication: list[AllFabrication] | None = pyd.Field(default=None, description="")
    weather_exposed: bool | None = pyd.Field(default=None, description="")
    fire_retardant: bool | None = pyd.Field(default=None, description="")
    decay_resistant: bool | None = pyd.Field(default=None, description="")
