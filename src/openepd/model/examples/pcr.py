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
from typing import Any, Final

from openepd.model.examples.org import EXAMPLE_ORG_ISO, EXAMPLE_ORG_NSF

EXAMPLE_PCR_ISO_21930 = {
    "ext": {"functional_unit": {"functional_units": []}},
    "attachments": {},
    "id": "EC3E432H",
    "issuer": EXAMPLE_ORG_ISO,
    "issuer_doc_id": "ISO 21930:2017",
    "name": (
        "ISO 21930:2017 Sustainability in buildings and civil engineering works — "
        "Core rules for environmental product declarations of construction products and services"
    ),
    "short_name": "ISO 21930 Sustainability in buildings and civil engineering works",
    "declared_units": [
        {"qty": 1.0, "unit": "kg"},
        {"qty": 1.0, "unit": "m"},
        {"qty": 1.0, "unit": "m2"},
        {"qty": 1.0, "unit": "m3"},
        {"qty": 1.0, "unit": "item"},
    ],
    "version": "2017",
    "date_of_issue": "2017-01-01T00:00:00Z",
    "doc": "https://www.iso.org/standard/61694.html",
    "status": "Published",
    "product_classes": {"EC3": ["ConstructionMaterials"], "io.cqd.ec3": ["ConstructionMaterials"]},
}
EXAMPLE_PCR_BIFMA_SEATING: Final[dict[str, Any]] = {
    "ext": {"functional_unit": {"functional_units": []}},
    "attachments": {},
    "id": "CQD7RFJ4",
    "issuer": EXAMPLE_ORG_NSF,
    "name": "BIFMA PCR for Seating: UNCPC 3811",
    "short_name": "BIFMA Seating",
    "declared_units": [{"qty": 1.0, "unit": "item"}],
    "version": "3",
    "date_of_issue": "2014-07-30T00:00:00Z",
    "valid_until": "2025-02-28T00:00:00Z",
    "doc": (
        "https://d2evkimvhatqav.cloudfront.net/documents/PCR-Product-Category-Rules/"
        "BIFMA-PCR-for-Seating-2024-Ext.pdf?v=1734018840"
    ),
    "parent": EXAMPLE_PCR_ISO_21930,
    "status": "Expired",
    "product_classes": {"uncpc": ["3811"], "EC3": ["Chairs"], "io.cqd.ec3": ["Chairs"]},
}
