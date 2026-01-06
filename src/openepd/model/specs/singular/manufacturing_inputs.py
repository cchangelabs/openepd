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
import pydantic

from openepd.model.category import CategoryMeta
from openepd.model.common import Amount
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
    _CATEGORY_META = CategoryMeta(
        unique_name="Cement",
        display_name="Cement",
        alt_names=["Ciment", "OPC", "Zement", "Blended Cement", "PLC"],
        historical_names=["Manufacturing Inputs >> Cementitious >> Cement"],
        description="Cements, including Portland and blended cements, that can serve as the primary binder in a concrete mix.",
        declared_unit=Amount(qty=1, unit="t"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="MasonryCement",
        display_name="Masonry Cement",
        historical_names=["Manufacturing Inputs >> Cementitious >> Masonry Cement"],
        description="A cementitious product typically composed of Portland cement and hydrated lime. Masonry cement is combined with sand to make mortar",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    astm_c91_type: MasonryCementAstmC91Type | None = pydantic.Field(default=None, description="", examples=["Type N"])


class SupplementaryCementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious materials that are not effective binders when used on their own."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="SupplementaryCementitiousMaterials",
        display_name="Supplementary Cementitious Materials",
        short_name="SCM",
        historical_names=["Manufacturing Inputs >> Cementitious >> SCM"],
        description="Cementitious materials that are not effective binders when used on their own.",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    cement_scm: list[CementScm] | None = pydantic.Field(default=None, description="", examples=[["ggbs"]])


class AccessFlooringPedestalsV1(BaseOpenEpdHierarchicalSpec):
    """
    Part of an access floor system.

    Pedestals are laid out on top of a floor slab and support access floor panels, creating a void space between the
    floor slab and finish floor.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AccessFlooringPedestals",
        display_name="Access Flooring Pedestals",
        short_name="Pedestals",
        historical_names=["Manufacturing Inputs >> Pedestals"],
        description="Part of an access floor system. Pedestals are laid out on top of a floor slab and support access floor panels, creating a void space between the floor slab and finish floor.",
        masterformat="09 69 00 Access Flooring",
        declared_unit=Amount(qty=1, unit="kg"),
    )


class CarpetBackingV1(BaseOpenEpdHierarchicalSpec):
    """Fabric backing holding a carpet together."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CarpetBacking",
        display_name="Carpet Backing",
        historical_names=["Manufacturing Inputs >> Carpet Backing"],
        description="Fabric backing holding a carpet together",
        declared_unit=Amount(qty=1, unit="t"),
    )


class CarpetFiberV1(BaseOpenEpdHierarchicalSpec):
    """Fiber yarn used in the manufacture of carpet, typically nylon or wool."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CarpetFiber",
        display_name="Carpet Fiber",
        alt_names=["Carpet Yarn"],
        historical_names=["Manufacturing Inputs >> Carpet Fiber"],
        description="Fiber yarn used in the manufacture of carpet, typically nylon or wool",
        declared_unit=Amount(qty=1, unit="t"),
    )

    # Own fields:
    yarn_material: CarpetYarnType | None = pydantic.Field(default=None, description="", examples=["Nylon 6,6"])
    yarn_recycled_content: float | None = pydantic.Field(default=None, description="", examples=[2.3])


class CementitiousMaterialsV1(BaseOpenEpdHierarchicalSpec):
    """Cementitious materials performance specification."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="CementitiousMaterials",
        display_name="Cementitious Materials",
        short_name="Cementitious",
        historical_names=["Manufacturing Inputs >> Cementitious"],
        description="General category for cements and cement components.",
        declared_unit=Amount(qty=1, unit="t"),
    )

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
    _CATEGORY_META = CategoryMeta(
        unique_name="ConcreteAdmixtures",
        display_name="Concrete Admixtures",
        short_name="Admixtures",
        historical_names=["Manufacturing Inputs >> Admixtures"],
        description="Concrete admixtures are chemical additives that are added to fresh concrete immediately before or during mixing. Admixtures have distinct functions and are categorized as: air-entraining, water-reducing, retarding, accelerating, and plasticizers (i.e., superplasticizers)",
        masterformat="03 05 00.03 Concrete Admixtures",
        declared_unit=Amount(qty=1, unit="kg"),
    )

    # Own fields:
    effects: list[AdmixtureEffects] | None = pydantic.Field(default=None, description="", examples=[["Air Entrainer"]])


class TextilesV1(BaseOpenEpdHierarchicalSpec):
    """Textiles for use in manufacturing end products."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="Textiles",
        display_name="Textiles",
        alt_names=["Cloth", "Fabric", "Leather", "Textile"],
        historical_names=["Manufacturing Inputs >> Textiles"],
        description="Textiles for use in manufacturing end products.",
        declared_unit=Amount(qty=1, unit="m^2"),
    )

    # Own fields:
    fabric_type: list[TextilesFabricType] | None = pydantic.Field(default=None, description="", examples=[["Leather"]])


class AccessFlooringPanelsV1(BaseOpenEpdHierarchicalSpec, AccessFlooringMixin):
    """
    Part of an access floor system.

    Panels are laid on top of an access floor pedestal, creating a finish floor.
    """

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AccessFlooringPanels",
        display_name="Access Floor Panels",
        short_name="Panels",
        historical_names=["Manufacturing Inputs >> Panels"],
        description="Part of an access floor system. Panels are laid on top of an access floor pedestal, creating a finish floor.",
        masterformat="09 69 00 Access Flooring",
        declared_unit=Amount(qty=1, unit="m^2"),
    )


class AsphaltInputsV1(BaseOpenEpdHierarchicalSpec):
    """Binders, additives, and other non-aggregate-like ingredients for asphalt."""

    _EXT_VERSION = "1.0"
    _CATEGORY_META = CategoryMeta(
        unique_name="AsphaltInputs",
        display_name="Asphalt Binders & Additives",
        short_name="Asphalt Inputs",
        historical_names=["Manufacturing Inputs >> Asphalt Inputs"],
        description="Binders, additives, and other non-aggregate-like ingredients for asphalt",
        declared_unit=Amount(qty=1, unit="t"),
    )


class ManufacturingInputsV1(BaseOpenEpdHierarchicalSpec):
    """
    Manufacturing inputs.

    Broad category for collecting materials primarily used as manufacturing inputs, rather than directly used in
    construction.
    """

    _EXT_VERSION = "1.2"
    _CATEGORY_META = CategoryMeta(
        unique_name="ManufacturingInputs",
        display_name="Manufacturing Inputs",
        description="Broad category for collecting materials primarily used as manufacturing inputs, rather than directly used in a construction.",
    )

    # Nested specs:
    AccessFlooringPedestals: AccessFlooringPedestalsV1 | None = None
    CarpetBacking: CarpetBackingV1 | None = None
    CarpetFiber: CarpetFiberV1 | None = None
    CementitiousMaterials: CementitiousMaterialsV1 | None = None
    ConcreteAdmixtures: ConcreteAdmixturesV1 | None = None
    Textiles: TextilesV1 | None = None
    AccessFlooringPanels: AccessFlooringPanelsV1 | None = None
    AsphaltInputs: AsphaltInputsV1 | None = None
