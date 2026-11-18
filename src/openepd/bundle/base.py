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
import abc
from collections.abc import Callable, Iterable, Iterator, Sequence
import csv
import re
from typing import IO, Self

from openepd.bundle.model import AssetInfo, AssetType, BundleManifest, RelType
from openepd.model.base import TOpenEpdObject

AssetFilter = Callable[[AssetInfo], bool]
"""A filter function for assets. Returns True if the asset should be included."""
AssetRef = str | AssetInfo
AssetRelation = tuple[str, AssetRef]
_REL_TYPE_PATTERN = re.compile(r"[a-z0-9._-]+\Z")


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
        "rels",
        "id",
        "version",
        "date_of_issue",
        "comment",
        "content_type",
        "size",
        "sha256",
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
    def _normalize_relations(
        cls,
        rels: Sequence[AssetRelation] | None,
        rel_asset: AssetRef | list[AssetRef] | None,
        rel_type: str | None,
    ) -> list[tuple[str, str]]:
        """Normalize relation pairs and the legacy single-type arguments."""
        if rels is not None and (rel_asset is not None or rel_type is not None):
            msg = "Specify rels or the legacy rel_asset/rel_type arguments, not both."
            raise ValueError(msg)

        if rels is None:
            if rel_asset is None and rel_type is None:
                return []
            if rel_asset is None or rel_type is None:
                msg = "Both legacy rel_asset and rel_type arguments are required."
                raise ValueError(msg)
            rel_assets = cls._asset_refs_to_str(rel_asset)
            if isinstance(rel_assets, str):
                rel_assets = [rel_assets]
            relations = [(rel_type, ref) for ref in rel_assets or []]
        else:
            relations = [(rel_type, cls._asset_ref_to_str(ref)) for rel_type, ref in rels]

        return [cls._validate_relation_pair(rel_type, ref) for rel_type, ref in relations]

    @classmethod
    def _serialize_relations_for_csv(cls, relations: Sequence[tuple[str, str]]) -> str | None:
        """Serialize validated relation pairs to the semicolon-separated TOC value."""
        if not relations:
            return None
        return ";".join(f"{rel_type}:{asset_ref}" for rel_type, asset_ref in relations)

    @classmethod
    def _validate_relation_pair(cls, rel_type: str, asset_ref: str) -> tuple[str, str]:
        if not isinstance(rel_type, str) or not _REL_TYPE_PATTERN.fullmatch(rel_type):
            raise ValueError(f"Invalid relation type {rel_type!r}.")
        if not asset_ref or asset_ref != asset_ref.strip() or ":" in asset_ref or ";" in asset_ref:
            raise ValueError(f"Invalid relation reference {asset_ref!r}.")
        return str(rel_type), asset_ref

    @classmethod
    def _effective_rel_type(cls, rel_type: str) -> str:
        """Map extension relation types to the reader-facing `related` type."""
        known_types = {relation_type.value for relation_type in RelType}
        return rel_type if rel_type in known_types else RelType.Related

    @classmethod
    def _relation_type_matches(cls, actual: str, requested: str) -> bool:
        return cls._effective_rel_type(actual) == cls._effective_rel_type(requested)

    @classmethod
    def _get_asset_relations(cls, asset_info: AssetInfo) -> list[tuple[str, str]]:
        """Return relation type/reference pairs, accepting legacy TOC rows."""
        if asset_info.rels is not None:
            if not asset_info.rels:
                return []
            relations = []
            for relation in asset_info.rels.split(";"):
                if relation.count(":") != 1:
                    raise ValueError(f"Invalid relation {relation!r} in asset {asset_info.ref!r}.")
                relations.append(cls._validate_relation_pair(*relation.split(":")))
            return relations

        if asset_info.rel_type is None and asset_info.rel_asset is None:
            return []
        if asset_info.rel_type is None or asset_info.rel_asset is None:
            raise ValueError(f"Incomplete legacy relation on asset {asset_info.ref!r}.")
        return [cls._validate_relation_pair(asset_info.rel_type, ref) for ref in asset_info.rel_asset.split(";")]

    @classmethod
    def _validate_relations(cls, assets: Iterable[AssetInfo]) -> None:
        """Validate relation syntax and graph invariants for a bundle."""
        assets_by_ref: dict[str, AssetInfo] = {}
        for asset in assets:
            assets_by_ref.setdefault(asset.ref, asset)

        relations_by_ref: dict[str, list[tuple[str, str]]] = {}
        parents_by_ref: dict[str, list[str]] = {}
        incoming_count = dict.fromkeys(assets_by_ref, 0)
        for asset in assets_by_ref.values():
            relations = cls._get_asset_relations(asset)
            if len(relations) != len(set(relations)):
                raise ValueError(f"Duplicate relation on asset {asset.ref!r}.")
            relations_by_ref[asset.ref] = relations
            parents_by_ref[asset.ref] = []
            translation_relations = [
                parent_ref for rel_type, parent_ref in relations if rel_type == RelType.Translation
            ]
            if len(translation_relations) > 1:
                raise ValueError(f"Asset {asset.ref!r} has more than one translation relation.")

            for rel_type, parent_ref in relations:
                parent = assets_by_ref.get(parent_ref)
                if parent is None:
                    raise ValueError(f"Relation on asset {asset.ref!r} references missing asset {parent_ref!r}.")
                if parent_ref == asset.ref:
                    raise ValueError(f"Asset {asset.ref!r} must not relate to itself.")
                parents_by_ref[asset.ref].append(parent_ref)
                incoming_count[parent_ref] += 1

                if rel_type == RelType.Translation:
                    if asset.type != parent.type:
                        msg = "A translation relation must connect assets of the same type."
                        raise ValueError(msg)
                    if not asset.lang:
                        raise ValueError(f"Translation asset {asset.ref!r} must have a language.")
                elif rel_type == RelType.Pdf and asset.content_type != "application/pdf":
                    raise ValueError(f"PDF representation {asset.ref!r} must have application/pdf content type.")
                elif rel_type == RelType.Embedded and parent.type == AssetType.Blob:
                    raise ValueError(f"Embedded relation parent {parent_ref!r} must be an object asset.")

        for relations in relations_by_ref.values():
            for rel_type, parent_ref in relations:
                if rel_type == RelType.Translation and any(
                    parent_rel_type == RelType.Translation for parent_rel_type, _ in relations_by_ref[parent_ref]
                ):
                    raise ValueError(f"Translation parent {parent_ref!r} must not itself be a translation.")

        ready = [asset_ref for asset_ref, count in incoming_count.items() if count == 0]
        visited_count = 0
        while ready:
            asset_ref = ready.pop()
            visited_count += 1
            for parent_ref in parents_by_ref[asset_ref]:
                incoming_count[parent_ref] -= 1
                if incoming_count[parent_ref] == 0:
                    ready.append(parent_ref)
        if visited_count != len(assets_by_ref):
            msg = "Asset relations must not contain cycles."
            raise ValueError(msg)


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
        rels: Sequence[AssetRelation] | None = None,
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
        rels: Sequence[AssetRelation] | None = None,
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
