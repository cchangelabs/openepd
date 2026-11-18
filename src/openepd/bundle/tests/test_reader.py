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
import csv
from io import StringIO
from pathlib import Path
import tempfile
import unittest
import zipfile

from openepd.bundle.model import AssetType, RelType
from openepd.bundle.reader import DefaultBundleReader
from openepd.model.pcr import Pcr

DATA_DIR = Path(__file__).parent / "data"


class DefaultBundleReaderTestCase(unittest.TestCase):
    reader: DefaultBundleReader

    def setUp(self) -> None:
        self.reader = DefaultBundleReader(DATA_DIR / "test-bundle.epb")

    def tearDown(self) -> None:
        self.reader.close()

    def test_open_valid_file(self):
        with DefaultBundleReader(DATA_DIR / "test-bundle.epb"):
            pass

    def test_open_invalid_file_invalid_manifest(self):
        with self.assertRaises(ValueError):
            DefaultBundleReader(DATA_DIR / "test-bundle-corrupted-manifest.epb")

    def test_open_invalid_file_missing_manifest(self):
        with self.assertRaises(ValueError):
            DefaultBundleReader(DATA_DIR / "test-bundle-missing-manifest.epb")

    def test_open_invalid_file_missing_manifest_format(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_file = Path(temp_dir) / "missing-format.epb"
            with zipfile.ZipFile(bundle_file, mode="w") as archive:
                archive.writestr("manifest", '{"generator":"test"}')

            with self.assertRaisesRegex(ValueError, "format"):
                DefaultBundleReader(bundle_file)

    def test_open_invalid_file_unsupported_manifest_major_version(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_file = Path(temp_dir) / "unsupported-format.epb"
            with zipfile.ZipFile(bundle_file, mode="w") as archive:
                archive.writestr("manifest", '{"format":"openEPD Bundle/2.0","generator":"test"}')

            with self.assertRaisesRegex(ValueError, "major version"):
                DefaultBundleReader(bundle_file)

    def test_open_invalid_file_malformed_manifest_format(self):
        for bundle_format in ("openEPD Bundle/1", "Other Bundle/1.0", "openEPD Bundle/1.0-beta"):
            with self.subTest(bundle_format=bundle_format), tempfile.TemporaryDirectory() as temp_dir:
                bundle_file = Path(temp_dir) / "malformed-format.epb"
                with zipfile.ZipFile(bundle_file, mode="w") as archive:
                    archive.writestr("manifest", f'{{"format":"{bundle_format}","generator":"test"}}')

                with self.assertRaisesRegex(ValueError, "Unsupported bundle format"):
                    DefaultBundleReader(bundle_file)

    def test_open_file_with_supported_manifest_major_version(self):
        toc_buffer = StringIO()
        toc_writer = csv.writer(toc_buffer, dialect="toc")
        toc_writer.writerow(("ref", "type", "rels", "size"))

        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_file = Path(temp_dir) / "supported-format.epb"
            with zipfile.ZipFile(bundle_file, mode="w") as archive:
                archive.writestr(
                    "manifest", '{"format":"openEPD Bundle/1.1","generator":"test","future_field":"ignored"}'
                )
                archive.writestr("toc", toc_buffer.getvalue())

            with DefaultBundleReader(bundle_file) as reader:
                self.assertEqual("openEPD Bundle/1.1", reader.get_manifest().format)

    def test_open_invalid_file_missing_toc(self):
        with self.assertRaises(ValueError):
            DefaultBundleReader(DATA_DIR / "test-bundle-missing-toc.epb")

    def test_open_invalid_bundle_with_missing_relation_target(self):
        toc_buffer = StringIO()
        toc_writer = csv.writer(toc_buffer, dialect="toc")
        toc_writer.writerow(("ref", "type", "rels", "size"))
        toc_writer.writerow(("blob/child.txt", "blob", "related:blob/missing.txt", 1))

        with tempfile.TemporaryDirectory() as temp_dir:
            bundle_file = Path(temp_dir) / "invalid-relation.epb"
            with zipfile.ZipFile(bundle_file, mode="w") as archive:
                archive.writestr("manifest", '{"format":"openEPD Bundle/1.0","generator":"test"}')
                archive.writestr("toc", toc_buffer.getvalue())

            with self.assertRaisesRegex(ValueError, "missing asset"):
                DefaultBundleReader(bundle_file)

    def test_read_all_root_objects(self):
        objects = self.reader.root_assets_iter()
        self.assertEqual(1, len(list(objects)))

    def test_read_find_translated_asset(self):
        pcr = self.reader.get_first_root_asset(AssetType.Pcr)
        self.assertIsNotNone(pcr)
        translations = self.reader.get_translations_for_asset(pcr)
        self.assertEqual(1, len(translations))

    def test_read_all_related_assets(self):
        pcr = self.reader.get_first_root_asset(AssetType.Pcr)
        self.assertIsNotNone(pcr)
        related = self.reader.get_relative_assets(pcr)
        self.assertEqual(2, len(related))

    def test_read_related_pdf(self):
        pcr = self.reader.get_first_root_asset(AssetType.Pcr)
        self.assertIsNotNone(pcr)
        related = self.reader.get_first_relative_asset(pcr, RelType.Pdf)
        self.assertIsNotNone(related)
        self.assertEqual(AssetType.Blob, related.type)
        with self.reader.read_blob_asset(related) as f:
            self.assertEqual(b"%PDF", f.read(4))

    def test_read_pcr_object(self):
        pcr = self.reader.get_first_root_asset(AssetType.Pcr)
        self.assertIsNotNone(pcr)
        pcr_obj = self.reader.read_object_asset(Pcr, pcr)
        self.assertEqual("1.0/1.5/1.1", pcr_obj.version)
