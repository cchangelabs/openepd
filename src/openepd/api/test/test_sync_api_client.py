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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from os import environ
from typing import cast
import unittest

from requests import Response

from openepd.api.errors import ApiError, AuthError, ValidationError
from openepd.api.sync_client import OpenEpdApiClientSync
from openepd.model.epd import Epd
from openepd.model.pcr import Pcr


@unittest.skipUnless(
    environ.get("OPENEPD_API_URL") and environ.get("OPENEPD_API_TOKEN"),
    "OPENEPD_API_URL and OPENEPD_API_TOKEN must be set to run this test",
)
class SyncClientApiTestCase(unittest.TestCase):
    api_client: OpenEpdApiClientSync

    def setUp(self):
        self.api_client = OpenEpdApiClientSync(
            environ.get("OPENEPD_API_URL"),
            environ.get("OPENEPD_API_TOKEN"),
        )

    def test_get_existing_epd_by_id(self):
        epd = self.api_client.epds.get_by_openxpd_uuid("ec3b9j5t")
        self.assertEqual(epd.id, "ec3b9j5t")

    def test_iterate_over_list(self):
        page_size = 2
        max_iterations = 5
        epds = self.api_client.epds.find('!EC3 search("AluminiumBillets") !pragma oMF("1.0/1")', page_size=page_size)
        ids = []
        for x in epds:
            ids.append(x.id)
            if len(ids) >= max_iterations * page_size:
                break
        unique_ids = set(ids)
        self.assertGreater(len(ids), page_size)
        self.assertEqual(len(ids), len(unique_ids), "Duplicate IDs found in list")

    def test_get_category_tree(self):
        tree = self.api_client.categories.get_tree()
        self.assertEqual("AllMaterials", tree.short_name)
        self.assertGreater(len(tree.subcategories), 0)

    def test_get_statistics(self):
        mf = '!EC3 search("AluminiumBillets") WHERE valid_until: > "2023-04-20" !pragma oMF("1.0/1")'
        stats = self.api_client.epds.get_statistics(mf)
        self.assertEqual(stats.declared_unit.qty, 1.0)
        self.assertEqual(stats.declared_unit.unit, "kg")
        self.assertIsNotNone(stats.average)
        self.assertIsNotNone(stats.epds_count)

    def test_get_statistics_invalid_omf(self):
        with self.assertRaises(ValidationError) as cm:
            self.api_client.epds.get_statistics("something invalid")

        exc = cast(ValidationError, cm.exception)
        self.assertEqual("invalid", exc.error_code)
        self.assertEqual(400, exc.http_status)
        self.assertGreater(len(exc.error_summary), 0)

    def test_get_statistics_omf_incorrect_field(self):
        with self.assertRaises(ValidationError) as cm:
            self.api_client.epds.get_statistics(
                '!EC3 search("AluminiumBillets") WHERE blah: > "2023-04-20" !pragma oMF("1.0/1")'
            )

        exc = cast(ValidationError, cm.exception)
        self.assertEqual("invalid", exc.error_code)
        self.assertEqual(400, exc.http_status)
        self.assertGreater(len(exc.error_summary), 0)

    def test_pcr_get_by_openxpd_uuid(self):
        pcr = self.api_client.pcrs.get_by_openxpd_uuid("ec3c8gt7")
        self.assertEqual(pcr.id, "ec3c8gt7")

    def test_create_pcr(self):
        new_pcr = Pcr.parse_obj(
            {
                "issuer": {"web_domain": "environdec.com"},
                "name": "Test PCR full name",
                "short_name": "Test PCR",
                "version": "1",
                "doc": "https://non-existing-url.com/pcrs/non-existing-pcr.pdf",
            }
        )
        try:
            pcr_ref = self.api_client.pcrs.create(new_pcr)
        except ApiError as e:
            raise e
        self.assertEqual("Test PCR full name", pcr_ref.name)
        self.assertIsNotNone(pcr_ref.id)
        self.assertIsNotNone(pcr_ref.ref)

    def test_auth_error(self):
        with self.assertRaises(AuthError):
            api_client = OpenEpdApiClientSync(
                environ.get("OPENEPD_API_URL"),
                "invalid-token",
            )
            api_client.epds.get_by_openxpd_uuid("ec3b9j5t")


@unittest.skip("This test is for local debugging only")
@unittest.skipUnless(
    environ.get("OPENEPD_API_URL") and environ.get("OPENEPD_API_TOKEN"),
    "OPENEPD_API_URL and OPENEPD_API_TOKEN must be set to run this test",
)
class LocalOnlySyncClientApiTestCase(unittest.TestCase):
    api_client: OpenEpdApiClientSync

    def setUp(self):
        self.api_client = OpenEpdApiClientSync(
            environ.get("OPENEPD_API_URL"),
            environ.get("OPENEPD_API_TOKEN"),
        )

    def test_post_with_refs(self):
        epd = self.api_client.epds.get_by_openxpd_uuid("ec3r59df")
        epd_dict = epd.to_serializable(exclude_unset=True, exclude_none=True)
        epd_dict.update(
            {
                "openepd_version": "0.1",
                "doctype": "OpenEPD",
                "id": "ec3r59df",
                "product_name": "4F0Z95E1 UPDATED FOR TESTING",
            }
        )
        epd = Epd.parse_obj(epd_dict)
        epd_updated = self.api_client.epds.post_with_refs(epd)
        self.assertIsNotNone(epd_updated)

    def test_post_with_refs_invalid_epd(self):
        epd = self.api_client.epds.get_by_openxpd_uuid("ec3r59df")
        epd_dict = epd.to_serializable(exclude_unset=True, exclude_none=True)
        epd_dict.update(
            {
                "openepd_version": "0.1",
                "doctype": "OpenEPD",
                "id": "ec3r59df",
                "valid_until": "2023-04-20",
                "date_of_issue": "2025-04-20",
                "product_name": "4F0Z95E1 UPDATED FOR TESTING",
            }
        )
        try:
            self.api_client.epds.post_with_refs(Epd.parse_obj(epd_dict))
        except Exception as e:
            self.assertIsInstance(e.errors(), list)  # type: ignore
        else:
            self.assertFalse(True, "Should not reach this point")  # NOSONAR

    def test_post_with_refs_return_response(self):
        epd = self.api_client.epds.get_by_openxpd_uuid("ec3r59df")
        epd_updated, response = self.api_client.epds.post_with_refs(epd, with_response=True)
        self.assertIsNotNone(response)
        self.assertIsNotNone(epd_updated)
        self.assertIsInstance(response, Response)
        self.assertTrue(epd_updated, Epd)
        self.assertTrue(response.ok)
