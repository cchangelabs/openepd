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

from openepd.model.examples.org import EXAMPLE_ORG_HERMAN_MILLER, EXAMPLE_ORG_NSF

EXAMPLE_GENERIC_ESTIMATE_SAMPLE: Final[dict[str, Any]] = {
    "id": "0197ad82-92cf-7978-a6c8-d4964c0a3624",
    "doctype": "openGenericEstimate",
    "openepd_version": "0.1",
    "name": "Generic Estimate Sample",
    "kg_per_declared_unit": {"qty": 10.0, "unit": "kg"},
    "reference_year": 2020,
    "composition": [
        {"name": "Mild Steel, machined", "kg_mass": 5.0, "id": "d50ccd58-1a8a-4327-8036-12ff68cecde7"},
        {"name": "Polyurethane foam", "kg_mass": 2.5, "tags": ["foam", "polyurethane"]},
    ],
    "lci_databases": [
        {
            "owner": {"web_domain": "ecoinvent.org"},
            "name": "ecoinvent",
            "version": "3.10",
            "link": "https://support.ecoinvent.org/ecoinvent-version-3.10",
        }
    ],
    "software_used": [
        {
            "owner": {"web_domain": "greendelta.com"},
            "primary_function": "LCA Analysis",
            "name": "openLCA",
            "version": "1.10",
            "link": "https://www.openlca.org/",
        }
    ],
    "publisher": EXAMPLE_ORG_HERMAN_MILLER,
    "reviewer": EXAMPLE_ORG_NSF,
    "owner": EXAMPLE_ORG_HERMAN_MILLER,
    "license_terms": "CC-BY",
    "model_repository": "https://example.com/repo/generic-estimate-model",
}
