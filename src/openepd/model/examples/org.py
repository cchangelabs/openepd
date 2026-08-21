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

EXAMPLE_ORG_NSF: Final[dict[str, Any]] = {
    "web_domain": "nsf.org",
    "name": "NSF International",
    "ref": "https://openepd.epd.world/api/orgs/nsf.org",
    "attachments": {
        "Program Operator instructions": (
            "https://d2evkimvhatqav.cloudfront.net/documents/NSF_Program_Operator_Instructions-news.pdf"
        )
    },
    "alt_names": ["NSF", "NSF Certification LLC", "NSF Certification"],
    "hq_location": {
        "pluscode": "86JR78MG+94",
        "latlng": {"lat": 42.283469, "lng": -83.6746525},
        "address": "789 N Dixboro Rd, Ann Arbor, MI 48105, USA",
        "country": "US",
    },
    "logo": "https://static.epd.world/images/d70cecab-c90a-4395-b715-02e4e2624461.png",
}

EXAMPLE_ORG_ISO: Final[dict[str, Any]] = {
    "web_domain": "iso.org",
    "name": "ISO",
    "ref": "https://openepd.epd.world/api/orgs/iso.org",
    "attachments": {},
    "alt_names": ["International Standards Organization"],
    "hq_location": {
        "pluscode": "87M32GC3+9V",
        "latlng": {"lat": 43.0208924, "lng": -78.4953015},
        "address": "Akron, NY 14001, USA",
        "country": "US",
    },
    "logo": "https://static.epd.world/images/c900dcbd-65ac-41d4-ad4f-958462d7496f.png",
}

EXAMPLE_ORG_WAP: Final[dict[str, Any]] = {
    "web_domain": "wapsustainability.com",
    "name": "WAP Sustainability",
    "ref": "https://openepd.epd.world/api/orgs/wapsustainability.com",
    "attachments": {},
    "alt_names": [
        "WAP Sustainability",
        "WAP Sustainability Consulting",
        "WAP Sustainability Consulting, LLC",
        "WAP",
    ],
    "hq_location": {
        "pluscode": "867P2MMR+PH",
        "latlng": {"lat": 35.0343565, "lng": -85.3085122},
        "address": "1701 Market St, Chattanooga, TN 37408, USA",
        "country": "US",
    },
    "logo": "https://static.epd.world/images/0d41be5eff0443e385134022ca79ee61.png",
}

EXAMPLE_ORG_HERMAN_MILLER: Final[dict[str, Any]] = {
    "web_domain": "hermanmiller.com",
    "name": "Herman Miller",
    "ref": "https://openepd.epd.world/api/orgs/hermanmiller.com",
    "attachments": {"TransparencyCatalogURL": "https://transparencycatalog.com/company/herman-miller"},
    "description": (
        "Over the last century, "
        "Herman Miller has been guided by a commitment to problem-solving designs that inspire the best in people. "
        "Along the way, Herman Miller has forged critical relationships with the most visionary designers of the day, "
        "from mid-century greats like George Nelson, the Eames Office, and Isamu Noguchi, "
        "to research-oriented visionaries like Robert Propst and Bill Stumpf—and with today's groundbreaking studios "
        "like Industrial Facility and Studio 7.5. "
        "From the birth of ergonomic furniture to manufacturing some of the twentieth century's most iconic pieces, "
        "Herman Miller has pioneered original, timeless design that makes an enduring impact, "
        "while building a lasting legacy of design, innovation, and social good. "
        "Herman Miller is a part of MillerKnoll, "
        "a collective of dynamic brands that come together to design the world we live in. "
        "For more information, visit [hermanmiller.com/about](https://www.hermanmiller.com/about/)."
    ),
    "hq_location": {
        "pluscode": "86JMQVQR+2C",
        "latlng": {"lat": 42.7875235, "lng": -86.1089301},
        "address": "Holland, MI 49423, USA",
        "country": "US",
    },
    "logo": "https://static.epd.world/images/329e6f5ec21a46d98fbb6a33713309ad.png",
}
