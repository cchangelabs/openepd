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
__all__ = [
    "is_m49_code",
    "iso_to_m49",
    "m49_to_iso",
    "m49_to_openepd",
    "m49_to_region_and_country_names",
    "openepd_to_m49",
    "region_and_country_names_to_m49",
]
from collections.abc import Collection

from openepd.m49.const import (
    COUNTRY_VERBOSE_NAME_TO_M49,
    ISO3166_ALPHA2_TO_M49,
    M49_AREAS,
    M49_TO_COUNTRY_VERBOSE_NAME,
    M49_TO_ISO3166_ALPHA2,
    M49_TO_REGION_VERBOSE_NAME,
    OPENEPD_SPECIAL_REGIONS,
    REGION_VERBOSE_NAME_TO_M49,
)


def iso_to_m49(regions: Collection[str]) -> set[str]:
    """
    Convert ISO3166 alpha2 country codes to M49 region codes.

    :param regions: List of ISO3166 alpha2 country codes (e.g., ["US", "CA", "MX"])
    :return: Set of M49 region codes (e.g., {"840", "124", "484"})
    :raises ValueError: If a country code is not found in M49 region codes.
    """

    if not regions:
        return set()

    result = set()
    for code in regions:
        m49_code = ISO3166_ALPHA2_TO_M49.get(code.upper())
        if m49_code:
            result.add(m49_code)
        else:
            msg = f"Country code '{code}' not found in M49 region codes."
            raise ValueError(msg)

    return result


def m49_to_iso(regions: Collection[str]) -> set[str]:
    """
    Convert M49 region codes to ISO3166 alpha2 country codes.

    :param regions: List of M49 region codes (e.g., ["840", "124", "484"])
    :return: Set of ISO3166 alpha2 country codes (e.g., {"US", "CA", "MX"})
    :raises ValueError: If a region code is not found in ISO3166.
    """

    if not regions:
        return set()

    result = set()
    for code in regions:
        iso_code = M49_TO_ISO3166_ALPHA2.get(code.upper())
        if iso_code:
            result.add(iso_code)
        else:
            msg = f"Region code '{code}' not found in ISO3166."
            raise ValueError(msg)

    return result


def region_and_country_names_to_m49(regions: Collection[str]) -> set[str]:
    """
    Convert user-friendly region and country names to M49 region codes.

    :param regions: List of user-friendly region and country names (e.g., ["Europe",
        "North America", "Austria", "Germany"])
    :return: Set of M49 region codes (e.g., {"150", "003", "040", "276"})
    :raises ValueError: If a region or country name is not found in M49 region codes.
    """

    if not regions:
        return set()

    result = set()
    for name in regions:
        m49_code = REGION_VERBOSE_NAME_TO_M49.get(name.title()) or COUNTRY_VERBOSE_NAME_TO_M49.get(name.title())
        if not m49_code:
            msg = f"Region or country name '{name}' not found in M49 region codes."
            raise ValueError(msg)
        result.add(m49_code)

    return result


def m49_to_region_and_country_names(regions: Collection[str]) -> set[str]:
    """
    Convert M49 region codes to user-friendly region names and country names.

    :param regions: List of M49 region codes (e.g., ["150", "003", "040", "276"])
    :return: Set of user-friendly region and country names (e.g., {"Europe", "North America", "Austria", "Germany"})
    :raises ValueError: If a region code is not found in M49 region codes.
    """

    if not regions:
        return set()

    result = set()
    for code in regions:
        if code not in M49_TO_REGION_VERBOSE_NAME and code not in M49_TO_COUNTRY_VERBOSE_NAME:
            msg = f"Region code '{code}' not found in M49 region codes."
            raise ValueError(msg)

        name = M49_TO_REGION_VERBOSE_NAME.get(code) or M49_TO_COUNTRY_VERBOSE_NAME.get(code, code)
        result.add(name)
    return result


def openepd_to_m49(regions: Collection[str]) -> set[str]:
    """
    Convert OpenEPD geography definitions to pure M49 region codes.

    :param regions: list of OpenEPD geography definitions including letter codes and aliases
        like "EU27" or "NAFTA" (e.g., ["EU27", "NAFTA"], ["US", "CA, MX"], ["NAFTA", "051"])
    :return: Set of M49 region codes (e.g., {"040", "056", "100", "191", "196", "203", "208", "233", "246", "250",
        "276", "300", "348", "372", "380", "428", "440", "442", "470", "528", "616", "620", "642", "703", "705", "724",
        "752", "840", "124", "484"}, {"840", "124", "484"}, {"840", "124", "484", "051"})
    :raises ValueError: If a region or country name is not found in ISO3166 or OpenEPD special regions.
    """

    if not regions:
        return set()

    result = set()
    for region in regions:
        if region in OPENEPD_SPECIAL_REGIONS:
            result.update(OPENEPD_SPECIAL_REGIONS[region].m49_codes)
        else:
            m49_code = ISO3166_ALPHA2_TO_M49.get(region.upper())
            if m49_code:
                result.add(m49_code)
            elif is_m49_code(region):
                result.add(region)
            else:
                msg = f"Region '{region}' not found in ISO3166 or OpenEPD special regions."
                raise ValueError(msg)
    return result


def m49_to_openepd(regions: list[str]) -> set[str]:
    """
    Convert M49 region codes to OpenEPD geography definitions.

    :param regions: List of M49 region codes (e.g., ["040", "056", "100", "191", "196", "203", "208", "233", "246",
        "250", "276", "300", "348", "372", "380", "428", "440", "442", "470", "528", "616", "620", "642", "703", "705",
        "724", "752", "840", "124", "484"], ["840", "124", "484"], ["040", "056", "100"])
    :return: Set of OpenEPD geography definitions including letter codes and aliases
        like "EU27" or "NAFTA" (e.g., {"EU27", "NAFTA"}, {"NAFTA"}, {"AT", "BE", "BG"})
    :raises ValueError: If a region code is not found in ISO3166 or OpenEPD special regions.
    """

    if not regions:
        return set()

    result = set()
    remaining_codes = set(regions)
    for special_region, special_region_data in OPENEPD_SPECIAL_REGIONS.items():
        special_region_codes = set(special_region_data.m49_codes)
        if special_region_codes.issubset(remaining_codes):
            result.add(special_region)
            remaining_codes -= special_region_codes

    for code in remaining_codes:
        iso_code = M49_TO_ISO3166_ALPHA2.get(code)
        if iso_code:
            result.add(iso_code)
        else:
            msg = f"Region code '{code}' not found in ISO3166 or OpenEPD special regions."
            raise ValueError(msg)

    return result


def is_m49_code(to_check: str) -> bool:
    """
    Check if passed string is M49 code.

    :param to_check: any string
    :return: `True` if passed string is M49 code, `False` otherwise
    """
    return to_check in M49_AREAS or to_check in M49_TO_ISO3166_ALPHA2
