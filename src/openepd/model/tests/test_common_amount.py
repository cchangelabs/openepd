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

from openepd.compat.pydantic import pyd
from openepd.model.common import AnyAmount, NonNegativeAmount


class AmountTestCase(unittest.TestCase):
    def test_amount_requires_qty_or_unit(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            NonNegativeAmount.parse_obj({})

    def test_any_amount_requires_qty_or_unit(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            AnyAmount.parse_obj({})

    def test_amount_rejects_negative_qty(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            NonNegativeAmount.parse_obj({"qty": -1, "unit": "kg"})

    def test_any_amount_allows_negative_qty(self) -> None:
        value = AnyAmount.parse_obj({"qty": -1, "unit": "kg"})
        self.assertEqual(value.qty, -1)
        self.assertEqual(value.unit, "kg")

    def test_to_quantity_str(self) -> None:
        amount = NonNegativeAmount.parse_obj({"qty": 2, "unit": "kg"})
        any_amount = AnyAmount.parse_obj({"qty": -2, "unit": "kg"})

        self.assertEqual(amount.to_quantity_str(), "2.0 kg")
        self.assertEqual(any_amount.to_quantity_str(), "-2.0 kg")
