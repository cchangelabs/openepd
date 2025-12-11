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

from openepd.model.category import CategoryMeta
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.singular import Specs


def _get_node_metadata(meta: CategoryMeta, ancestors: list[str]) -> dict[str, Any]:
    """
    Return metadata dictionary for a single category node.

    :param meta: CategoryMeta instance for the node.
    :param ancestors: List of ancestor category names.
    :return: Dictionary of metadata for the node.
    """
    item: dict[str, Any] = {
        "unique_name": meta.unique_name,
        "display_name": meta.display_name,
        "hierarchical_name": " >> ".join((ancestors + [meta.unique_name])[1:]),
        "parent": ancestors[-1] if ancestors else None,
    }
    for attr in ["short_name", "historical_names", "alt_names", "description", "masterformat"]:
        value = getattr(meta, attr, None)
        if value:
            item[attr] = value
    if meta.declared_unit:
        item["declared_unit"] = meta.declared_unit
    return item


def _traverse_category_tree(
    ancestors: list[str],
    node_name: str | None,
    node: type[BaseOpenEpdHierarchicalSpec],
    result: list[dict[str, Any]],
    require_meta: bool = False,
) -> None:
    """
    Recursively traverse the category tree and collect metadata for each node.

    :param ancestors: List of ancestor category names.
    :param node_name: Name of the current node.
    :param node: The current category node class.
    :param result: List to append metadata dictionaries to.
    :param require_meta: If True, raise error if node does not have _CATEGORY_META.
    """
    if hasattr(node, "_CATEGORY_META"):
        meta: CategoryMeta = node._CATEGORY_META
        node_name = node_name or meta.unique_name
        result.append(_get_node_metadata(meta, ancestors))
    elif require_meta:
        err_msg = f"Node '{node.__name__}' does not have associated '_CATEGORY_META'."
        raise ValueError(err_msg)
    for field_name, field_info in getattr(node, "__fields__", {}).items():
        field_type = getattr(field_info, "type_", None)
        if isinstance(field_type, type) and issubclass(field_type, BaseOpenEpdHierarchicalSpec):
            _traverse_category_tree(
                ancestors + [node_name] if node_name else ancestors,
                field_name,
                field_type,
                result,
                require_meta=require_meta,
            )


def collect_category_metadata(require_meta: bool = False) -> list[dict[str, Any]]:
    """
    Collect metadata for all categories in the hierarchy starting from the given node.

    :param require_meta: If True, raise error if a node does not have _CATEGORY_META.
    :return: List of dictionaries containing metadata for each category node.
    """
    result: list[dict[str, Any]] = []
    _traverse_category_tree([], None, Specs, result, require_meta=require_meta)
    return result
