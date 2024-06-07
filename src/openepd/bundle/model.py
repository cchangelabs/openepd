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
from enum import StrEnum

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema


class BundleManifestAssetsStats(BaseOpenEpdSchema):
    """The statistics of assets in a bundle."""

    total_count: int = 0
    """The total number of assets."""

    total_size: int = 0
    """The total size of assets in bytes."""

    count_by_type: dict[str, int] = pyd.Field(default_factory=dict)
    """The number of assets by type."""


class AssetType(StrEnum):
    """The type of asset."""

    Epd = "epd"
    Pcr = "pcr"
    Org = "org"
    Blob = "blob"


class RelType(StrEnum):
    """The type of relationship between assets."""

    Translation = "translation"
    """A translation of the asset."""
    Pdf = "repr.pdf"
    """A PDF representation of the asset."""
    Ilcd = "repr.ilcd"
    """An ILCD representation of the asset."""


class BundleManifest(BaseOpenEpdSchema):
    """The manifest of a bundle."""

    format: str = "openEPD Bundle/1.0"
    """The format of the bundle."""
    generator: str
    """The generator of the bundle."""
    assets: BundleManifestAssetsStats = pyd.Field(default_factory=BundleManifestAssetsStats)
    comment: str | None = pyd.Field(default=None)


class AssetInfo(BaseOpenEpdSchema):
    """A table of contents item."""

    ref: str
    """The ID of the asset."""
    name: str | None = None
    """The name of the asset."""
    type: AssetType
    """The type of the asset."""
    lang: str | None
    """The language of the asset."""
    rel_type: str | None
    rel_asset: str | None
    comment: str | None = pyd.Field(default=None)
    content_type: str | None = pyd.Field(default=None)
    size: int | None = pyd.Field(default=None)
    custom_type: str | None = pyd.Field(default=None)
    custom_data: str | None = pyd.Field(default=None)
