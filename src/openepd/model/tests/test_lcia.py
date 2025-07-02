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
from typing import Any
import unittest

from openepd.model.common import Measurement
from openepd.model.lcia import ImpactSet, ScopeSet


class LciaTestCase(unittest.TestCase):
    TEST_SOCPESET1 = ScopeSet(A1=Measurement(mean=1.0, unit="kgCO2e"))
    TEST_SOCPESET2 = ScopeSet(A1=Measurement(mean=2.0, unit="kgCO2e"))

    def _create_test_impactset(self) -> ImpactSet:
        impactset = ImpactSet()
        impactset.gwp = self.TEST_SOCPESET1
        impactset.set_scopeset_by_name("custom", self.TEST_SOCPESET2)
        return impactset

    def test_scopeset_set_by_name_method(self):
        impactset = self._create_test_impactset()

        self.assertEqual(self.TEST_SOCPESET1, impactset.get_scopeset_by_name("gwp"))
        self.assertEqual(self.TEST_SOCPESET2, impactset.get_scopeset_by_name("custom"))

        impactset_dict = impactset.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        self.assertIn("gwp", impactset_dict)
        self.assertIn("custom", impactset_dict)
        self.assertEqual(
            self.TEST_SOCPESET1.model_dump(by_alias=True, exclude_none=True, exclude_unset=True), impactset_dict["gwp"]
        )
        self.assertEqual(
            self.TEST_SOCPESET2.model_dump(by_alias=True, exclude_none=True, exclude_unset=True),
            impactset_dict["custom"],
        )

    def test_set_item(self):
        impactset = self._create_test_impactset()
        impactset["my-impact"] = self.TEST_SOCPESET1

        self.assertEqual(self.TEST_SOCPESET1, impactset.get_scopeset_by_name("my-impact"))
        impactset_dict = impactset.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)
        self.assertIn("my-impact", impactset_dict)
        self.assertEqual(
            self.TEST_SOCPESET1.model_dump(by_alias=True, exclude_none=True, exclude_unset=True),
            impactset_dict["my-impact"],
        )

    def test_containes_operator(self):
        impactset = self._create_test_impactset()
        impactset["something"] = None
        self.assertIn("gwp", impactset)
        self.assertIn("custom", impactset)
        self.assertNotIn("something", impactset)

    def test_len_operator(self):
        impactset = self._create_test_impactset()
        impactset["something"] = None  # This one should not be included as it is None
        self.assertEqual(len(impactset), 2)

    def test_iter_operator(self):
        impactset = self._create_test_impactset()
        impactset["something"] = None  # This one should not be included as it is None
        impactset_keys = list(impactset)
        self.assertEqual([("gwp", self.TEST_SOCPESET1), ("custom", self.TEST_SOCPESET2)], impactset_keys)

    def test_items_method(self):
        impactset = self._create_test_impactset()
        impactset["something"] = None
        items: list[tuple[str, dict[str, Any]]] = []
        for name, scopeset in impactset.items():
            items.append((name, scopeset.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)))
        expected_items = [
            ("gwp", self.TEST_SOCPESET1.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)),
            ("custom", self.TEST_SOCPESET2.model_dump(by_alias=True, exclude_none=True, exclude_unset=True)),
        ]
        self.assertEqual(expected_items, items)
