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

from openepd.model.org import Plant


class PlantTestCase(unittest.TestCase):
    def test_plant_parse(self):
        test_data = {
            "id": "85644Q4R+3P.cemex.com",
            "name": "Redlands RM (DUAL)",
            "ref": "https://openepd.staging.epd.world/api/plants/85644Q4R+3P.cemex.com",
            "pluscode": "85644Q4R+3P",
            "address": "8203 Alabama St, Highland, CA 92346, USA",
        }
        p = Plant.parse_obj(test_data)

        self.assertEqual(p.id, "85644Q4R+3P.cemex.com")
