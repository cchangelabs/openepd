#
#  Copyright 2026 by C Change Labs Inc. www.c-change-labs.com
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
from collections.abc import Callable, Iterator, Sequence
import csv
import io
from os import PathLike
import re
from typing import IO, cast
import zipfile

from openepd.bundle.base import AssetFilter, AssetRef, BaseBundleReader
from openepd.bundle.model import (
    BUNDLE_FORMAT_MAJOR_VERSION,
    BUNDLE_FORMAT_NAME,
    AssetInfo,
    AssetType,
    BundleManifest,
)
from openepd.model.base import TOpenEpdObject

_BUNDLE_FORMAT_PATTERN = re.compile(rf"{re.escape(BUNDLE_FORMAT_NAME)}/(?P<major>\d+)\.(?P<minor>\d+)")


class DefaultBundleReader(BaseBundleReader):
    """Default bundle reader implementation. Reads the bundle from a ZIP file."""

    def __init__(self, bundle_file: PathLike | IO[bytes] | str):
        self._bundle_archive = zipfile.ZipFile(bundle_file, mode="r")
        try:
            with self._bundle_archive.open("manifest", "r") as manifest_stream:
                self.__manifest = BundleManifest.model_validate_json(manifest_stream.read())
            self.__check_format(self.__manifest.format)
        except Exception as e:
            raise ValueError("The bundle file is not valid. Manifest reading error: " + str(e)) from e
        try:
            self.__check_toc()
        except Exception as e:
            raise ValueError("The bundle file is not valid. TOC reading error: " + str(e)) from e

    @staticmethod
    def __check_format(bundle_format: str) -> None:
        format_match = _BUNDLE_FORMAT_PATTERN.fullmatch(bundle_format)
        if format_match is None:
            msg = f"Unsupported bundle format: {bundle_format!r}"
            raise ValueError(msg)
        if int(format_match.group("major")) != BUNDLE_FORMAT_MAJOR_VERSION:
            msg = f"Unsupported bundle format major version: {format_match.group('major')}"
            raise ValueError(msg)

    def close(self):
        """Close the reader."""
        self._bundle_archive.close()

    def get_manifest(self) -> BundleManifest:
        """Get the manifest of the bundle. Manifest object is immutable."""
        return self.__manifest.model_copy(deep=True)

    def __create_asset_filter(
        self,
        asset_type: AssetType | str | None = None,
        name: str | None = None,
        parent_ref: AssetRef | None = None,
        ref_type: str | None = None,
        is_translated: bool | None = None,
    ) -> AssetFilter:
        def _filter(a: AssetInfo):
            if asset_type is not None and a.type != asset_type:
                return False
            if name is not None and a.name != name:
                return False
            if parent_ref is not None:
                parent_ref_str = self._asset_ref_to_str(parent_ref)
                rel_asset_list = self._get_rel_asset_list(a)
                if parent_ref_str not in rel_asset_list:
                    return False
            if ref_type is not None and not any(
                self._relation_type_matches(rel_type, ref_type) for rel_type, _ in self._get_asset_relations(a)
            ):
                return False
            if is_translated is not None and a.lang is not None and "translated" in a.lang:
                return True
            return True

        return _filter

    def __preprocess_csv_dict(self, input_dict: dict[str, str | None]) -> dict[str, str | None]:
        default_to_none_fields = (
            "rels",
            "rel_type",
            "rel_asset",
            "lang",
            "content_type",
            "custom_type",
            "custom_data",
        )
        for x in default_to_none_fields:
            if input_dict.get(x) == "":
                input_dict[x] = None
        return input_dict

    def _get_rel_asset_list(self, asset_info: AssetInfo) -> list[str]:
        """Get the list of related asset references from an AssetInfo object."""
        return [asset_ref for _, asset_ref in self._get_asset_relations(asset_info)]

    def assets_iter(self) -> Iterator[AssetInfo]:
        """Iterate over all assets in the bundle."""
        with self._bundle_archive.open("toc", "r") as toc_stream:
            toc_reader = csv.DictReader(io.TextIOWrapper(toc_stream, encoding="utf-8"), dialect="toc")
            for x in toc_reader:
                yield AssetInfo.model_validate(self.__preprocess_csv_dict(x))

    def __check_toc(self):
        with self._bundle_archive.open("toc", "r") as toc_stream:
            toc_reader = csv.DictReader(io.TextIOWrapper(toc_stream, encoding="utf-8"), dialect="toc")
            columns = set(toc_reader.fieldnames or ())
            required_columns = {"ref", "type", "rels", "size"}
            legacy_columns = {"ref", "type", "rel_type", "rel_asset", "size"}
            if not (required_columns <= columns or legacy_columns <= columns):
                msg = "The bundle file is not valid. TOC reading error: missing required columns"
                raise ValueError(msg)
            assets = [AssetInfo.model_validate(self.__preprocess_csv_dict(row)) for row in toc_reader]
        self._validate_relations(assets)

    def root_assets_iter(
        self,
        filter_or_type: AssetFilter | str | AssetType | None = None,
        name: str | None = None,
        parent_ref: AssetRef | None = None,
        ref_type: str | None = None,
        is_translated: bool | None = None,
    ) -> Iterator[AssetInfo]:
        """Iterate over all root assets in the bundle."""
        _filter: AssetFilter
        if isinstance(filter_or_type, Callable):  # type: ignore
            _filter = filter_or_type  # type: ignore
        else:
            _filter = self.__create_asset_filter(
                asset_type=cast(str, filter_or_type),
                name=name,
                parent_ref=parent_ref,
                ref_type=ref_type,
                is_translated=is_translated,
            )

        for x in self.assets_iter():
            if _filter(x) and not self._get_asset_relations(x):
                yield x

    def get_relative_assets_iter(
        self, asset: AssetRef, rel_type: str | Sequence[str] | None = None
    ) -> Iterator[AssetInfo]:
        """Iterate over all assets that are relative to the given asset."""
        if rel_type is not None and isinstance(rel_type, str):
            rel_type = [rel_type]
        asset_ref = self._asset_ref_to_str(asset)
        for x in self.assets_iter():
            relations = self._get_asset_relations(x)
            if asset_ref in {ref for _, ref in relations} and (
                rel_type is None
                or any(
                    self._relation_type_matches(relation_type, requested)
                    for relation_type, _ in relations
                    for requested in rel_type
                )
            ):
                yield x

    def get_asset_by_ref(self, asset_ref: AssetRef) -> AssetInfo | None:
        """Get the asset by its reference."""
        if isinstance(asset_ref, AssetInfo):
            return asset_ref
        asset_ref = self._asset_ref_to_str(asset_ref)
        for x in self.assets_iter():
            if x.ref == asset_ref:
                return x
        return None

    def read_blob_asset(self, asset_ref: AssetRef) -> IO[bytes]:
        """Read the blob asset."""
        asset = self.get_asset_by_ref(asset_ref)
        if asset is None:
            msg = "Asset not found"
            raise ValueError(msg)
        return self._bundle_archive.open(asset.ref, "r")

    def read_object_asset(self, obj_class: type[TOpenEpdObject], asset_ref: AssetRef) -> TOpenEpdObject:
        """Read the object asset."""
        asset = self.get_asset_by_ref(asset_ref)
        if asset is None:
            msg = "Asset not found"
            raise ValueError(msg)
        if obj_class.get_asset_type() is None:
            msg = f"Target object {obj_class.__name__} is not supported asset"
            raise ValueError(msg)
        if asset.type != obj_class.get_asset_type():
            msg = f"Asset type mismatch. Expected {obj_class.get_asset_type()}, got {asset.type}"
            raise ValueError(msg)
        with self._bundle_archive.open(asset.ref, "r") as asset_stream:
            return obj_class.model_validate_json(asset_stream.read())
