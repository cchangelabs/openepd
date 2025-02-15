#
#  Copyright 2025 by C Change Labs Inc. www.c-change-labs.com
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
from typing import Dict, List, Set

from .m49 import (
    AFRICA,
    AMERICAS,
    ASIA,
    EUROPE,
    M49_AREAS,
    M49_CODE_AFRICA,
    M49_CODE_ASIA,
    M49_CODE_CENTRAL_AMERICA,
    M49_CODE_EUROPE,
    M49_CODE_NORTH_AMERICA,
    M49_CODE_OCEANIA,
    M49_CODE_SOUTH_AMERICA,
    M49_CODE_WORLD,
    M49_TO_ISO3166_ALPHA2,
    OCEANIA,
    WORLD,
)

# reverse mapping from ISO3166 alpha2 to M49
ISO3166_ALPHA2_TO_M49 = {v: k for k, v in M49_TO_ISO3166_ALPHA2.items()}

# user-friendly region names
REGION_NAME_TO_M49 = {
    "Word": M49_CODE_WORLD,
    "Africa": M49_CODE_AFRICA,
    "Asia": M49_CODE_ASIA,
    "Europe": M49_CODE_EUROPE,
    "North America": M49_CODE_NORTH_AMERICA,
    "South America": M49_CODE_SOUTH_AMERICA,
    "Oceania": M49_CODE_OCEANIA,
    "Central America": M49_CODE_CENTRAL_AMERICA,
}

# reverse mapping of M49 code to region name
M49_TO_REGION_NAME = {
    M49_CODE_WORLD: "World",
    M49_CODE_AFRICA: "Africa",
    M49_CODE_ASIA: "Asia",
    M49_CODE_EUROPE: "Europe",
    M49_CODE_NORTH_AMERICA: "North America",
    M49_CODE_SOUTH_AMERICA: "South America",
    M49_CODE_OCEANIA: "Oceania",
    M49_CODE_CENTRAL_AMERICA: "Central America",
}

# openepd specific mappings
OPENEPD_SPECIAL_REGIONS = {
    "EU27": {
        "description": "European Union (27 member states)",
        "m49_codes": set(
            ISO3166_ALPHA2_TO_M49[cc]
            for cc in [
                "AT",
                "BE",
                "BG",
                "HR",
                "CY",
                "CZ",
                "DK",
                "EE",
                "FI",
                "FR",
                "DE",
                "GR",
                "HU",
                "IE",
                "IT",
                "LV",
                "LT",
                "LU",
                "MT",
                "NL",
                "PL",
                "PT",
                "RO",
                "SK",
                "SI",
                "ES",
                "SE",
            ]
            if cc in ISO3166_ALPHA2_TO_M49
        ),
    },
    "NAFTA": {
        "description": "North American Free Trade Agreement",
        "m49_codes": {"840", "124", "484"},  # US, Canada, Mexico
    },
}


class GeographicRegionConverter:
    """
    Utility class for converting between different geographic region formats.
    """

    @staticmethod
    def iso_to_m49(regions: List[str]) -> List[str]:
        """
        Convert ISO3166 alpha2 country codes to M49 region codes.

        Args:
            regions: List of ISO3166 alpha2 country codes (e.g., ["US", "CA", "MX"])

        Returns:
            List of M49 region codes (e.g., ["840", "124", "484"])
        """
        return [ISO3166_ALPHA2_TO_M49.get(code.upper(), code) for code in regions]

    @staticmethod
    def m49_to_iso(regions: List[str]) -> List[str]:
        """
        Convert M49 region codes to ISO3166 alpha2 country codes.

        Args:
            regions: List of M49 region codes (e.g., ["840", "124", "484"])

        Returns:
            List of ISO3166 alpha2 country codes (e.g., ["US", "CA", "MX"])
        """
        return [M49_TO_ISO3166_ALPHA2.get(code.upper(), code) for code in regions]
