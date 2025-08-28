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
import re
from typing import Any, Final, Optional

from openlocationcode import openlocationcode
import pydantic
from pydantic import ConfigDict

from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import DATA_URL_REGEX, Location, WithAltIdsMixin, WithAttachmentsMixin
from openepd.model.validation.common import ReferenceStr

ORG_LOGO_MAX_LENGTH: Final[int] = math.ceil(32 * 1024 * 4 / 3)
"""
Maximum length of Org.logo field.

Logo file size must be less than 32KB. Base64 encoding overhead (approximately 33%) requires 
limiting the encoded string length to 4/3 of the file size limit.
"""


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

    alt_names: list[str] | None = pydantic.Field(
        description="List of other names for organization",
        examples=[["C-Change Labs", "C-Change Labs inc."]],
        default=None,
        max_length=255,
    )
    # TODO: NEW field, not in the spec

    @pydantic.field_validator("alt_names", mode="before")
    def _validate_alt_names(cls, value: Any) -> list[str] | None:
        if value is None:
            return value

        if not isinstance(value, list):
            msg = f"Expected type list or None, got {type(value)}"
            raise TypeError(msg)

        if any((len(item) > 200) for item in value):
            msg = "One or more alt_names are longer than 200 characters"
            raise ValueError(msg)

        return value

    owner: Optional["OrgRef"] = pydantic.Field(description="Organization that controls this organization", default=None)
    subsidiaries: list["OrgRef"] | None = pydantic.Field(
        description="Organizations controlled by this organization", default=None, max_length=255
    )

    @pydantic.field_validator("subsidiaries", mode="before")
    def _validate_subsidiaries(cls, value: Any) -> list[str] | None:
        if value is None:
            return value

        if not isinstance(value, list):
            msg = f"Expected type list or None, got {type(value)}"
            raise TypeError(msg)

        for item in value:
            if len(item.name) > 200:
                msg = "One or more subsidiaries name are longer than 200 characters"
                raise ValueError(msg)

        return value

    description: str | None = pydantic.Field(
        default=None,
        max_length=2000,
        description=(
            "Text that describes the company, its products, or its sustainability commitments, "
            'similar to "about us" or "sustainability commitment" text on a corporate website.  '
            "Typically used for publication in EPDs and for viewing by users.  "
            "Supports plain text or github flavored markdown."
        ),
        examples=[
            (
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
            )
        ],
    )
    hq_location: Location | None = pydantic.Field(
        default=None,
        description="Location of a place of business, preferably the corporate headquarters.",
    )
    logo: pydantic.AnyUrl | None = pydantic.Field(
        default=None,
        description=(
            "URL pointer to, or dataURL, for a square logo for the company, preferably 300x300 pixels."
            "A logo of the type used on social media platforms such as LinkedIn is recommended."
        ),
        examples=["data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA", "https://example.com/logo.png"],
    )

    @pydantic.field_validator("logo")
    def _validate_logo(cls, v: pydantic.AnyUrl | None) -> pydantic.AnyUrl | None:
        if v and len(v) > ORG_LOGO_MAX_LENGTH:
            msg = f"Logo URL must not exceed {ORG_LOGO_MAX_LENGTH} characters"
            raise ValueError(msg)
        if v and v.scheme == "data" and not re.compile(DATA_URL_REGEX).match(str(v)):
            msg = "Invalid data URL format"
            raise ValueError(msg)
        return v


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
        description="(DEPRECATED) Plus code (aka Open Location Code) of plant's location. "
        "This field is deprecated. If users need a pluscode they can obtain it from `id`.",
        json_schema_extra={
            "deprecated": True,
        },
    )
    latitude: float | None = pydantic.Field(
        default=None,
        description="(DEPRECATED) Latitude of the plant location. Use 'location' fields instead.",
        json_schema_extra={
            "deprecated": True,
        },
    )
    longitude: float | None = pydantic.Field(
        default=None,
        description="(DEPRECATED) Longitude of the plant location. Use 'location' fields instead.",
        json_schema_extra={
            "deprecated": True,
        },
    )
    owner: Org | None = pydantic.Field(description="Organization that owns the plant", default=None)
    address: str | None = pydantic.Field(
        max_length=200,
        default=None,
        description="(DEPRECATED) Text address, preferably geocoded. Use 'location' fields instead",
        examples=["1503 Orchard Hill Rd, LaGrange, GA 30240, United States"],
        json_schema_extra={
            "deprecated": True,
        },
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
            msg = "Incorrectly formed id: should be pluscode.owner_web_domain"
            raise ValueError(msg) from e

        if not openlocationcode.isValid(pluscode):
            msg = "Incorrect pluscode for plant"
            raise ValueError(msg)

        if not web_domain:
            msg = "Incorrect web_domain for plant"
            raise ValueError(msg)
        return v

    model_config = ConfigDict(populate_by_name=True)
