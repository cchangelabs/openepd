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
from openepd.model.specs.aluminium import AluminiumV1
from openepd.model.specs.asphalt import AsphaltV1
from openepd.model.specs.glass import GlazingV1
from openepd.model.specs.wood import TimberV1


class Specs(BaseOpenEpdSchema):
    """Material specific specs."""

    cmu: concrete.CmuSpec | None = pyd.Field(default=None, description="Concrete Masonry Unit-specific (CMU) specs")
    CMU: concrete.CmuSpec | None = pyd.Field(default=None, description="Concrete Masonry Unit-specific (CMU) specs")
    Concrete: concrete.ConcreteV1 | None = pyd.Field(
        default=None, title="ConcreteV1", description="Concrete-specific specs"
    )
    PrecastConcrete: concrete.PrecastConcreteV1 | None = pyd.Field(
        default=None, title="PrecastConcreteV1", description="Precast Concrete-specific specs"
    )
    Steel: steel.SteelV1 | None = pyd.Field(default=None, title="SteelV1", description="Steel-specific specs")
    Asphalt: AsphaltV1 | None = pyd.Field(default=None, title="AsphaltV1")
    Aluminium: AluminiumV1 | None = pyd.Field(default=None, title="AluminiumV1", description="Aluminium-specific specs")
    Timber: TimberV1 | None = pyd.Field(default=None, title="TimberV1", description="Timber-specific specs")
    Glazing: GlazingV1 | None = pyd.Field(default=None, title="GlazingV1", description="Glazing-specific specs")
