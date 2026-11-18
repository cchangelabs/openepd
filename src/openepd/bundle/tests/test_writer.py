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
from io import BytesIO, StringIO
from pathlib import Path
import tempfile
import unittest
import zipfile

from openepd.bundle.model import AssetType, RelType
from openepd.bundle.reader import DefaultBundleReader
from openepd.bundle.writer import DefaultBundleWriter
from openepd.model.pcr import Pcr

SRC_DATA = Path(__file__).parent / "data" / "source"


class DefaultBundleReaderTestCase(unittest.TestCase):
    writer: DefaultBundleWriter

    def __create_writer(self, comment: str | None = None) -> tuple[str, DefaultBundleWriter]:
        tmp_file = tempfile.mktemp(suffix=".epb")  # noqa NOSONAR
        return tmp_file, DefaultBundleWriter(tmp_file, comment=comment)

    def __create_reader(self, file_name: str) -> DefaultBundleReader:
        return DefaultBundleReader(Path(file_name))

    def test_write_empty_bundle(self):
        bundle_comment = "First empty bundle"
        file_name, writer = self.__create_writer(bundle_comment)
        with writer:
            pass
        with self.__create_reader(file_name) as reader:
            manifest = reader.get_manifest()
            self.assertEqual(bundle_comment, manifest.comment)
            self.assertEqual(0, len(list(reader.root_assets_iter())))

    def test_toc_uses_spec_columns_and_is_readable(self):
        file_name, writer = self.__create_writer()
        with writer:
            root = writer.write_blob_asset(BytesIO(b"root"), "text/plain")
            writer.write_blob_asset(BytesIO(b"related"), "text/plain", root, "translation", lang="fr")

        with zipfile.ZipFile(file_name) as archive:
            toc = csv.DictReader(StringIO(archive.read("toc").decode("utf-8")), dialect="toc")
            self.assertEqual(
                [
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
                ],
                toc.fieldnames,
            )
            rows = list(toc)
            self.assertEqual("", rows[0]["rels"])
            self.assertEqual(f"translation:{root.ref}", rows[1]["rels"])
            self.assertEqual("", rows[0]["id"])
            self.assertEqual("", rows[0]["version"])
            self.assertEqual("", rows[0]["date_of_issue"])
            self.assertEqual("", rows[0]["sha256"])

        with self.__create_reader(file_name) as reader:
            assets = list(reader.assets_iter())
            self.assertEqual(2, len(assets))
            self.assertEqual(f"translation:{root.ref}", assets[1].rels)
            self.assertEqual(assets[1].ref, reader.get_first_relative_asset(root).ref)

    def test_write_and_read_multiple_relation_types(self):
        file_name, writer = self.__create_writer()
        with writer:
            first_parent = writer.write_blob_asset(BytesIO(b"first"), "text/plain")
            second_parent = writer.write_blob_asset(BytesIO(b"second"), "text/plain")
            child = writer.write_blob_asset(
                BytesIO(b"child"),
                "text/plain",
                rels=[
                    (RelType.Related, first_parent),
                    ("acme.audit-trail", first_parent),
                    (RelType.Supplement, second_parent),
                ],
            )

        with self.__create_reader(file_name) as reader:
            child_from_bundle = reader.get_asset_by_ref(child.ref)
            self.assertEqual(
                f"related:{first_parent.ref};acme.audit-trail:{first_parent.ref};supplement:{second_parent.ref}",
                child_from_bundle.rels,
            )
            self.assertEqual(
                [child.ref],
                [asset.ref for asset in reader.get_relative_assets(first_parent, RelType.Related)],
            )
            self.assertEqual(
                [child.ref],
                [asset.ref for asset in reader.get_relative_assets(second_parent, RelType.Supplement)],
            )

    def test_writer_rejects_missing_relation_target(self):
        _, writer = self.__create_writer()
        writer.write_blob_asset(
            BytesIO(b"child"),
            "text/plain",
            rels=[(RelType.Related, "blob/missing.txt")],
        )
        with self.assertRaisesRegex(ValueError, "missing asset"):
            writer.close()

    def test_add_objects_with_minimal_info(self):
        file_name, writer = self.__create_writer()
        with (
            writer,
            open(SRC_DATA / "test-pcr.json") as pcr_file,
            open(SRC_DATA / "test-pcr.pdf", "rb") as pcr_pdf_file,
            open(SRC_DATA / "extraction-report.txt", "rb") as report_file,
        ):
            pcr_obj = Pcr.model_validate_json(pcr_file.read())
            pcr_asset = writer.write_object_asset(pcr_obj)
            writer.write_blob_asset(pcr_pdf_file, "application/pdf", pcr_asset, RelType.Pdf)
            writer.write_blob_asset(report_file, "text/plain", pcr_asset, "report")
        with self.__create_reader(file_name) as reader:
            self.assertEqual(1, len(list(reader.root_assets_iter())))
            self.assertEqual(3, len(list(reader.assets_iter())))
            pcr_from_bundle = reader.read_object_asset(Pcr, reader.get_first_root_asset(AssetType.Pcr))
            self.assertEqual(pcr_obj, pcr_from_bundle)

    def test_add_objects_with_custom_names(self):
        file_name, writer = self.__create_writer()
        with (
            writer,
            open(SRC_DATA / "test-pcr.json") as pcr_file,
            open(SRC_DATA / "test-pcr.pdf", "rb") as pcr_pdf_file,
            open(SRC_DATA / "extraction-report.txt", "rb") as report_file,
        ):
            pcr_obj = Pcr.model_validate_json(pcr_file.read())
            pcr_asset = writer.write_object_asset(
                pcr_obj,
                file_name="original-pcr.json",
                lang="en",
                comment="My comment",
                name="Original PCR",
            )
            writer.write_blob_asset(
                pcr_pdf_file,
                "application/pdf",
                pcr_asset,
                RelType.Pdf,
                file_name="pcr.pdf",
            )
            writer.write_blob_asset(
                report_file,
                "text/plain",
                pcr_asset,
                "report",
                file_name="ec3-extraction-report.txt",
            )
        with self.__create_reader(file_name) as reader:
            self.assertEqual(1, len(list(reader.root_assets_iter())))
            self.assertEqual(3, len(list(reader.assets_iter())))
            pcr_asset_from_bundle = reader.get_first_root_asset(AssetType.Pcr)
            self.assertEqual("en", pcr_asset_from_bundle.lang)
            self.assertEqual("pcr/original-pcr.json", pcr_asset_from_bundle.ref)
            self.assertEqual("My comment", pcr_asset_from_bundle.comment)
            self.assertEqual("Original PCR", pcr_asset_from_bundle.name)
            pdf_asset_from_bundle = reader.get_first_relative_asset(pcr_asset_from_bundle, RelType.Pdf)
            self.assertEqual("blob/pcr.pdf", pdf_asset_from_bundle.ref)
