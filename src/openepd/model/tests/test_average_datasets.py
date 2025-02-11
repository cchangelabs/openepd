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

from openepd.compat.pydantic import pyd
from openepd.model.generic_estimate import GenericEstimatePreview
from openepd.model.industry_epd import IndustryEpdPreview


class AverageDatasetTestCase(unittest.TestCase):
    def test_generic_estimate_doctype(self):
        self.assertEqual(GenericEstimatePreview.parse_obj({}).doctype, "openGenericEstimate")
        self.assertEqual(
            GenericEstimatePreview.parse_obj({"doctype": "openGenericEstimate"}).doctype, "openGenericEstimate"
        )
        self.assertEqual(GenericEstimatePreview.parse_obj({"id": "EC300001"}).doctype, "openGenericEstimate")

        for o in [{"doctype": None}, {"doctype": "openEPD"}, {"doctype": "openIndustryEpd"}]:
            with self.assertRaises(pyd.ValidationError):
                GenericEstimatePreview.parse_obj(o)

    def test_iepd_doctype(self):
        self.assertEqual(IndustryEpdPreview.parse_obj({}).doctype, "openIndustryEpd")
        self.assertEqual(IndustryEpdPreview.parse_obj({"doctype": "openIndustryEpd"}).doctype, "openIndustryEpd")
        self.assertEqual(IndustryEpdPreview.parse_obj({"id": "EC300001"}).doctype, "openIndustryEpd")

        for o in [{"doctype": None}, {"doctype": "openEPD"}, {"doctype": "openGenericEstimate"}]:
            with self.assertRaises(pyd.ValidationError):
                IndustryEpdPreview.parse_obj(o)
