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
import abc
import datetime
from typing import ClassVar, Final, Generic, TypeAlias, TypeVar

import pydantic
from pydantic import ConfigDict

from openepd.api.dto.base import BaseMetaDto, BaseOpenEpdApiModel, MetaExtensionBase
from openepd.api.dto.meta import PerformanceMetaMixin
from openepd.model.base import AnySerializable

DEFAULT_PAGE_SIZE: Final[int] = 100
MAX_PAGE_SIZE: Final[int] = 250


class AuditableDto(BaseOpenEpdApiModel, metaclass=abc.ABCMeta):
    """Base class for all DTOs that hold audit information."""

    created_by: str = pydantic.Field(
        title="Created By",
        examples=["johnsmith@cqd.io"],
        description="User's email or script name that created this list.",
    )
    updated_by: str = pydantic.Field(
        title="Updated By",
        examples=["bobbuilder@buildingtransparency.org"],
        description="User's email or script name that updated this list last time.",
    )
    created_on: datetime.datetime = pydantic.Field(
        title="Created On",
        examples=["2019-06-13T13:17:09+00:00"],
        description="A timestamp when this object has been created "
        "in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.",
    )
    updated_on: datetime.datetime = pydantic.Field(
        title="Updated On",
        examples=["2020-07-13T13:17:09+00:00"],
        description="A timestamp when this object has been updated last time "
        "in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.",
    )


Payload: TypeAlias = AnySerializable
TPayload = TypeVar("TPayload", bound=Payload)
TMetaDto = TypeVar("TMetaDto", bound=BaseMetaDto)
TMetaExtension = TypeVar("TMetaExtension", bound=MetaExtensionBase)


class MetaCollectionDto(BaseOpenEpdApiModel, Generic[TMetaExtension]):
    """
    Use this class as a container for different meta objects.

    From a specific controller, you should return a specific subclass of MetaCollectionDto and appropriate mixins. This
    would allow to retain type information to generate schema for meta section of response.

    For example, EPD Search method, which should return some metadata about performance, material filter, and paging,
    would return a concrete subclass of MetaCollectionDto like this one:

    `class EpdSearchViewMeta(MaterialFilterMetaMixin, PagingMetaMixin, WarningMetaMixin, MetaCollectionDto)`

    Mixins are used to define the resulting meta's dictionary-like structure, this would result in a json like:
    ```
    {
    "paging": {"page_size": 100, "total_count": 1, "total_pages": 1},
    "ec3_warnings": null,
    "material_filter": {...}
    }
    ```

    It is generified by the extension type of similar structure (key-dict value), which should not be a part of OpenEPD
    spec. This allows to add custom meta objects to the response, which would be ignored by OpenEPD implementors.
    """

    ext: TMetaExtension | None = None

    model_config: ClassVar[ConfigDict] = ConfigDict(
        json_schema_extra={
            "description": "Base structure of the response meta section",
        }
    )


class BaseMeta(
    PerformanceMetaMixin,
    MetaCollectionDto[TMetaExtension],
    Generic[TMetaExtension],
    metaclass=abc.ABCMeta,
):
    """Base class for creating meta objects specific to a controller."""

    pass


TMeta = TypeVar("TMeta", bound=MetaCollectionDto, covariant=True)


class OpenEpdApiResponse(BaseOpenEpdApiModel, Generic[TPayload, TMeta]):
    """Standard DTO representing response from OpenEPD API server."""

    payload: TPayload
    # there is an issue with using covariant type variables as parameters when used for container mutable types,
    # as described in https://github.com/python/mypy/issues/7049
    # However, in our workflow TMeta is not a container type which is further returned back to caller.
    meta: TMeta  # type: ignore[misc]
