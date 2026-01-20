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
from typing import TypeVar

T = TypeVar("T")


def none_raises(optional: T | None, message: str = "Unexpected `None`") -> T:
    """
    Convert an optional to its value.

    Raises an `AssertionError` if the value is `None`
    """
    if optional is None:
        raise AssertionError(message)
    return optional
