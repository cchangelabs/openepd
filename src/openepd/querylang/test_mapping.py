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
import json
import unittest

from openepd.utils.reflection import is_field_matched

from .dto import FieldMappingDto
from .mapping import (
    FieldMappingLibrary,
    is_field_matched_by_def,
)


def _build_sample_field_mappings() -> list[FieldMappingDto]:
    return [
        FieldMappingDto(
            lang_field_name="section.sub.field1",
            target_field_name="db.field_one",
            datatype="string",
            description="first field",
            supported_operators=["=", "!="],
        ),
        FieldMappingDto(
            lang_field_name="section.sub.field2",
            target_field_name="db.field_two",
            datatype="int",
            description="second field",
            supported_operators=[">", "<"],
        ),
        FieldMappingDto(
            lang_field_name="another.group.field3",
            target_field_name="db.field_three",
            datatype="bool",
        ),
    ]


class TestMappingHelpers(unittest.TestCase):
    def test_is_field_matched_string_short_name(self):
        with self.subTest("match short name equal"):
            self.assertTrue(is_field_matched("a.b.c", "c", "c"))
        with self.subTest("mismatch short name"):
            self.assertFalse(is_field_matched("a.b.c", "c", "x"))

    def test_is_field_matched_string_full_name_with_caret(self):
        with self.subTest("full name exact"):
            self.assertTrue(is_field_matched("a.b.c", "c", "^a.b.c"))
        with self.subTest("full name partial should not match"):
            self.assertFalse(is_field_matched("a.b.c", "c", "^a.b"))

    def test_is_field_matched_callable(self):
        def matcher(name: str, full_name: str) -> bool:
            return name.startswith("f") and full_name.endswith("3")

        with self.subTest("callable matches"):
            self.assertTrue(is_field_matched("x.y.field3", "field3", matcher))
        with self.subTest("callable mismatch"):
            self.assertFalse(is_field_matched("x.y.field2", "field2", matcher))

    def test_is_field_matched_by_def_uses_delimiter(self):
        fm = _build_sample_field_mappings()[0]
        with self.subTest("short name matches"):
            self.assertTrue(is_field_matched_by_def(fm, "field1", "."))
        with self.subTest("caret full name matches"):
            self.assertTrue(is_field_matched_by_def(fm, "^section.sub.field1", "."))
        with self.subTest("caret other full name mismatch"):
            self.assertFalse(is_field_matched_by_def(fm, "^section.sub.field2", "."))


class TestFieldMappingLibrary(unittest.TestCase):
    def setUp(self):
        self.sample = _build_sample_field_mappings()

    def test_library_from_list_and_get_by_name(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        self.assertIs(lib.get_by_name("section.sub.field1"), self.sample[0])
        self.assertIsNone(lib.get_by_name("missing"))

    def test_library_from_json(self):
        json_str = json.dumps([fm.model_dump() for fm in self.sample])
        lib = FieldMappingLibrary.from_json(json_str)
        self.assertIsInstance(lib.get_by_name("section.sub.field2"), FieldMappingDto)
        self.assertEqual(lib.delimiter, ".")

    def test_add_and_iteration(self):
        lib = FieldMappingLibrary.from_list(self.sample[:2])
        lib.add(self.sample[2])
        names = {fm.lang_field_name for fm in lib}
        self.assertSetEqual(
            names,
            {"section.sub.field1", "section.sub.field2", "another.group.field3"},
        )

    def test_get_first_with_string_and_callable(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        self.assertEqual(lib.get_first("field2").lang_field_name, "section.sub.field2")
        self.assertEqual(lib.get_first("^another.group.field3").lang_field_name, "another.group.field3")

        def starts_with_field(name: str, full: str) -> bool:
            return name.startswith("field")

        self.assertIn(
            lib.get_first(starts_with_field).lang_field_name,
            {"section.sub.field1", "section.sub.field2", "another.group.field3"},
        )

    def test_filter_accepts_multiple_matchers(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        result = lib.filter("field1", "^another.group.field3")
        names = sorted(fm.lang_field_name for fm in result)
        self.assertListEqual(names, ["another.group.field3", "section.sub.field1"])

    def test_override_single(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        lib.override(
            "field1",
            target_field_name="db.field_1",
            datatype="text",
            description="changed",
            supported_operators=["in"],
        )
        fm = lib.get_by_name("section.sub.field1")
        self.assertEqual(fm.target_field_name, "db.field_1")
        self.assertEqual(fm.datatype, "text")
        self.assertEqual(fm.description, "changed")
        self.assertEqual(fm.supported_operators, ["in"])

    def test_override_raises_when_not_found(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        with self.assertRaises(KeyError):
            lib.override("missing", description="nope")

    def test_override_all(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        matchers = ["field1", "^another.group.field3"]
        lib.override_all(matchers, datatype="custom")
        self.assertEqual(lib.get_by_name("section.sub.field1").datatype, "custom")
        self.assertEqual(lib.get_by_name("another.group.field3").datatype, "custom")
        # Unmatched remains unchanged
        self.assertEqual(lib.get_by_name("section.sub.field2").datatype, "int")

    def test_exclude(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        lib.exclude("field2")
        self.assertIsNone(lib.get_by_name("section.sub.field2"))
        # others remain
        self.assertIsNotNone(lib.get_by_name("section.sub.field1"))

    def test_keep_only(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        lib.keep_only({"^section.sub.field1", "field3"})
        names = {fm.lang_field_name for fm in lib}
        self.assertSetEqual(names, {"section.sub.field1", "another.group.field3"})

    def test_clone_and_to_list(self):
        lib = FieldMappingLibrary.from_list(self.sample)
        clone = lib.clone()
        # Mutate original, clone should not change
        lib.override("field1", description="original changed")
        cloned_fm = clone.get_by_name("section.sub.field1")
        self.assertEqual(cloned_fm.description, "first field")

        as_list = clone.to_list()
        self.assertIsInstance(as_list, list)
        self.assertSetEqual(
            {fm.lang_field_name for fm in as_list},
            {"section.sub.field1", "section.sub.field2", "another.group.field3"},
        )
