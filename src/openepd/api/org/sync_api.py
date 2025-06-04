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
from openepd.model.org import Org, OrgRef


class OrgApi(BaseApiMethodGroup):
    """API methods for Orgs."""

    @overload
    def create(self, to_create: Org, with_response: Literal[True]) -> tuple[OrgRef, Response]: ...

    @overload
    def create(self, to_create: Org, with_response: Literal[False] = False) -> OrgRef: ...

    def create(self, to_create: Org, with_response: bool = False) -> OrgRef | tuple[OrgRef, Response]:
        """
        Create a new organization.

        :param to_create: Organization to create
        :param with_response: if True, return a tuple of (OrgRef, Response), otherwise return only OrgRef
        :return: Organization reference or Organization reference with HTTP Response object depending on parameter
        :raise ValidationError: if given object Org is invalid
        """
        response = self._client.do_request("post", "/orgs", json=to_create.to_serializable())
        content = response.json()
        ref = OrgRef.parse_obj(content)
        if with_response:
            return ref, response
        return ref

    @overload
    def edit(self, to_edit: Org, with_response: Literal[True]) -> tuple[OrgRef, Response]: ...

    @overload
    def edit(self, to_edit: Org, with_response: Literal[False] = False) -> OrgRef: ...

    def edit(self, to_edit: Org, with_response: bool = False) -> OrgRef | tuple[OrgRef, Response]:
        """
        Edit an organization.

        :param to_edit: Organization to edit
        :param with_response: if True, return a tuple of (OrgRef, Response), otherwise return only Org
        :return: Organization reference or Organization reference with HTTP Response object depending on parameter
        :raise ValueError: if the organization web_domain is not set
        """
        entity_id = to_edit.web_domain
        if not entity_id:
            msg = "The organization web_domain must be set to edit an organization."
            raise ValueError(msg)
        response = self._client.do_request(
            "put",
            f"/orgs/{encode_path_param(entity_id)}",
            json=to_edit.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        response.raise_for_status()
        content = response.json()
        ref = OrgRef.parse_obj(content)
        if with_response:
            return ref, response
        return ref
