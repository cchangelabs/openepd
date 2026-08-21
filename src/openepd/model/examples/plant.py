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

from openepd.model.examples.org import EXAMPLE_ORG_HERMAN_MILLER

EXAMPLE_PLANT_HERMAN_MILLER_MELKSHAM_UK: Final[dict[str, Any]] = {
    "id": "9C3V9V47+MV.hermanmiller.com",
    "name": "Melksham, UK",
    "pluscode": "9C3V9V47+MV",
    "latitude": 51.356694,
    "longitude": -2.1353505,
    "owner": EXAMPLE_ORG_HERMAN_MILLER,
    "address": "1 Portal Rd, Bowerhill, Melksham SN12 6GN, UK",
    "location": {
        "pluscode": "9C3V9V47+MV",
        "latlng": {"lat": 51.356694, "lng": -2.1353505},
        "address": "1 Portal Rd, Bowerhill, Melksham SN12 6GN, UK",
        "country": "GB",
        "jurisdiction": "GB",
    },
}
