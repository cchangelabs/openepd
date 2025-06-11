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
from openepd.model.standard import Standard, StandardRef


class StandardApi(BaseApiMethodGroup):
    """API methods for Standards."""

    @overload
    def create(self, to_create: Standard, with_response: Literal[True]) -> tuple[StandardRef, Response]: ...

    @overload
    def create(self, to_create: Standard, with_response: Literal[False] = False) -> StandardRef: ...

    def create(self, to_create: Standard, with_response: bool = False) -> StandardRef | tuple[StandardRef, Response]:
        """
        Create a new standard.

        :param to_create: Standard to create
        :param with_response: if True, return a tuple of (StandardRef, Response), otherwise return only StandardRef
        :return: Standard reference or Standard reference with HTTP Response object depending on parameter
        :raise ValidationError: if given object Standard is invalid
        """
        response = self._client.do_request("post", "/standards", json=to_create.to_serializable())
        content = response.json()
        ref = StandardRef.model_validate(content)
        if with_response:
            return ref, response
        return ref

    @overload
    def edit(self, to_edit: Standard, with_response: Literal[True]) -> tuple[StandardRef, Response]: ...

    @overload
    def edit(self, to_edit: Standard, with_response: Literal[False] = False) -> StandardRef: ...

    def edit(self, to_edit: Standard, with_response: bool = False) -> StandardRef | tuple[StandardRef, Response]:
        """
        Edit a standard.

        :param to_edit: Standard to edit
        :param with_response: if True, return a tuple of (StandardRef, Response), otherwise return only StandardRef
        :return: Standard reference or Standard reference with HTTP Response object depending on parameter
        :raise ValueError: if the standard short_name is not set
        """
        entity_id = to_edit.short_name
        if not entity_id:
            msg = "The standard short_name must be set to edit a standard."
            raise ValueError(msg)
        response = self._client.do_request(
            "put",
            f"/standards/{encode_path_param(entity_id)}",
            json=to_edit.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        response.raise_for_status()
        content = response.json()
        ref = StandardRef.model_validate(content)
        if with_response:
            return ref, response
        return ref
