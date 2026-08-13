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
import unittest

from openepd.compat.pydantic import pyd
from openepd.model.epd import Epd
from openepd.model.ext.harmonization.coproducts import CoproductAllocationBasis
from openepd.model.ext.harmonization.custom import CustomHarmonizationFactor
from openepd.model.ext.harmonization.eac import EacCoverage, EacHarmonizationFactor, EacStandard
from openepd.model.ext.harmonization.ext import (
    HarmonizationEpdExtension,
)
from openepd.model.ext.harmonization.mbvfa import MbvfaAttribute, MbvfaTrackingApproach
from openepd.model.ext.harmonization.offsets import OffsetCoverage, OffsetStandard


class HarmonizationExtTestCase(unittest.TestCase):
    def test_parse_coproducts_extension_from_epd(self) -> None:
        epd = Epd.parse_obj(
            {
                "ext": {
                    "harmonization": {
                        "coproducts": {
                            "description": "Alternative burden sharing based on economic coproduct allocation.",
                            "in_reported": False,
                            "harmonization_factors": True,
                            "allocation_basis": "economic",
                            "base_allocation_basis": "mass",
                            "multiply_after": ["coproducts"],
                            "impacts": {
                                "TRACI 2.1": {
                                    "gwp": {
                                        "A1A2A3": {"qty": 1.23, "unit": "kgCO2e"},
                                        "A4": {"qty": 0.0, "unit": "kgCO2e"},
                                    }
                                }
                            },
                        }
                    }
                }
            }
        )

        ext = epd.get_ext(HarmonizationEpdExtension)
        self.assertIsInstance(ext, HarmonizationEpdExtension)
        self.assertIsNotNone(ext.coproducts)

        assert ext.coproducts is not None
        self.assertEqual(
            ext.coproducts.description,
            "Alternative burden sharing based on economic coproduct allocation.",
        )
        self.assertFalse(ext.coproducts.in_reported)
        self.assertTrue(ext.coproducts.harmonization_factors)
        self.assertEqual(ext.coproducts.allocation_basis, CoproductAllocationBasis.ECONOMIC)
        self.assertEqual(ext.coproducts.base_allocation_basis, CoproductAllocationBasis.MASS)
        self.assertEqual(ext.coproducts.multiply_after, ["coproducts"])
        self.assertEqual(ext.coproducts.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.qty, 1.23)
        self.assertEqual(ext.coproducts.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.unit, "kgCO2e")

        serialized = ext.coproducts.to_serializable(by_alias=True, exclude_none=True)
        self.assertEqual(serialized["allocation_basis"], "economic")
        self.assertEqual(serialized["base_allocation_basis"], "mass")
        self.assertEqual(serialized["impacts"]["TRACI 2.1"]["gwp"]["A1A2A3"]["qty"], 1.23)

    def test_coproducts_rejects_invalid_enum_values(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"coproducts": {"allocation_basis": "not-valid"}})

        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"coproducts": {"base_allocation_basis": "not-valid"}})

    def test_multiply_after_item_length_is_limited(self) -> None:
        with self.assertRaises(pyd.ValidationError) as context:
            HarmonizationEpdExtension.parse_obj(
                {
                    "eac": {
                        "harmonization_factors": True,
                        "multiply_after": ["x" * 201],
                    }
                }
            )

        errors = context.exception.errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["loc"], ("eac", "multiply_after", 0))
        self.assertEqual(
            errors[0]["msg"],
            "ensure this value has at most 200 characters",
        )
        self.assertEqual(errors[0]["type"], "value_error.any_str.max_length")

    def test_multiply_after_item_length_is_reflected_in_schema(self) -> None:
        schema = EacHarmonizationFactor.schema()

        self.assertEqual(schema["properties"]["multiply_after"]["maxItems"], 25)
        self.assertEqual(schema["properties"]["multiply_after"]["items"]["maxLength"], 200)

    def test_harmonization_extension_name(self) -> None:
        self.assertEqual(HarmonizationEpdExtension.get_extension_name(), "harmonization")

    def test_parse_eac_extension_from_epd(self) -> None:
        epd = Epd.parse_obj(
            {
                "ext": {
                    "harmonization": {
                        "eac": {
                            "description": "All electricity consumption at the Harford plant is covered by on-site solar or green-e RECs.",
                            "in_reported": True,
                            "harmonization_factors": True,
                            "EAC_standard": "Green-e REC",
                            "EAC_standard_version": "4.5",
                            "EAC_coverage": "Entire Facility",
                            "EAC_verification_link": "https://example.com/retirement-proof",
                            "multiply_after": ["coproducts"],
                            "impacts": {
                                "TRACI 2.1": {
                                    "gwp": {
                                        "A1A2A3": {"qty": 3.2, "unit": "kgCO2e"},
                                        "A4": {"qty": -0.1, "unit": "kgCO2e"},
                                    }
                                }
                            },
                            "resource_uses": {
                                "rpre": {
                                    "A1A2A3": {"qty": -2.0, "unit": "MJ"},
                                }
                            },
                            "output_flows": {
                                "hwd": {
                                    "A1A2A3": {"qty": -0.05, "unit": "kg"},
                                }
                            },
                        }
                    }
                }
            }
        )

        ext = epd.get_ext(HarmonizationEpdExtension)
        self.assertIsInstance(ext, HarmonizationEpdExtension)
        self.assertIsNotNone(ext.eac)

        assert ext.eac is not None
        self.assertEqual(
            ext.eac.description,
            "All electricity consumption at the Harford plant is covered by on-site solar or green-e RECs.",
        )
        self.assertTrue(ext.eac.in_reported)
        self.assertTrue(ext.eac.harmonization_factors)
        self.assertEqual(ext.eac.eac_standard, EacStandard.GREEN_E_REC)
        self.assertEqual(ext.eac.eac_standard_version, "4.5")
        self.assertEqual(ext.eac.eac_coverage, EacCoverage.ENTIRE_FACILITY)
        self.assertEqual(str(ext.eac.eac_verification_link), "https://example.com/retirement-proof")
        self.assertEqual(ext.eac.multiply_after, ["coproducts"])
        self.assertEqual(ext.eac.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.qty, 3.2)
        self.assertEqual(ext.eac.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.unit, "kgCO2e")
        self.assertEqual(ext.eac.impacts["TRACI 2.1"].__root__["gwp"].A4.qty, -0.1)
        self.assertEqual(ext.eac.resource_uses.__root__["rpre"].A1A2A3.qty, -2.0)
        self.assertEqual(ext.eac.resource_uses.__root__["rpre"].A1A2A3.unit, "MJ")
        self.assertEqual(ext.eac.output_flows.__root__["hwd"].A1A2A3.qty, -0.05)
        self.assertEqual(ext.eac.output_flows.__root__["hwd"].A1A2A3.unit, "kg")

        serialized = ext.eac.to_serializable(by_alias=True, exclude_none=True)
        self.assertEqual(serialized["EAC_standard"], "Green-e REC")
        self.assertEqual(serialized["EAC_standard_version"], "4.5")
        self.assertEqual(serialized["EAC_coverage"], "Entire Facility")
        self.assertEqual(serialized["EAC_verification_link"], "https://example.com/retirement-proof")
        self.assertEqual(serialized["impacts"]["TRACI 2.1"]["gwp"]["A1A2A3"]["qty"], 3.2)
        self.assertEqual(serialized["impacts"]["TRACI 2.1"]["gwp"]["A4"]["qty"], -0.1)
        self.assertEqual(serialized["resource_uses"]["rpre"]["A1A2A3"]["qty"], -2.0)
        self.assertEqual(serialized["resource_uses"]["rpre"]["A1A2A3"]["unit"], "MJ")
        self.assertEqual(serialized["output_flows"]["hwd"]["A1A2A3"]["qty"], -0.05)
        self.assertEqual(serialized["output_flows"]["hwd"]["A1A2A3"]["unit"], "kg")

    def test_eac_rejects_invalid_enum_values(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"eac": {"EAC_standard": "Not a valid standard"}})

        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"eac": {"EAC_coverage": "Not a valid coverage"}})

    def test_parse_mbvfa_extension_from_epd(self) -> None:
        epd = Epd.parse_obj(
            {
                "ext": {
                    "harmonization": {
                        "mbvfa": {
                            "description": "Book-and-claim recycled feedstock allocation for selected inputs.",
                            "in_reported": True,
                            "harmonization_factors": True,
                            "tracking_approach": "book-and-claim",
                            "attribute": "recycled-content",
                            "multiply_after": ["coproducts"],
                            "impacts": {
                                "TRACI 2.1": {
                                    "gwp": {
                                        "A1A2A3": {"qty": -1.23, "unit": "kgCO2e"},
                                        "A4": {"qty": 0.0, "unit": "kgCO2e"},
                                    }
                                }
                            },
                        }
                    }
                }
            }
        )

        ext = epd.get_ext(HarmonizationEpdExtension)
        self.assertIsInstance(ext, HarmonizationEpdExtension)
        self.assertIsNotNone(ext.mbvfa)

        assert ext.mbvfa is not None
        self.assertEqual(ext.mbvfa.description, "Book-and-claim recycled feedstock allocation for selected inputs.")
        self.assertTrue(ext.mbvfa.in_reported)
        self.assertTrue(ext.mbvfa.harmonization_factors)
        self.assertEqual(ext.mbvfa.tracking_approach, MbvfaTrackingApproach.BOOK_AND_CLAIM)
        self.assertEqual(ext.mbvfa.attribute, MbvfaAttribute.RECYCLED_CONTENT)
        self.assertEqual(ext.mbvfa.multiply_after, ["coproducts"])
        self.assertEqual(ext.mbvfa.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.qty, -1.23)
        self.assertEqual(ext.mbvfa.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.unit, "kgCO2e")

        serialized = ext.mbvfa.to_serializable(by_alias=True, exclude_none=True)
        self.assertEqual(serialized["tracking_approach"], "book-and-claim")
        self.assertEqual(serialized["attribute"], "recycled-content")
        self.assertEqual(serialized["impacts"]["TRACI 2.1"]["gwp"]["A1A2A3"]["qty"], -1.23)

    def test_mbvfa_rejects_invalid_enum_values(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"mbvfa": {"tracking_approach": "not-valid"}})

        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"mbvfa": {"attribute": "not-valid"}})

    def test_parse_offsets_extension_from_epd(self) -> None:
        epd = Epd.parse_obj(
            {
                "ext": {
                    "harmonization": {
                        "offsets": {
                            "description": "All electricity consumption at the Harford plant is covered by offsets.",
                            "in_reported": False,
                            "harmonization_factors": True,
                            "offset_standards": ["VCS", "Gold"],
                            "offset_standard_version": "4.5",
                            "offset_coverage": "Entire Facility",
                            "offset_verification_link": "https://example.com/offset-retirement-proof",
                            "multiply_after": ["coproducts"],
                            "impacts": {
                                "TRACI 2.1": {
                                    "gwp": {
                                        "A1A2A3": {"qty": -12.34, "unit": "kgCO2e"},
                                        "A4": {"qty": 0.0, "unit": "kgCO2e"},
                                    }
                                }
                            },
                        }
                    }
                }
            }
        )

        ext = epd.get_ext(HarmonizationEpdExtension)
        self.assertIsInstance(ext, HarmonizationEpdExtension)
        self.assertIsNotNone(ext.offsets)

        assert ext.offsets is not None
        self.assertEqual(
            ext.offsets.description,
            "All electricity consumption at the Harford plant is covered by offsets.",
        )
        self.assertFalse(ext.offsets.in_reported)
        self.assertTrue(ext.offsets.harmonization_factors)
        self.assertEqual(ext.offsets.offset_standards, [OffsetStandard.VCS, OffsetStandard.GOLD])
        self.assertEqual(ext.offsets.offset_standard_version, "4.5")
        self.assertEqual(ext.offsets.offset_coverage, OffsetCoverage.ENTIRE_FACILITY)
        self.assertEqual(str(ext.offsets.offset_verification_link), "https://example.com/offset-retirement-proof")
        self.assertEqual(ext.offsets.multiply_after, ["coproducts"])
        self.assertEqual(ext.offsets.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.qty, -12.34)
        self.assertEqual(ext.offsets.impacts["TRACI 2.1"].__root__["gwp"].A1A2A3.unit, "kgCO2e")

        serialized = ext.offsets.to_serializable(by_alias=True, exclude_none=True)
        self.assertEqual(serialized["offset_standards"], ["VCS", "Gold"])
        self.assertEqual(serialized["offset_standard_version"], "4.5")
        self.assertEqual(serialized["offset_coverage"], "Entire Facility")
        self.assertEqual(serialized["offset_verification_link"], "https://example.com/offset-retirement-proof")
        self.assertEqual(serialized["impacts"]["TRACI 2.1"]["gwp"]["A1A2A3"]["qty"], -12.34)

    def test_offsets_reject_invalid_enum_values(self) -> None:
        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"offsets": {"offset_standards": ["Not a valid standard"]}})

        with self.assertRaises(pyd.ValidationError):
            HarmonizationEpdExtension.parse_obj({"offsets": {"offset_coverage": "Not a valid coverage"}})

    def test_custom_factor_extra_is_allowed_and_typed(self) -> None:
        ext = HarmonizationEpdExtension.parse_obj(
            {
                "eac": {"harmonization_factors": False},
                "biochar": {
                    "name": "Biochar sequestration accounting",
                    "description": "Custom non-standard accounting factor.",
                    "harmonization_factors": True,
                    "in_reported": True,
                    "multiply_after": ["coproducts"],
                    "internal_method": "v1",
                },
            }
        )

        self.assertIn("biochar", ext.__dict__)
        self.assertIsInstance(ext.__dict__["biochar"], CustomHarmonizationFactor)
        custom_factor = ext.__dict__["biochar"]
        self.assertEqual(custom_factor.name, "Biochar sequestration accounting")
        self.assertEqual(custom_factor.multiply_after, ["coproducts"])
        self.assertEqual(custom_factor.__dict__["internal_method"], "v1")

    def test_custom_factor_extra_accepts_preparsed_model(self) -> None:
        custom_factor = CustomHarmonizationFactor(
            name="Biochar sequestration accounting",
            description="Custom non-standard accounting factor.",
            harmonization_factors=True,
            in_reported=True,
            multiply_after=["coproducts"],
            internal_method="v1",
        )

        ext = HarmonizationEpdExtension(biochar=custom_factor)

        self.assertIn("biochar", ext.__dict__)
        self.assertIs(ext.__dict__["biochar"], custom_factor)
        self.assertEqual(ext.__dict__["biochar"].name, "Biochar sequestration accounting")
        self.assertEqual(ext.__dict__["biochar"].multiply_after, ["coproducts"])
        self.assertEqual(ext.__dict__["biochar"].__dict__["internal_method"], "v1")

    def test_custom_factor_extra_not_typed_for_non_object_payload(self) -> None:
        with self.assertRaises(pyd.ValidationError) as context:
            HarmonizationEpdExtension.parse_obj(
                {
                    "eac": {"harmonization_factors": False},
                    "biochar": "not-an-object",
                }
            )

        errors = context.exception.errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["loc"], ("__root__", "biochar"))
        self.assertEqual(errors[0]["msg"], "must be an object payload compatible with CustomHarmonizationFactor")
        self.assertEqual(errors[0]["type"], "value_error")

    def test_custom_factor_missing_required_name_raises_validation_error(self) -> None:
        with self.assertRaises(pyd.ValidationError) as context:
            HarmonizationEpdExtension.parse_obj(
                {
                    "eac": {"harmonization_factors": False},
                    "biochar": {
                        "description": "Custom factor without required name.",
                        "harmonization_factors": True,
                    },
                }
            )

        errors = context.exception.errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["loc"], ("__root__", "biochar", "name"))
        self.assertEqual(errors[0]["msg"], "field required")
        self.assertEqual(errors[0]["type"], "value_error.missing")

    def test_custom_factor_count_is_limited(self) -> None:
        allowed_payload = {
            f"custom_{idx}": {"name": f"Factor {idx}", "harmonization_factors": True}
            for idx in range(HarmonizationEpdExtension.MAX_CUSTOM_FACTORS)
        }

        ext = HarmonizationEpdExtension.parse_obj(allowed_payload)
        for idx in range(HarmonizationEpdExtension.MAX_CUSTOM_FACTORS):
            self.assertIsInstance(ext.__dict__[f"custom_{idx}"], CustomHarmonizationFactor)

        too_many_payload = dict(allowed_payload)
        too_many_payload["custom_overflow"] = {"name": "Overflow factor", "harmonization_factors": True}

        with self.assertRaises(pyd.ValidationError) as context:
            HarmonizationEpdExtension.parse_obj(too_many_payload)

        errors = context.exception.errors()
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["loc"], ("__root__",))
        self.assertEqual(
            errors[0]["msg"],
            f"at most {HarmonizationEpdExtension.MAX_CUSTOM_FACTORS} custom harmonization factors are allowed",
        )
        self.assertEqual(errors[0]["type"], "value_error")
