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
from pydantic import BaseModel, Field

from .range import SpecsRange


class AverageDatasetMaterialSpecsMixin(BaseModel, title="Average Dataset Material Specs"):
    """Material specs fields for average dataset (Industry-wide EPDs, Generic Estimates)."""

    specs: SpecsRange | None = Field(
        default=None,
        description="Average dataset material performance specifications.",
    )
