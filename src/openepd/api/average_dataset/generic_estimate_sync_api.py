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
from openepd.api.utils import encode_path_param, remove_none_id_fields
from openepd.model.generic_estimate import (
    GenericEstimate,
    GenericEstimatePreview,
    GenericEstimateRef,
    GenericEstimateWithDeps,
)


class GenericEstimateApi(BaseApiMethodGroup):
    """API methods for Generic Estimates."""

    @overload
    def get_by_openxpd_uuid(self, uuid: str, with_response: Literal[True]) -> tuple[GenericEstimate, Response]: ...

    @overload
    def get_by_openxpd_uuid(self, uuid: str, with_response: Literal[False] = False) -> GenericEstimate: ...

    def get_by_openxpd_uuid(
        self, uuid: str, with_response: bool = False
    ) -> GenericEstimate | tuple[GenericEstimate, Response]:
        """
        Get Generic Estimate by OpenEPD UUID.

        :param uuid: Open xPD UUID
        :param with_response: whether to return just object or with response
        :return: GE or GE with response depending on param with_response
        :raise ObjectNotFound: if Generic Estimate is not found
        """
        response = self._client.do_request("get", f"/generic_estimates/{uuid}")
        if with_response:
            return GenericEstimate.parse_obj(response.json()), response
        return GenericEstimate.parse_obj(response.json())

    @overload
    def post_with_refs(
        self, ge: GenericEstimateWithDeps, with_response: Literal[True]
    ) -> tuple[GenericEstimate, Response]: ...

    @overload
    def post_with_refs(
        self,
        ge: GenericEstimateWithDeps,
        with_response: Literal[False] = False,
    ) -> GenericEstimate: ...

    def post_with_refs(
        self, ge: GenericEstimateWithDeps, with_response: bool = False
    ) -> GenericEstimate | tuple[GenericEstimate, Response]:
        """
        Post an GenericEstimate with references.

        :param ge: GenericEstimate
        :param with_response: return the response object togather with the GenericEstimate
        :param exclude_defaults: If True, fields with default values are excluded from the payload
        :return: GenericEstimate alone, or GenericEstimate with HTTP Response object depending on parameter
        """
        data = ge.to_serializable(exclude_unset=True, by_alias=True)
        # Remove 'id' fields with None values, as 'id' cannot be None
        data = remove_none_id_fields(data)
        response = self._client.do_request(
            "patch",
            "/generic_estimates/post_with_refs",
            json=data,
        )
        content = response.json()
        if with_response:
            return GenericEstimate.parse_obj(content), response
        return GenericEstimate.parse_obj(content)

    @overload
    def create(self, ge: GenericEstimate, with_response: Literal[True]) -> tuple[GenericEstimateRef, Response]: ...

    @overload
    def create(self, ge: GenericEstimate, with_response: Literal[False] = False) -> GenericEstimateRef: ...

    def create(
        self, ge: GenericEstimate, with_response: bool = False
    ) -> GenericEstimateRef | tuple[GenericEstimateRef, Response]:
        """
        Create a Generic Estimate.

        :param ge: Generic Estimate
        :param with_response: return the response object together with the EPD
        :return: Generic Estimate or Generic Estimate with HTTP Response object depending on parameter
        """
        response = self._client.do_request(
            "post",
            "/generic_estimates",
            json=ge.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        if with_response:
            return GenericEstimateRef.parse_obj(content), response
        return GenericEstimateRef.parse_obj(content)

    @overload
    def edit(self, ge: GenericEstimate, with_response: Literal[True]) -> tuple[GenericEstimateRef, Response]: ...

    @overload
    def edit(self, ge: GenericEstimate, with_response: Literal[False] = False) -> GenericEstimateRef: ...

    def edit(
        self, ge: GenericEstimate, with_response: bool = False
    ) -> GenericEstimateRef | tuple[GenericEstimateRef, Response]:
        """
        Edit a Generic Estimate.

        :param ge: GenericEstimate
        :param with_response: return the response object together with the GE
        :return: GE or GE with HTTP Response object depending on parameter
        """
        ge_id = ge.id
        if not ge_id:
            msg = "The ID must be set to edit a GenericEstimate."
            raise ValueError(msg)

        response = self._client.do_request(
            "put",
            f"/generic_estimates/{encode_path_param(ge_id)}",
            json=ge.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        if with_response:
            return GenericEstimateRef.parse_obj(content), response
        return GenericEstimateRef.parse_obj(content)

    @overload
    def list_raw(
        self, page_num: int, page_size: int, with_response: Literal[False] = False
    ) -> list[GenericEstimatePreview]: ...

    @overload
    def list_raw(
        self, page_num: int, page_size: int, with_response: Literal[True]
    ) -> tuple[list[GenericEstimatePreview], Response]: ...

    def list_raw(
        self, page_num: int = 1, page_size: int = 10, with_response: bool = False
    ) -> list[GenericEstimatePreview] | tuple[list[GenericEstimatePreview], Response]:
        """
        List generic estimates.

        :param page_num: page number
        :param page_size: page size
        :param with_response: whether to return just object or with response

        :return: GE or GE with HTTP Response object depending on parameter
        """
        response = self._client.do_request(
            "get",
            "/generic_estimates",
            params=dict(
                page_number=page_num,
                page_size=page_size,
            ),
        )
        data = [GenericEstimatePreview.parse_obj(o) for o in response.json()]
        if with_response:
            return data, response
        return data

    def list(self, page_size: int | None = None) -> StreamingListResponse[GenericEstimatePreview]:
        """
        List GenericEstimates.

        :param page_size: page size, None for default
        :return: streaming list of GEs
        """

        def _get_page(p_num: int, p_size: int) -> GenericEstimateListResponse:
            data_list, response = self.list_raw(page_num=p_num, page_size=p_size, with_response=True)
            return GenericEstimateListResponse(
                payload=data_list, meta=GenericEstimateSearchMeta(paging=paging_meta_from_v1_api(response))
            )

        return StreamingListResponse[GenericEstimatePreview](_get_page, page_size=page_size)


class GenericEstimateSearchMeta(PagingMetaMixin, BaseMeta):
    """Metadata for EPD Search endpoint."""

    pass


GenericEstimateListResponse: TypeAlias = OpenEpdApiResponse[list[GenericEstimatePreview], GenericEstimateSearchMeta]
