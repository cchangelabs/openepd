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
from unittest.mock import Mock, patch

import pydantic as pyd

from openepd.model.common import AnyAmount, NonNegativeAmount


class AmountTestCase(unittest.TestCase):
    @patch("openepd.model.validation.quantity.ExternalValidationConfig.QUANTITY_VALIDATOR")
    def test_amount_with_unit_validates_unit_is_known(self, validator_mock: Mock) -> None:
        """When a unit is provided, it should be checked against the external quantity validator."""
        validate_same_dimensionality_mock = Mock()
        validator_mock.validate_same_dimensionality = validate_same_dimensionality_mock

        NonNegativeAmount.model_validate({"qty": 1, "unit": "kg"})

        validate_same_dimensionality_mock.assert_called_once_with("kg", "kg")

    @patch("openepd.model.validation.quantity.ExternalValidationConfig.QUANTITY_VALIDATOR")
    def test_amount_without_unit_skips_unit_validation(self, validator_mock: Mock) -> None:
        """When no unit is provided, the external quantity validator should not be invoked."""
        validate_same_dimensionality_mock = Mock()
        validator_mock.validate_same_dimensionality = validate_same_dimensionality_mock

        NonNegativeAmount.model_validate({"qty": 1})

        validate_same_dimensionality_mock.assert_not_called()

    @patch("openepd.model.validation.quantity.ExternalValidationConfig.QUANTITY_VALIDATOR")
    def test_amount_rejects_unknown_unit(self, validator_mock: Mock) -> None:
        """When the external validator rejects the unit, model validation should fail with a clear message."""
        validator_mock.validate_same_dimensionality = Mock(side_effect=ValueError("unknown unit"))

        with self.assertRaises(pyd.ValidationError) as ctx:
            NonNegativeAmount.model_validate({"qty": 1, "unit": "not-a-unit"})

        self.assertIn("Valid unit is required", str(ctx.exception))

    def test_amount_requires_qty_or_unit(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            NonNegativeAmount.model_validate({})

    def test_any_amount_requires_qty_or_unit(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            AnyAmount.model_validate({})

    def test_amount_rejects_negative_qty(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            NonNegativeAmount.model_validate({"qty": -1, "unit": "kg"})

    def test_any_amount_allows_negative_qty(self) -> None:
        value = AnyAmount.model_validate({"qty": -1, "unit": "kg"})
        self.assertEqual(value.qty, -1)
        self.assertEqual(value.unit, "kg")

    def test_to_quantity_str(self) -> None:
        amount = NonNegativeAmount.model_validate({"qty": 2, "unit": "kg"})
        any_amount = AnyAmount.model_validate({"qty": -2, "unit": "kg"})

        self.assertEqual(amount.to_quantity_str(), "2.0 kg")
        self.assertEqual(any_amount.to_quantity_str(), "-2.0 kg")
