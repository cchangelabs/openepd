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
"""
Category metadata utilities for OpenEPD.

This module provides functions to traverse the category hierarchy and collect metadata for each category node.
"""

from collections.abc import Iterator
from types import UnionType
from typing import Any

import pydantic as pyd

from openepd.model.category import CategoryMeta
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.singular import Specs


def _get_category_node_metadata(
    meta: CategoryMeta, ancestors: list[str], is_deprecated: bool, previous: dict[str, Any] | None
) -> dict[str, Any]:
    """
    Generate a metadata dictionary for a single category node.

    :param meta: CategoryMeta instance for the node.
    :param ancestors: List of ancestor category names.
    :param is_deprecated: Whether the node is deprecated.
    :param previous: Previous metadata dictionary for this node, if any.
    :return: Metadata dictionary for the node.
    """
    hierarchical_name = " >> ".join((ancestors + [meta.unique_name])[1:])
    item: dict[str, Any]
    if previous:
        item = previous
        if not is_deprecated:
            item["hierarchical_name"] = hierarchical_name
        else:
            hierarchical_name = item["hierarchical_name"]
        if hierarchical_name != meta.unique_name and hierarchical_name not in item.get("historical_names", []):
            item.setdefault("historical_names", []).append(hierarchical_name)
        return item
    item = {
        "unique_name": meta.unique_name,
        "display_name": meta.display_name,
        "hierarchical_name": hierarchical_name,
        "parent": ancestors[-1] if ancestors else None,
    }
    for attr in [
        "short_name",
        "historical_names",
        "alt_names",
        "description",
        "masterformat",
    ]:
        value = getattr(meta, attr, None)
        if value:
            item[attr] = list(value) if isinstance(value, list) else value
    if meta.declared_unit:
        item["declared_unit"] = meta.declared_unit
    return item


def _iter_category_fields(
    category_cls: type[BaseOpenEpdHierarchicalSpec],
) -> Iterator[tuple[str, pyd.fields.FieldInfo]]:
    """
    Yield all field name and field definition pairs from a category class.

    :param category_cls: The category class to inspect.
    :yield: Tuples of (field name, field definition).
    """
    yield from category_cls.model_fields.items()


def _get_field_type(field: pyd.fields.FieldInfo) -> type:
    """
    Retrieve the type of a given model field.

    :param field: The model field to inspect.
    :return: The type of the field.
    """
    annotation = field.annotation
    if isinstance(annotation, UnionType):
        args = [a for a in annotation.__args__ if a is not type(None)]
        return args[0] if args else annotation  # type: ignore[return-value]
    assert annotation
    return annotation


def _is_field_deprecated(field: pyd.fields.FieldInfo) -> bool:
    """
    Determine if a model field is marked as deprecated.

    :param field: The model field to inspect.
    :return: True if the field is deprecated, False otherwise.
    """
    extra = field.json_schema_extra
    return bool(field.deprecated) or bool(isinstance(extra, dict) and extra.get("deprecated", False))


def _traverse_category_tree(
    ancestors: list[str],
    node_name: str | None,
    node: type[BaseOpenEpdHierarchicalSpec],
    is_deprecated: bool,
    metadata_result: dict[str, dict[str, Any]],
    require_meta: bool = False,
) -> None:
    """
    Recursively traverse the category tree and collect metadata for each node.

    :param ancestors: List of ancestor category names.
    :param node_name: Name of the current node.
    :param node: The current category node class.
    :param is_deprecated: Whether the current node is deprecated.
    :param metadata_result: Dictionary to store metadata for each node.
    :param require_meta: If True, raise error if node does not have _CATEGORY_META.
    """
    if hasattr(node, "_CATEGORY_META"):
        meta: CategoryMeta = node._CATEGORY_META
        node_name = node_name or meta.unique_name
        metadata = _get_category_node_metadata(meta, ancestors, is_deprecated, metadata_result.get(node_name))
        metadata_result[node_name] = metadata
    elif require_meta:
        err_msg = f"Node '{node.__name__}' does not have associated '_CATEGORY_META'."
        raise ValueError(err_msg)
    for field_name, field in _iter_category_fields(node):
        field_type = _get_field_type(field)
        if isinstance(field_type, type) and issubclass(field_type, BaseOpenEpdHierarchicalSpec):
            child_deprecated = is_deprecated or _is_field_deprecated(field)
            _traverse_category_tree(
                ancestors + [node_name] if node_name else ancestors,
                field_name,
                field_type,
                child_deprecated,
                metadata_result,
                require_meta=require_meta,
            )


def collect_category_metadata(require_meta: bool = False) -> list[dict[str, Any]]:
    """
    Collect metadata for all categories in the hierarchy starting from the root node.

    :param require_meta: If True, raise error if a node does not have _CATEGORY_META.
    :return: List of metadata dictionaries for each category node.
    """
    metadata_result: dict[str, dict[str, Any]] = {}
    _traverse_category_tree([], None, Specs, False, metadata_result, require_meta=require_meta)
    return list(metadata_result.values())
