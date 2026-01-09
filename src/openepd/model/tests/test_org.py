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
from openepd.model.org import Org, OrgRef
from openepd.model.tests.common import ImageFieldTestCase


class OrgTestCase(ImageFieldTestCase):
    def test_logo(self) -> None:
        self._test_data_url_image_field(Org, "logo")

    def test_org_subsidiary_is_orgref_instance(self) -> None:
        """
        Test that a subsidiary entry in the Org model is correctly validated as an OrgRef instance.

        This test ensures that when an Org is instantiated with a subsidiary dictionary, the resulting
        subsidiary object is an instance of OrgRef.
        """
        org_data: dict = {
            "subsidiaries": [
                {
                    "web_domain": "epd-australasia.com",
                    "name": "EPD Australasia",
                    "ref": "https://openepd.cqd.io/api/orgs/epd-australasia.com",
                }
            ],
        }
        org_instance: Org = Org.model_validate(org_data)
        self.assertIsInstance(org_instance.subsidiaries[0], OrgRef)
