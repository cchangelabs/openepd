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
from unittest import TestCase

from openepd.category.base import CategoryNode, CategoryTree
from openepd.model.category import Category


class CategoryTreeTestCase(TestCase):
    """Unit tests for the CategoryTree class."""

    def test_empty_tree_root_node(self) -> None:
        """Test that a new CategoryTree has a root node of type CategoryNode."""
        tree = CategoryTree()
        self.assertIsInstance(tree.root_node, CategoryNode)
        self.assertTrue(tree.root_node.is_root)
        self.assertTrue(tree.root_node.is_leaf)

    def test_add_and_find_node(self) -> None:
        """Test adding a child node and finding it by name."""
        tree = CategoryTree()
        child = tree.root_node.create_child_node(unique_name="Steel", display_name="Steel")
        found = tree.find_one("Steel")
        self.assertIs(found, child)
        self.assertEqual(found.display_name, "Steel")

    def test_find_all_returns_multiple(self) -> None:
        """Test that find_all returns all nodes with the same name."""
        tree = CategoryTree()
        child1 = tree.root_node.create_child_node(unique_name="Steel1", short_name="Steel")
        child2 = tree.root_node.create_child_node(unique_name="Steel2", short_name="Steel")
        found = tree.find_all("Steel")
        self.assertIn(child1, found)
        self.assertIn(child2, found)
        self.assertEqual(len(found), 2)

    def test_find_one_raises_on_multiple(self) -> None:
        """Test that find_one raises ValueError if multiple nodes match the name."""
        tree = CategoryTree()
        tree.root_node.create_child_node(unique_name="Steel1", display_name="Steel")
        tree.root_node.create_child_node(unique_name="Steel2", display_name="Steel")
        with self.assertRaises(ValueError):
            tree.find_one("Steel")

    def test_as_dto(self) -> None:
        """Test that as_dto returns a Category DTO with correct structure."""
        tree = CategoryTree()
        tree.root_node.create_child_node(unique_name="Steel", display_name="Steel")
        dto = tree.as_dto()
        self.assertIsInstance(dto, Category)
        self.assertEqual(dto.display_name, "")  # root node has empty display_name by default
        self.assertEqual(len(dto.subcategories), 1)
        self.assertEqual(dto.subcategories[0].display_name, "Steel")

    def test_clone_tree(self) -> None:
        """Test that clone returns a deep copy of the tree."""
        tree = CategoryTree()
        tree.root_node.create_child_node(unique_name="Steel", display_name="Steel")
        clone = tree.clone()
        self.assertIsInstance(clone, CategoryTree)
        self.assertIsNot(clone, tree)
        self.assertNotEqual(id(clone.root_node), id(tree.root_node))
        self.assertEqual(len(list(clone.root_node.children)), 1)
        self.assertEqual(list(clone.root_node.children)[0].display_name, "Steel")

    def test_root_node_setter(self) -> None:
        """Test that setting root_node updates the tree's root and search index."""
        tree = CategoryTree()
        new_root = CategoryNode(tree, unique_name="NewRoot")
        tree.root_node = new_root
        self.assertIs(tree.root_node, new_root)
