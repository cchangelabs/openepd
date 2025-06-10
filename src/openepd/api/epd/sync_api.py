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
from typing import Literal, overload

from requests import Response

from openepd.api.base_sync_client import BaseApiMethodGroup
from openepd.api.common import StreamingListResponse
from openepd.api.epd.dto import EpdSearchResponse, EpdStatisticsResponse, StatisticsDto
from openepd.api.utils import encode_path_param, remove_none_id_fields
from openepd.model.epd import Epd


class EpdApi(BaseApiMethodGroup):
    """API methods for EPDs."""

    def get_by_openxpd_uuid(self, uuid: str) -> Epd:
        """
        Get EPD by OpenEPD UUID.

        :param uuid: OpenEPD UUID
        :return: EPD
        :raise ObjectNotFound: if EPD is not found
        """
        content = self._client.do_request("get", f"/epds/{uuid}").json()
        return Epd.model_validate(content)

    def find_raw(self, omf: str, page_num: int = 1, page_size: int = 10) -> EpdSearchResponse:
        """
        Find EPDs by Open Material Filter(OMF).

        OMF is a query language for searching materials/EPDs, running statistics and so on.
        It can exist in a string form, which is accepted by most of the endpoints.

        :param omf: OMF - open material filter string (see OMF spec).
        :param page_num: page number
        :param page_size: page size
        :return: the list of EPDs
        """
        content = self._client.do_request(
            "get",
            "/v2/epds/search",
            params=dict(
                omf=omf,
                page_number=page_num,
                page_size=page_size,
            ),
        ).json()
        return EpdSearchResponse.model_validate(content)

    def find(self, omf: str, page_size: int | None = None) -> StreamingListResponse[Epd]:
        """
        Find EPDs by Open Material Filter(OMF).

        OMF is a query language for searching materials/EPDs, running statistics and so on.
        It can exist in a string form, which is accepted by most of the endpoints.

        :param omf: OMF - open material filter string (see OMF spec).
        :param page_size: page size, None for default
        :return: streaming list of EPDs
        """

        def _get_page(p_num: int, p_size: int) -> EpdSearchResponse:
            return self.find_raw(omf, page_num=p_num, page_size=p_size)

        return StreamingListResponse[Epd](_get_page, page_size=page_size)

    def get_statistics_raw(self, omf: str) -> EpdStatisticsResponse:
        """
        Get statistics for a given search query.

        Statistics contains aggregated parameters such as percentiles distributions of GWP and other parameters.
        Please note - in addition to product EPDs statistics might include industry-wide EPDs and even generic
        estimates to provide a more complete picture where there is not enough product EPDs.

        :param omf: OMF - open material filter string (see OMF spec).
        :return: statistics wrapped in OpenEpdApiResponse
        """
        content = self._client.do_request("get", "/v2/epds/statistics", params=dict(omf=omf)).json()
        return EpdStatisticsResponse.model_validate(content)

    def get_statistics(self, omf: str) -> StatisticsDto:
        """
        Get statistics for a given search query.

        Statistics contains aggregated parameters such as percentiles distributions of GWP and other parameters.
        Please note - in addition to product EPDs statistics might include industry-wide EPDs and even generic
        estimates to provide a more complete picture where there is not enough product EPDs.

        :param omf: OMF - open material filter string (see OMF spec).
        :return: statistics wrapped in OpenEpdApiResponse
        """
        return self.get_statistics_raw(omf).payload

    @overload
    def post_with_refs(self, epd: Epd, with_response: Literal[True]) -> tuple[Epd, Response]: ...

    @overload
    def post_with_refs(self, epd: Epd, with_response: Literal[False] = False) -> Epd: ...

    def post_with_refs(self, epd: Epd, with_response: bool = False) -> Epd | tuple[Epd, Response]:
        """
        Post an EPD with references.

        :param epd: EPD
        :param with_response: return the response object togather with the EPD
        :param exclude_defaults: If True, fields with default values are excluded from the payload
        :return: EPD or EPD with HTTP Response object depending on parameter
        """
        epd_data = epd.to_serializable(exclude_unset=True, by_alias=True)
        # Remove 'id' fields with None values, as 'id' cannot be None
        epd_data = remove_none_id_fields(epd_data)
        response = self._client.do_request(
            "patch",
            "/epds/post-with-refs",
            json=epd_data,
        )
        content = response.json()
        if with_response:
            return Epd.model_validate(content), response
        return Epd.model_validate(content)

    @overload
    def create(self, epd: Epd, with_response: Literal[True]) -> tuple[Epd, Response]: ...

    @overload
    def create(self, epd: Epd, with_response: Literal[False] = False) -> Epd: ...

    def create(self, epd: Epd, with_response: bool = False) -> Epd | tuple[Epd, Response]:
        """
        Create an EPD.

        :param epd: EPD
        :param with_response: return the response object together with the EPD
        :return: EPD or EPD with HTTP Response object depending on parameter
        """
        response = self._client.do_request(
            "post",
            "/epds",
            json=epd.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        if with_response:
            return Epd.model_validate(content), response
        return Epd.model_validate(content)

    @overload
    def edit(self, epd: Epd, with_response: Literal[True]) -> tuple[Epd, Response]: ...

    @overload
    def edit(self, epd: Epd, with_response: Literal[False] = False) -> Epd: ...

    def edit(self, epd: Epd, with_response: bool = False) -> Epd | tuple[Epd, Response]:
        """
        Edit an EPD.

        :param epd: EPD
        :param with_response: return the response object together with the EPD
        :return: EPD or EPD with HTTP Response object depending on parameter
        """
        epd_id = epd.id
        if not epd_id:
            msg = "The EPD ID must be set to edit an EPD."
            raise ValueError(msg)
        response = self._client.do_request(
            "put",
            f"/epds/{encode_path_param(epd_id)}",
            json=epd.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        if with_response:
            return Epd.model_validate(content), response
        return Epd.model_validate(content)
