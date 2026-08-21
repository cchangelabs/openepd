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

from openepd.model.examples.org import EXAMPLE_ORG_HERMAN_MILLER, EXAMPLE_ORG_NSF, EXAMPLE_ORG_WAP
from openepd.model.examples.pcr import EXAMPLE_PCR_BIFMA_SEATING
from openepd.model.examples.plant import EXAMPLE_PLANT_HERMAN_MILLER_MELKSHAM_UK

EXAMPLE_EPD_WORK_SURFACES: Final[dict[str, Any]] = {
    "id": "EC3BFRKG",
    "ext": {
        "cqd_epd_internal": {"box_id": "1670285291944", "copy_of": None},
        "ec3": {
            "uaGWP_a1a2a3_traci21": 58.76638612884466,
            "uaGWP_a1a2a3_ar5": 58.856815427680544,
            "category": "Furnishings >> WorkSurfaces",
            "manufacturer_specific": True,
            "plant_specific": True,
            "product_specific": True,
            "batch_specific": None,
            "supply_chain_specificity": 0.0,
            "original_data_format": "pdf",
        },
    },
    "doctype": "openEPD",
    "openepd_version": "0.1",
    "date_of_issue": "2021-02-24T00:00:00Z",
    "valid_until": "2026-02-24T00:00:00Z",
    "declared_unit": {"qty": 1.0, "unit": "m2"},
    "compliance": [],
    "product_classes": {"EC3": "Furnishings >> WorkSurfaces", "io.cqd.ec3": "Furnishings >> WorkSurfaces"},
    "language": "en",
    "private": False,
    "pcr": EXAMPLE_PCR_BIFMA_SEATING,
    "product_image": "https://static.epd.world/images/a33a8516010849d6a7f35f154d51eb1a.png",
    "declaration_url": "cqd.io/e/ec3bfrkg1j",
    "product_service_life_years": 10.0,
    "alt_ids": {},
    "third_party_verifier": EXAMPLE_ORG_NSF,
    "third_party_verifier_email": "afavilla@nsf.org",
    "third_party_verifier_name": "Tony Favilla",
    "epd_developer": EXAMPLE_ORG_WAP,
    "epd_developer_email": "matt@wapsustainability.com",
    "program_operator": EXAMPLE_ORG_NSF,
    "program_operator_doc_id": "EPD10526",
    "product_name": "Ratio Desk with Screen",
    "product_description": (
        "The Ratio height adjustable desk enables a smooth transition between sitting and standing. "
        "Users can vary their posture as they need, "
        "to find the right balance between sitting and standing throughout the day. "
        "With its clean lines and lightweight design, "
        "Ratio has been designed to blend into the modern office environment."
    ),
    "manufacturer": EXAMPLE_ORG_HERMAN_MILLER,
    "plants": [EXAMPLE_PLANT_HERMAN_MILLER_MELKSHAM_UK],
    "applicable_in": ["001"],
    "specs": {
        "ext_version": "1.2",
        "Furnishings": {
            "ext_version": "1.1",
            "WorkSurfaces": {"ext_version": "1.0"},
        },
    },
    "includes": [],
    "ec3": {
        "uaGWP_a1a2a3_traci21": 58.76638612884466,
        "uaGWP_a1a2a3_ar5": 58.856815427680544,
        "category": "Furnishings >> WorkSurfaces",
        "manufacturer_specific": True,
        "plant_specific": True,
        "product_specific": True,
        "supply_chain_specificity": 0.0,
        "original_data_format": "pdf",
    },
    "impacts": {
        "CML 2012": {
            "gwp": {
                "A1A2A3": {"mean": 50.0, "unit": "kgCO2e", "rsd": 0.2083266665599966, "dist": "log-normal"},
                "C_scenarios": [],
            },
            "odp": {
                "A1A2A3": {"mean": 0.00000108, "unit": "kgCFC11e", "dist": "log-normal"},
                "C_scenarios": [],
            },
        },
        "TRACI 2.1": {
            "gwp": {
                "A1A2A3": {"mean": 50.0, "unit": "kgCO2e", "rsd": 0.2083266665599966, "dist": "log-normal"},
            },
        },
    },
    "resource_uses": {},
    "output_flows": {},
}
