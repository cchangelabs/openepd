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

from openepd.model.base import BaseOpenEpdSchema, OpenEpdExtension


class MyModel(BaseOpenEpdSchema):
    my_field: str


class MyExtension(OpenEpdExtension):
    test_field: str

    @classmethod
    def get_extension_name(cls) -> str:
        return "my_ext"


class BaseOpenEpdSchemaTestCase(unittest.TestCase):
    def test_serialization_with_extensions(self) -> None:
        """Test that a model with extensions serializes correctly to a dictionary."""

        my_model: MyModel = self._create_model_with_extensions()
        actual: dict = my_model.to_serializable()
        expected: dict = {"my_field": "my_field", "ext": {"my_ext": {"test_field": "test"}, "ext2": {"extra": "data"}}}
        self.assertEqual(expected, actual)

    def test_json_output_with_extensions(self) -> None:
        """Test that a model with extensions serializes correctly to a JSON string."""
        my_model: MyModel = self._create_model_with_extensions()
        actual: str = my_model.to_json()
        expected: str = (
            "{\n"
            '"ext": {\n'
            '"my_ext": {\n'
            '"test_field": "test"\n'
            "},\n"
            '"ext2": {\n'
            '"extra": "data"\n'
            "}\n"
            "},\n"
            '"my_field": "my_field"\n'
            "}"
        )
        self.assertEqual(expected, actual)

    def _create_model_with_extensions(self) -> MyModel:
        """
        Create a MyModel instance with predefined extensions for testing.

        :return: MyModel instance with extensions set.
        """
        my_model: MyModel = MyModel(my_field="my_field")
        my_model.set_ext(MyExtension(test_field="test"))
        my_model.set_ext_field("ext2", {"extra": "data"})
        return my_model
