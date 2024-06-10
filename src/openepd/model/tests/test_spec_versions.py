#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
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

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.generated.steel import SteelV1


class SpecVersionTestCase(unittest.TestCase):
    def test_version_is_output_by_default(self):
        steel = SteelV1(recycled_content=0.3)
        self.assertEqual(steel.to_serializable()["ext_version"], "1.0")

    def test_version_validation(self):
        accepted_v1_versions = ["1.0", "1.33", "1.2"]
        wrong_v1_versions = [None, "17", 17, "2.0", "abc", "1.b", "1.2.33"]

        for version in accepted_v1_versions:
            SteelV1(ext_version=version, recycled_content=0.3)

        for version in wrong_v1_versions:
            with self.assertRaises(ValueError):
                SteelV1(ext_version=version, recycled_content=0.3)

    def test_fail_early_if_forgot_to_declare_ext_version(self):
        class SpecV1WithoutExtVersion(BaseOpenEpdHierarchicalSpec):
            pass

        class SpecV1WithWrongVersion(BaseOpenEpdHierarchicalSpec):
            _EXT_VERSION = "ABC"

        with self.assertRaises(ValueError):
            SpecV1WithoutExtVersion()

        with self.assertRaises(ValueError):
            SpecV1WithWrongVersion()
