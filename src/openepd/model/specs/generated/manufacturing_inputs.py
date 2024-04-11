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
from openepd.model.specs.concrete import Cementitious
from openepd.model.specs.generated.enums import (
    AdmixtureEffects,
    CarpetYarnType,
    CementAstmType,
    CementC1157,
    CementCsaA3001,
    CementEn197_1,
    CementScm,
    MasonryCementAstmC91Type,
    TextilesFabricType,
)


class CementV1(BaseOpenEpdHierarchicalSpec):
    """Cement performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cementitious: Cementitious | None = pyd.Field(default=None, description="")
    white_cement: bool | None = pyd.Field(default=None, description="", example=True)
    astm_type: CementAstmType | None = pyd.Field(default=None, description="", example="C150 Type I")
    c1157: list[CementC1157] | None = pyd.Field(default=None, description="", example=["GU"])
    csa_a3001: list[CementCsaA3001] | None = pyd.Field(default=None, description="", example=["A3001 GU"])
    en197_1: CementEn197_1 | None = pyd.Field(default=None, description="", example="CEM I")
    oil_well_cement: bool | None = pyd.Field(default=None, description="", example=True)


class MasonryCementV1(BaseOpenEpdHierarchicalSpec):
    """Masonry cement performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    astm_c91_type: MasonryCementAstmC91Type | None = pyd.Field(default=None, description="", example="Type N")


class SupplementaryCementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Supplementary cementitious materials performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cement_scm: list[CementScm] | None = pyd.Field(default=None, description="", example=["ggbs"])


class AccessFlooringPedestalsV1(BaseOpenEpdHierarchicalSpec):
    """Access flooring pedestals performance specification."""

    _EXT_VERSION = "1.0"


class CarpetBackingV1(BaseOpenEpdHierarchicalSpec):
    """Fabric backing holding a carpet together."""

    _EXT_VERSION = "1.0"


class CarpetFiberV1(BaseOpenEpdHierarchicalSpec):
    """Fiber yarn used in the manufacture of carpet, typically nylon or wool."""

    _EXT_VERSION = "1.0"

    # Own fields:
    yarn_material: CarpetYarnType | None = pyd.Field(default=None, description="", example="Nylon 6,6")
    yarn_recycled_content: float | None = pyd.Field(default=None, description="", example=2.3)


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
    effects: list[AdmixtureEffects] | None = pyd.Field(default=None, description="", example=["Air Entrainer"])


class TextilesV1(BaseOpenEpdHierarchicalSpec):
    """Textiles performance specification."""

    _EXT_VERSION = "1.0"

    # Own fields:
    fabric_type: list[TextilesFabricType] | None = pyd.Field(default=None, description="", example=["Leather"])


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
