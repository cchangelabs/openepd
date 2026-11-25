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

from openepd.model.pcr import Pcr, PcrRef


class PcrTestCase(unittest.TestCase):
    def test_pcr_ref_fields_are_optional(self) -> None:
        pcr_ref = PcrRef.model_validate({})

        self.assertIsNone(pcr_ref.id)
        self.assertIsNone(pcr_ref.name)
        self.assertIsNone(pcr_ref.ref)

        pcr = Pcr.model_validate({})
        self.assertIsNone(pcr.id)
        self.assertIsNone(pcr.name)
        self.assertIsNone(pcr.ref)

    def test_pcr_includes_reference_fields(self) -> None:
        pcr = Pcr.model_validate(
            {
                "id": "ec3xpgq2",
                "name": "Concrete and concrete elements",
                "ref": "https://openepd.buildingtransparency.org/api/pcrs/1u7zsed8",
            }
        )

        self.assertEqual(pcr.id, "ec3xpgq2")
        self.assertEqual(pcr.name, "Concrete and concrete elements")
        self.assertEqual(str(pcr.ref), "https://openepd.buildingtransparency.org/api/pcrs/1u7zsed8")

    def test_pcr_accepts_various_geographies(self) -> None:
        """
        Test that the Pcr model accepts a variety of valid geography codes in the 'applicable_in' field.

        This test ensures that the Pcr model can be validated with a list of different geography codes,
        including region codes, country codes, and numeric codes.
        """
        valid_geographies = ["NAFTA", "EU27", "BA", "CA-AB", "108"]
        Pcr.model_validate({"applicable_in": valid_geographies})
