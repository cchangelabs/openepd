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
import pydantic

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.org import OrgRef
from openepd.model.validation.common import ReferenceStr


class StandardRef(BaseOpenEpdSchema):
    """Reference version (short) of Standard."""

    ref: ReferenceStr | None = pydantic.Field(
        default=None,
        examples=["https://openepd.buildingtransparency.org/api/standards/EN15804"],
        description="Reference to this Standard's JSON object",
    )
    short_name: str | None = pydantic.Field(
        description="Short-form of name of standard.  Must be unique. Case-insensitive"
    )


class Standard(StandardRef):
    """A standard, such as EN 15804, ISO 14044, ISO 14024:2018, etc."""

    name: str | None = pydantic.Field(
        description="Full document name.  Must be unique. Case-insensitive",
        default=None,
    )
    link: pydantic.AnyUrl | None = pydantic.Field(
        description="Link to the exact standard (including version) referred to",
        default=None,
    )
    issuer: OrgRef | None = pydantic.Field(description="Org that issued this standard", default=None)
