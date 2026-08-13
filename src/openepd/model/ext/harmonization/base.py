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
from abc import ABC

from openepd.compat.pydantic import pyd
from openepd.model.base import BaseOpenEpdSchema
from openepd.model.common import AnyAmount
from openepd.model.lcia import LCIAMethod


class LifecycleModuleAmounts(pyd.BaseModel):
    """Impact amounts organized by EN 15804 lifecycle modules."""

    A1A2A3: AnyAmount | None = pyd.Field(
        description="Sum of A1..A3",
        default=None,
    )
    A1: AnyAmount | None = pyd.Field(
        description="Raw Material Supply",
        default=None,
    )
    A2: AnyAmount | None = pyd.Field(
        description="Transport to Manufacturing",
        default=None,
    )
    A3: AnyAmount | None = pyd.Field(
        description="Manufacturing",
        default=None,
    )
    A4: AnyAmount | None = pyd.Field(
        description="Transport to Construction",
        default=None,
    )
    A5: AnyAmount | None = pyd.Field(
        description="Construction",
        default=None,
    )
    B1: AnyAmount | None = pyd.Field(
        description="Use impacts over Reference Service Life (Predicted)",
        default=None,
    )
    B2: AnyAmount | None = pyd.Field(
        description="Predicted Maintenance Impacts over Reference Service Life",
        default=None,
    )
    B3: AnyAmount | None = pyd.Field(
        description="Predicted Repair impacts over Reference Service Life",
        default=None,
    )
    B4: AnyAmount | None = pyd.Field(
        description="Predicted Replacement Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR.",
        default=None,
    )
    B5: AnyAmount | None = pyd.Field(
        description="Predicted Refurbishment Impacts over the Building lifetime "
        "('Estimated Construction Works lifespan') specified in the PCR.",
        default=None,
    )
    B6: AnyAmount | None = pyd.Field(
        description="Predicted Impacts related to Operational Energy Use",
        default=None,
    )
    B7: AnyAmount | None = pyd.Field(
        description="Predicted Impacts related to Operational Water Use",
        default=None,
    )
    C1: AnyAmount | None = pyd.Field(
        description="Deconstruction and Demolition",
        default=None,
    )
    C2: AnyAmount | None = pyd.Field(
        description="Transport to waste processing or disposal.",
        default=None,
    )
    C3: AnyAmount | None = pyd.Field(
        description="Waste Processing",
        default=None,
    )
    C4: AnyAmount | None = pyd.Field(
        description="Disposal",
        default=None,
    )
    D: AnyAmount | None = pyd.Field(
        default=None,
        description="Potential net benefits from reuse, recycling, and/or energy recovery beyond the system boundary.",
    )


class IndicatorAmountsByLifecycleModule(pyd.BaseModel):
    """
    Map each indicator/category key to lifecycle-module amounts.

    Dynamic keys are indicator names relevant to the section where this model is used,
    for example impact indicators (``gwp``), resource uses, or output flows.
    """

    __root__: dict[str, LifecycleModuleAmounts]


class HarmonizationFactorBase(BaseOpenEpdSchema, ABC):
    description: str | None = pyd.Field(
        default=None,
        description="Optional details or justification for this harmonization factor.",
        example="All electricity consumption at the Harford plant is covered by on-site solar or green-e RECs.",
        max_length=2000,
    )
    in_reported: bool = pyd.Field(
        default=False,
        description=(
            "True means this factor is already included in the reported impacts. "
            "To harmonize with a methodology that does not allow it, subtract these values. "
            "False means this factor is not included; add these values when harmonizing with a methodology that allows it."
        ),
    )
    harmonization_factors: bool = pyd.Field(
        default=False,
        description=(
            "True means harmonization factors are provided in this extension. "
            "When true, any omitted impact is considered not materially affected (<1%). "
            "False means this extension only reports whether this accounting method is used; "
            "all harmonization factors should be treated as unknown (not zero)."
        ),
    )
    multiply_after: list[pyd.constr(max_length=200)] = pyd.Field(  # type: ignore[valid-type]
        default_factory=list,
        description=(
            "Harmonization factor IDs that must be applied before this factor because they interact multiplicatively. "
            "When applicable, first apply each listed factor to produce an interim result, then apply this factor's multiplier."
        ),
        example=["coproducts"],
        max_items=25,
    )
    impacts: dict[LCIAMethod, IndicatorAmountsByLifecycleModule] | None = pyd.Field(
        default=None,
        description="Optional harmonization impact deltas grouped by LCIA method and indicator.",
    )
    resource_uses: IndicatorAmountsByLifecycleModule | None = pyd.Field(
        default=None,
        description=(
            "Optional harmonization deltas for resource use indicators grouped by indicator and lifecycle module."
        ),
    )
    output_flows: IndicatorAmountsByLifecycleModule | None = pyd.Field(
        default=None,
        description=(
            "Optional harmonization deltas for output flow indicators grouped by indicator and lifecycle module."
        ),
    )
