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

import pydantic
from pydantic import ConfigDict


class BaseOpenEpdApiModel(pydantic.BaseModel):
    """Base class for OpenEPD API DTOs."""

    model_config = ConfigDict(extra="ignore")


class BaseMetaDto(BaseOpenEpdApiModel, metaclass=abc.ABCMeta):
    """Base class for all meta DTOs."""

    pass


class MetaExtensionBase(BaseOpenEpdApiModel):
    """Base class for custom meta extensions."""

    pass
