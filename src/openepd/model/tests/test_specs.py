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

from openepd.model.specs import SteelV1
from openepd.model.specs.singular import Specs
from openepd.model.specs.singular.steel import RebarSteelV1
from openepd.model.validation.quantity import LengthMmStr


class SpecsTestCase(unittest.TestCase):
    def test_ensure_path_raise_exception_if_path_not_exists(self) -> None:
        specs = Specs(Steel=SteelV1())
        invalid_paths = ["not.a.real.path", "Steel.not_a_steel_property"]
        for path in invalid_paths:
            with self.subTest(path), self.assertRaises(KeyError):
                specs.get_by_spec_path(path, ensure_path=True)

    def test_asserted_type_raise_exception_if_type_is_invalid(self) -> None:
        specs = Specs(Steel=SteelV1(RebarSteel=RebarSteelV1(diameter_min=LengthMmStr("5 mm"))))
        with self.assertRaises(TypeError):
            specs.get_by_spec_path(("Steel", "RebarSteel", "diameter_min"), asserted_type=int)

    def test_get_by_spec_path_returns_valid_answers(self) -> None:
        cases = [
            (
                Specs(Steel=SteelV1(RebarSteel=RebarSteelV1(diameter_min=LengthMmStr("5 mm")))),
                "Steel.RebarSteel.diameter_min",
                "5 mm",
                None,
                None,
            ),
            (
                Specs(Steel=SteelV1(RebarSteel=RebarSteelV1(diameter_min=LengthMmStr("5 mm")))),
                "Steel__RebarSteel__diameter_min",
                "5 mm",
                None,
                "__",
            ),
            (
                Specs(Steel=SteelV1(RebarSteel=RebarSteelV1(diameter_min=LengthMmStr("5 mm")))),
                ("Steel", "RebarSteel", "diameter_min"),
                "5 mm",
                None,
                None,
            ),
            (
                Specs(Steel=SteelV1(RebarSteel=RebarSteelV1(diameter_min=LengthMmStr("5 mm")))),
                ("Steel", "RebarSteel", "diameter_min"),
                "5 mm",
                str,
                None,
            ),
            (
                Specs(Steel=SteelV1(RebarSteel=RebarSteelV1(diameter_min=LengthMmStr("5 mm")))),
                ("Steel", "RebarSteel", "diameter_min"),
                "5 mm",
                LengthMmStr,
                None,
            ),
        ]
        for case in cases:
            with self.subTest(case):
                specs, path, expected, asserted_type, delimiter = case
                if delimiter is None:
                    result = specs.get_by_spec_path(path, asserted_type=asserted_type)
                else:
                    result = specs.get_by_spec_path(path, asserted_type=asserted_type, delimiter=delimiter)
                self.assertEqual(result, expected)
