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
from typing import Any

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Amount


class Category(BaseOpenEpdSchema):
    """DTO for Category model, recursive."""

    id: str = pyd.Field(description="Category short ID (readable unique string)", alias="unique_name")
    name: str = pyd.Field(
        default="",
        deprecated="Use `display_name` instead",
        description="(deprecated) Category display name (user-friendly)",
    )
    display_name: str = pyd.Field(description="Category display name (user-friendly)")
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

    @pyd.root_validator(pre=True)
    def synchronize_category_names(cls, values: dict[str, Any]) -> dict[str, Any]:
        """
        Ensure that both `name` and `display_name` fields are synchronized.

        If only one of `name` or `display_name` is provided, this method copies its value to the missing field.
        This guarantees that both fields are always present and consistent.

        :param values: Dictionary of field values for the Category model.
        :return: Updated dictionary with synchronized `name` and `display_name` fields.
        """
        name = values.get("name")
        display_name = values.get("display_name")

        if not name and display_name:
            values["name"] = display_name
        elif name and not display_name:
            values["display_name"] = name

        return values
