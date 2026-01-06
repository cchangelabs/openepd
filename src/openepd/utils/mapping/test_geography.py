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
import unittest

from openepd.utils.mapping.geography import GeographyToOpenEpdMapper


class GeographyMapperTest(unittest.TestCase):
    mapper: GeographyToOpenEpdMapper

    def setUp(self):
        self.mapper = GeographyToOpenEpdMapper()

    def test_map_values_to_openepd_geography(self):
        test_cases: list[tuple[str, set[str] | None]] = [
            ("United States", {"US"}),
            ("US", {"US"}),
            ("840", {"US"}),
            ("Canada", {"CA"}),
            ("cAnADa", {"CA"}),
            (" cAnADa   ", {"CA"}),
            ("NAFTA", {"NAFTA"}),
            ("Something", None),
        ]

        for input_value, expected in test_cases:
            with self.subTest(f"should map `{input_value}` to `{expected}`"):
                actual = self.mapper.map(input_value, default_value=None, raise_if_missing=False)
                self.assertEqual(
                    expected, actual, f"Mapping failed for input '{input_value}'. Expected {expected}, got {actual}."
                )
