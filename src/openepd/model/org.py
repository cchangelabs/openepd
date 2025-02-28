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
from typing import Annotated, List, Optional

from openlocationcode import openlocationcode
import pydantic
from pydantic import ConfigDict, Field, StringConstraints

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Location, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.validation.common import ReferenceStr


class OrgRef(BaseOpenEpdSchema):
    """Represents Organisation with minimal data."""

    web_domain: str | None = pydantic.Field(
        description="A web domain owned by organization. Typically is the org's home website address",
        default=None,
    )
    name: str | None = pydantic.Field(
        max_length=200,
        description="Common name for organization",
        examples=["C Change Labs"],
        default=None,
    )
    ref: ReferenceStr | None = pydantic.Field(
        default=None,
        examples=["https://openepd.buildingtransparency.org/api/orgs/c-change-labs.com"],
        description="Reference to this Org's JSON object",
    )


class Org(WithAttachmentsMixin, WithAltIdsMixin, OrgRef):
    """Represent an organization."""

    alt_names: (
        Annotated[
            list[str],
            Annotated[
                List[Annotated[str, StringConstraints(max_length=200)]],
                Field(max_length=255),
            ],
        ]
        | None
    ) = pydantic.Field(
        description="List of other names for organization",
        examples=[["C-Change Labs", "C-Change Labs inc."]],
        default=None,
    )
    # TODO: NEW field, not in the spec

    owner: Optional["OrgRef"] = pydantic.Field(description="Organization that controls this organization", default=None)
    subsidiaries: (
        Annotated[
            list["OrgRef"],
            Annotated[
                List[Annotated[str, StringConstraints(max_length=200)]],
                Field(max_length=255),
            ],
        ]
        | None
    ) = pydantic.Field(
        description="Organizations controlled by this organization",
        default=None,
    )
    hq_location: Location | None = pydantic.Field(
        default=None,
        description="Location of a place of business, preferably the corporate headquarters.",
    )


class PlantRef(BaseOpenEpdSchema):
    """Represents Plant with minimal data."""

    id: str | None = pydantic.Field(
        description="Plus code (aka Open Location Code) of plant's location and "
        "owner's web domain joined with `.`(dot).",
        examples=["865P2W3V+3W.interface.com"],
        default=None,
    )
    name: str | None = pydantic.Field(
        max_length=200,
        description="Manufacturer's name for plant. Recommended < 40 chars",
        examples=["Dalton, GA"],
        default=None,
    )
    ref: ReferenceStr | None = pydantic.Field(
        default=None,
        examples=["https://openepd.buildingtransparency.org/api/orgs/c-change-labs.com"],
        description="Reference to this Plant's JSON object",
    )


class Plant(PlantRef, WithAttachmentsMixin, WithAltIdsMixin):
    """Represent a manufacturing plant."""

    pluscode: str | None = pydantic.Field(
        default=None,
        description="(deprecated) Plus code (aka Open Location Code) of plant's location",
        deprecated="Pluscode field is deprecated. If users need a pluscode they can obtain it from "
        "`id` like this: `id.spit('.', maxsplit=1)[0]`",
    )
    latitude: float | None = pydantic.Field(
        default=None,
        description="(deprecated) Latitude of the plant location. Use 'location' fields instead.",
    )
    longitude: float | None = pydantic.Field(
        default=None,
        description="(deprecated) Longitude of the plant location. Use 'location' fields instead.",
    )
    owner: Org | None = pydantic.Field(description="Organization that owns the plant", default=None)
    address: str | None = pydantic.Field(
        max_length=200,
        default=None,
        description="(deprecated) Text address, preferably geocoded. Use 'location' fields instead",
        examples=["1503 Orchard Hill Rd, LaGrange, GA 30240, United States"],
    )
    contact_email: pydantic.EmailStr | None = pydantic.Field(
        description="Email contact", examples=["info@interface.com"], default=None
    )
    location: Location | None = pydantic.Field(description="Location of the plant", default=None)

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "org"

    @pydantic.field_validator("id")
    def _validate_id(cls, v: str) -> str:
        if not v:
            return v
        try:
            pluscode, web_domain = v.split(".", maxsplit=1)
        except ValueError as e:
            raise ValueError("Incorrectly formed id: should be pluscode.owner_web_domain") from e

        if not openlocationcode.isValid(pluscode):
            raise ValueError("Incorrect pluscode for plant")

        if not web_domain:
            raise ValueError("Incorrect web_domain for plant")
        return v

    model_config = ConfigDict(populate_by_name=True)
