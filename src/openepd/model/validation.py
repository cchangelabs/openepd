#
#  Copyright 2024 by C Change Labs Inc. www.c-change-labs.com
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
#  This software was developed with support from the Skanska USA,
#  Charles Pankow Foundation, Microsoft Sustainability Fund, Interface, MKA Foundation, and others.
#  Find out more at www.BuildingTransparency.org
#
from typing import Annotated, Any

import pydantic as pyd

RatioFloat = Annotated[float, pyd.Field(ge=0, le=1, example=0.5)]
"""Float field which represents a percentage ratio between 0 and 1."""


def together_validator(field1: str, field2: Any, values: dict[str, Any]) -> Any:
    """Shared validator to ensure that two fields are provided together or not provided at all."""
    value1 = values.get(field1)
    value2 = values.get(field2)
    if value1 is not None and value2 is None or value1 is None and value2 is not None:
        raise ValueError(f"Both or neither {field1} and {field2} days must be provided together")
