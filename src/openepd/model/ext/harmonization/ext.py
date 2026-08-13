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

from typing import ClassVar

from openepd.compat.pydantic import pyd
from openepd.model.base import OpenEpdExtension
from openepd.model.ext.harmonization.coproducts import CoproductsHarmonizationFactor
from openepd.model.ext.harmonization.custom import CustomHarmonizationFactor
from openepd.model.ext.harmonization.eac import EacHarmonizationFactor
from openepd.model.ext.harmonization.mbvfa import MbvfaHarmonizationFactor
from openepd.model.ext.harmonization.offsets import OffsetsHarmonizationFactor


class HarmonizationEpdExtension(OpenEpdExtension):
    """OpenEPD extension payload for harmonization factors."""

    MAX_CUSTOM_FACTORS: ClassVar[int] = 10
    """Maximum number of custom harmonization factors allowed in addition to known fields."""

    class Config:
        extra = pyd.Extra.allow

        @staticmethod
        def schema_extra(schema: dict, model: type["HarmonizationEpdExtension"]) -> None:
            # Reflect dynamic extension value type and custom-factor cap in OpenAPI schema.
            schema["additionalProperties"] = {"$ref": "#/components/schemas/CustomHarmonizationFactor"}
            schema["maxProperties"] = len(model.__fields__) + model.MAX_CUSTOM_FACTORS

    coproducts: CoproductsHarmonizationFactor | None = pyd.Field(
        default=None,
        description=(
            "Documents allocation of impact burdens to products other than the primary product. "
            "These factors can be used to harmonize across allocation methodologies."
        ),
    )
    eac: EacHarmonizationFactor | None = pyd.Field(
        default=None,
        description=(
            "Documents the use and effects of Energy Attribute Certificates, "
            "including RECs and Guarantees of Origin, rather than grid emissions."
        ),
    )
    mbvfa: MbvfaHarmonizationFactor | None = pyd.Field(
        default=None,
        description=(
            "Documents the use and effects of Mass Balanced Virtual Feedstock Allocation, "
            "including book-and-claim and related accounting approaches."
        ),
    )
    offsets: OffsetsHarmonizationFactor | None = pyd.Field(
        default=None,
        description="Documents the use and effects of offsets, including registry standards and retirement coverage.",
    )

    @pyd.root_validator(pre=True)
    def parse_custom_factors(cls, values: dict) -> dict:
        """Parse unknown extension keys as CustomHarmonizationFactor values when object-like payloads are provided."""
        if not isinstance(values, dict):
            return values

        known_fields = set(cls.__fields__.keys())
        custom_factor_keys = [key for key in values if key not in known_fields]
        if len(custom_factor_keys) > cls.MAX_CUSTOM_FACTORS:
            msg = f"at most {cls.MAX_CUSTOM_FACTORS} custom harmonization factors are allowed"
            raise ValueError(msg)

        for key, value in values.items():
            if key in known_fields:
                continue
            if isinstance(value, CustomHarmonizationFactor):
                continue
            if isinstance(value, dict):
                try:
                    values[key] = CustomHarmonizationFactor.parse_obj(value)
                except pyd.ValidationError as e:
                    raise pyd.ValidationError(
                        [
                            pyd.error_wrappers.ErrorWrapper(raw_error.exc, loc=(key, *raw_error.loc_tuple()))  # type: ignore[union-attr]
                            for raw_error in e.raw_errors
                        ],
                        cls,  # type: ignore[arg-type]
                    ) from e
            else:
                raise pyd.ValidationError(
                    [
                        pyd.error_wrappers.ErrorWrapper(
                            ValueError("must be an object payload compatible with CustomHarmonizationFactor"),
                            loc=key,
                        )
                    ],
                    cls,  # type: ignore[arg-type]
                )

        return values

    @classmethod
    def get_extension_name(cls) -> str:
        """
        Return the OpenEPD extension namespace segment.

        :returns: The extension name used under ``ext.<name>``.
        """
        return "harmonization"
