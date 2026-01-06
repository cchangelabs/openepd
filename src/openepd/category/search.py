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

from itertools import chain
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from openepd.category.base import CategoryNode


class CategoryFinder:
    """
    Fast, case-insensitive lookup of category nodes by multiple names.

    The finder builds two in-memory indexes from a category tree rooted at ``root``:

    - an "exact" index mapping unique keys to a single :class:`CategoryNode`
      (``unique_name``, ``hierarchical_name``, and all ``historical_names``), and
    - a "multi" index mapping non-unique, user-facing labels to lists of nodes
      (``display_name``, ``short_name``, ``alt_names``), plus all keys from the exact index.

    Including exact keys in the multi index allows callers that only have access to the
    multi-key search to still resolve identifiers that are otherwise unique. However,
    callers that know they are working with a unique key should prefer the dedicated
    ``get()`` method (which uses the exact index) rather than relying on the multi index.
    The search is case-insensitive and ignores surrounding whitespace.
    """

    def __init__(self, root: CategoryNode) -> None:
        """
        Initialize a finder for the provided category tree root.

        :param root: The root :class:`CategoryNode` of the tree to index.
        """
        self._root = root
        self._exact_index: dict[str, CategoryNode] | None = None
        self._multi_index: dict[str, list[CategoryNode]] | None = None

    # ---- Index construction -------------------------------------------------
    def _normalize_key(self, key: str) -> str:
        """
        Normalize a lookup key for indexing and search.

        Converts the string to lowercase and strips leading/trailing whitespace.

        :param key: The input key string.
        :return: Normalized key suitable for case-insensitive lookup.
        """
        return key.lower().strip()

    def _add_exact(self, key: str, node: CategoryNode, exact: dict[str, CategoryNode]) -> None:
        """
        Add a unique key-to-node mapping to the exact index.

        Duplicate normalized keys raise a :class:`KeyError` since exact keys must be unique.

        :param key: The key to index.
        :param node: The category node to map to the key.
        :param exact: The exact index to modify.
        :raises KeyError: If the normalized key already exists in the exact index.
        """
        norm = self._normalize_key(key)
        if not norm:
            return
        existing = exact.get(norm)
        if existing is not None:
            # If the same node is being re-inserted under the same normalized key, allow it (idempotent).
            if existing is node:
                return
            msg = (
                "Duplicate unique key detected for category index: "
                f"{key!r} already used by {existing.hierarchical_name!r}"
            )
            raise KeyError(msg)
        exact[norm] = node

    def _add_multi(self, key: str, node: CategoryNode, multi: dict[str, list[CategoryNode]]) -> None:
        """
        Add a non-unique key-to-node association to the multi index.

        :param key: The key to index.
        :param node: The category node to associate with the key.
        :param multi: The multi index to modify.
        """
        norm = self._normalize_key(key)
        if not norm:
            return
        bucket = multi.setdefault(norm, [])
        if node not in bucket:
            bucket.append(node)

    def _populate_indexes(
        self,
        root: CategoryNode,
        exact: dict[str, CategoryNode],
        multi: dict[str, list[CategoryNode]],
    ) -> None:
        """
        Populate the provided indexes by traversing the category tree iteratively.

        :param root: The root node to start traversal from.
        :param exact: The exact (unique) index to populate.
        :param multi: The multi (non-unique) index to populate.
        """
        stack: list[CategoryNode] = [root]
        while stack:
            node = stack.pop()

            # Exact (unique) keys
            for key in chain([node.unique_name, node.hierarchical_name], node.historical_names):
                self._add_exact(key, node, exact)

            # Multi (non-unique) keys; include exact keys for convenience
            for key in chain(
                [node.unique_name, node.hierarchical_name, node.display_name, node.short_name],
                node.alt_names,
                node.historical_names,
            ):
                self._add_multi(key, node, multi)

            # Traverse children
            for child in node.children:
                stack.append(child)

    def _ensure_index_built(self) -> tuple[dict[str, CategoryNode], dict[str, list[CategoryNode]]]:
        """
        Build the internal indexes if needed and return them.

        The returned tuple is ``(exact_index, multi_index)``.

        :return: A tuple with the exact and multi indexes.
        :raises KeyError: If a key expected to be unique is encountered more than once.
        """
        exact = self._exact_index
        multi = self._multi_index
        if exact is not None and multi is not None:
            return exact, multi

        exact = {}
        multi = {}
        self._populate_indexes(self._root, exact, multi)

        self._exact_index = exact
        self._multi_index = multi
        return exact, multi

    # ---- Public API ---------------------------------------------------------
    def get(self, name: str) -> CategoryNode | None:
        """
        Return a single node by a unique key, or ``None`` if not found.

        This method consults the "exact" index. Valid keys include:

        - ``unique_name`` (stable identifier)
        - ``hierarchical_name`` (current hierarchy path)
        - any value from ``historical_names``

        Matching is case-insensitive and ignores surrounding whitespace.

        :param name: The name to look up.
        :return: The matching node or ``None`` if not found.
        """
        key = self._normalize_key(name)
        if not key:
            return None
        exact, _ = self._ensure_index_built()
        return exact.get(key)

    def find(self, name: str) -> list[CategoryNode]:
        """
        Return all nodes that match the given name (case-insensitive).

        This method consults the "multi" index. It may return multiple nodes when labels are not unique
        (for example, display names or alternative names reused across branches). Exact keys are also
        included in this index for convenience.

        :param name: The name or label to search for.
        :return: A list of matching :class:`CategoryNode` instances (possibly empty).
        """
        key = self._normalize_key(name)
        if not key:
            return []
        _, multi = self._ensure_index_built()
        if key in multi:
            return list(multi[key])
        return []
