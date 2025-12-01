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
from typing import Any, Final
import unittest

from openepd.model.common import DATA_URL_IMAGE_MAX_LENGTH, Amount

GE_REQUIRED_FIELDS: Final[dict[str, Any]] = {
    "id": "0197ad82-92cf-7978-a6c8-d4964c0a3624",
    "kg_per_declared_unit": Amount(qty=12.5, unit="kg").to_serializable(exclude_unset=True),
}
"""
Required fields for Generic Estimates to be used in tests.
"""


class ImageFieldTestCase(unittest.TestCase):
    def _test_data_url_image_field(self, dto_class, dto_field) -> None:
        dto_class.model_validate({dto_field: None})
        dto_class.model_validate({dto_field: "data:image/png;base64,NSUhiVRw0KGgoAAAABO"})
        dto_class.model_validate({dto_field: "data:image/png,NSUhiVRw0KGgoAAAABO"})
        dto_class.model_validate({dto_field: "data:;base64,NSUhiVRw0KGgoAAAABO"})
        dto_class.model_validate({dto_field: "data:,NSUhiVRw0KGgoAAAABO"})
        dto_class.model_validate({dto_field: "https://example.com"})

        with self.assertRaises(ValueError):
            dto_class.model_validate({dto_field: "example"})
        with self.assertRaises(ValueError):
            dto_class.model_validate({dto_field: "example.com"})
        with self.assertRaises(ValueError):
            # image data should be <= 32KB
            dto_class.model_validate({dto_field: "data:image/png;base64," + "a" * DATA_URL_IMAGE_MAX_LENGTH})
        with self.assertRaises(ValueError):
            # invalid dataUrl
            dto_class.model_validate({dto_field: "data:base64,NSUhiVRw0KGgoAAAABO"})
        with self.assertRaises(ValueError):
            # invalid dataUrl
            dto_class.model_validate({dto_field: "data:NSUhiVRw0KGgoAAAABO"})
