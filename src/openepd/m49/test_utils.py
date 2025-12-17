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

from openepd.m49.utils import (
    flatten_to_iso3166_alpha2,
    iso_to_m49,
    m49_to_iso,
    m49_to_openepd,
    m49_to_region_and_country_names,
    openepd_to_m49,
    region_and_country_names_to_m49,
)


class M49UtilsTestCase(TestCase):
    def test_iso_to_m49(self) -> None:
        positive_test_cases = [
            (["US", "CA", "MX"], ["840", "124", "484"]),
            (["DE", "FR", "IT"], ["276", "250", "380"]),
            (["US", "CA", "MX", "DE", "FR", "IT"], ["840", "124", "484", "276", "250", "380"]),
        ]
        for input_data, expected in positive_test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = iso_to_m49(input_data)
                self.assertCountEqual(result, expected)

        negative_test_cases = [
            (["USA"], ValueError),  # invalid ISO code
            (["US", "USA"], ValueError),  # mixed valid and invalid ISO codes
            ([""], ValueError),
        ]

        for input_data, expected_exception in negative_test_cases:
            with self.subTest(input_data=input_data, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    iso_to_m49(input_data)

    def test_m49_to_iso(self) -> None:
        positive_test_cases = [
            (["840", "124", "484"], ["US", "CA", "MX"]),
            (["840", "840", "124", "124", "484"], ["US", "CA", "MX"]),
            (["276", "250", "380"], ["DE", "FR", "IT"]),
            (["840", "124", "484", "276", "250", "380"], ["US", "CA", "MX", "DE", "FR", "IT"]),
        ]
        for input_data, expected in positive_test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = m49_to_iso(input_data)
                self.assertCountEqual(result, expected)

        negative_test_cases = [
            (["999"], ValueError),  # invalid M49 code
            (["840", "999"], ValueError),  # mixed valid and invalid M49 codes
            ([""], ValueError),
        ]

        for input_data, expected_exception in negative_test_cases:
            with self.subTest(input_data=input_data, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    m49_to_iso(input_data)

    def test_region_and_country_names_to_m49(self) -> None:
        positive_test_cases = [
            (["World", "Africa", "Asia"], ["001", "002", "142"]),
            (["World", "World", "Africa", "Asia", "Asia"], ["001", "002", "142"]),
            (["Europe", "North America"], ["150", "003"]),
            (["Europe", "North America", "Austria", "Germany"], ["150", "003", "040", "276"]),
            (["europe", "north america", "austria", "germany"], ["150", "003", "040", "276"]),
            (["Bolivia"], ["068"]),
        ]
        for input_data, expected in positive_test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = region_and_country_names_to_m49(input_data)
                self.assertCountEqual(result, expected)

        negative_test_cases = [
            (["WWWorld"], ValueError),  # invalid region
            (["World", "WWWorld"], ValueError),  # mixed valid and invalid regions
            (["Abcde"], ValueError),  # invalid country
            ([""], ValueError),
            # ([], ValueError),
        ]

        for input_data, expected_exception in negative_test_cases:
            with self.subTest(input_data=input_data, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    region_and_country_names_to_m49(input_data)

    def test_m49_to_region_and_country_names(self) -> None:
        positive_test_cases = [
            (["001", "002", "142"], ["World", "Africa", "Asia"]),
            (["001", "001", "002", "002", "142"], ["World", "Africa", "Asia"]),
            (["150", "003"], ["Europe", "North America"]),
            (["150", "003", "040", "276"], ["Europe", "North America", "Austria", "Germany"]),
            (["068"], ["Bolivia"]),
        ]
        for input_data, expected in positive_test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = sorted(m49_to_region_and_country_names(input_data))
                self.assertCountEqual(result, expected)

        negative_test_cases = [
            (["999"], ValueError),  # invalid M49 code
            (["001", "999"], ValueError),  # mixed valid and invalid M49 codes
            ([""], ValueError),
        ]

        for input_data, expected_exception in negative_test_cases:
            with self.subTest(input_data=input_data, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    m49_to_region_and_country_names(input_data)

    def test_openepd_to_m49(self) -> None:
        positive_test_cases = [
            (
                ["EU27", "NAFTA"],
                [
                    "040",
                    "056",
                    "100",
                    "191",
                    "196",
                    "203",
                    "208",
                    "233",
                    "246",
                    "250",
                    "276",
                    "300",
                    "348",
                    "372",
                    "380",
                    "428",
                    "440",
                    "442",
                    "470",
                    "528",
                    "616",
                    "620",
                    "642",
                    "703",
                    "705",
                    "724",
                    "752",
                    "840",
                    "124",
                    "484",
                ],
            ),
            (["US", "CA", "MX"], ["840", "124", "484"]),
            (
                ["US", "CA", "MX", "EU27", "NAFTA"],
                [
                    "840",
                    "124",
                    "484",
                    "040",
                    "056",
                    "100",
                    "191",
                    "196",
                    "203",
                    "208",
                    "233",
                    "246",
                    "250",
                    "276",
                    "300",
                    "348",
                    "372",
                    "380",
                    "428",
                    "440",
                    "442",
                    "470",
                    "528",
                    "616",
                    "620",
                    "642",
                    "703",
                    "705",
                    "724",
                    "752",
                ],
            ),
            (["NAFTA", "051"], ["840", "124", "484", "051"]),
            (
                ["051", "US", "CA", "MX", "EU27", "NAFTA"],
                [
                    "840",
                    "124",
                    "484",
                    "040",
                    "056",
                    "100",
                    "191",
                    "196",
                    "203",
                    "208",
                    "233",
                    "246",
                    "250",
                    "276",
                    "300",
                    "348",
                    "372",
                    "380",
                    "428",
                    "440",
                    "442",
                    "470",
                    "528",
                    "616",
                    "620",
                    "642",
                    "703",
                    "705",
                    "724",
                    "752",
                    "051",
                ],
            ),
        ]
        for input_data, expected in positive_test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = openepd_to_m49(input_data)
                self.assertCountEqual(result, expected)

        negative_test_cases = [
            (["EU36", "ABCDE"], ValueError),  # invalid OpenEPD geography definitions
            (["999"], ValueError),  # invalid OpenEPD geography definitions
            (["US", "BC", "DE"], ValueError),  # mixed valid and invalid OpenEPD geography definitions
            (["NAFTA", "999"], ValueError),  # mixed valid and invalid OpenEPD geography definitions
            ([""], ValueError),
        ]

        for input_data, expected_exception in negative_test_cases:
            with self.subTest(input_data=input_data, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    openepd_to_m49(input_data)

    def test_m49_to_openepd(self) -> None:
        positive_test_cases = [
            (["840", "124", "484"], ["NAFTA"]),
            (["840", "124"], ["US", "CA"]),
            (
                [
                    "040",
                    "056",
                    "100",
                    "191",
                    "196",
                    "203",
                    "208",
                    "233",
                    "246",
                    "250",
                    "276",
                    "300",
                    "348",
                    "372",
                    "380",
                    "428",
                    "440",
                    "442",
                    "470",
                    "528",
                    "616",
                    "620",
                    "642",
                    "703",
                    "705",
                    "724",
                    "752",
                ],
                ["EU27"],
            ),
            (["040", "056", "100"], ["AT", "BE", "BG"]),
            (
                [
                    "040",
                    "056",
                    "100",
                    "191",
                    "196",
                    "203",
                    "208",
                    "233",
                    "246",
                    "250",
                    "276",
                    "300",
                    "348",
                    "372",
                    "380",
                    "428",
                    "440",
                    "442",
                    "470",
                    "528",
                    "616",
                    "620",
                    "642",
                    "703",
                    "705",
                    "724",
                    "752",
                    "840",
                    "124",
                    "484",
                ],
                ["EU27", "NAFTA"],
            ),
            (["840", "124", "484", "398"], ["NAFTA", "KZ"]),
            (["840", "124", "484", "398", "356"], ["NAFTA", "KZ", "IN"]),
            (
                [
                    "040",
                    "056",
                    "100",
                    "191",
                    "196",
                    "203",
                    "208",
                    "233",
                    "246",
                    "250",
                    "276",
                    "300",
                    "348",
                    "372",
                    "380",
                    "428",
                    "440",
                    "442",
                    "470",
                    "528",
                    "616",
                    "620",
                    "642",
                    "703",
                    "705",
                    "724",
                    "752",
                    "242",
                ],
                ["EU27", "FJ"],
            ),
        ]

        for input_data, expected in positive_test_cases:
            with self.subTest(input_data=input_data, expected=expected):
                result = m49_to_openepd(input_data)
                self.assertCountEqual(result, expected)

        negative_test_cases = [
            (["999"], ValueError),  # invalid M49 code
            (["840", "999"], ValueError),  # mixed valid and invalid M49 codes
            ([""], ValueError),
        ]

        for input_data, expected_exception in negative_test_cases:
            with self.subTest(input_data=input_data, expected_exception=expected_exception):
                with self.assertRaises(expected_exception):
                    m49_to_openepd(input_data)

    def test_flatten_to_iso3166_alpha2(self) -> None:
        """
        Test flatten_to_iso3166_alpha2 with various region identifiers and options.

        This covers M49 codes, ISO codes, special region aliases, and expand_subdivisions option.
        """

        # Test with special region alias
        result = flatten_to_iso3166_alpha2(["EU27", "US"])
        self.assertIn("US", result)
        self.assertIn("FR", result)
        self.assertIn("DE", result)
        self.assertGreater(len(result), 3)

        # Test with M49 codes
        result = flatten_to_iso3166_alpha2(["840", "124"])
        self.assertEqual(result, {"US", "CA"})

        # Test with special region and M49 code
        result = flatten_to_iso3166_alpha2(["NAFTA", "051"])
        self.assertIn("US", result)
        self.assertIn("CA", result)
        self.assertIn("MX", result)
        self.assertIn("AM", result)

        # Test with expand_subdivisions
        result = flatten_to_iso3166_alpha2(["US"], expand_subdivisions=True)
        self.assertTrue(any(code.startswith("US-") for code in result))
        self.assertNotIn("US", result)

        # Test with unrecognized code
        result = flatten_to_iso3166_alpha2(["ZZ"])
        self.assertIn("ZZ", result)

        # Test with empty input
        result = flatten_to_iso3166_alpha2([])
        self.assertEqual(result, set())
