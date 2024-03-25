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
from openepd.compat.pydantic import pyd
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec

from .enums import *

UnknownStrTypeHandleMe = str


class CementV1(BaseOpenEpdHierarchicalSpec):
    """Cement performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cementitious: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueValidatedJSONProperty"
    )
    white_cement: bool | None = pyd.Field(default=None, description="", example="True")
    astm_type: CementAstmType | None = pyd.Field(default=None, description="", example="C150 Type I")
    c1157: list[C1157] | None = pyd.Field(default=None, description="", example="['GU']")
    csa_a3001: list[CsaA3001] | None = pyd.Field(default=None, description="", example="['A3001 GU']")
    en197_1: CementEn197_1 | None = pyd.Field(default=None, description="", example="CEM I")
    oil_well_cement: bool | None = pyd.Field(default=None, description="", example="True")


class MasonryCementV1(BaseOpenEpdHierarchicalSpec):
    """Masonry cement performance specification."""

    _EXT_VERSION = "1.0"
    """Concretes that are mixed just before use, and then poured on-site into forms"""

    # Own fields:
    masonry_cement_astm_c91_type: MasonryCementAstmC91Type | None = pyd.Field(
        default=None, description="", example="Type N"
    )


class SupplementaryCementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Supplementary cementitious materials performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cement_scm: list[CementScm] | None = pyd.Field(default=None, description="", example="['ggbs']")


class AccessFlooringPedestalsV1(BaseOpenEpdHierarchicalSpec):
    """Access flooring pedestals performance specification."""

    _EXT_VERSION = "1.0"

    pass


class CarpetBackingV1(BaseOpenEpdHierarchicalSpec):
    """Carpet backing performance specification."""

    _EXT_VERSION = "1.0"
    """Fabric backing holding a carpet together"""

    # Own fields:
    rel_carpet: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipFrom"
    )


class CarpetFiberV1(BaseOpenEpdHierarchicalSpec):
    """Carpet fiber performance specification."""

    _EXT_VERSION = "1.0"
    """Fiber yarn used in the manufacture of carpet, typically nylon or wool"""

    # Own fields:
    yarn_material: CarpetYarnType | None = pyd.Field(default=None, description="", example="Nylon 6,6")
    yarn_recycled_content: float | None = pyd.Field(default=None, description="", example="2.3")
    rel_carpet: UnknownStrTypeHandleMe | None = pyd.Field(
        default=None, description="", example="test_valueRelationshipFrom"
    )


class CementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious materials performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Cement: CementV1 | None = None
    MasonryCement: MasonryCementV1 | None = None
    SupplementaryCementitiousMaterials: SupplementaryCementitiousMaterialsV1 | None = None


class ConcreteAdmixturesV1(BaseOpenEpdHierarchicalSpec):
    """Concrete admixtures performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    admixture_effects: list[AdmixtureEffects] | None = pyd.Field(
        default=None, description="", example="['Air Entrainer']"
    )


class TextilesV1(BaseOpenEpdHierarchicalSpec):
    """Textiles performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    textiles_fabric_type: list[TextilesFabricType] | None = pyd.Field(
        default=None, description="", example="['Leather']"
    )


class ManufacturingInputsV1(BaseOpenEpdHierarchicalSpec):
    """Manufacturing inputs performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    AccessFlooringPedestals: AccessFlooringPedestalsV1 | None = None
    CarpetBacking: CarpetBackingV1 | None = None
    CarpetFiber: CarpetFiberV1 | None = None
    CementitiousMaterials: CementitiousMaterialsV1 | None = None
    ConcreteAdmixtures: ConcreteAdmixturesV1 | None = None
    Textiles: TextilesV1 | None = None
