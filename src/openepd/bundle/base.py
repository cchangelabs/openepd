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
from collections.abc import Callable, Iterator, Sequence
import csv
from typing import IO, Self

from openepd.bundle.model import AssetInfo, AssetType, BundleManifest, RelType
from openepd.model.base import TOpenEpdObject

AssetFilter = Callable[[AssetInfo], bool]
"""A filter function for assets. Returns True if the asset should be included."""
AssetRef = str | AssetInfo


class toc_dialect(csv.Dialect):
    """Describe the usual properties of Excel-generated CSV files."""

    delimiter = ","
    quotechar = '"'
    doublequote = True
    skipinitialspace = True
    lineterminator = "\r\n"
    quoting = csv.QUOTE_NONNUMERIC


csv.register_dialect("toc", toc_dialect)


class BundleMixin:
    """Mixin for bundle readers and writers."""

    _TOC_FIELDS: tuple[str, ...] = (
        "ref",
        "name",
        "type",
        "lang",
        "rel_type",
        "rel_asset",
        "comment",
        "content_type",
        "size",
        "custom_type",
        "custom_data",
    )

    @classmethod
    def _asset_ref_to_str(cls, asset_ref: AssetRef) -> str:
        if isinstance(asset_ref, AssetInfo):
            return asset_ref.ref
        else:
            return asset_ref

    @classmethod
    def _asset_refs_to_str(cls, asset_refs: AssetRef | list[AssetRef] | None) -> list[str] | str | None:
        """Convert single or multiple asset references to strings."""
        if asset_refs is None:
            return None
        if isinstance(asset_refs, list):
            return [cls._asset_ref_to_str(asset_ref) for asset_ref in asset_refs]
        else:
            return cls._asset_ref_to_str(asset_refs)

    @classmethod
    def _serialize_rel_asset_for_csv(cls, rel_asset: list[str] | str | None) -> str | None:
        """
        Serialize rel_asset for CSV storage.

        Multiple assets are joined with semicolons.
        """
        if rel_asset is None:
            return None
        if isinstance(rel_asset, list):
            # For empty list, return None. For non-empty list, join with semicolons
            return ";".join(rel_asset) if rel_asset else None
        else:
            # Single asset - return as string
            return str(rel_asset)

    @classmethod
    def _deserialize_rel_asset_from_csv(cls, rel_asset_str: str | None) -> list[str] | str | None:
        """
        Deserialize rel_asset from CSV storage.

        Semicolon-separated values become lists.
        """
        if rel_asset_str is None or rel_asset_str == "":
            return None
        if ";" in rel_asset_str:
            return rel_asset_str.split(";")
        else:
            return rel_asset_str


class BaseBundleReader(BundleMixin, metaclass=abc.ABCMeta):
    """Base class for bundle readers."""

    def __enter__(self) -> Self:
        return self

    def __exit__(self, type, value, traceback):  # noqa: A002
        self.close()

    @abc.abstractmethod
    def get_manifest(self) -> BundleManifest:
        """Get the manifest of the bundle. Manifest object is immutable."""
        pass

    @abc.abstractmethod
    def close(self):
        """Close the reader."""
        pass

    @abc.abstractmethod
    def get_relative_assets_iter(
        self, asset: AssetRef, rel_type: str | Sequence[str] | None = None
    ) -> Iterator[AssetInfo]:
        """
        Get all assets that are related to the given asset.

        :param asset: The asset to get related assets for.
        :param rel_type: The type of the relation. If None, all relations are returned.
        :return: An iterator over the related assets.
        """
        pass

    @abc.abstractmethod
    def assets_iter(self) -> Iterator[AssetInfo]:
        """Get an iterator over all assets in the bundle."""
        pass

    @abc.abstractmethod
    def root_assets_iter(
        self,
        filter_or_type: AssetFilter | str | AssetType | None = None,
        name: str | None = None,
        parent_ref: AssetRef | None = None,
        ref_type: str | None = None,
        is_translated: bool | None = None,
    ) -> Iterator[AssetInfo]:
        """
        Get an iterator over all root assets in the bundle. Optionally, filter the assets.

        :param filter_or_type: A filter function or an asset type to filter by.
        :param name: The name of the asset to filter by.
        :param parent_ref: The parent asset to filter by.
        :param ref_type: The type of the asset to filter by.
        :param is_translated: Whether the asset is translated.
        :return: An iterator over the root assets.
        """
        pass

    @abc.abstractmethod
    def get_asset_by_ref(self, asset_ref: AssetRef) -> AssetInfo | None:
        """Get an asset by its reference or None if not found."""
        pass

    @abc.abstractmethod
    def read_blob_asset(self, asset_ref: AssetRef) -> IO[bytes]:
        """Read a blob asset by given reference."""
        pass

    @abc.abstractmethod
    def read_object_asset(self, obj_class: type[TOpenEpdObject], asset_ref: AssetRef) -> TOpenEpdObject:
        """Read an object asset by given reference."""
        pass

    def get_relative_assets(self, asset: AssetInfo, rel_type: str | Sequence[str] | None = None) -> list[AssetInfo]:
        """Get all assets that are related to the given asset."""
        return list(self.get_relative_assets_iter(asset, rel_type))

    def get_first_relative_asset(
        self, asset: AssetInfo, rel_type: str | Sequence[str] | None = None
    ) -> AssetInfo | None:
        """
        Get the first asset that is related to the given asset or None if not found.

        :param asset: The asset to get related assets for.
        :param rel_type: The type of the relation. If None, all relations are returned.
        """
        for x in self.get_relative_assets_iter(asset, rel_type):
            return x
        return None

    def get_translations_for_asset(self, asset: AssetRef) -> list[AssetInfo]:
        """Get all translations for the given asset."""
        return list(self.get_relative_assets_iter(asset, rel_type=RelType.Translation))

    def get_first_root_asset(self, asset_type: AssetType) -> AssetInfo | None:
        """Get the first root asset of the given type or None if not found."""
        for x in self.root_assets_iter(asset_type):
            return x
        return None


class BaseBundleWriter(BundleMixin, metaclass=abc.ABCMeta):
    """Base class for bundle writers."""

    def __enter__(self) -> Self:
        return self

    def __exit__(self, type, value, traceback):  # noqa: A002
        self.close()

    @abc.abstractmethod
    def write_blob_asset(
        self,
        data: IO[bytes],
        content_type: str | None,
        rel_asset: AssetRef | list[AssetRef] | None = None,
        rel_type: str | None = None,
        file_name: str | None = None,
        name: str | None = None,
        lang: str | None = None,
        comment: str | None = None,
        custom_type: str | None = None,
        custom_data: str | None = None,
    ) -> AssetInfo:
        """Write a blob asset."""
        pass

    @abc.abstractmethod
    def write_object_asset(
        self,
        obj: TOpenEpdObject,
        rel_asset: AssetRef | list[AssetRef] | None = None,
        rel_type: str | None = None,
        file_name: str | None = None,
        name: str | None = None,
        lang: str | None = None,
        comment: str | None = None,
        custom_type: str | None = None,
        custom_data: str | None = None,
    ) -> AssetInfo:
        """Write an object asset."""
        pass

    @abc.abstractmethod
    def commit(self):
        """Write all relevant metadata into the bundle."""
        pass

    @abc.abstractmethod
    def close(self):
        """Close the writer."""
        pass
