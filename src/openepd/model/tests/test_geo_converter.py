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

from openepd.model.geo_converter import GeographicRegionConverter


class GeoConverterTestCase(TestCase):
    def test_iso_to_m49(self) -> None:
        test_cases = [
            (["US", "CA", "MX"], ["840", "124", "484"]),
            (["DE", "FR", "IT"], ["276", "250", "380"]),
            (["US", "CA", "MX", "DE", "FR", "IT"], ["840", "124", "484", "276", "250", "380"]),
        ]
        for input_data, expected in test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = GeographicRegionConverter.iso_to_m49(input_data)
                self.assertEqual(result, expected)

    def test_m49_to_iso(self) -> None:
        test_cases = [
            (["840", "124", "484"], ["US", "CA", "MX"]),
            (["276", "250", "380"], ["DE", "FR", "IT"]),
            (["840", "124", "484", "276", "250", "380"], ["US", "CA", "MX", "DE", "FR", "IT"]),
        ]
        for input_data, expected in test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = GeographicRegionConverter.m49_to_iso(input_data)
                self.assertEqual(result, expected)
