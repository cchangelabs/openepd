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
import math
from typing import Annotated, Final, Optional

from openlocationcode import openlocationcode

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import DataUrl, Location, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.validation.common import ReferenceStr

ORG_LOGO_MAX_LENGTH: Final[int] = math.ceil(32 * 1024 * 4 / 3)
"""
Maximum length of Org.logo field.

Logo file size must be less than 32KB. Base64 encoding overhead (approximately 33%) requires 
limiting the encoded string length to 4/3 of the file size limit.
"""


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
    description: str | None = pyd.Field(
        default=None,
        max_length=2000,
        description=(
            "Text that describes the company, its products, or its sustainability commitments, "
            'similar to "about us" or "sustainability commitment" text on a corporate website.  '
            "Typically used for publication in EPDs and for viewing by users.  "
            "Supports plain text or github flavored markdown."
        ),
        example=(
            "# Our Mission\n"
            "Driven by the mission to design and make the world's best products in the most sustainable way, "
            "MillerKnoll's sustainability strategy focuses on three key areas:\n"
            "* Carbon : Design the lowest carbon footprint products "
            "and commit to achieving net-zero carbon emissions by 20501.\n"
            "* Materials : Use sustainable, 100% bio-based or recycled materials by 2050.\n"
            "* Circularity : Design timeless, durable products with zero waste by 2050.\n"
            "# Supplier Support\n"
            "At MillerKnoll, we are committed to working closely with our suppliers "
            "to reduce our collective impact on the environment. "
            "We encourage our suppliers to minimize their operations' environmental impacts "
            "and require they assist us in decreasing our facilities' environmental effects."
        ),
    )
    hq_location: Location | None = pyd.Field(
        default=None,
        description="Location of a place of business, preferably the corporate headquarters.",
    )
    logo: pyd.AnyUrl | DataUrl | None = pyd.Field(
        default=None,
        description=(
            "URL pointer to, or dataURL, for a square logo for the company, preferably 300x300 pixels."
            "A logo of the type used on social media platforms such as LinkedIn is recommended."
        ),
        example="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",
    )

    @pyd.validator("logo")
    def validate_logo(cls, v: str | None) -> str | None:
        if v and len(v) > ORG_LOGO_MAX_LENGTH:
            msg = f"Logo URL must not exceed {ORG_LOGO_MAX_LENGTH} characters"
            raise ValueError(msg)
        return v


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
            msg = "Incorrectly formed id: should be pluscode.owner_web_domain"
            raise ValueError(msg) from e

        if not openlocationcode.isValid(pluscode):
            msg = "Incorrect pluscode for plant"
            raise ValueError(msg)

        if not web_domain:
            msg = "Incorrect web_domain for plant"
            raise ValueError(msg)
        return v

    class Config(BaseOpenEpdSchema.Config):
        allow_population_by_field_name = True
