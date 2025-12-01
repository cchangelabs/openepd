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

from openepd.model.base import OPENEPD_VERSION_FIELD, OpenEpdDoctypes
from openepd.model.factory import DocumentFactory
from openepd.model.tests.common import GE_REQUIRED_FIELDS
from openepd.model.versioning import OpenEpdVersions


class DocumentFactoryTestCase(unittest.TestCase):
    def test_document_factory_supports_all_doc_types(self):
        for doctype in OpenEpdDoctypes:
            # For some reason, StrEnum is not counted as `str` for literal values.
            # Explicitly convert to str.
            data = {OPENEPD_VERSION_FIELD: OpenEpdVersions.get_current().as_str(), "doctype": str(doctype)}
            if doctype == OpenEpdDoctypes.GenericEstimate:
                data.update(**GE_REQUIRED_FIELDS)
            DocumentFactory.from_dict(data)
