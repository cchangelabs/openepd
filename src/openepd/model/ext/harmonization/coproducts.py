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

import pydantic as pyd

from openepd.model.ext.harmonization.base import HarmonizationFactorBase


class CoproductAllocationBasis(StrEnum):
    """
    How coproducts are assigned a share of process burdens.

    * `mass`: Coproduct(s) are allocated a share of total emissions proportional to their mass.
    * `economic`: Coproduct(s) are allocated a share of total emissions proportional to expected economic value.
    * `zero`: Coproduct(s) are allocated none of the emissions and treated similar to waste products.
    """

    MASS = "mass"
    ECONOMIC = "economic"
    ZERO = "zero"


class CoproductsHarmonizationFactor(HarmonizationFactorBase):
    """Documents allocation of impact burdens to products other than the primary product."""

    allocation_basis: CoproductAllocationBasis | None = pyd.Field(
        default=None,
        description=(
            "How coproducts are assigned a portion of process burdens with these harmonization factors "
            "(for example, on an economic basis)."
        ),
        examples=[CoproductAllocationBasis.ECONOMIC],
    )
    base_allocation_basis: CoproductAllocationBasis | None = pyd.Field(
        default=None,
        description=(
            "How coproducts are assigned a portion of process burdens without these harmonization factors "
            "(for example, on a mass basis)."
        ),
        examples=[CoproductAllocationBasis.MASS],
    )
