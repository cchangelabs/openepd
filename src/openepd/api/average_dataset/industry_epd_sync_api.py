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
from typing import Literal, TypeAlias, overload

from requests import Response

from openepd.api.base_sync_client import BaseApiMethodGroup
from openepd.api.common import StreamingListResponse, paging_meta_from_v1_api
from openepd.api.dto.common import BaseMeta, OpenEpdApiResponse
from openepd.api.dto.meta import PagingMetaMixin
from openepd.api.utils import encode_path_param
from openepd.model.industry_epd import IndustryEpd, IndustryEpdPreview, IndustryEpdRef


class IndustryEpdApi(BaseApiMethodGroup):
    """API methods for Industry EPD."""

    @overload
    def get_by_openxpd_uuid(self, uuid: str, with_response: Literal[True]) -> tuple[IndustryEpd, Response]: ...

    @overload
    def get_by_openxpd_uuid(self, uuid: str, with_response: Literal[False] = False) -> IndustryEpd: ...

    def get_by_openxpd_uuid(self, uuid: str, with_response: bool = False) -> IndustryEpd | tuple[IndustryEpd, Response]:
        """
        Get Industry EPD by OpenEPD UUID.

        :param uuid: OpenEPD UUID
        :param with_response: whether to return just object or with response
        :return: IEPD or IEPD with response depending on param with_response
        :raise ObjectNotFound: if Industry EPD is not found
        """
        response = self._client.do_request("get", f"/industry_epds/{uuid}")
        if with_response:
            return IndustryEpd.model_validate(response.json()), response
        return IndustryEpd.model_validate(response.json())

    @overload
    def create(self, iepd: IndustryEpd, with_response: Literal[True]) -> tuple[IndustryEpdRef, Response]: ...

    @overload
    def create(self, iepd: IndustryEpd, with_response: Literal[False] = False) -> IndustryEpdRef: ...

    def create(
        self, iepd: IndustryEpd, with_response: bool = False
    ) -> IndustryEpdRef | tuple[IndustryEpdRef, Response]:
        """
        Create an Industry EPD.

        :param iepd: Industry EPD
        :param with_response: return the response object together with the EPD
        :return: Industry EPD or Industry EPD with HTTP Response object depending on parameter
        """
        response = self._client.do_request(
            "post",
            "/industry_epds",
            json=iepd.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        if with_response:
            return IndustryEpdRef.model_validate(content), response
        return IndustryEpdRef.model_validate(content)

    @overload
    def edit(self, iepd: IndustryEpd, with_response: Literal[True]) -> tuple[IndustryEpdRef, Response]: ...

    @overload
    def edit(self, iepd: IndustryEpd, with_response: Literal[False] = False) -> IndustryEpdRef: ...

    def edit(self, iepd: IndustryEpd, with_response: bool = False) -> IndustryEpdRef | tuple[IndustryEpdRef, Response]:
        """
        Edit an Industr EPD.

        :param iepd: IndustryEpd
        :param with_response: return the response object together with the IEPD
        :return: IEPD or IEPD with HTTP Response object depending on parameter
        """
        iepd_id = iepd.id
        if not iepd_id:
            msg = "The ID must be set to edit a IndustryEpd."
            raise ValueError(msg)

        response = self._client.do_request(
            "put",
            f"/industry_epds/{encode_path_param(iepd_id)}",
            json=iepd.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        if with_response:
            return IndustryEpdRef.model_validate(content), response
        return IndustryEpdRef.model_validate(content)

    @overload
    def list_raw(
        self, page_num: int, page_size: int, with_response: Literal[False] = False
    ) -> list[IndustryEpdPreview]: ...

    @overload
    def list_raw(
        self, page_num: int, page_size: int, with_response: Literal[True]
    ) -> tuple[list[IndustryEpdPreview], Response]: ...

    def list_raw(
        self, page_num: int = 1, page_size: int = 10, with_response: bool = False
    ) -> list[IndustryEpdPreview] | tuple[list[IndustryEpdPreview], Response]:
        """
        List industry epds.

        :param page_num: page number
        :param page_size: page size
        :param with_response: whether to return just object or with response
        :return: list of IEPDs or list of IEPDs with response depending on param with_response
        """
        response = self._client.do_request(
            "get",
            "/industry_epds",
            params=dict(
                page_number=page_num,
                page_size=page_size,
            ),
        )
        data = [IndustryEpdPreview.model_validate(o) for o in response.json()]
        if with_response:
            return data, response
        return data

    def list(self, page_size: int | None = None) -> StreamingListResponse[IndustryEpdPreview]:
        """
        List IndustryEpds.

        :param page_size: page size, None for default
        :return: streaming list of IEPDs
        """

        def _get_page(p_num: int, p_size: int) -> IndustryEpdListResponse:
            data_list, response = self.list_raw(page_num=p_num, page_size=p_size, with_response=True)
            return IndustryEpdListResponse(
                payload=data_list,
                meta=IndustryEpdSearchMeta(paging=paging_meta_from_v1_api(response)),
            )

        return StreamingListResponse[IndustryEpdPreview](_get_page, page_size=page_size)


class IndustryEpdSearchMeta(PagingMetaMixin, BaseMeta):
    """Metadata for EPD Search endpoint."""

    pass


IndustryEpdListResponse: TypeAlias = OpenEpdApiResponse[list[IndustryEpdPreview], IndustryEpdSearchMeta]
