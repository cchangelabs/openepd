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
from __future__ import annotations

import dataclasses
from typing import Any

import pydantic

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Amount


class Category(BaseOpenEpdSchema):
    """DTO for Category model, recursive."""

    id: str = pydantic.Field(description="Category short ID (readable unique string)", alias="unique_name")
    name: str = pydantic.Field(
        default="",
        description="(deprecated) Category display name (user-friendly)",
        json_schema_extra={
            "deprecated": True,
        },
    )
    display_name: str = pydantic.Field(description="Category display name (user-friendly)")
    short_name: str = pydantic.Field(description="Category short user-friendly name")
    openepd_hierarchical_name: str = pydantic.Field(
        "Special form of hierarchical category ID where the >> is hierarchy separator"
    )
    masterformat: str | None = pydantic.Field(description="Default category code in Masterformat", default=None)
    description: str | None = pydantic.Field(description="Category verbose description", default=None)
    declared_unit: Amount | None = pydantic.Field(
        description="Declared unit of category, for example 1 kg", default=None
    )
    subcategories: list[Category] = pydantic.Field(
        description="List of subcategories. This makes categories tree-like structure", default_factory=list
    )

    @pydantic.model_validator(mode="before")
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


@dataclasses.dataclass
class CategoryMeta:
    """
    Metadata for a category node in the hierarchy.

    Used with BaseOpenEpdHierarchicalSpec to declare category metadata. Provides stable identifiers, display names,
    historical and alternative names, description, MasterFormat code, and declared unit for a category node.
    """

    unique_name: str
    """
    Stable, unique identifier for the category node (PascalCase).

    Used as a natural key and matches property names in :class:`openepd.model.specs.singular.Specs`.
    """
    display_name: str
    """
    Human-readable display name for the category.

    Intended for UI. May change over time. Not unique within the category tree.
    """
    short_name: str | None = None
    """
    Short, user-friendly name for the category.

    Unique within its parent. If None, defaults to display_name.
    """
    historical_names: list[str] | None = None
    """
    Historical hierarchical paths to this category node.

    Each path is a string using '>>' as a separator, representing a previous route through the hierarchy.
    Unique within the tree.
    """
    alt_names: list[str] | None = None
    """
    Alternative names for the category, possibly in different languages.

    Not unique within the category tree.
    """
    description: str | None = None
    """
    Description of the category's purpose or contents.
    """
    masterformat: str | None = None
    """
    MasterFormat code for the category.

    See: https://en.wikipedia.org/wiki/MasterFormat
    Multiple categories may share the same code, and some may not be mapped to any MasterFormat code.
    """
    declared_unit: Amount | None = None
    """
    Declared unit typically used for items in this category.

    If not specified, this category does not have a stable or specific declared unit.
    """
