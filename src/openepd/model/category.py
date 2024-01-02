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
from openepd.model.common import Amount


class Category(BaseOpenEpdSchema):
    """DTO for Category model, recursive."""

    id: str = pyd.Field(description="Category short ID (readable unique string)")
    name: str = pyd.Field(description="Category display name (user-friendly)")
    short_name: str = pyd.Field(description="Category short user-friendly name")
    openepd_hierarchical_name: str = pyd.Field(
        "Special form of hierarchical category ID where the >> is hierarchy separator"
    )
    masterformat: str | None = pyd.Field(description="Default category code in Masterformat")
    description: str | None = pyd.Field(description="Category verbose description")
    declared_unit: Amount | None = pyd.Field(description="Declared unit of category, for example 1 kg")
    subcategories: list["Category"] = pyd.Field(
        description="List of subcategories. This makes categories tree-like structure"
    )
