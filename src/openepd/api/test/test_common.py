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
import math
import unittest

from openepd.api.common import StreamingListResponse
from openepd.api.dto.common import MetaCollectionDto, OpenEpdApiResponse
from openepd.api.dto.meta import PagingMeta, PagingMetaMixin
from openepd.api.errors import ValidationError


class PagingMetaResponseForTest(PagingMetaMixin, MetaCollectionDto):
    pass


class StreamingListResponseTestCase(unittest.TestCase):
    DATA: list[int] = [x for x in range(100)]

    @classmethod
    def fetch_data(
        cls,
        page_num: int,
        page_size: int,
    ) -> OpenEpdApiResponse[list[int], PagingMetaResponseForTest]:
        payload = cls.DATA[(page_num - 1) * page_size : page_num * page_size]

        response = OpenEpdApiResponse(
            payload=payload,
            meta=PagingMetaResponseForTest(),  # type: ignore[call-arg]
        )
        response.meta.paging = PagingMeta(
            total_count=len(cls.DATA), total_pages=math.ceil(len(cls.DATA) / page_size), page_size=page_size
        )
        return response

    def test_streaming_list_response(self):
        page_size = 10
        sl = StreamingListResponse[int](self.fetch_data, page_size=page_size)

        self.assertEqual(len(sl), len(self.DATA))
        self.assertEqual(sl.get_total_pages(), math.ceil(len(self.DATA) / page_size))

        result = []
        for x in sl:
            result.append(x)
        self.assertEqual(result, self.DATA)

    def test_streaming_list_skip_pages(self):
        page_size = 7
        sl = StreamingListResponse[int](self.fetch_data, page_size=page_size)

        result = []
        for x in sl.iterator(start_from_page=4):
            result.append(x)
        self.assertEqual(result, self.DATA[(4 - 1) * page_size :])


class TestValidationErrorSerialization(unittest.TestCase):
    TEST_CASES: list[tuple[str, dict, str]] = [
        (
            "Advanced positive scenario",
            {
                "field1": ["blah"],
                "field2": {"subfield": ["error 2"]},
                "field3": {0: {"subfield": ["error 3"]}},
                "field4": {"subfield1": {"subfield2": ["error 2"]}},
            },
            """Validation errors:
field1:
  blah
field2.subfield:
  error 2
field3.0.subfield:
  error 3
field4.subfield1.subfield2:
  error 2
             """,
        )
    ]

    def test_validation_errors_serialization(self):
        for name, errors_dict, expected_output in self.TEST_CASES:
            with self.subTest(name):
                error = ValidationError(400, "Validation error", errors_dict, None, None)
                print(str(error))
                self.assertEqual(expected_output.strip(), str(error))
