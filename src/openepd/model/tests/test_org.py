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

from openepd.model.org import ORG_LOGO_MAX_LENGTH, Org


class OrgTestCase(unittest.TestCase):
    def test_logo(self):
        Org.model_validate({"logo": "data:image/png;base64,NSUhiVRw0KGgoAAAABO"})
        Org.model_validate({"logo": "data:image/png,NSUhiVRw0KGgoAAAABO"})
        Org.model_validate({"logo": "data:;base64,NSUhiVRw0KGgoAAAABO"})
        Org.model_validate({"logo": "data:,NSUhiVRw0KGgoAAAABO"})
        Org.model_validate({"logo": "https://example.com"})

        with self.assertRaises(ValueError):
            Org.model_validate({"logo": "example"})
        with self.assertRaises(ValueError):
            Org.model_validate({"logo": "example.com"})
        with self.assertRaises(ValueError):
            # image data should be <= 32KB
            Org.model_validate({"logo": "data:image/png;base64," + "a" * ORG_LOGO_MAX_LENGTH})
        with self.assertRaises(ValueError):
            # invalid dataUrl
            Org.model_validate({"logo": "data:base64,NSUhiVRw0KGgoAAAABO"})
        with self.assertRaises(ValueError):
            # invalid dataUrl
            Org.model_validate({"logo": "data:NSUhiVRw0KGgoAAAABO"})
