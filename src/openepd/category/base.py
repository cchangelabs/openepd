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

__all__ = ["CATEGORY_TREE", "CategoryNode", "CategoryTree"]

from collections.abc import Collection
from typing import Final

from openepd.category.generated import get_category_definitions
from openepd.category.search import CategoryFinder
from openepd.model.category import Category
from openepd.model.common import Amount


def normalize_string_collection(strings: Collection[str] | None) -> list[str]:
    """
    Normalize a collection of strings to a list.

    Converts the input collection of strings to a list. If the input is None, returns an empty list.

    :param strings: A collection of strings or None.
    :return: A list of strings, or an empty list if input is None.
    """
    if strings is None:
        return []
    return list(strings)


class CategoryNode:
    """
    Represents a node in the category hierarchy tree.

    Each node contains metadata about a category, its parent, and its children.
    """

    def __init__(
        self,
        tree: CategoryTree,
        *,
        unique_name: str = "",
        display_name: str = "",
        short_name: str = "",
        hierarchical_name: str = "",
        historical_names: Collection[str] | None = None,
        alt_names: Collection[str] | None = None,
        description: str = "",
        masterformat: str | None = None,
        declared_unit: Amount | None = None,
        parent: CategoryNode | None = None,
    ) -> None:
        """
        Initialize a CategoryNode.

        :param tree: The category tree to which this node belongs.
        :param unique_name: Stable, unique identifier for the category node (PascalCase).
        :param display_name: Human-readable display name for the category.
        :param short_name: Short, user-friendly name for the category.
        :param hierarchical_name: The current hierarchical path from the second-level category to this category.
        :param historical_names: List of historical hierarchical paths to this category.
        :param alt_names: Alternative names for the category, possibly in different languages.
        :param description: Description of the category's purpose or contents.
        :param masterformat: MasterFormat code for the category.
        :param declared_unit: Declared unit typically used for items in this category.
        :param parent: Reference to the parent CategoryNode, or None if this is the root node.
        :param children: List of child CategoryNodes.
        """
        self._tree = tree
        self._unique_name = unique_name
        self._display_name = display_name
        self._short_name = short_name
        self._hierarchical_name = hierarchical_name
        self._historical_names = normalize_string_collection(historical_names)
        self._alt_names = normalize_string_collection(alt_names)
        self._description = description
        self._masterformat = masterformat
        self._declared_unit = declared_unit
        self._parent = parent
        self._children: list[CategoryNode] = []

    @property
    def unique_name(self) -> str:
        """
        Stable, unique identifier for the category node (PascalCase).

        Used as a natural key and matches property names in `openepd.model.specs.singular.Specs`.

        :return: The unique name of the category.
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, value: str) -> None:
        """
        Set the unique name of the category.

        :param value: Stable, unique identifier for the category node (PascalCase).
        """
        if self._unique_name != value:
            self._tree.notify_name_changed()

        self._unique_name = value

    @property
    def display_name(self) -> str:
        """
        Human-readable display name for the category.

        May change over time.

        :return: The display name of the category.
        """
        return self._display_name

    @display_name.setter
    def display_name(self, value: str) -> None:
        """
        Set the display name of the category.

        :param value: Human-readable display name for the category.
        """
        if self._display_name != value:
            self._tree.notify_name_changed()

        self._display_name = value

    @property
    def short_name(self) -> str:
        """
        Short, user-friendly name for the category.

        Unique within its parent. May match display_name.

        :return: The short name of the category.
        """
        return self._short_name

    @short_name.setter
    def short_name(self, value: str) -> None:
        """
        Set the short name of the category.

        :param value: Short, user-friendly name for the category.
        """
        if self._short_name != value:
            self._tree.notify_name_changed()

        self._short_name = value

    @property
    def hierarchical_name(self) -> str:
        """
        The current hierarchical path from the second-level category to this category.

        This is a string using '>>' as a separator, representing the current route through the hierarchy.
        Unique within the tree.
        For example: Steel >> ColdFormedSteel >> DeckingSteel

        :return: The hierarchical name path of the category.
        """
        return self._hierarchical_name

    @hierarchical_name.setter
    def hierarchical_name(self, value: str) -> None:
        """
        Set the hierarchical name of the category.

        :param value: The current hierarchical path from the second-level category to this category.
        """
        if self._hierarchical_name != value:
            self._tree.notify_name_changed()

        self._hierarchical_name = value

    @property
    def historical_names(self) -> Collection[str]:
        """
        List of historical hierarchical paths to this category.

        Each path is a string using '>>' as a separator, representing a previous route through the hierarchy.
        Unique within the tree.

        :return: List of historical hierarchical paths.
        """
        return tuple(self._historical_names)

    @historical_names.setter
    def historical_names(self, value: Collection[str]) -> None:
        """
        Set the historical names of the category.

        :param value: List of historical hierarchical paths to this category.
        """
        new_value = list(value)
        if self._historical_names != new_value:
            self._tree.notify_name_changed()
        self._historical_names = new_value

    @property
    def alt_names(self) -> Collection[str]:
        """
        Alternative names for the category, possibly in different languages.

        Unique within the tree.

        :return: List of alternative names.
        """
        return tuple(self._alt_names)

    @alt_names.setter
    def alt_names(self, value: Collection[str]) -> None:
        """
        Set the alternative names of the category.

        :param value: Alternative names for the category, possibly in different languages.
        """
        new_value = list(value)
        if self._alt_names != new_value:
            self._tree.notify_name_changed()
        self._alt_names = new_value

    @property
    def description(self) -> str:
        """
        Description of the category's purpose or contents.

        :return: The description of the category.
        """
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """
        Set the description of the category.

        :param value: Description of the category's purpose or contents.
        """
        self._description = value

    @property
    def masterformat(self) -> str | None:
        """
        MasterFormat code for the category.

        See: https://en.wikipedia.org/wiki/MasterFormat

        Multiple categories may share the same code, and some may not be mapped to any MasterFormat code.

        :return: The MasterFormat code, or None if not mapped.
        """
        return self._masterformat

    @masterformat.setter
    def masterformat(self, value: str | None) -> None:
        """
        Set the MasterFormat code for the category.

        :param value: MasterFormat code for the category.
        """
        self._masterformat = value

    @property
    def declared_unit(self) -> Amount | None:
        """
        Declared unit typically used for items in this category.

        If not specified, this category does not have a stable or specific declared unit.

        :return: The declared unit, or None if not specified.
        """
        return self._declared_unit

    @declared_unit.setter
    def declared_unit(self, value: Amount | None) -> None:
        """
        Set the declared unit for the category.

        :param value: Declared unit typically used for items in this category.
        """
        self._declared_unit = value

    @property
    def parent(self) -> CategoryNode | None:
        """
        Reference to the parent CategoryNode, or None if this is the root node.

        :return: The parent CategoryNode, or None.
        """
        return self._parent

    @parent.setter
    def parent(self, value: CategoryNode | None) -> None:
        """
        Set the parent CategoryNode.

        :param value: Reference to the parent CategoryNode, or None if this is the root node.
        """
        if self._parent != value:
            self._tree.notify_parent_changed()
        self._parent = value

    @property
    def children(self) -> Collection[CategoryNode]:
        """
        List of child CategoryNodes.

        :return: List of child CategoryNodes.
        """
        return tuple(self._children)

    def add_child_node(self, child: CategoryNode) -> None:
        """
        Add a child node to this category node.

        Ensures the child node belongs to the same category tree and sets its parent if not already set.
        Raises a ValueError if the child node's parent is not this node or if the child belongs to a different tree.
        If the child is already present, the method does nothing.

        :param child: The CategoryNode instance to add as a child.
        :raises ValueError: If the child node does not belong to the same tree or its parent is not this node.
        """
        if child._tree is not self._tree:
            msg = "Cannot add child node: The child node must belong to the same category tree as the parent node."
            raise ValueError(msg)

        if child.parent is None:
            child.parent = self

        if child.parent is not self:
            msg = "Cannot add child node: The child's parent must be this node."
            raise ValueError(msg)

        if child in self.children:
            return

        self._tree.notify_children_changed()
        self._children.append(child)

    def remove_child_node(self, child: CategoryNode) -> None:
        """
        Remove a specified child node from this category node.

        If the child node is not present among this node's children, a ValueError is raised.

        :param child: The CategoryNode instance to remove from the children list.
        :raises ValueError: If the specified child node is not found among this node's children.
        """
        try:
            self._children.remove(child)
            self._tree.notify_children_changed()
        except ValueError as exc:
            msg = "Cannot remove child node: the specified node is not a child of this category node."
            raise ValueError(msg) from exc

    def create_child_node(
        self,
        *,
        unique_name: str = "",
        display_name: str = "",
        short_name: str = "",
        hierarchical_name: str = "",
        historical_names: Collection[str] | None = None,
        alt_names: Collection[str] | None = None,
        description: str = "",
        masterformat: str | None = None,
        declared_unit: Amount | None = None,
    ) -> CategoryNode:
        """
        Create and add a new child node to this category.

        This method instantiates a new :class:`CategoryNode` as a child of the current node,
        initializing it with the provided metadata and linking it to the category tree.

        :param unique_name: Stable, unique identifier for the child node (PascalCase).
        :param display_name: Human-readable display name for the child category.
        :param short_name: Short, user-friendly name for the child category.
        :param hierarchical_name: Hierarchical path from the second-level category to the child.
        :param historical_names: List of historical hierarchical paths to the child category.
        :param alt_names: Alternative names for the child category, possibly in different languages.
        :param description: Description of the child category's purpose or contents.
        :param masterformat: MasterFormat code for the child category.
        :param declared_unit: Declared unit typically used for items in the child category.
        :return: The newly created child :class:`CategoryNode`.
        """
        child_node = CategoryNode(
            tree=self._tree,
            parent=self,
            unique_name=unique_name,
            display_name=display_name,
            short_name=short_name,
            hierarchical_name=hierarchical_name,
            historical_names=historical_names,
            alt_names=alt_names,
            description=description,
            masterformat=masterformat,
            declared_unit=declared_unit,
        )
        self.add_child_node(child_node)
        return child_node

    @property
    def ancestors(self) -> list[CategoryNode]:
        """
        Get all ancestor nodes, starting from the immediate parent up to the root.

        :return: List of ancestor CategoryNodes, ordered from parent to root.
        """
        ancestors: list[CategoryNode] = []
        current: CategoryNode | None = self.parent
        while current is not None:
            ancestors.append(current)
            current = current.parent
        return ancestors

    @property
    def is_root(self) -> bool:
        """
        Check if this node is the root of the category tree.

        :return: True if this node has no parent, False otherwise.
        """
        return self.parent is None

    @property
    def is_leaf(self) -> bool:
        """
        Check if this node is a leaf (has no children).

        :return: True if this node has no children, False otherwise.
        """
        return not self.children

    def as_dto(self) -> Category:
        """
        Convert this category node and its subtree into a serializable Category data transfer object (DTO).

        Recursively traverses all child nodes, building a nested Category structure suitable for serialization
        or API responses. All relevant metadata and subcategories are included.

        :return: A Category DTO representing this node and its descendants.
        """
        subcategory_dtos: list[Category] = [child.as_dto() for child in self.children]
        return Category(
            id=self.unique_name,
            display_name=self.display_name,
            short_name=self.short_name,
            openepd_hierarchical_name=self.hierarchical_name,
            masterformat=self.masterformat,
            description=self.description,
            declared_unit=self.declared_unit,
            subcategories=subcategory_dtos,
        )

    def clone_tree(self) -> CategoryTree:
        """
        Create a deep clone of the entire category tree rooted at this node.

        The result is a new CategoryTree instance with a fully independent hierarchy, preserving all metadata.

        :return: A new CategoryTree instance with the cloned hierarchy.
        """
        new_tree = CategoryTree()
        cloned_root = self._clone_subtree(new_tree)
        new_tree.root_node = cloned_root
        return new_tree

    def _clone_subtree(self, tree: CategoryTree) -> CategoryNode:
        """
        Recursively clone this category node and its entire subtree into a new category tree.

        The cloned node becomes the root of the new subtree. All metadata and children are deeply copied.

        :param tree: The target CategoryTree instance to attach the cloned nodes to.
        :return: The root node of the cloned subtree (a new CategoryNode instance).
        """
        cloned_node = CategoryNode(
            tree=tree,
            unique_name=self.unique_name,
            display_name=self.display_name,
            short_name=self.short_name,
            hierarchical_name=self.hierarchical_name,
            historical_names=self.historical_names,
            alt_names=self.alt_names,
            description=self.description,
            masterformat=self.masterformat,
            declared_unit=Amount(**self.declared_unit.to_serializable()) if self.declared_unit else None,
        )

        for child in self.children:
            child_clone = child._clone_subtree(tree)
            cloned_node.add_child_node(child_clone)
        return cloned_node


class CategoryTree:
    """
    Represents the root and search interface for a category hierarchy tree.

    Provides methods to find, clone, and manage category nodes. The tree is mutable, but cloning is recommended
    before making modifications to preserve the integrity of the global category structure.
    """

    def __init__(self, root_node: CategoryNode | None = None) -> None:
        """
        Initialize a CategoryTree instance.

        If no root node is provided, a new root CategoryNode is created.
        """
        self._root_node: CategoryNode = root_node or CategoryNode(self)
        self._finder: CategoryFinder = CategoryFinder(self._root_node)

    @property
    def root_node(self) -> CategoryNode:
        """
        Get the root node of the category tree.

        :return: The root CategoryNode.
        """
        return self._root_node

    @root_node.setter
    def root_node(self, value: CategoryNode) -> None:
        """
        Set the root node of the category tree.

        :param value: The new root CategoryNode
        """
        self._root_node = value
        self._finder = CategoryFinder(value)

    def find_one(self, name: str) -> CategoryNode | None:
        """
        Find a single category node by name (case-insensitive).

        This method first attempts to retrieve a unique category node by the given name using the search index.
        If not found, it performs a broader search for all matching nodes. If multiple matches are found,
        a ValueError is raised with a descriptive message.

        :param name: The name of the category to search for.
        :return: The matching CategoryNode if found, or None if no match exists.
        :raises ValueError: If multiple categories match the given name.
        """
        direct_match = self._finder.get(name)
        if direct_match:
            return direct_match

        matching_nodes = self._finder.find(name)
        if not matching_nodes:
            return None
        if len(matching_nodes) == 1:
            return matching_nodes[0]

        matched_names = ", ".join(f"`{node.unique_name}`" for node in matching_nodes)
        error_message = (
            f"Ambiguous category name '{name}': multiple matches found: {matched_names}. "
            "Use `find_all` to retrieve all matches."
        )
        raise ValueError(error_message)

    def find_all(self, name: str) -> list[CategoryNode]:
        """
        Find all CategoryNode objects matching the given name (case-insensitive).

        :param name: Name to search for.
        :return: List of matching CategoryNode objects (may be empty).
        """
        return self._finder.find(name)

    def as_dto(self) -> Category:
        """
        Convert the entire category tree to a serializable Category data transfer object (DTO).

        This method traverses the tree from the root node, recursively converting each node and its descendants
        into a nested Category DTO structure. The resulting object is suitable for serialization or use in API
        responses, and includes all relevant metadata and subcategories.

        :return: The root Category DTO representing the entire category hierarchy.
        """
        return self.root_node.as_dto()

    def clone(self) -> CategoryTree:
        """
        Create a deep clone of the entire category tree.

        :return: A new CategoryTree instance with a fully independent hierarchy.
        """
        return self.root_node.clone_tree()

    def notify_name_changed(self) -> None:
        """Notify the tree that a node's name has changed."""
        self._reset_search()

    def notify_parent_changed(self) -> None:
        """Notify the tree that a node's parent has changed."""
        self._reset_search()

    def notify_children_changed(self) -> None:
        """Notify the tree that a node's children have changed."""
        self._reset_search()

    def _reset_search(self) -> None:
        """Reset the internal search index for category lookups."""
        self._finder = CategoryFinder(self.root_node)


def _build_category_tree_for_specs() -> CategoryTree:
    """
    Construct a CategoryTree instance from the current category definitions.

    This function loads all category definitions, creates corresponding CategoryNode instances,
    and links them according to their parent-child relationships. The resulting tree has its root node set
    and is ready for traversal or queries.

    :raises ValueError: If no root category node is found in the definitions.
    :return: The fully constructed CategoryTree instance.
    """
    node_map: dict[str, CategoryNode] = {}
    category_definitions = get_category_definitions()
    category_tree = CategoryTree()

    # Create all nodes without linking parents or children
    for definition in category_definitions:
        unique_name: str = definition["unique_name"]
        display_name: str = definition["display_name"]
        short_name: str = definition.get("short_name") or display_name
        alt_names: list[str] = definition.get("alt_names") or []
        description: str = definition.get("description") or ""
        masterformat: str | None = definition.get("masterformat")
        declared_unit = definition.get("declared_unit")
        hierarchical_name: str = definition.get("hierarchical_name") or ""
        historical_names: list[str] = definition.get("historical_names") or []

        node_map[unique_name] = CategoryNode(
            tree=category_tree,
            unique_name=unique_name,
            display_name=display_name,
            short_name=short_name,
            hierarchical_name=hierarchical_name,
            historical_names=historical_names,
            alt_names=alt_names,
            description=description,
            masterformat=masterformat,
            declared_unit=declared_unit,
            parent=None,
        )

    # Link parent and child nodes
    for definition in category_definitions:
        child_name = definition["unique_name"]
        parent_name = definition.get("parent")
        if parent_name:
            parent_node = node_map[parent_name]
            child_node = node_map[child_name]
            child_node.parent = parent_node
            parent_node.add_child_node(child_node)

    # Set the root node and return the tree
    for node in node_map.values():
        if node.parent is None:
            category_tree.root_node = node
            return category_tree

    msg = "No root category node found in the category definitions. Ensure at least one node has no parent specified."
    raise ValueError(msg)


CATEGORY_TREE: Final[CategoryTree] = _build_category_tree_for_specs()
"""
The global category tree for the current `openepd.model.specs.singular.Specs` hierarchy.

This tree provides access to all category nodes and their relationships, as defined by the current category
definitions. Use this object to look up categories, traverse the hierarchy, or perform category-based queries.

.. note::
   Although this object is mutable, it is recommended to clone it before making modifications. This ensures
   the integrity of the global category structure for other consumers.
"""
