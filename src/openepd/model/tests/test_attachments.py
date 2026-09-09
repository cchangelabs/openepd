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
from typing import Final
import unittest

import pydantic as pyd

from openepd.model.common import WithAttachmentsMixin

SAMPLE_URL: Final[str] = "https://example.com/epd"


class WithAttachmentsMixinTestCase(unittest.TestCase):
    def test_get_attachment_returns_stored_url(self) -> None:
        url = SAMPLE_URL
        model = WithAttachmentsMixin(attachments={"EPD": url})

        attachment = model.get_attachment("EPD")

        self.assertIsNotNone(attachment)
        self.assertEqual(str(attachment), url)

    def test_get_attachment_as_string_returns_stored_url(self) -> None:
        url = SAMPLE_URL
        model = WithAttachmentsMixin(attachments={"EPD": url})

        self.assertEqual(model.get_attachment_as_string("EPD"), url)

    def test_get_attachment_as_string_converts_anyurl(self) -> None:
        url_str = SAMPLE_URL
        any_url = pyd.TypeAdapter(pyd.AnyUrl).validate_python(url_str)
        model = WithAttachmentsMixin(attachments={"EPD": any_url})

        self.assertEqual(model.get_attachment_as_string("EPD"), url_str)

    def test_attachment_accessors_return_none_when_attachment_is_missing(self) -> None:
        model = WithAttachmentsMixin(attachments={"EPD": SAMPLE_URL})

        self.assertIsNone(model.get_attachment("Datasheet"))
        self.assertIsNone(model.get_attachment_as_string("Datasheet"))

    def test_attachment_accessors_return_none_when_attachments_are_unset(self) -> None:
        model = WithAttachmentsMixin()

        self.assertIsNone(model.get_attachment("EPD"))
        self.assertIsNone(model.get_attachment_as_string("EPD"))
