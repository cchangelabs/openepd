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
import pydantic as pyd

from openepd.model.ext.harmonization.base import HarmonizationFactorBase


class CustomHarmonizationFactor(HarmonizationFactorBase):
    model_config = pyd.ConfigDict(extra="allow")

    name: str = pyd.Field(
        description="Display name for the harmonization factor.",
        examples=["Custom Harmonization Factor"],
        min_length=1,
        max_length=250,
    )
