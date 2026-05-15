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
"""
Tests for reflection utilities (fields_traverse and helpers).

These tests exercise nested models, container handling, exclusion matchers,
and ensure recursion does not loop infinitely for self-referential models.
"""

from __future__ import annotations

import unittest

import pydantic as pyd

from openepd.utils.reflection import FieldInfo, TypeWithContainer, fields_traverse


class ReflectionTestCase(unittest.TestCase):
    """Tests for reflection utilities (fields_traverse and helpers)."""

    def test_fields_traverse_basic(self) -> None:
        """Ensure basic nested fields are discovered with correct metadata."""

        class Address(pyd.BaseModel):
            street: str = pyd.Field(..., description="Street name")
            city: str

        class Person(pyd.BaseModel):
            name: str
            age: int | None
            address: Address

        fields = fields_traverse(Person)
        self.assertEqual(set(fields.keys()), {"name", "age", "address.street", "address.city"})

        # Verify metadata for an annotated field
        street_info: FieldInfo = fields["address.street"]
        self.assertEqual(street_info.description, "Street name")
        self.assertFalse(street_info.is_optional)

        age_info: FieldInfo = fields["age"]
        self.assertTrue(age_info.is_optional)

    def test_fields_traverse_containers_and_exclude(self) -> None:
        """Containers (list/dict) should be unwrapped and exclusion matchers respected."""

        class Address(pyd.BaseModel):
            street: str
            city: str

        class Company(pyd.BaseModel):
            employees: list[Address]
            office_by_city: dict[str, Address]

        all_fields = fields_traverse(Company)
        expected = {
            "employees.street",
            "employees.city",
            "office_by_city.street",
            "office_by_city.city",
        }
        self.assertTrue(expected.issubset(set(all_fields.keys())))

        # Excluding a top-level field name (by exact field name) removes its nested entries
        no_emps = fields_traverse(Company, exclude_list={"employees"})
        self.assertFalse(any(k.startswith("employees.") for k in no_emps.keys()))
        self.assertTrue(any(k.startswith("office_by_city.") for k in no_emps.keys()))

        # Excluding a full path using '^' excludes that specific nested key
        excl_city = fields_traverse(Company, exclude_list={"^office_by_city.city"})
        self.assertNotIn("office_by_city.city", excl_city)
        self.assertIn("office_by_city.street", excl_city)

    def test_self_referential_and_callable_exclude(self) -> None:
        """Self-referential models should not recurse infinitely and callable excludes work."""

        class SelfRef(pyd.BaseModel):
            c: SelfRef | None = None
            val: int

        # Resolve forward refs (pydantic v2)
        SelfRef.model_rebuild()

        fields = fields_traverse(SelfRef)
        # Top-level and one-level nested field should be present
        self.assertIn("val", fields)
        self.assertIn("c.val", fields)
        # Ensure recursion stopped at one level (no c.c.val keys)
        self.assertFalse(any(k.startswith("c.c") for k in fields.keys()))

        # Exclude via callable matcher: remove any field whose full name ends with 'val'
        def ends_with_val(name: str, full_name: str) -> bool:  # pragma: no cover - simple helper
            return full_name.endswith("val")

        excl = fields_traverse(SelfRef, exclude_list={ends_with_val})
        self.assertNotIn("val", excl)
        self.assertNotIn("c.val", excl)

    def test_modify_field_name_simple(self) -> None:
        """Modifier is applied to top-level fields and reflected in keys and FieldInfo.name."""

        class M(pyd.BaseModel):
            a: int
            b: str

        def prefix_mod(name: str, data_type: TypeWithContainer, delimiter: str) -> str:
            # Delimiter is accepted for compatibility but unused in this simple modifier
            return "x_" + name

        result = fields_traverse(M, modify_field_name=prefix_mod)
        self.assertSetEqual(set(result.keys()), {"x_a", "x_b"})
        self.assertEqual(result["x_a"].name, "x_a")
        self.assertEqual(result["x_b"].name, "x_b")

    def test_modify_field_name_nested_and_container(self) -> None:
        """Modifiers receive type information and are used for nested prefixes and lists."""

        class Address(pyd.BaseModel):
            street: str
            city: str

        class Person(pyd.BaseModel):
            address: Address
            tags: list[str]

        def mod(name: str, data_type: TypeWithContainer, delimiter: str) -> str:
            # Append a suffix for list containers, prefix otherwise
            if data_type.container_type is list:
                return name + "_list"
            return "x_" + name

        result = fields_traverse(Person, modify_field_name=mod)
        self.assertIn("x_address.x_street", result)
        self.assertIn("x_address.x_city", result)
        self.assertIn("tags_list", result)
        self.assertEqual(result["tags_list"].name, "tags_list")
