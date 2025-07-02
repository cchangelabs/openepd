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

__all__ = (
    "OPENEPD_GEOGRAPHY_MAPPER",
    "GeographyToOpenEpdMapper",
)

from openepd.m49 import const as m49_const
from openepd.m49 import utils as m49_utils
from openepd.utils.mapping.common import BaseDataMapper


class GeographyToOpenEpdMapper(BaseDataMapper[str, set[str]]):
    """Mapper that converts various geography inputs (e.g. country name, ISO code, M49) into openEPD compliant geography."""

    def map(
        self, input_value: str, default_value: str | set[str] | None, *, raise_if_missing: bool = False
    ) -> set[str] | None:
        """Map input geography value to openEpd geography codes."""
        result: set[str] = set()
        try:
            if input_value:
                input_value = input_value.strip()
            if m49_utils.is_m49_code(input_value):
                result = m49_utils.m49_to_openepd([input_value])
            elif m49_utils.is_iso_code(input_value):
                result = m49_utils.m49_to_openepd(m49_utils.iso_to_m49([input_value]))
            elif input_value.upper() in m49_const.OPENEPD_SPECIAL_REGIONS:  # Special regions like "NAFTA" or "EU"
                result = {input_value.upper()}
            else:  # this might be a verbose region or country name
                mapped_m49 = m49_utils.region_and_country_names_to_m49([input_value])
                result = m49_utils.m49_to_openepd(mapped_m49)
        except ValueError:
            result = set()
        if result:
            return result
        if raise_if_missing:
            raise ValueError(f"Input '{input_value}' could not be mapped to OpenEpd geography codes.")
        if isinstance(default_value, str):
            return {default_value}
        return default_value


OPENEPD_GEOGRAPHY_MAPPER = GeographyToOpenEpdMapper()
