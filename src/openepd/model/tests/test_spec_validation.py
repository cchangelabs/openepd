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
from unittest.mock import Mock, patch

import pydantic

from openepd.model.epd import Epd
from openepd.model.specs import ConcreteV1
from openepd.model.specs.enums import AciExposureClass, CsaExposureClass, EnExposureClass
from openepd.model.specs.singular.masonry import AutoclavedAeratedConcreteV1


class SpecValidationTestCase(unittest.TestCase):
    def test_exclusive_list_validation(self) -> None:
        ok_cases = (
            {"aci_exposure_classes": []},
            {"aci_exposure_classes": None},
            {"aci_exposure_classes": [AciExposureClass.F0]},
            {
                "aci_exposure_classes": [
                    AciExposureClass.F0,
                    AciExposureClass.W0,
                    AciExposureClass.C2,
                ]
            },
            {
                "csa_exposure_classes": [
                    CsaExposureClass.C_XL,
                    CsaExposureClass.C_1,
                    CsaExposureClass.N,
                ]
            },
            {"csa_exposure_classes": []},
            {"csa_exposure_classes": None},
            {"csa_exposure_classes": [CsaExposureClass.N]},
            {
                "en_exposure_classes": [
                    EnExposureClass.en206_X0,
                    EnExposureClass.en206_XC1,
                    EnExposureClass.en206_XD1,
                    EnExposureClass.en206_XS1,
                    EnExposureClass.en206_XF1,
                    EnExposureClass.en206_XA1,
                ]
            },
            {"en_exposure_classes": []},
            {"en_exposure_classes": None},
            {"en_exposure_classes": [EnExposureClass.en206_XA1]},
        )
        for case in ok_cases:
            ConcreteV1(**case)

        not_ok_cases = (
            {"aci_exposure_classes": [AciExposureClass.F0, AciExposureClass.F1]},
            {"aci_exposure_classes": [AciExposureClass.S0, AciExposureClass.S1]},
            {
                "csa_exposure_classes": [
                    CsaExposureClass.C_XL,
                    CsaExposureClass.C_1,
                    CsaExposureClass.C_2,
                ]
            },
            {"csa_exposure_classes": [CsaExposureClass.S_1, CsaExposureClass.S_2]},
            {
                "en_exposure_classes": [
                    EnExposureClass.en206_XC1,
                    EnExposureClass.en206_XC2,
                ]
            },
            {
                "en_exposure_classes": [
                    EnExposureClass.en206_XD1,
                    EnExposureClass.en206_XD2,
                ]
            },
        )
        for case in not_ok_cases:
            with self.assertRaises(pydantic.ValidationError):
                ConcreteV1(**case)

    def test_spec_backward_compatibility(self) -> None:
        old_spec_concrete = {
            "concrete": {
                "strength_28d": "2000 psi",
                "slump": "2 in",
                "strength_other": "3000 psi",
                "strength_other_d": 14,
                "w_c_ratio": 0.2,
                "aci_exposure_classes": ["aci.F1", "aci.S0"],
                "csa_exposure_classes": ["csa.C-1", "csa.N"],
                "en_exposure_classes": ["en206.X0", "en206.XF4"],
                "application": {
                    "fnd": True,
                    "sog": True,
                    "hrz": True,
                    "vrt_wall": True,
                    "vrt_column": True,
                    "vrt_other": True,
                    "sht": True,
                    "cdf": True,
                    "sac": True,
                    "pav": True,
                    "oil": True,
                    "grt": True,
                    "ota": True,
                },
                "options": {
                    "lightweight": True,
                    "scc": True,
                    "finishable": True,
                    "air": True,
                    "co2_entrain": True,
                    "white_cement": True,
                    "plc": True,
                    "fiber_reinforced": True,
                },
            }
        }
        expected_new_specs_concrete = Epd.model_validate(
            {
                "specs": {
                    **old_spec_concrete,
                    "Concrete": {
                        "strength_28d": "2000 psi",
                        "min_slump": "2 in",
                        "strength_other": "3000 psi",
                        "strength_other_d": 14,
                        "w_c_ratio": 0.2,
                        "aci_exposure_classes": ["aci.F1", "aci.S0"],
                        "csa_exposure_classes": ["csa.C-1", "csa.N"],
                        "en_exposure_classes": ["en206.X0", "en206.XF4"],
                        "application": {
                            "fnd": True,
                            "sog": True,
                            "hrz": True,
                            "vrt_wall": True,
                            "vrt_column": True,
                            "vrt_other": True,
                            "sht": True,
                            "cdf": True,
                            "sac": True,
                            "pav": True,
                            "oil": True,
                            "grt": True,
                            "ota": True,
                        },
                        "lightweight": True,
                        "self_consolidating": True,
                        "finishable": True,
                        "air_entrain": True,
                        "co2_entrain": True,
                        "white_cement": True,
                        "plc": True,
                        "fiber_reinforced": True,
                    },
                }
            }
        )

        old_spec_steel = {
            "steel": {
                "form_factor": "Sheet",
                "steel_composition": "Carbon",
                "Fy": "400 MPa",
                "making_route": {"bof": True},
                "ASTM": [{"short_name": "A36"}, {"short_name": "A572"}],
                "SAE": [{"short_name": "1020"}, {"short_name": "1045"}],
                "EN": [{"short_name": "S235JR"}, {"short_name": "S275JR"}],
                "options": {
                    "cold_finished": True,
                    "galvanized": True,
                    "epoxy": True,
                    "steel_fabricated": True,
                },
            }
        }
        expected_new_specs_steel = Epd.model_validate(
            {
                "specs": {
                    **old_spec_steel,
                    "Steel": {
                        "yield_tensile_str": "400 MPa",
                        "composition": "Carbon",
                        "cold_finished": True,
                        "galvanized": True,
                        "making_route": {"bof": True},
                        "astm_standards": [
                            {"short_name": "A36"},
                            {"short_name": "A572"},
                        ],
                        "sae_standards": [
                            {"short_name": "1020"},
                            {"short_name": "1045"},
                        ],
                        "en_standards": [
                            {"short_name": "S235JR"},
                            {"short_name": "S275JR"},
                        ],
                        "RebarSteel": {
                            "epoxy_coated": True,
                            "fabricated": True,
                        },
                    },
                }
            }
        )

        cases = (
            ("concrete", old_spec_concrete, expected_new_specs_concrete),
            ("steel", old_spec_steel, expected_new_specs_steel),
        )
        self.maxDiff = None
        for name, old, epd_expected in cases:
            with self.subTest(name=name):
                epd_actual = Epd.model_validate({"specs": old})

                specs_actual = epd_actual.specs.model_dump_json(
                    exclude_unset=True, exclude_none=True, exclude_defaults=True
                )
                specs_expected = epd_expected.specs.model_dump_json(
                    exclude_unset=True, exclude_none=True, exclude_defaults=True
                )

                self.assertEqual(specs_actual, specs_expected)

    def test_spec_backward_compatibility_prefers_new(self) -> None:
        specs = {
            "concrete": {"strength_28d": "2000 psi", "slump": "2 in", "w_c_ratio": 0.2},
            "Concrete": {
                "strength_28d": "3000 psi",  # value explicitly given - new prevails
                "min_slump": None,  # none, but explicitly given - new prevails
                # but w_c_ratio not given, so taking one from 'concrete' backup spec
            },
        }
        expected_specs = Epd.model_validate(
            {
                "specs": {
                    "Concrete": {
                        "strength_28d": "3000 psi",
                        "min_slump": None,
                        "w_c_ratio": 0.2,
                    }
                }
            }
        ).specs.Concrete.model_dump_json(exclude_unset=True, exclude_none=True, exclude_defaults=True)

        epd = Epd.model_validate({"specs": specs})
        actual_specs = epd.specs.Concrete.model_dump_json(exclude_unset=True, exclude_none=True, exclude_defaults=True)

        self.assertEqual(actual_specs, expected_specs)

    @patch("openepd.model.validation.quantity.ExternalValidationConfig.QUANTITY_VALIDATOR")
    def test_aac_thermal_conductivity_validation(self, validator_mock: Mock) -> None:
        """
        Test validation of the thermal_conductivity field in AutoclavedAeratedConcreteV1.

        Valid values should be accepted, and invalid values should raise ValidationError.
        """
        validate_unit_correctness_mock = Mock()
        validate_quantity_greater_or_equal_mock = Mock()
        validator_mock.validate_unit_correctness = validate_unit_correctness_mock
        validator_mock.validate_quantity_greater_or_equal = validate_quantity_greater_or_equal_mock
        AutoclavedAeratedConcreteV1(thermal_conductivity="1 W / (m * K)")
        validate_unit_correctness_mock.assert_called_once()
        validate_quantity_greater_or_equal_mock.assert_called_once()
