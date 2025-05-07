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
from openepd.model.base import OPENEPD_VERSION_FIELD, OpenEpdDoctypes, OpenEpdExtension, Version
from openepd.model.common import Ingredient
from openepd.model.epd import Epd, EpdFactory, EpdPreviewV0, EpdV0
from openepd.model.validation.quantity import AmountMass
from openepd.model.versioning import OpenEpdVersions

OPENEPD_VERSION = OpenEpdVersions.get_current()
OPENEPD_V0_VERSION = OpenEpdVersions.get_most_recent_version(0)


class MyExtension(OpenEpdExtension):
    @classmethod
    def get_extension_name(cls) -> str:
        return "my_ext"

    test_field: AmountMass = pyd.Field()


class EPDTestCase(unittest.TestCase):
    def test_epd_openepd_version(self):
        self.assertEqual(Epd().openepd_version, OPENEPD_VERSION.as_str())
        self.assertEqual(Epd.parse_obj({OPENEPD_VERSION_FIELD: "0.2"}).openepd_version, "0.2")
        self.assertEqual(Epd(openepd_version="0.2").to_serializable()[OPENEPD_VERSION_FIELD], "0.2")
        self.assertEqual(Epd().to_serializable()[OPENEPD_VERSION_FIELD], str(OPENEPD_VERSION))
        # test validation
        with self.assertRaises(ValueError):
            EpdV0.parse_obj({OPENEPD_VERSION_FIELD: "asdb"})
        with self.assertRaises(ValueError):
            EpdV0.parse_obj({OPENEPD_VERSION_FIELD: "1.2"})

    def test_epd_factory(self):
        standard_fields = {"doctype": OpenEpdDoctypes.Epd}
        # current v0 version
        self.assertEqual(
            EpdFactory.from_dict({OPENEPD_VERSION_FIELD: OPENEPD_VERSION.as_str(), **standard_fields}).openepd_version,
            OPENEPD_VERSION.as_str(),
        )
        # current latest version
        self.assertEqual(
            EpdFactory.from_dict(
                {OPENEPD_VERSION_FIELD: OPENEPD_V0_VERSION.as_str(), **standard_fields}
            ).openepd_version,
            OPENEPD_V0_VERSION.as_str(),
        )
        # one minor version back - OK
        minor_smaller_version = Version(major=OPENEPD_VERSION.major, minor=OPENEPD_VERSION.minor - 1)
        self.assertEqual(
            EpdFactory.from_dict(
                {OPENEPD_VERSION_FIELD: minor_smaller_version.as_str(), **standard_fields}
            ).openepd_version,
            minor_smaller_version.as_str(),
        )

        # one major version higher - not ok
        major_higher_version = Version(major=OPENEPD_VERSION.major + 1, minor=OPENEPD_VERSION.minor)
        with self.assertRaises(ValueError):
            EpdFactory.from_dict({OPENEPD_VERSION_FIELD: major_higher_version.as_str(), **standard_fields})

        # one minor version higher - not ok too
        minor_higher_version = Version(major=OPENEPD_VERSION.major, minor=OPENEPD_VERSION.minor + 1)
        with self.assertRaises(ValueError):
            EpdFactory.from_dict({OPENEPD_VERSION_FIELD: minor_higher_version.as_str(), **standard_fields})

    def test_factory_supports_all_versions(self):
        for version in OpenEpdVersions.get_supported_versions():
            EpdFactory.from_dict({OPENEPD_VERSION_FIELD: version.as_str(), "doctype": OpenEpdDoctypes.Epd})

    def test_legacy_openepd_doctype(self):
        for o in [{}, {"id": "EC300001"}, {"doctype": "openEPD"}, {"doctype": "OpenEPD"}]:
            self.assertEqual(EpdPreviewV0.parse_obj(o).doctype, "openEPD")

        for o in [{"doctype": "abc"}, {"doctype": "openIndustryEpd"}, {"doctype": "openGenericEstimate"}]:
            with self.assertRaises(pyd.ValidationError):
                self.assertEqual(EpdPreviewV0.parse_obj(o).doctype, "openEPD")

    def test_id_valiation_works(self):
        for the_id in [None, "EC300001", "ec300001"]:
            self.assertEqual(the_id, Epd.parse_obj({"id": the_id}).id)

        for the_id in ["", "abc", 15, "Ec3000001"]:
            with self.assertRaises(pyd.ValidationError):
                Epd.parse_obj({"id": the_id})

    def test_ingredient_indirect(self) -> None:
        epd = EpdV0.parse_obj(
            {
                "includes": [
                    {"qty": 2.1, "link": "http://google.com/evidence"},
                    {"gwp_fraction": 0.2, "evidence_type": "Product EPD", "citation": "Own data"},
                ]
            }
        )
        self.assertEqual(epd.includes[0].qty, 2.1)
        self.assertIsInstance(epd.includes[0], Ingredient)
        self.assertIsInstance(epd.includes[1], Ingredient)
        self.assertEqual(epd.includes[1].gwp_fraction, 0.2)

    def test_parse_extension(self) -> None:
        """Test that parsing of extensions works."""
        epd = Epd.parse_obj(
            {
                "ext": {
                    "my_ext": {
                        "test_field": {"amount": 2, "unit": "kg"},
                    }
                }
            }
        )
        ext = epd.get_ext(MyExtension)
        self.assertIsInstance(ext, MyExtension)
        self.assertIsInstance(ext.test_field, AmountMass)
