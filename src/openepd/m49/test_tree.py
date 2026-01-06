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
from unittest import TestCase

from .tree import GeographyItem, GeographyTree, get_m49_tree, get_openepd_geography_tree


class M49TreeTestCase(TestCase):
    def test_can_build_m49_tree(self):
        tree = get_m49_tree()
        self.assertIsNotNone(tree)
        # Root basics
        self.assertIsInstance(tree, GeographyTree)
        self.assertIsNotNone(tree.root)
        self.assertIsInstance(tree.root, GeographyItem)
        self.assertEqual(tree.root.level, 0)
        self.assertIn("001", tree.root.m49_codes)  # World code
        # Top-level children should include the main continents/regions
        child_codes = {next(iter(c.m49_codes)) for c in tree.root.children}
        for code in ["002", "150", "009", "142"]:  # Africa, Americas, Europe, Oceania, Asia
            self.assertIn(code, child_codes)

        # Leaves should be countries (no children)
        leaves = tree.find_all(is_leaf=True)
        self.assertGreater(len(leaves), 0)
        for leaf in leaves[:10]:  # spot check a few
            self.assertTrue(leaf.is_leaf)
            self.assertIsNotNone(leaf.iso_codes)
            self.assertGreater(len(leaf.iso_codes), 0)

    def test_can_build_openepd_tree(self):
        tree = get_openepd_geography_tree()
        self.assertIsNotNone(tree)
        self.assertIsInstance(tree, GeographyTree)

        # Ensure special regions are attached to the root
        special_region_codes = {child.openepd_code for child in tree.root.children if child.openepd_special_region}
        self.assertIn("NAFTA", special_region_codes)
        self.assertIn("EU27", special_region_codes)

        # Special regions should have children and be non-leaf
        nafta_nodes = [c for c in tree.root.children if c.openepd_code == "NAFTA"]
        self.assertEqual(len(nafta_nodes), 1)
        nafta = nafta_nodes[0]
        self.assertFalse(nafta.is_leaf)
        self.assertGreater(len(nafta.children), 0)
        for member in nafta.children:
            self.assertIsInstance(member, GeographyItem)
            self.assertFalse(member.openepd_special_region)
