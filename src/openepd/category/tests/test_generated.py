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

from openepd.category.generated import get_category_definitions
from openepd.model.category_meta import collect_category_metadata


class GetCategoryDefinitionsTestCase(TestCase):
    def test_generated_category_definitions_are_in_sync(self) -> None:
        """
        Test that the generated category definitions are synchronized with the metadata in ``Specs``.

        This test ensures that the output of ``get_category_definitions`` matches the metadata collected from ``Specs``.
        If the test fails, it indicates that the generated code is out of sync and should be updated by running
        ``make codegen-category-tree``.
        """
        expected_definitions = collect_category_metadata()
        generated_definitions = list(get_category_definitions())
        error_message = (
            "Generated category definitions in `src/openepd/category/generated.py` are out of sync with `Specs`. "
            "Please run `make codegen-category-tree` to update the generated code."
        )
        self.assertEqual(expected_definitions, generated_definitions, msg=error_message)
