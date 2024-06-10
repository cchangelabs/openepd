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
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec


class CastDecksAndUnderlaymentV1(BaseOpenEpdHierarchicalSpec):
    """
    Cast roof deck substrate systems.

    Typically made of gyspum concrete or cementitious wood fiber, that provide structural support to
    roofing materials.
    """

    _EXT_VERSION = "1.0"
