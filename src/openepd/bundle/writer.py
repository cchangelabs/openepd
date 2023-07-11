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
import csv
from io import BytesIO, StringIO
from os import PathLike
from pathlib import Path
import shutil
from typing import IO
import zipfile

from openepd.__version__ import VERSION
from openepd.bundle.base import AssetRef, BaseBundleWriter
from openepd.bundle.model import AssetInfo, AssetType, BundleManifest, BundleManifestAssetsStats
from openepd.model.base import TOpenEpdObject


class DefaultBundleWriter(BaseBundleWriter):
    """Default bundle writer implementation. Writes the bundle to a ZIP file."""

    def __init__(self, bundle_file: str | PathLike | IO[bytes], comment: str | None = None):
        if isinstance(bundle_file, (PathLike, str)) and Path(bundle_file).exists():
            raise ValueError("Amending existing files is not supported yet.")
        self._bundle_archive = zipfile.ZipFile(bundle_file, mode="w")
        self.__manifest = BundleManifest(
            format="openEPD Bundle/1.0",
            generator=f"openEPD Python SDK/{VERSION}",
            comment=comment,
            assets=BundleManifestAssetsStats(),
        )
        self.__added_entries: set[str] = set()
        self.__toc_buffer = StringIO()
        self._toc_writer = csv.DictWriter(self.__toc_buffer, fieldnames=self._TOC_FIELDS, dialect="toc")
        self._toc_writer.writeheader()

    def write_blob_asset(
        self,
        data: IO[bytes],
        content_type: str | None = None,
        rel_asset: AssetRef | None = None,
        rel_type: str | None = None,
        file_name: str | None = None,
        name: str | None = None,
        lang: str | None = None,
        comment: str | None = None,
        custom_type: str | None = None,
        custom_data: str | None = None,
    ) -> AssetInfo:
        """Write a blob asset to the bundle."""
        rel_ref_str = self._asset_ref_to_str(rel_asset) if rel_asset is not None else None
        ref_str = self.__generate_entry_name(
            AssetType.Blob, self.__get_ext_for_content_type(content_type, "bin"), file_name
        )
        asset_info = AssetInfo(
            ref=ref_str,
            name=name,
            type=AssetType.Blob,
            lang=lang,
            rel_type=rel_type,
            rel_asset=rel_ref_str,
            content_type=content_type,
            comment=comment,
            custom_type=custom_type,
            custom_data=custom_data,
        )
        self.__write_data_stream(asset_info, data)
        self.__register_entry(asset_info)
        return asset_info

    def write_object_asset(
        self,
        obj: TOpenEpdObject,
        rel_asset: AssetRef | None = None,
        rel_type: str | None = None,
        file_name: str | None = None,
        name: str | None = None,
        lang: str | None = None,
        comment: str | None = None,
        custom_type: str | None = None,
        custom_data: str | None = None,
    ) -> AssetInfo:
        """Write an object asset to the bundle. Object means subclass of BaseOpenEpdSchem."""
        asset_type_str = obj.get_asset_type()
        if asset_type_str is None:
            raise ValueError(f"Object {obj} does not have a valid asset type and can't be written to a bundle.")
        asset_type = AssetType(asset_type_str)
        rel_ref_str = self._asset_ref_to_str(rel_asset) if rel_asset is not None else None
        ref_str = self.__generate_entry_name(
            asset_type, self.__get_ext_for_content_type("application/json", "json"), file_name
        )
        asset_info = AssetInfo(
            ref=ref_str,
            name=name,
            type=asset_type,
            lang=lang,
            rel_asset=rel_ref_str,
            rel_type=rel_type,
            content_type="application/json",
            comment=comment,
            custom_type=custom_type,
            custom_data=custom_data,
        )
        self.__write_data_stream(
            asset_info, BytesIO(obj.json(indent=2, exclude_unset=True, exclude_none=True).encode("utf-8"))
        )
        self.__register_entry(asset_info)
        return asset_info

    def commit(self):
        """Write the manifest and TOC to the bundle. This will be called automatically when the bundle is closed."""
        with self._bundle_archive.open("manifest", "w") as manifest_stream:
            manifest_stream.write(self.__manifest.json(indent=2, exclude_none=True).encode("utf-8"))
        with self._bundle_archive.open("toc", "w") as toc_stream:
            toc_stream.write(self.__toc_buffer.getvalue().encode("utf-8"))

    def close(self):
        """Write the manifest and TOC and close the bundle stream."""
        self.commit()
        self._bundle_archive.close()

    def __register_entry(self, asset_info: AssetInfo):
        if asset_info.ref in self.__added_entries:
            raise ValueError(f"Asset {asset_info.ref} already exists in the bundle.")
        self._toc_writer.writerow(asset_info.dict(exclude_unset=True, exclude_none=True))
        self.__added_entries.add(asset_info.ref)
        type_counter = self.__manifest.assets.count_by_type.get(asset_info.type, 0) + 1
        self.__manifest.assets.count_by_type[asset_info.type] = type_counter
        self.__manifest.assets.total_count += 1
        if asset_info.size is None:
            raise ValueError("Size of asset is not set.")
        self.__manifest.assets.total_size += asset_info.size

    def __generate_entry_name(self, asset_type: str, extension: str | None = None, file_name: str | None = None) -> str:
        current_counter = self.__manifest.assets.count_by_type.get(asset_type, 0)
        current_counter += 1
        if file_name is None:
            extension = extension or "bin"
            return f"{asset_type}/{str(current_counter).rjust(6, '0')}.{extension}"
        else:
            return f"{asset_type}/{file_name}"

    def __mkdir_for_type(self, asset_type: str):
        try:
            info = self._bundle_archive.getinfo(f"{asset_type}/")
            if info.is_dir():
                return
            raise ValueError(f"Object with name {asset_type} already exists in the bundle.")
        except KeyError:
            self._bundle_archive.mkdir(str(asset_type))

    def __write_data_stream(self, asset_info: AssetInfo, data: IO[bytes]):
        self.__mkdir_for_type(asset_info.type)
        with self._bundle_archive.open(asset_info.ref, "w") as asset_stream:
            shutil.copyfileobj(data, asset_stream, 1024 * 8)  # type: ignore
        added_obj = self._bundle_archive.getinfo(asset_info.ref)
        asset_info.size = added_obj.file_size

    def __get_ext_for_content_type(self, content_type: str | None, default: str = "bin") -> str:
        if content_type is not None:
            return default
        match content_type:
            case "text/plain":
                return "txt"
            case "application/json":
                return "json"
            case "application/xml":
                return "xml"
            case "application/zip":
                return "zip"
            case "application/pdf":
                return "pdf"
            case "image/png":
                return "png"
            case "image/jpeg":
                return "jpg"
            case "image/gif":
                return "gif"
            case "image/svg+xml":
                return "svg"
            case "image/tiff":
                return "tiff"
            case "image/webp":
                return "webp"
            case "image/bmp":
                return "bmp"
        return default
