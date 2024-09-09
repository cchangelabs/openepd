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

from openepd.compat.pydantic import pyd
from openepd.model.specs import ConcreteV1
from openepd.model.specs.generated.enums import AciExposureClass, CsaExposureClass, EnExposureClass


class SpecValidationTestCase(unittest.TestCase):

    def test_exclusive_list_validation(self) -> None:
        ok_cases = (
            {"aci_exposure_classes": []},
            {"aci_exposure_classes": None},
            {"aci_exposure_classes": [AciExposureClass.F0]},
            {"aci_exposure_classes": [AciExposureClass.F0, AciExposureClass.W0, AciExposureClass.C2]},
            {"csa_exposure_classes": [CsaExposureClass.C_XL, CsaExposureClass.C_1, CsaExposureClass.N]},
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
            {"csa_exposure_classes": [CsaExposureClass.C_XL, CsaExposureClass.C_1, CsaExposureClass.C_2]},
            {"csa_exposure_classes": [CsaExposureClass.S_1, CsaExposureClass.S_2]},
            {"en_exposure_classes": [EnExposureClass.en206_XC1, EnExposureClass.en206_XC2]},
            {"en_exposure_classes": [EnExposureClass.en206_XD1, EnExposureClass.en206_XD2]},
        )
        for case in not_ok_cases:
            with self.assertRaises(pyd.ValidationError):
                ConcreteV1(**case)
