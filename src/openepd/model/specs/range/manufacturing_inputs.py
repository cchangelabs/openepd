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
__all__ = (
    "AccessFlooringPedestalsRangeV1",
    "CarpetBackingRangeV1",
    "CarpetFiberRangeV1",
    "CementRangeV1",
    "CementitiousMaterialsRangeV1",
    "ConcreteAdmixturesRangeV1",
    "ManufacturingInputsRangeV1",
    "MasonryCementRangeV1",
    "SupplementaryCementitiousMaterialsRangeV1",
    "TextilesRangeV1",
)


from openepd.compat.pydantic import pyd
from openepd.model.common import RangeFloat
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
from openepd.model.specs.range.mixins.access_flooring_mixin import AccessFlooringRangeMixin


class CementRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cements.

    Includes Portland and blended cements, that can serve as the primary binder in a concrete mix.

    Range version.
    """

    _EXT_VERSION = "1.0"

    cementitious: Cementitious | None = pyd.Field(default=None, description="")
    white_cement: bool | None = pyd.Field(default=None, description="")
    astm_type: list[CementAstmType] | None = pyd.Field(default=None, description="")
    c1157: list[CementC1157] | None = pyd.Field(default=None, description="")
    csa_a3001: list[CementCsaA3001] | None = pyd.Field(default=None, description="")
    en197_1: list[CementEn197_1] | None = pyd.Field(default=None, description="")
    oil_well_cement: bool | None = pyd.Field(default=None, description="")


class MasonryCementRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    A cementitious product typically composed of Portland cement and hydrated lime.

    Masonry cement is combined with sand to make mortar.

    Range version.
    """

    _EXT_VERSION = "1.0"

    astm_c91_type: list[MasonryCementAstmC91Type] | None = pyd.Field(default=None, description="")


class SupplementaryCementitiousMaterialsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious materials that are not effective binders when used on their own.

    Range version.
    """

    _EXT_VERSION = "1.0"

    cement_scm: list[CementScm] | None = pyd.Field(default=None, description="")


class AccessFlooringPedestalsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Part of an access floor system.

    Pedestals are laid out on top of a floor slab and support access floor panels, creating a void space between the
    floor slab and finish floor.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CarpetBackingRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fabric backing holding a carpet together.

    Range version.
    """

    _EXT_VERSION = "1.0"


class CarpetFiberRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Fiber yarn used in the manufacture of carpet, typically nylon or wool.

    Range version.
    """

    _EXT_VERSION = "1.0"

    yarn_material: list[CarpetYarnType] | None = pyd.Field(default=None, description="")
    yarn_recycled_content: RangeFloat | None = pyd.Field(default=None, description="")


class CementitiousMaterialsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Cementitious materials performance specification.

    Range version.
    """

    _EXT_VERSION = "1.0"

    Cement: CementRangeV1 | None = None
    MasonryCement: MasonryCementRangeV1 | None = None
    SupplementaryCementitiousMaterials: SupplementaryCementitiousMaterialsRangeV1 | None = None


class ConcreteAdmixturesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Concrete admixtures.

    Chemical additives that are added to fresh concrete immediately before or during mixing. Admixtures have distinct
    functions and are categorized as: air-entraining, water-reducing, retarding, accelerating, and plasticizers
    (i.e., superplasticizers).

    Range version.
    """

    _EXT_VERSION = "1.0"

    effects: list[AdmixtureEffects] | None = pyd.Field(default=None, description="")


class TextilesRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Textiles for use in manufacturing end products.

    Range version.
    """

    _EXT_VERSION = "1.0"

    fabric_type: list[TextilesFabricType] | None = pyd.Field(default=None, description="")


class AccessFlooringPanelsRangeV1(BaseOpenEpdHierarchicalSpec, AccessFlooringRangeMixin):
    """
    Part of an access floor system.

    Panels are laid on top of an access floor pedestal, creating a finish floor.
    """

    _EXT_VERSION = "1.0"


class AsphaltInputsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Binders, additives, and other non-aggregate-like ingredients for asphalt.

    Range version.
    """

    _EXT_VERSION = "1.0"


class ManufacturingInputsRangeV1(BaseOpenEpdHierarchicalSpec):
    """
    Manufacturing inputs.

    Broad category for collecting materials primarily used as manufacturing inputs, rather than directly used in
    construction.

    Range version.
    """

    _EXT_VERSION = "1.2"

    AccessFlooringPedestals: AccessFlooringPedestalsRangeV1 | None = None
    CarpetBacking: CarpetBackingRangeV1 | None = None
    CarpetFiber: CarpetFiberRangeV1 | None = None
    CementitiousMaterials: CementitiousMaterialsRangeV1 | None = None
    ConcreteAdmixtures: ConcreteAdmixturesRangeV1 | None = None
    Textiles: TextilesRangeV1 | None = None
    AccessFlooringPanels: AccessFlooringPanelsRangeV1 | None = None
    AsphaltInputs: AsphaltInputsRangeV1 | None = None
