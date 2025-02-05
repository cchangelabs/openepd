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
import importlib
import inspect
import pkgutil
from types import ModuleType
from typing import Iterable
import unittest

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class SpecVersionTestCase(unittest.TestCase):
    def test_ext_version_defined_for_all_specs(self):

        modules = list(self.__find_iteratively("..specs", relative_to=__package__))
        for name, module in modules:
            material_specs_in_module = [
                cls
                for _, cls in inspect.getmembers(module, inspect.isclass)
                if issubclass(cls, BaseOpenEpdHierarchicalSpec)
                and cls.__module__ == module.__name__
                and cls != BaseOpenEpdHierarchicalSpec
            ]
            for spec in material_specs_in_module:
                self.assertIsNotNone(spec._EXT_VERSION, f"_EXT_VERSION is not defined for {spec.__name__}")

    @classmethod
    def __find_iteratively(cls, module_name: str, relative_to: str) -> Iterable[tuple[str, ModuleType]]:
        spec = importlib.util.find_spec(module_name, relative_to)
        if spec:
            module = importlib.import_module(spec.name)
            for module_info in pkgutil.walk_packages(module.__path__):
                if module_info.ispkg:
                    yield from cls.__find_iteratively(".".join((module.__name__, module_info.name)), relative_to)
                else:
                    yield module_info.name, importlib.import_module(".".join((module.__name__, module_info.name)))
