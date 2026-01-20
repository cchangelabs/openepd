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
from enum import StrEnum


class SerializationStyle(StrEnum):
    Pretty = "pretty"
    Compact = "compact"


FIELD_SEPARATOR = ":"  # Divides term into field and operator parts. E.g. field_name: in(1, 2, 3)
OBJECT_FIELD_ACCESSOR = "."  # Separates object name from it field. E.g. epd.date, pcr.name
PRAGMA_KEYWORD = "!pragma"
SIGNIFICANT_DIGITS_PRECISION = 6
