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
import pydantic

from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec
from openepd.model.specs.concrete import Cementitious
from openepd.model.specs.enums import (
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
from openepd.model.specs.singular.mixins.access_flooring_mixin import AccessFlooringMixin


class CementV1(BaseOpenEpdHierarchicalSpec):
    """
    Cements.

    Includes Portland and blended cements, that can serve as the primary binder in a concrete mix.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    cementitious: Cementitious | None = pydantic.Field(default=None, description="")
    white_cement: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )
    astm_type: CementAstmType | None = pydantic.Field(default=None, description="", examples=["C150 Type I"])
    c1157: list[CementC1157] | None = pydantic.Field(default=None, description="", examples=[["GU"]])
    csa_a3001: list[CementCsaA3001] | None = pydantic.Field(default=None, description="", examples=[["A3001 GU"]])
    en197_1: CementEn197_1 | None = pydantic.Field(default=None, description="", examples=["CEM I"])
    oil_well_cement: bool | None = pydantic.Field(
        default=None,
        description="",
        examples=[True],
    )


class MasonryCementV1(BaseOpenEpdHierarchicalSpec):
    """
    A cementitious product typically composed of Portland cement and hydrated lime.

    Masonry cement is combined with sand to make mortar.
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    astm_c91_type: MasonryCementAstmC91Type | None = pydantic.Field(default=None, description="", examples=["Type N"])


class SupplementaryCementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious materials that are not effective binders when used on their own."""

    _EXT_VERSION = "1.0"

    # Own fields:
    cement_scm: list[CementScm] | None = pydantic.Field(default=None, description="", examples=[["ggbs"]])


class AccessFlooringPedestalsV1(BaseOpenEpdHierarchicalSpec):
    """
    Part of an access floor system.

    Pedestals are laid out on top of a floor slab and support access floor panels, creating a void space between the
    floor slab and finish floor.
    """

    _EXT_VERSION = "1.0"


class CarpetBackingV1(BaseOpenEpdHierarchicalSpec):
    """Fabric backing holding a carpet together."""

    _EXT_VERSION = "1.0"


class CarpetFiberV1(BaseOpenEpdHierarchicalSpec):
    """Fiber yarn used in the manufacture of carpet, typically nylon or wool."""

    _EXT_VERSION = "1.0"

    # Own fields:
    yarn_material: CarpetYarnType | None = pydantic.Field(default=None, description="", examples=["Nylon 6,6"])
    yarn_recycled_content: float | None = pydantic.Field(default=None, description="", examples=[2.3])


class CementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious materials performance specification."""

    _EXT_VERSION = "1.0"

    # Nested specs:
    Cement: CementV1 | None = None
    MasonryCement: MasonryCementV1 | None = None
    SupplementaryCementitiousMaterials: SupplementaryCementitiousMaterialsV1 | None = None


class ConcreteAdmixturesV1(BaseOpenEpdHierarchicalSpec):
    """
    Concrete admixtures.

    Chemical additives that are added to fresh concrete immediately before or during mixing. Admixtures have distinct
    functions and are categorized as: air-entraining, water-reducing, retarding, accelerating, and plasticizers
    (i.e., superplasticizers).
    """

    _EXT_VERSION = "1.0"

    # Own fields:
    effects: list[AdmixtureEffects] | None = pydantic.Field(default=None, description="", examples=[["Air Entrainer"]])


class TextilesV1(BaseOpenEpdHierarchicalSpec):
    """Textiles for use in manufacturing end products."""

    _EXT_VERSION = "1.0"

    # Own fields:
    fabric_type: list[TextilesFabricType] | None = pydantic.Field(default=None, description="", examples=[["Leather"]])


class AccessFlooringPanelsV1(BaseOpenEpdHierarchicalSpec, AccessFlooringMixin):
    """
    Part of an access floor system.

    Panels are laid on top of an access floor pedestal, creating a finish floor.
    """

    _EXT_VERSION = "1.0"


class AsphaltInputsV1(BaseOpenEpdHierarchicalSpec):
    """Binders, additives, and other non-aggregate-like ingredients for asphalt."""

    _EXT_VERSION = "1.0"


class ManufacturingInputsV1(BaseOpenEpdHierarchicalSpec):
    """
    Manufacturing inputs.

    Broad category for collecting materials primarily used as manufacturing inputs, rather than directly used in
    construction.
    """

    _EXT_VERSION = "1.2"

    # Nested specs:
    AccessFlooringPedestals: AccessFlooringPedestalsV1 | None = None
    CarpetBacking: CarpetBackingV1 | None = None
    CarpetFiber: CarpetFiberV1 | None = None
    CementitiousMaterials: CementitiousMaterialsV1 | None = None
    ConcreteAdmixtures: ConcreteAdmixturesV1 | None = None
    Textiles: TextilesV1 | None = None
    AccessFlooringPanels: AccessFlooringPanelsV1 | None = None
    AsphaltInputs: AsphaltInputsV1 | None = None
