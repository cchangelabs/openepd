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
from openepd.api.utils import encode_path_param
from openepd.model.pcr import Pcr, PcrRef


class PcrApi(BaseApiMethodGroup):
    """API methods for EPDs."""

    def get_by_openxpd_uuid(self, uuid: str) -> Pcr:
        """
        Get PCR by Open xPD UUID.

        :param uuid: Open xPD UUID
        :return: PCR
        :raise ObjectNotFound: if PCR not found
        :raise ValidationError: if openxpd_uuid is invalid
        """
        content = self._client.do_request("get", f"/pcrs/{uuid}").json()
        return Pcr.parse_obj(content)

    def create(self, pcr: Pcr) -> PcrRef:
        """
        Create a new PCR.

        :param pcr: PCR to create
        :return: reference to the created PCR
        :raise ValidationError: if given object PCR is invalid
        """
        pcr_ref_obj = self._client.do_request("post", "/pcrs", json=pcr.to_serializable()).json()
        return PcrRef.parse_obj(pcr_ref_obj)

    @overload
    def edit(self, to_edit: Pcr, with_response: Literal[True]) -> tuple[PcrRef, Response]: ...

    @overload
    def edit(self, to_edit: Pcr, with_response: Literal[False] = False) -> PcrRef: ...

    def edit(self, to_edit: Pcr, with_response: bool = False) -> PcrRef | tuple[PcrRef, Response]:
        """
        Edit a pcr.

        :param to_edit: Pcr to edit
        :param with_response: if True, return a tuple of (PcrRef, Response), otherwise return only PcrRef
        :return: Pcr reference or Pcr reference with HTTP Response object depending on parameter
        :raise ValueError: if the pcr ID is not set
        """
        entity_id = to_edit.id
        if not entity_id:
            msg = "The pcr ID must be set to edit a pcr."
            raise ValueError(msg)
        response = self._client.do_request(
            "put",
            f"/pcrs/{encode_path_param(entity_id)}",
            json=to_edit.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        content = response.json()
        ref = PcrRef.parse_obj(content)
        if with_response:
            return ref, response
        return ref
