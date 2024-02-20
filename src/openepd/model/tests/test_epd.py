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
import unittest

from openepd.model.base import Version
from openepd.model.epd import OPENEPD_V0_VERSION, OPENEPD_VERSION, Epd, parse_epd


class EPDTestCase(unittest.TestCase):
    def test_epd_openepd_version(self):
        self.assertEqual(Epd().openepd_version, OPENEPD_VERSION.as_str())
        self.assertEqual(Epd.parse_obj({"openepd_version": "1.2"}).openepd_version, "1.2")
        self.assertEqual(Epd(openepd_version="1.2").to_serializable()["openepd_version"], "1.2")
        self.assertEqual(Epd().to_serializable()["openepd_version"], str(OPENEPD_VERSION))

    def test_epd_factory(self):
        # current v0 version
        self.assertEqual(
            parse_epd({"openepd_version": OPENEPD_VERSION.as_str()}).openepd_version, OPENEPD_VERSION.as_str()
        )
        # current latest version
        self.assertEqual(
            parse_epd({"openepd_version": OPENEPD_V0_VERSION.as_str()}).openepd_version, OPENEPD_V0_VERSION.as_str()
        )
        # one minor version back - OK
        minor_smaller_version = Version(major=OPENEPD_VERSION.major, minor=OPENEPD_VERSION.minor - 1)
        self.assertEqual(
            parse_epd({"openepd_version": minor_smaller_version.as_str()}).openepd_version,
            minor_smaller_version.as_str(),
        )

        # one major version higher - not ok
        major_higher_version = Version(major=OPENEPD_VERSION.major + 1, minor=OPENEPD_VERSION.minor)
        with self.assertRaises(ValueError):
            parse_epd({"openepd_version": major_higher_version.as_str()})

        # one minor version higher - not ok too
        minor_higher_version = Version(major=OPENEPD_VERSION.major, minor=OPENEPD_VERSION.minor + 1)
        with self.assertRaises(ValueError):
            parse_epd({"openepd_version": minor_higher_version.as_str()})
