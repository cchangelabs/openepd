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
"""Generate prompts for missing category metadata.

This module walks the hierarchical :class:`Specs` tree (Pydantic v1 models),
identifies specification classes that do not yet define ``_CATEGORY_META``,
and writes prompt text to help author that metadata.
"""

import json
from collections.abc import Iterator

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.singular import Specs


CATEGORY_TREE_JSON_PATH: str = "category_hierarchical.json"
PROMPTS_OUTPUT_PATH: str = "prompts.md"
PROMPT_SEPARATOR: str = "_____________________________________________\n"
PROMPT_TEMPLATE: str = """\
Write ``_CATEGORY_META`` for class ``{clazz.__module__}.{clazz.__name__}``.
Place ``_CATEGORY_META`` directly below ``_EXT_VERSION`` in the class body.

Use :class:`openepd.model.category.CategoryMeta` as the target structure.
Derive field values from the JSON data below.

```json
{meta_js}
```
"""


def iter_category_spec_nodes(
    node_name: str | None,
    node: type[BaseOpenEpdHierarchicalSpec],
) -> Iterator[tuple[str | None, type[BaseOpenEpdHierarchicalSpec]]]:
    """Iterate over hierarchical spec nodes.

    The traversal walks the Pydantic v1 model tree by following fields whose
    type is a subclass of :class:`BaseOpenEpdHierarchicalSpec`.

    Parameters
    ----------
    node_name:
        Name of the current node within its parent, or the logical root name
        when starting the traversal.
    node:
        Specification class to inspect for child specification nodes.

    Yields
    ------
    tuple[str | None, type[BaseOpenEpdHierarchicalSpec]]
        Pairs of the node's name and the corresponding specification class.

    """

    yield node_name, node

    for field_name, field_info in getattr(node, "__fields__", {}).items():
        field_type = getattr(field_info, "type_", None)
        if isinstance(field_type, type) and issubclass(
            field_type, BaseOpenEpdHierarchicalSpec
        ):
            yield from iter_category_spec_nodes(field_name, field_type)


def build_prompt_for_node(
    node_name: str,
    node: type[BaseOpenEpdHierarchicalSpec],
    meta_by_unique_name: dict[str, dict],
) -> str:
    """Build a prompt string for a specification node.

    The prompt instructs the reader to define ``_CATEGORY_META`` for the
    provided specification class, using JSON metadata looked up by
    ``node_name``.

    Parameters
    ----------
    node_name:
        Unique name of the specification node, as used in the JSON index.
    node:
        Specification class that requires ``_CATEGORY_META``.
    meta_by_unique_name:
        Mapping from unique node names to their JSON metadata dictionaries
        loaded from :data:`CATEGORY_TREE_JSON_PATH`.

    Returns
    -------
    str
        Rendered prompt text for the given node.

    Raises
    ------
    KeyError
        If no JSON metadata is available for ``node_name``.

    """

    meta = meta_by_unique_name[node_name]
    del meta["hierarchical_name"]
    meta_js = json.dumps(meta, indent=4)
    return PROMPT_TEMPLATE.format(clazz=node, meta_js=meta_js)


def main() -> None:
    """Generate prompts for specification classes missing ``_CATEGORY_META``.

    The function performs the following steps.

    * Traverse the :class:`Specs` hierarchy to collect all specification
      classes.
    * Filter classes that do not yet define ``_CATEGORY_META``.
    * Load category metadata from :data:`CATEGORY_TREE_JSON_PATH`.
    * Generate prompt text for a subset of missing classes.
    * Write the prompts to :data:`PROMPTS_OUTPUT_PATH` separated by
      :data:`PROMPT_SEPARATOR`.

    """

    all_nodes = list(iter_category_spec_nodes("ConstructionMaterials", Specs))
    print(f"Total spec nodes: {len(all_nodes)}")

    with open(CATEGORY_TREE_JSON_PATH, encoding="utf-8") as file:
        json_data = json.load(file)

    meta_by_unique_name: dict[str, dict] = {
        item["unique_name"]: item for item in json_data
    }

    nodes_missing_meta = []
    for node_name, node in all_nodes:
        if hasattr(node, "_CATEGORY_META"):
            continue
        nodes_missing_meta.append((node_name, node))

    print(f"Nodes missing _CATEGORY_META: {len(nodes_missing_meta)}")

    prompts = []
    manual_handling = []
    for node_name, node in nodes_missing_meta[:50]:
        if hasattr(node, "_CATEGORY_META"):
            continue
        if node_name is None:
            continue
        if node_name not in meta_by_unique_name:
            manual_handling.append(node_name)
            continue
        prompts.append(build_prompt_for_node(node_name, node, meta_by_unique_name))

    prompts_str = PROMPT_SEPARATOR.join(prompts)
    with open(PROMPTS_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(prompts_str)

    print(f"For manual handling: {manual_handling}")


if __name__ == "__main__":
    main()
