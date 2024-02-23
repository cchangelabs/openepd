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

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.specs import concrete, steel


class Specs(BaseOpenEpdSchema):
    """Material specific specs."""

    cmu: concrete.CmuSpec | None = pyd.Field(default=None, description="Concrete Masonry Unit-specific (CMU) specs")
    CMU: concrete.CmuSpec | None = pyd.Field(default=None, description="Concrete Masonry Unit-specific (CMU) specs")
    Steel: steel.SteelV1 | None = pyd.Field(default=None, title="SteelV1", description="Steel-specific specs")
    Concrete: concrete.ConcreteV1 | None = pyd.Field(
        default=None, title="ConcreteV1", description="Concrete-specific specs"
    )
