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


class Plant(WithAttachmentsMixin, WithAltIdsMixin, BaseOpenEpdSchema):
    """Represent a manufacturing plant."""

    # TODO: Add proper validator
    id: str | None = pyd.Field(
        description="Plus code (aka Open Location Code) of plant's location and "
        "owner's web domain joined with `.`(dot).",
        example="865P2W3V+3W.interface.com",
        alias="pluscode",
        default=None,
    )
    owner: Org | None = pyd.Field(description="Organization that owns the plant", default=None)
    name: str | None = pyd.Field(
        max_length=200,
        description="Manufacturer's name for plant. Recommended < 40 chars",
        example="Dalton, GA",
        default=None,
    )
    address: str | None = pyd.Field(
        max_length=200,
        default=None,
        description="Text address, preferably geocoded",
        example="1503 Orchard Hill Rd, LaGrange, GA 30240, United States",
    )
    contact_email: pyd.EmailStr | None = pyd.Field(
        description="Email contact", example="info@interface.com", default=None
    )

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "org"

    class Config(BaseOpenEpdSchema.Config):
        allow_population_by_field_name = True
