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
from abc import ABC
import types
from typing import ClassVar
import unittest

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.epd import Epd
from openepd.model.examples import epd as epd_examples
from openepd.model.examples import generic_estimate as generic_estimate_examples
from openepd.model.examples import industry_epd as industry_epd_examples
from openepd.model.examples import org as org_examples
from openepd.model.examples import pcr as pcr_examples
from openepd.model.examples import plant as plant_examples
from openepd.model.generic_estimate import GenericEstimate
from openepd.model.industry_epd import IndustryEpd
from openepd.model.org import Org, Plant
from openepd.model.pcr import Pcr


class ExampleValidationTestBase(unittest.TestCase, ABC):
    """
    Base test case that validates example dictionaries for a given model type.

    Subclasses should set the following class attributes:

    - EXAMPLES_MODULE: module that contains example dict constants
    - EXAMPLE_PREFIX: prefix string used to identify example constants in the
      module (only attributes starting with this prefix will be validated)
    - MODEL_TYPE: the Pydantic model class used to validate the example dicts

    :cvar EXAMPLES_MODULE: Module containing example dictionaries.
    :cvar EXAMPLE_PREFIX: Prefix that identifies example variables in module.
    :cvar MODEL_TYPE: Pydantic model class used to validate examples.
    """

    __test__ = False

    EXAMPLES_MODULE: ClassVar[types.ModuleType]
    EXAMPLE_PREFIX: ClassVar[str]
    MODEL_TYPE: ClassVar[type[BaseOpenEpdSchema]]

    def test_example_dicts_validate(self) -> None:
        """Validate example dictionaries and ensure basic round-trip stability."""

        for attribute_name, attribute_value in vars(self.EXAMPLES_MODULE).items():
            if not attribute_name.startswith(self.EXAMPLE_PREFIX):
                # Skip unrelated module attributes
                continue
            with self.subTest(example=attribute_name):
                self.maxDiff = None
                # Validate without raising pydantic.ValidationError
                instance = self.MODEL_TYPE.model_validate(attribute_value)
                self.assertIsInstance(instance, self.MODEL_TYPE)
                # Ensure a basic serialize -> deserialize round-trip is stable
                self.assertEqual(instance.to_serializable(), attribute_value)


class OrgExampleValidationTest(ExampleValidationTestBase):
    """Validate all example organization dictionaries against the ``Org`` model."""

    __test__ = True
    EXAMPLES_MODULE = org_examples
    EXAMPLE_PREFIX = "EXAMPLE_ORG_"
    MODEL_TYPE = Org


class PcrExampleValidationTest(ExampleValidationTestBase):
    """Validate all example PCR dictionaries against the ``Pcr`` model."""

    __test__ = True
    EXAMPLES_MODULE = pcr_examples
    EXAMPLE_PREFIX = "EXAMPLE_PCR_"
    MODEL_TYPE = Pcr


class EpdExampleValidationTest(ExampleValidationTestBase):
    """Validate all example EPD dictionaries against the ``Epd`` model."""

    __test__ = True
    EXAMPLES_MODULE = epd_examples
    EXAMPLE_PREFIX = "EXAMPLE_EPD_"
    MODEL_TYPE = Epd


class GenericEstimateExampleValidationTest(ExampleValidationTestBase):
    """Validate all generic estimate examples against the ``GenericEstimate`` model."""

    __test__ = True
    EXAMPLES_MODULE = generic_estimate_examples
    EXAMPLE_PREFIX = "EXAMPLE_GENERIC_ESTIMATE_"
    MODEL_TYPE = GenericEstimate


class IndustryEpdExampleValidationTest(ExampleValidationTestBase):
    """Validate all industry EPD examples against the ``IndustryEpd`` model."""

    __test__ = True
    EXAMPLES_MODULE = industry_epd_examples
    EXAMPLE_PREFIX = "EXAMPLE_INDUSTRY_EPD_"
    MODEL_TYPE = IndustryEpd


class PlantExampleValidationTest(ExampleValidationTestBase):
    """Validate all plant example dictionaries against the ``Plant`` model."""

    __test__ = True
    EXAMPLES_MODULE = plant_examples
    EXAMPLE_PREFIX = "EXAMPLE_PLANT_"
    MODEL_TYPE = Plant
