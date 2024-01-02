#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from openepd.api.base_sync_client import BaseApiMethodGroup
from openepd.api.pcr.dto import PcrRef
from openepd.model.pcr import Pcr


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
