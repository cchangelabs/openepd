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
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from openepd.category.base import CategoryNode


class CategoryFinder:
    """
    Utility for fast lookup of CategoryNode objects by various names.

    Each instance provides indexed lookup for efficient search by multiple category attributes.
    """

    def __init__(self, root: CategoryNode) -> None:
        """
        Initialize the CategoryFinder with the root of the category tree.

        :param root: The root CategoryNode of the tree.
        """
        self._root = root
        self._index: dict[str, list[CategoryNode]] | None = None

    def _load_index(self) -> dict[str, list[CategoryNode]]:
        """
        Build and return the index mapping various lowercased names to CategoryNode lists.

        :return: Dictionary mapping lowercased keys to lists of CategoryNode objects.
        """
        index = self._index
        if index is not None:
            return index
        index = {}
        self._index = index

        def add_to_index(key: str, node: CategoryNode) -> None:
            key = key.lower()
            if key:
                nodes = index.setdefault(key, [])
                if node not in nodes:
                    nodes.append(node)

        def traverse(node: CategoryNode) -> None:
            add_to_index(node.unique_name, node)
            add_to_index(node.display_name, node)
            add_to_index(node.short_name, node)
            add_to_index(node.hierarchical_name, node)
            for alt in node.alt_names:
                add_to_index(alt, node)
            for hist in node.historical_names:
                add_to_index(hist, node)
            for child in node.children:
                traverse(child)

        traverse(self._root)
        return index

    def find(self, name: str) -> list[CategoryNode]:
        """
        Find all CategoryNode objects matching the various names.

        :param name: Name to search for (case-insensitive).
        :return: List of matching CategoryNode objects (may be empty).
        """
        name = name.lower()
        index = self._load_index()
        return index.get(name, [])
