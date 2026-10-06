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


class LCIAMethodTestCase(unittest.TestCase):
    def test_normalize_method(self) -> None:
        self.assertIs(LCIAMethod.normalize_method("TRACI 2.1"), LCIAMethod.TRACI_2_1)
        self.assertEqual(LCIAMethod.normalize_method("custom method"), "custom method")
        self.assertIs(LCIAMethod.normalize_method(LCIAMethod.TRACI_2_1), LCIAMethod.TRACI_2_1)
        self.assertIs(LCIAMethod.normalize_method(None), LCIAMethod.UNKNOWN)
        self.assertIsNone(LCIAMethod.normalize_method(None, none_as_unknown=False))


class ImpactsTestCase(unittest.TestCase):
    def test_model_validate_parses_lcia_method_keys(self) -> None:
        impacts = Impacts.model_validate(
            {
                "TRACI 2.1": {},
                "Unknown LCIA": {},
                "Custom LCIA": {},
            }
        )

        self.assertEqual(
            impacts.available_methods(),
            {LCIAMethod.TRACI_2_1, LCIAMethod.UNKNOWN, "Custom LCIA"},
        )
        self.assertIsNotNone(impacts.get_impact_set(LCIAMethod.TRACI_2_1))
        self.assertIsNotNone(impacts.get_impact_set(None))
        self.assertIsInstance(impacts.root["Custom LCIA"], ImpactSet)

    def test_set_unknown_lcia_and_lookup(self) -> None:
        impacts = Impacts({})
        impact_set = ImpactSet()

        impacts.set_unknown_lcia(impact_set)

        self.assertIs(impacts.get_impact_set(None), impact_set)
        self.assertIsNone(impacts.get_impact_set("unrecognized method"))
        self.assertEqual(impacts.available_methods(), {LCIAMethod.UNKNOWN})

    def test_get_custom_lcia_method(self) -> None:
        impacts = Impacts({})
        custom_impact_set = ImpactSet()
        impacts.set_impact_set("Custom LCIA", custom_impact_set)

        self.assertIs(impacts.get_impact_set("Custom LCIA"), custom_impact_set)
        self.assertIsNone(impacts.get_impact_set("custom lcia"))

    def test_set_impact_set_resolves_method_inputs(self) -> None:
        cases = (
            (LCIAMethod.TRACI_2_1, LCIAMethod.TRACI_2_1),
            ("TRACI 2.2", LCIAMethod.TRACI_2_2),
            (LCIAMethod.UNKNOWN, LCIAMethod.UNKNOWN),
            ("Unknown LCIA", LCIAMethod.UNKNOWN),
            ("not a method", "not a method"),
            ("traci 2.1", "traci 2.1"),
            (None, LCIAMethod.UNKNOWN),
        )
        for method, expected_key in cases:
            with self.subTest(method=method):
                impacts = Impacts({})
                impact_set = ImpactSet()

                impacts.set_impact_set(method, impact_set)

                self.assertEqual(list(impacts.root), [expected_key])
                stored_key = next(iter(impacts.root))
                if isinstance(expected_key, LCIAMethod):
                    self.assertIs(stored_key, expected_key)
                else:
                    self.assertIs(type(stored_key), str)
                self.assertIs(impacts.root[expected_key], impact_set)

    def test_set_impact_set_preserves_custom_and_case_sensitive_methods(self) -> None:
        impacts = Impacts({})
        methods = (LCIAMethod.TRACI_2_1, "traci 2.1", "not a method", None)
        impact_sets = [ImpactSet() for _ in methods]

        for method, impact_set in zip(methods, impact_sets, strict=True):
            impacts.set_impact_set(method, impact_set)

        self.assertEqual(
            set(impacts.root),
            {LCIAMethod.TRACI_2_1, "traci 2.1", "not a method", LCIAMethod.UNKNOWN},
        )
        for key, impact_set in zip(
            (LCIAMethod.TRACI_2_1, "traci 2.1", "not a method", LCIAMethod.UNKNOWN),
            impact_sets,
            strict=True,
        ):
            self.assertIs(impacts.root[key], impact_set)

    def test_set_impact_set_replaces_existing_impact_set(self) -> None:
        cases = (
            (LCIAMethod.TRACI_2_1, "TRACI 2.1", LCIAMethod.TRACI_2_1),
            ("TRACI 2.1", LCIAMethod.TRACI_2_1, LCIAMethod.TRACI_2_1),
            ("not a method", "not a method", "not a method"),
            ("traci 2.1", "traci 2.1", "traci 2.1"),
            (None, None, LCIAMethod.UNKNOWN),
            (LCIAMethod.UNKNOWN, None, LCIAMethod.UNKNOWN),
            (None, "Unknown LCIA", LCIAMethod.UNKNOWN),
        )
        for original_method, replacement_method, expected_key in cases:
            with self.subTest(original_method=original_method, replacement_method=replacement_method):
                impacts = Impacts({})
                original_impact_set = ImpactSet()
                replacement_impact_set = ImpactSet()
                impacts.set_impact_set(original_method, original_impact_set)

                impacts.set_impact_set(replacement_method, replacement_impact_set)

                self.assertEqual(list(impacts.root), [expected_key])
                self.assertIs(impacts.root[expected_key], replacement_impact_set)

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

    def test_replace_lcia_method_supports_method_names_and_custom_methods(self) -> None:
        cases = (
            ("Custom LCIA", "Another custom LCIA", "Another custom LCIA"),
            ("Custom LCIA", "TRACI 2.2", LCIAMethod.TRACI_2_2),
            ("TRACI 2.1", "Custom LCIA", "Custom LCIA"),
            ("TRACI 2.1", "TRACI 2.2", LCIAMethod.TRACI_2_2),
        )
        for source, destination, expected_key in cases:
            with self.subTest(source=source, destination=destination):
                impacts = Impacts({})
                impact_set = ImpactSet()
                impacts.set_impact_set(source, impact_set)

                impacts.replace_lcia_method(source, destination)

                self.assertEqual(list(impacts.root), [expected_key])
                self.assertIs(impacts.root[expected_key], impact_set)

    def test_replace_lcia_method_when_supported_method_is_stored_as_string(self) -> None:
        impact_set = ImpactSet()
        impacts = Impacts({})
        impacts.root["TRACI 2.1"] = impact_set

        self.assertIs(type(next(iter(impacts.root))), str)

        impacts.replace_lcia_method("TRACI 2.1", "Custom LCIA")

        self.assertEqual(list(impacts.root), ["Custom LCIA"])
        self.assertIs(impacts.root["Custom LCIA"], impact_set)

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
