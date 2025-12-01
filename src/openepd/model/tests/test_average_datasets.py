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

import pydantic

from openepd.model.common import Constituent
from openepd.model.generic_estimate import GenericEstimatePreview
from openepd.model.industry_epd import IndustryEpdPreview
from openepd.model.tests.common import GE_REQUIRED_FIELDS


class AverageDatasetTestCase(unittest.TestCase):
    def test_generic_estimate_doctype(self):
        self.assertEqual(GenericEstimatePreview.model_validate({**GE_REQUIRED_FIELDS}).doctype, "openGenericEstimate")
        self.assertEqual(
            GenericEstimatePreview.model_validate({"doctype": "openGenericEstimate", **GE_REQUIRED_FIELDS}).doctype,
            "openGenericEstimate",
        )
        self.assertEqual(
            GenericEstimatePreview.model_validate(GE_REQUIRED_FIELDS).doctype,
            "openGenericEstimate",
        )

        for o in [
            {"doctype": None},
            {"doctype": "openEPD"},
            {"doctype": "openIndustryEpd"},
        ]:
            with self.assertRaises(pydantic.ValidationError):
                GenericEstimatePreview.model_validate({**GE_REQUIRED_FIELDS, **o})

    def test_iepd_doctype(self):
        self.assertEqual(IndustryEpdPreview.model_validate({}).doctype, "openIndustryEpd")
        self.assertEqual(
            IndustryEpdPreview.model_validate({"doctype": "openIndustryEpd"}).doctype,
            "openIndustryEpd",
        )
        self.assertEqual(
            IndustryEpdPreview.model_validate({"id": "EC300001"}).doctype,
            "openIndustryEpd",
        )

        for o in [
            {"doctype": None},
            {"doctype": "openEPD"},
            {"doctype": "openGenericEstimate"},
        ]:
            with self.assertRaises(pydantic.ValidationError):
                IndustryEpdPreview.model_validate(o)


class GECompositionTestCase(unittest.TestCase):
    def test_generic_estimate_composition_constituent_bounds(self) -> None:
        # Valid constituent
        valid_constituent = Constituent(
            name="Test Constituent",
            kg_C=10.0,
            kg_C_biogenic=5.0,
            kg_mass=20.0,
            kg_post_consumer_recycled=10.0,
            kg_pre_consumer_recycled=5.0,
        )
        ge = GenericEstimatePreview.model_validate(
            {**GE_REQUIRED_FIELDS, "composition": [valid_constituent.model_dump()]}
        )
        self.assertEqual(len(ge.composition), 1)

        # Invalid: kg_C_biogenic > kg_C
        invalid_constituent_1 = valid_constituent.model_dump()
        invalid_constituent_1["kg_C_biogenic"] = 15.0
        invalid_constituent_1["kg_C"] = 10.0
        with self.assertRaises(pydantic.ValidationError) as e:
            GenericEstimatePreview.model_validate({**GE_REQUIRED_FIELDS, "composition": [invalid_constituent_1]})
        self.assertIn("kg_C_biogenic must be less than or equal to kg_C", str(e.exception))

        # Invalid: kg_post_consumer_recycled > kg_mass
        invalid_constituent_2 = valid_constituent.model_dump()
        invalid_constituent_2["kg_post_consumer_recycled"] = 25.0
        invalid_constituent_2["kg_mass"] = 20.0
        with self.assertRaises(pydantic.ValidationError) as e:
            GenericEstimatePreview.model_validate({**GE_REQUIRED_FIELDS, "composition": [invalid_constituent_2]})
        self.assertIn("kg_post_consumer_recycled must be less than or equal to kg_mass", str(e.exception))

        # Invalid: kg_pre_consumer_recycled > kg_mass
        invalid_constituent_3 = valid_constituent.model_dump()
        invalid_constituent_3["kg_pre_consumer_recycled"] = 25.0
        invalid_constituent_3["kg_mass"] = 20.0
        with self.assertRaises(pydantic.ValidationError) as e:
            GenericEstimatePreview.model_validate({**GE_REQUIRED_FIELDS, "composition": [invalid_constituent_3]})
        self.assertIn("kg_pre_consumer_recycled must be less than or equal to kg_mass", str(e.exception))

    def test_generic_estimate_lci_databases_and_software(self) -> None:
        # Test with valid lci_databases and software_used
        valid_database = {
            "guid": "40888d44-916d-4220-8353-dcdbc4e38d1b",
            "owner": {"name": "Ecoinvent", "web_domain": "ecoinvent.org"},
            "name": "ecoinvent",
            "version": "3.10",
            "link": "https://support.ecoinvent.org/ecoinvent-version-3.10",
        }

        valid_software = {
            "guid": "50999e55-027e-5331-9464-edddc5f49e2c",
            "owner": {"name": "GreenDelta", "web_domain": "greendelta.com"},
            "primary_function": "LCA Analysis",
            "name": "openLCA",
            "version": "2.3.1",
            "link": "https://share.greendelta.com/index.php/s/D1xa3haTiHJdhqt?path=%2F2.3.1",
        }

        ge = GenericEstimatePreview.model_validate(
            {
                **GE_REQUIRED_FIELDS,
                "lci_databases": [valid_database],
                "software_used": [valid_software],
            }
        )

        self.assertEqual(len(ge.lci_databases), 1)
        self.assertEqual(ge.lci_databases[0].name, "ecoinvent")
        self.assertEqual(ge.lci_databases[0].version, "3.10")
        self.assertEqual(ge.lci_databases[0].owner.name, "Ecoinvent")

        self.assertEqual(len(ge.software_used), 1)
        self.assertEqual(ge.software_used[0].name, "openLCA")
        self.assertEqual(ge.software_used[0].version, "2.3.1")
        self.assertEqual(ge.software_used[0].primary_function, "LCA Analysis")
        self.assertEqual(ge.software_used[0].owner.name, "GreenDelta")

        # Test with ResourceRef using guid
        ge_with_ref = GenericEstimatePreview.model_validate(
            {
                **GE_REQUIRED_FIELDS,
                "lci_databases": [{"guid": "40888d44-916d-4220-8353-dcdbc4e38d1b"}],
                "software_used": [{"guid": "50999e55-027e-5331-9464-edddc5f49e2c"}],
            }
        )

        self.assertEqual(len(ge_with_ref.lci_databases), 1)
        self.assertEqual(ge_with_ref.lci_databases[0].guid, "40888d44-916d-4220-8353-dcdbc4e38d1b")
        self.assertEqual(len(ge_with_ref.software_used), 1)
        self.assertEqual(ge_with_ref.software_used[0].guid, "50999e55-027e-5331-9464-edddc5f49e2c")

        # Test with None values (optional fields)
        ge_without = GenericEstimatePreview.model_validate({**GE_REQUIRED_FIELDS})
        self.assertIsNone(ge_without.lci_databases)
        self.assertIsNone(ge_without.software_used)

        # Test with empty lists
        ge_empty = GenericEstimatePreview.model_validate(
            {
                **GE_REQUIRED_FIELDS,
                "lci_databases": [],
                "software_used": [],
            }
        )
        self.assertEqual(len(ge_empty.lci_databases), 0)
        self.assertEqual(len(ge_empty.software_used), 0)
