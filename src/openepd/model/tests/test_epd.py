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
import pydantic

from openepd.model.base import OPENEPD_VERSION_FIELD, OpenEpdDoctypes, OpenEpdExtension, Version
from openepd.model.common import Ingredient, Measurement
from openepd.model.epd import Epd, EpdFactory, EpdPreviewV0, EpdV0
from openepd.model.lcia import Impacts, ImpactSet, ScopeSet, ScopeSetGwp
from openepd.model.specs import ConcreteV1, SteelV1
from openepd.model.specs.enums import SteelComposition
from openepd.model.specs.singular.concrete import ReadyMixV1
from openepd.model.tests.common import ImageFieldTestCase
from openepd.model.validation.quantity import AmountMass
from openepd.model.versioning import OpenEpdVersions

OPENEPD_VERSION = OpenEpdVersions.get_current()
OPENEPD_V0_VERSION = OpenEpdVersions.get_most_recent_version(0)


class MyExtension(OpenEpdExtension):
    @classmethod
    def get_extension_name(cls) -> str:
        return "my_ext"

    test_field: AmountMass = pydantic.Field()


class MyEpd(Epd):
    enum_field: SteelComposition = SteelComposition.CARBON


class EPDTestCase(ImageFieldTestCase):
    def test_strenum_serialization_deserialization(self) -> None:
        """
        Test that StrEnum fields are correctly serialized and deserialized in SteelV1 and Epd models.

        Ensures that:
        - Parsing from string values yields the correct enum members.
        - Serialization produces string values, not enum members.
        - The dict representation retains enum members.
        """
        # Test SteelV1 parsing and serialization
        steel_obj = SteelV1.model_validate({"composition": "Carbon"})
        self.assertIs(steel_obj.composition, SteelComposition.CARBON)
        self.assertNotIsInstance(steel_obj.to_serializable()["composition"], SteelComposition)
        self.assertIs(steel_obj.model_dump()["composition"], SteelComposition.CARBON)

        steel_obj = SteelV1(composition=SteelComposition.CARBON)
        self.assertIs(steel_obj.composition, SteelComposition.CARBON)
        self.assertNotIsInstance(steel_obj.to_serializable()["composition"], SteelComposition)
        self.assertIs(steel_obj.model_dump()["composition"], SteelComposition.CARBON)

        # Test Epd parsing and serialization
        epd_obj = MyEpd.model_validate({"enum_field": "Carbon", "specs": {"Steel": {"composition": "Carbon"}}})
        self.assertIs(epd_obj.enum_field, SteelComposition.CARBON)
        self.assertIs(epd_obj.specs.Steel.composition, SteelComposition.CARBON)

        serializable = epd_obj.to_serializable()
        self.assertNotIsInstance(serializable["enum_field"], SteelComposition)
        self.assertNotIsInstance(serializable["specs"]["Steel"]["composition"], SteelComposition)

        obj_dict = epd_obj.model_dump()
        self.assertIs(obj_dict["enum_field"], SteelComposition.CARBON)
        self.assertIs(obj_dict["specs"]["Steel"]["composition"], SteelComposition.CARBON)

    def test_epd_openepd_version(self):
        self.assertEqual(Epd().openepd_version, OPENEPD_VERSION.as_str())
        self.assertEqual(Epd.model_validate({OPENEPD_VERSION_FIELD: "0.2"}).openepd_version, "0.2")
        self.assertEqual(Epd(openepd_version="0.2").to_serializable()[OPENEPD_VERSION_FIELD], "0.2")
        self.assertEqual(Epd().to_serializable()[OPENEPD_VERSION_FIELD], str(OPENEPD_VERSION))
        # test validation
        with self.assertRaises(ValueError):
            EpdV0.model_validate({OPENEPD_VERSION_FIELD: "asdb"})
        with self.assertRaises(ValueError):
            EpdV0.model_validate({OPENEPD_VERSION_FIELD: "1.2"})

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
                {
                    OPENEPD_VERSION_FIELD: minor_smaller_version.as_str(),
                    **standard_fields,
                }
            ).openepd_version,
            minor_smaller_version.as_str(),
        )

        # one major version higher - not ok
        major_higher_version = Version(major=OPENEPD_VERSION.major + 1, minor=OPENEPD_VERSION.minor)
        with self.assertRaises(ValueError):
            EpdFactory.from_dict(
                {
                    OPENEPD_VERSION_FIELD: major_higher_version.as_str(),
                    **standard_fields,
                }
            )

        # one minor version higher - not ok too
        minor_higher_version = Version(major=OPENEPD_VERSION.major, minor=OPENEPD_VERSION.minor + 1)
        with self.assertRaises(ValueError):
            EpdFactory.from_dict(
                {
                    OPENEPD_VERSION_FIELD: minor_higher_version.as_str(),
                    **standard_fields,
                }
            )

    def test_factory_supports_all_versions(self):
        for version in OpenEpdVersions.get_supported_versions():
            EpdFactory.from_dict(
                {
                    OPENEPD_VERSION_FIELD: version.as_str(),
                    "doctype": OpenEpdDoctypes.Epd,
                }
            )

    def test_legacy_openepd_doctype(self):
        for o in [
            {},
            {"id": "EC300001"},
            {"doctype": "openEPD"},
            {"doctype": "OpenEPD"},
        ]:
            self.assertEqual(EpdPreviewV0.model_validate(o).doctype, "openEPD")

        for o in [
            {"doctype": "abc"},
            {"doctype": "openIndustryEpd"},
            {"doctype": "openGenericEstimate"},
        ]:
            with self.assertRaises(pydantic.ValidationError):
                self.assertEqual(EpdPreviewV0.model_validate(o).doctype, "openEPD")

    def test_id_valiation_works(self):
        for the_id in [None, "EC300001", "ec300001"]:
            self.assertEqual(the_id, Epd.model_validate({"id": the_id}).id)

        for the_id in ["", "abc", 15, "Ec3000001"]:
            with self.assertRaises(pydantic.ValidationError):
                Epd.model_validate({"id": the_id})

    def test_ingredient_indirect(self) -> None:
        epd = EpdV0.model_validate(
            {
                "includes": [
                    {"qty": 2.1, "link": "http://google.com/evidence"},
                    {
                        "gwp_fraction": 0.2,
                        "evidence_type": "Product EPD",
                        "citation": "Own data",
                    },
                ]
            }
        )
        self.assertEqual(epd.includes[0].qty, 2.1)
        self.assertIsInstance(epd.includes[0], Ingredient)
        self.assertIsInstance(epd.includes[1], Ingredient)
        self.assertEqual(epd.includes[1].gwp_fraction, 0.2)

    def test_parse_extension(self) -> None:
        """Test that parsing of extensions works."""
        epd = Epd.model_validate(
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

    def test_revalidate(self):
        epd = Epd(
            impacts=Impacts(
                {
                    "TRACI 2.1": ImpactSet(
                        gwp=ScopeSet(A1=Measurement(mean=1.0, unit="kgCO2e")),
                        # In this example we're setting generic scopeset with WRONG unit. It should allow to set it,
                        # but resulting object won't pass validation
                        # (if ExternalValidationConfig.QUANTITY_VALIDATOR is set)
                    )
                }
            ),
        )
        revalidated = epd.revalidate()
        self.assertIsInstance(
            revalidated.impacts.get_impact_set("TRACI 2.1").gwp, ScopeSetGwp
        )  # ScopeSet must be replaced

    def test_epp_ext_version(self):
        epd = Epd()
        epd.specs.Concrete = ConcreteV1(ReadyMix=ReadyMixV1())
        epd.specs = epd.specs
        self.assertEqual(epd.specs.Concrete.ReadyMix.ext_version, epd.specs.Concrete.ReadyMix._EXT_VERSION)
        serialized_epd = epd.to_serializable()
        self.assertEqual(
            serialized_epd["specs"]["Concrete"]["ReadyMix"]["ext_version"], epd.specs.Concrete.ReadyMix._EXT_VERSION
        )

    def test_product_image(self):
        self._test_data_url_image_field(Epd, "product_image")

    def test_product_image_small(self):
        self._test_data_url_image_field(Epd, "product_image_small")

    def test_product_usage_image(self):
        self._test_data_url_image_field(Epd, "product_usage_image")

    def test_manufacturing_image(self):
        self._test_data_url_image_field(Epd, "manufacturing_image")
