#
#  Copyright 2023 by C Change Labs Inc. www.c-change-labs.com
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
from typing import Annotated, Optional

import pydantic as pyd

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import Location, WithAltIdsMixin, WithAttachmentsMixin


class Org(WithAttachmentsMixin, WithAltIdsMixin, BaseOpenEpdSchema):
    """Represent an organization."""

    web_domain: str | None = pyd.Field(
        description="A web domain owned by organization. Typically is the org's home website address", default=None
    )
    name: str | None = pyd.Field(
        max_length=200,
        description="Common name for organization",
        default=None,
        json_schema_extra=dict(example="C Change Labs"),
    )
    alt_names: Annotated[list[str], pyd.conlist(pyd.constr(max_length=200), max_length=255)] | None = pyd.Field(
        description="List of other names for organization",
        default=None,
        json_schema_extra=dict(example=["C-Change Labs", "C-Change Labs inc."]),
    )
    # TODO: NEW field, not in the spec
    owner: Optional["Org"] = pyd.Field(description="Organization that controls this organization", default=None)
    subsidiaries: Annotated[list[str], pyd.conlist(pyd.constr(max_length=200), max_length=255)] | None = pyd.Field(
        description="Organizations controlled by this organization",
        default=None,
        json_schema_extra=dict(example=["cqd.io", "supplychaincarbonpricing.org"]),
    )
    hq_location: Location | None = pyd.Field(
        default=None,
        description="Location of a place of business, prefereably the corporate headquarters.",
    )


class Plant(WithAttachmentsMixin, WithAltIdsMixin, BaseOpenEpdSchema):
    """Represent a manufacturing plant."""

    model_config = pyd.ConfigDict(populate_by_name=True)

    # TODO: Add proper validator
    id: str | None = pyd.Field(
        description="Plus code (aka Open Location Code) of plant's location and "
        "owner's web domain joined with `.`(dot).",
        alias="pluscode",
        default=None,
        json_schema_extra=dict(example="865P2W3V+3W.interface.com"),
    )
    owner: Org | None = pyd.Field(description="Organization that owns the plant", default=None)
    name: str | None = pyd.Field(
        max_length=200,
        description="Manufacturer's name for plant. Recommended < 40 chars",
        default=None,
        json_schema_extra=dict(example="Dalton, GA"),
    )
    address: str | None = pyd.Field(
        max_length=200,
        default=None,
        description="Text address, preferably geocoded",
        json_schema_extra=dict(example="1503 Orchard Hill Rd, LaGrange, GA 30240, United States"),
    )
    contact_email: pyd.EmailStr | None = pyd.Field(
        description="Email contact",
        default=None,
        json_schema_extra=dict(example="info@interface.com"),
    )

    @classmethod
    def get_asset_type(cls) -> str | None:
        """Return the asset type of this class (see BaseOpenEpdSchema.get_asset_type for details)."""
        return "org"
