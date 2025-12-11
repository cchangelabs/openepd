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
import unittest

from openepd.model.category import Category


class CategoryTestCase(unittest.TestCase):
    """Test case for the Category model, focusing on display_name and deprecated name field population."""

    def test_display_name_populated_from_name(self) -> None:
        """Test that display_name is populated from the deprecated name field if display_name is not provided."""
        category = Category(
            id="cat1",
            name="Deprecated Name",
            short_name="Short",
            openepd_hierarchical_name="cat1",
            masterformat=None,
            description=None,
            declared_unit=None,
            subcategories=[],
        )
        self.assertEqual(category.display_name, "Deprecated Name")

    def test_name_populated_from_display_name(self) -> None:
        """Test that the deprecated name field is populated from display_name if name is not provided."""
        category = Category(
            id="cat2",
            display_name="Display Name",
            short_name="Short",
            openepd_hierarchical_name="cat2",
            masterformat=None,
            description=None,
            declared_unit=None,
            subcategories=[],
        )
        self.assertEqual(category.name, "Display Name")
