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
from typing import Any
import unittest

import pydantic as pyd

from openepd.model.common import Measurement
from openepd.model.lcia import Impacts, ImpactSet, LCIAMethod, ScopeSet


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


class ImpactsTestCase(unittest.TestCase):
    def test_model_validate_parses_lcia_method_keys(self) -> None:
        impacts = Impacts.model_validate(
            {
                "TRACI 2.1": {},
                "Unknown LCIA": {},
            }
        )

        self.assertEqual(
            impacts.available_methods(),
            {LCIAMethod.TRACI_2_1, LCIAMethod.UNKNOWN},
        )
        self.assertIsNotNone(impacts.get_impact_set(LCIAMethod.TRACI_2_1))
        self.assertIsNotNone(impacts.get_impact_set(None))

    def test_model_validate_rejects_unsupported_lcia_method(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            Impacts.model_validate({"unsupported method": {}})

    def test_set_unknown_lcia_and_lookup(self) -> None:
        impacts = Impacts({})
        impact_set = ImpactSet()

        impacts.set_unknown_lcia(impact_set)

        self.assertIs(impacts.get_impact_set(None), impact_set)
        self.assertIs(impacts.get_impact_set("unrecognized method"), impact_set)
        self.assertEqual(impacts.available_methods(), {LCIAMethod.UNKNOWN})

    def test_set_impact_set_resolves_method_inputs(self) -> None:
        impacts = Impacts({})
        enum_impact_set = ImpactSet()
        string_impact_set = ImpactSet()
        unknown_impact_set = ImpactSet()
        none_impact_set = ImpactSet()

        impacts.set_impact_set(LCIAMethod.TRACI_2_1, enum_impact_set)
        impacts.set_impact_set("TRACI 2.2", string_impact_set)
        impacts.set_impact_set("not a method", unknown_impact_set)
        self.assertIs(impacts.get_impact_set(None), unknown_impact_set)
        impacts.set_impact_set(None, none_impact_set)

        self.assertIs(impacts.get_impact_set(LCIAMethod.TRACI_2_1), enum_impact_set)
        self.assertIs(impacts.get_impact_set("TRACI 2.2"), string_impact_set)
        self.assertIs(impacts.get_impact_set(None), none_impact_set)
        self.assertEqual(
            impacts.available_methods(),
            {LCIAMethod.TRACI_2_1, LCIAMethod.TRACI_2_2, LCIAMethod.UNKNOWN},
        )

    def test_get_impact_set_returns_default_when_missing(self) -> None:
        impacts = Impacts({})
        default = ImpactSet()

        self.assertIsNone(impacts.get_impact_set(LCIAMethod.TRACI_2_1))
        self.assertIs(impacts.get_impact_set(LCIAMethod.TRACI_2_1, default), default)

    def test_replace_lcia_method_moves_existing_impact_set(self) -> None:
        impact_set = ImpactSet()
        impacts = Impacts({LCIAMethod.TRACI_2_1: impact_set})

        impacts.replace_lcia_method(LCIAMethod.TRACI_2_1, LCIAMethod.TRACI_2_2)

        self.assertIsNone(impacts.get_impact_set(LCIAMethod.TRACI_2_1))
        self.assertIs(impacts.get_impact_set(LCIAMethod.TRACI_2_2), impact_set)

    def test_replace_lcia_method_with_same_method_preserves_impact_set(self) -> None:
        impact_set = ImpactSet()
        other_impact_set = ImpactSet()
        impacts = Impacts(
            {
                LCIAMethod.TRACI_2_1: impact_set,
                LCIAMethod.TRACI_2_2: other_impact_set,
            }
        )
        original_items = list(impacts.root.items())

        impacts.replace_lcia_method(LCIAMethod.TRACI_2_1, LCIAMethod.TRACI_2_1)

        self.assertEqual(list(impacts.root.items()), original_items)

    def test_replace_missing_lcia_method_does_not_change_impacts(self) -> None:
        impact_set = ImpactSet()
        impacts = Impacts({LCIAMethod.TRACI_2_2: impact_set})

        impacts.replace_lcia_method(LCIAMethod.TRACI_2_1, LCIAMethod.TRACI_2_2)

        self.assertEqual(impacts.available_methods(), {LCIAMethod.TRACI_2_2})
        self.assertIs(impacts.get_impact_set(LCIAMethod.TRACI_2_2), impact_set)

    def test_as_dict_returns_underlying_mapping(self) -> None:
        impacts = Impacts({})

        self.assertIs(impacts.as_dict(), impacts.root)
