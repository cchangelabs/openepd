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
__all__ = ("encode_path_param",)

from urllib.parse import quote


def encode_path_param(value: str) -> str:
    """
    Encode a path parameter value.

    :param value: parameter value
    :return: encoded value
    """
    return quote(value, safe="")


def remove_none_id_fields(d: dict) -> dict:
    """
    Remove any key 'id' with a None value from the dictionary, including nested dicts.

    :param d: the dict which may contain 'id' keys with None values.
    :return: a new dict with 'id' keys that have None values removed.

    :note:
        - This function does not modify the original dictionary (no side effects).
        - It returns a new dictionary with the necessary modifications applied.

    :example:
        >>> data = {
        ...     "id": None,
        ...     "name": "item1",
        ...     "details": {
        ...         "id": None,
        ...         "category": "tools",
        ...         "nested": {
        ...             "id": None,
        ...             "value": 42
        ...         }
        ...     }
        ... }
        >>> remove_none_id_fields(data)
        {'name': 'item1', 'details': {'category': 'tools', 'nested': {'value': 42}}}
    """
    if not isinstance(d, dict):
        return d

    cleaned_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            v = remove_none_id_fields(v)
        if not (k == "id" and v is None):
            cleaned_dict[k] = v

    return cleaned_dict
