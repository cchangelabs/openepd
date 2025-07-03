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
import unittest

from openepd.model.epd import Epd
from openepd.model.lcia import Impacts


class SchemaGenerationTestCase(unittest.TestCase):
    def test_impacts_schema(self):
        expected_property_def = {"allOf": [{"$ref": "#/components/schemas/ImpactSet"}]}
        actual = Impacts.model_json_schema(ref_template="#/components/schemas/{model}")
        for key in actual["properties"]:
            actual_def = {"allOf": actual["properties"][key]["allOf"]}
            self.assertEqual(expected_property_def, actual_def)

    def test_epd_generated_without_errors_schema(self):
        Epd.model_json_schema(ref_template="#/components/schemas/{model}")
