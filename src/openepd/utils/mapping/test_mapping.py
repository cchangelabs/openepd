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
import re
from unittest import TestCase

from openepd.utils.mapping.common import KeyValueMapper, ReferenceMapper, RegexMapper, SimpleDataMapper


class SimpleDataMapperTest(TestCase):
    """Test cases for SimpleDataMapper class."""

    def test_map_with_existing_value(self):
        """Test mapping with an existing value in the database."""

        class TestMapper(SimpleDataMapper[str]):
            DATABASE = {"key1": "value1", "key2": "value2", "key3": "value3"}

        mapper = TestMapper()
        result = mapper.map("key1", None)
        self.assertEqual(result, "value1")

    def test_map_with_non_existing_value(self):
        """Test mapping with a non-existing value in the database."""

        class TestMapper(SimpleDataMapper[str]):
            DATABASE = {"key1": "value1", "key2": "value2", "key3": "value3"}

        mapper = TestMapper()
        result = mapper.map("key4", None)
        self.assertIsNone(result)

    def test_map_with_default_value(self):
        """Test mapping with a non-existing value and a default value."""

        class TestMapper(SimpleDataMapper[str]):
            DATABASE = {"key1": "value1", "key2": "value2", "key3": "value3"}

        mapper = TestMapper()
        result = mapper.map("key4", "default_value")
        self.assertEqual(result, "default_value")

    def test_map_with_raise_if_missing(self):
        """Test mapping with raise_if_missing=True for a non-existing value."""

        class TestMapper(SimpleDataMapper[str]):
            DATABASE = {"key1": "value1", "key2": "value2", "key3": "value3"}

        mapper = TestMapper()
        with self.assertRaises(ValueError):
            mapper.map("key4", None, raise_if_missing=True)


class KeyValueMapperTest(TestCase):
    """Test cases for KeyValueMapper class."""

    def test_map_with_matching_keyword(self):
        """Test mapping with a matching keyword."""

        class TestMapper(KeyValueMapper[str]):
            KV = {
                "impact1": ["keyword1", "keyword2"],
                "impact2": ["keyword3", "keyword4"],
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with keyword1", None)
        self.assertEqual(result, "impact1")

    def test_map_with_case_insensitive_match(self):
        """Test mapping with a case-insensitive match."""

        class TestMapper(KeyValueMapper[str]):
            KV = {
                "impact1": ["keyword1", "keyword2"],
                "impact2": ["keyword3", "keyword4"],
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with KEYWORD1", None)
        self.assertEqual(result, "impact1")

    def test_map_with_non_matching_keyword(self):
        """Test mapping with a non-matching keyword."""

        class TestMapper(KeyValueMapper[str]):
            KV = {
                "impact1": ["keyword1", "keyword2"],
                "impact2": ["keyword3", "keyword4"],
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with no matching keywords", None)
        self.assertIsNone(result)

    def test_map_with_default_value(self):
        """Test mapping with a non-matching keyword and a default value."""

        class TestMapper(KeyValueMapper[str]):
            KV = {
                "impact1": ["keyword1", "keyword2"],
                "impact2": ["keyword3", "keyword4"],
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with no matching keywords", "default_impact")
        self.assertEqual(result, "default_impact")

    def test_map_with_raise_if_missing(self):
        """Test mapping with raise_if_missing=True for a non-matching keyword."""

        class TestMapper(KeyValueMapper[str]):
            KV = {
                "impact1": ["keyword1", "keyword2"],
                "impact2": ["keyword3", "keyword4"],
            }

        mapper = TestMapper()
        with self.assertRaises(ValueError):
            mapper.map("This is a test with no matching keywords", None, raise_if_missing=True)


class RegexMapperTest(TestCase):
    """Test cases for RegexMapper class."""

    def test_map_with_matching_pattern(self):
        """Test mapping with a matching pattern."""

        class TestMapper(RegexMapper[str]):
            PATTERNS = {
                "impact1": r"pattern1|pattern2",
                "impact2": r"pattern3|pattern4",
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with pattern1", None)
        self.assertEqual(result, "impact1")

    def test_map_with_case_insensitive_match(self):
        """Test mapping with a case-insensitive match."""

        class TestMapper(RegexMapper[str]):
            PATTERNS = {
                "impact1": r"pattern1|pattern2",
                "impact2": r"pattern3|pattern4",
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with PATTERN1", None)
        self.assertEqual(result, "impact1")

    def test_map_with_non_matching_pattern(self):
        """Test mapping with a non-matching pattern."""

        class TestMapper(RegexMapper[str]):
            PATTERNS = {
                "impact1": r"pattern1|pattern2",
                "impact2": r"pattern3|pattern4",
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with no matching patterns", None)
        self.assertIsNone(result)

    def test_map_with_default_value(self):
        """Test mapping with a non-matching pattern and a default value."""

        class TestMapper(RegexMapper[str]):
            PATTERNS = {
                "impact1": r"pattern1|pattern2",
                "impact2": r"pattern3|pattern4",
            }

        mapper = TestMapper()
        result = mapper.map("This is a test with no matching patterns", "default_impact")
        self.assertEqual(result, "default_impact")

    def test_map_with_raise_if_missing(self):
        """Test mapping with raise_if_missing=True for a non-matching pattern."""

        class TestMapper(RegexMapper[str]):
            PATTERNS = {
                "impact1": r"pattern1|pattern2",
                "impact2": r"pattern3|pattern4",
            }

        mapper = TestMapper()
        with self.assertRaises(ValueError):
            mapper.map("This is a test with no matching patterns", None, raise_if_missing=True)


class ReferenceMapperTest(TestCase):
    """Test cases for ReferenceMapper class."""

    def test_map_with_string_rule(self):
        """Test mapping with a string rule."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": "value1",
                "key2": "value2",
            }

        mapper = TestMapper()
        result = mapper.map("value1", None)
        self.assertEqual(result, "key1")

    def test_map_with_regex_rule(self):
        """Test mapping with a regex rule."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": re.compile(r"pattern1"),
                "key2": re.compile(r"pattern2"),
            }

        mapper = TestMapper()
        result = mapper.map("This contains pattern1", None)
        self.assertEqual(result, "key1")

    def test_map_with_list_of_rules(self):
        """Test mapping with a list of rules."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": ["value1", "value2"],
                "key2": ["value3", re.compile(r"pattern4")],
            }

        mapper = TestMapper()
        # Test with string match
        result1 = mapper.map("value1", None)
        self.assertEqual(result1, "key1")

        # Test with regex match
        result2 = mapper.map("This contains pattern4", None)
        self.assertEqual(result2, "key2")

    def test_map_with_case_insensitive_match(self):
        """Test mapping with a case-insensitive match."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": "value1",
                "key2": re.compile(r"pattern2", re.IGNORECASE),
            }

        mapper = TestMapper()
        # Test with string match
        result1 = mapper.map("VALUE1", None)
        self.assertEqual(result1, "key1")

        # Test with regex match
        result2 = mapper.map("This contains PATTERN2", None)
        self.assertEqual(result2, "key2")

    def test_map_with_non_matching_rule(self):
        """Test mapping with a non-matching rule."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": "value1",
                "key2": re.compile(r"pattern2"),
            }

        mapper = TestMapper()
        result = mapper.map("no_match", None)
        self.assertIsNone(result)

    def test_map_with_default_value(self):
        """Test mapping with a non-matching rule and a default value."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": "value1",
                "key2": re.compile(r"pattern2"),
            }

        mapper = TestMapper()
        result = mapper.map("no_match", "default_key")
        self.assertEqual(result, "default_key")

    def test_map_with_raise_if_missing(self):
        """Test mapping with raise_if_missing=True for a non-matching rule."""

        class TestMapper(ReferenceMapper):
            MAPPING = {
                "key1": "value1",
                "key2": re.compile(r"pattern2"),
            }

        mapper = TestMapper()
        with self.assertRaises(ValueError):
            mapper.map("no_match", None, raise_if_missing=True)
