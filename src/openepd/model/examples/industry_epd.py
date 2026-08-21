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

from openepd.model.examples.org import (
    EXAMPLE_ORG_HERMAN_MILLER,
    EXAMPLE_ORG_NSF,
    EXAMPLE_ORG_WAP,
)

EXAMPLE_INDUSTRY_EPD_METAL_PRODUCTS: Final[dict[str, Any]] = {
    "id": "WAP12345",
    "doctype": "openIndustryEpd",
    "openepd_version": "0.1",
    "date_of_issue": "2022-06-01T00:00:00Z",
    "valid_until": "2027-06-01T00:00:00Z",
    "version": 1,
    "description": (
        "Industry-average dataset for galvanized steel sheet used in building enclosure applications. "
        "Includes aggregated production data from participating manufacturers in the GB/IE region."
    ),
    "kg_per_declared_unit": {"qty": 1.0, "unit": "kg"},
    "sample_size": {"plants": 4, "manufacturers": 3},
    "publishers": [EXAMPLE_ORG_WAP],
    "manufacturers": [EXAMPLE_ORG_HERMAN_MILLER],
    "epd_developer": EXAMPLE_ORG_WAP,
    "third_party_verifier": EXAMPLE_ORG_NSF,
    "program_operator": EXAMPLE_ORG_NSF,
    "program_operator_doc_id": "IND-GALV-2022",
    "geography": ["GB", "IE"],
    "language": "en",
    "private": False,
    "specs": {"ext_version": "1.0"},
    "product_classes": {"EC3": "ConstructionMaterials"},
    "impacts": {"CML 2012": {"gwp": {"A1A2A3": {"mean": 2.1, "unit": "kgCO2e", "rsd": 0.12, "dist": "normal"}}}},
    "resource_uses": {},
    "output_flows": {},
}
