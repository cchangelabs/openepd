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
import pydantic as pyd

from openepd.api.dto.base import BaseOpenEpdApiModel


class PcrRef(BaseOpenEpdApiModel):
    """Reference to a PCR."""

    id: str | None = pyd.Field(
        description="The unique ID for this PCR.  To ensure global uniqueness, should be registered "
        "at open-xpd-uuid.cqd.io/register or a coordinating registry.",
        example="ec3xpgq2",
        default=None,
    )
    name: str | None = pyd.Field(
        max_length=200,
        description="Full document name as listed in source document",
        example="c-PCR-003 Concrete and concrete elements (EN 16757)",
    )
    ref: pyd.AnyUrl | None = pyd.Field(
        description="Reference to this PCR's JSON object",
        example="https://openepd.buildingtransparency.org/api/pcrs/1u7zsed8",
    )
