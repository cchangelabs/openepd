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
from openepd.model.org import Plant, PlantRef


class PlantApi(BaseApiMethodGroup):
    """API methods for Plants."""

    @overload
    def create(self, to_create: Plant, with_response: Literal[True]) -> tuple[PlantRef, Response]: ...

    @overload
    def create(self, to_create: Plant, with_response: Literal[False] = False) -> PlantRef: ...

    def create(self, to_create: Plant, with_response: bool = False) -> PlantRef | tuple[PlantRef, Response]:
        """
        Create a new plant.

        :param to_create: Plant to create
        :param with_response: if True, return a tuple of (PlantRef, Response), otherwise return only PlantRef
        :return: Plant reference or Plant reference with HTTP Response object depending on parameter
        :raise ValidationError: if given object Plant is invalid
        """
        response = self._client.do_request("post", "/plants", json=to_create.to_serializable())
        content = response.json()
        ref = PlantRef.model_validate(content)
        if with_response:
            return ref, response
        return ref

    @overload
    def edit(self, to_edit: Plant, with_response: Literal[True]) -> tuple[PlantRef, Response]: ...

    @overload
    def edit(self, to_edit: Plant, with_response: Literal[False] = False) -> PlantRef: ...

    def edit(self, to_edit: Plant, with_response: bool = False) -> PlantRef | tuple[PlantRef, Response]:
        """
        Edit a plant.

        :param to_edit: Plant to edit
        :param with_response: if True, return a tuple of (PlantRef, Response), otherwise return only PlantRef
        :return: Plant reference or Plant reference with HTTP Response object depending on parameter
        :raise ValueError: if the plant ID is not set
        """
        entity_id = to_edit.id
        if not entity_id:
            msg = "The plant ID must be set to edit a plant."
            raise ValueError(msg)
        response = self._client.do_request(
            "put",
            f"/plants/{encode_path_param(entity_id)}",
            json=to_edit.to_serializable(exclude_unset=True, exclude_defaults=True, by_alias=True),
        )
        response.raise_for_status()
        content = response.json()
        ref = PlantRef.model_validate(content)
        if with_response:
            return ref, response
        return ref
