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
from typing import Annotated, Optional

from openlocationcode import openlocationcode

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Location, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.validation.common import ReferenceStr


class OrgRef(BaseOpenEpdSchema):
    """Represents Organisation with minimal data."""

    web_domain: str | None = pyd.Field(
        description="A web domain owned by organization. Typically is the org's home website address", default=None
    )
    name: str | None = pyd.Field(
        max_length=200,
        description="Common name for organization",
        example="C Change Labs",
        default=None,
    )
    ref: ReferenceStr | None = pyd.Field(
        default=None,
        example="https://openepd.buildingtransparency.org/api/orgs/c-change-labs.com",
        description="Reference to this Org's JSON object",
    )


class Org(WithAttachmentsMixin, WithAltIdsMixin, OrgRef):
    """Represent an organization."""

    alt_names: Annotated[list[str], pyd.conlist(pyd.constr(max_length=200), max_items=255)] | None = pyd.Field(
        description="List of other names for organization",
        example=["C-Change Labs", "C-Change Labs inc."],
        default=None,
    )
    # TODO: NEW field, not in the spec

    owner: Optional["OrgRef"] = pyd.Field(description="Organization that controls this organization", default=None)
    subsidiaries: Annotated[list["OrgRef"], pyd.conlist(pyd.constr(max_length=200), max_items=255)] | None = pyd.Field(
        description="Organizations controlled by this organization",
        default=None,
    )
    hq_location: Location | None = pyd.Field(
        default=None,
        description="Location of a place of business, preferably the corporate headquarters.",
    )


class PlantRef(BaseOpenEpdSchema):
    """Represents Plant with minimal data."""

    id: str | None = pyd.Field(
        description="Plus code (aka Open Location Code) of plant's location and "
        "owner's web domain joined with `.`(dot).",
        example="865P2W3V+3W.interface.com",
        default=None,
    )
    name: str | None = pyd.Field(
        max_length=200,
        description="Manufacturer's name for plant. Recommended < 40 chars",
        example="Dalton, GA",
        default=None,
    )
    ref: ReferenceStr | None = pyd.Field(
        default=None,
        example="https://openepd.buildingtransparency.org/api/orgs/c-change-labs.com",
        description="Reference to this Plant's JSON object",
    )


class Plant(PlantRef, WithAttachmentsMixin, WithAltIdsMixin):
    """Represent a manufacturing plant."""

    pluscode: str | None = pyd.Field(
        default=None,
        description="(deprecated) Plus code (aka Open Location Code) of plant's location",
        deprecated="Pluscode field is deprecated. If users need a pluscode they can obtain it from "
        "`id` like this: `id.spit('.', maxsplit=1)[0]`",
    )
    latitude: float | None = pyd.Field(
        default=None, description="(deprecated) Latitude of the plant location. Use 'location' fields instead."
    )
    longitude: float | None = pyd.Field(
        default=None, description="(deprecated) Longitude of the plant location. Use 'location' fields instead."
    )
    owner: Org | None = pyd.Field(description="Organization that owns the plant", default=None)
    address: str | None = pyd.Field(
        max_length=200,
        default=None,
        description="(deprecated) Text address, preferably geocoded. Use 'location' fields instead",
        example="1503 Orchard Hill Rd, LaGrange, GA 30240, United States",
    )
    contact_email: pyd.EmailStr | None = pyd.Field(
        description="Email contact", example="info@interface.com", default=None
    )
    location: Location | None = pyd.Field(description="Location of the plant", default=None)

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "org"

    @pyd.validator("id")
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

    class Config(BaseOpenEpdSchema.Config):
        allow_population_by_field_name = True
