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
import ast
from collections import ChainMap, defaultdict
from enum import Enum
import importlib
import inspect
import os
import pkgutil
import re
from types import GenericAlias, NoneType, UnionType
import typing
from typing import _GenericAlias

import click
import jinja2

from openepd.model.common import RangeAmount, RangeFloat, RangeInt, RangeRatioFloat
from openepd.model.specs.base import BaseOpenEpdHierarchicalSpec, CodegenSpec
from openepd.model.validation.numbers import RatioFloat
from openepd.model.validation.quantity import SUPPORTED_RANGES_BY_UNIT, QuantityStr

skip_fields = ("ext", "ext_version")
skip_classes = ("BaseOpenEpdHierarchicalSpec",)
skip_import_prefixes = (
    "openepd.model.specs.singular",
    "openepd.model.specs.enums",
    "openepd.model.validation.quantity",
    "openepd.model.specs.base",
    "openepd.model.base",
    "openepd.model.common",
    "openepd.validation.numbers",
)


def __range_spec_class_name_from_spec_name(spec_name: str) -> str:
    class_name_match = re.match(r"^(\w+)(V\d+)$", spec_name)
    if not class_name_match:
        # case for special objects like top-level Specs which does not have a versioning scheme
        return f"{spec_name}Range"
    return f"{class_name_match.group(1)}Range{class_name_match.group(2)}"


def filter__format_multiline_comment(v: str | None) -> str:
    if v is None:
        return ""
    if not v.startswith("\n"):
        return f"\n    {v}\n"
    return v


def __all_annotations(cls) -> ChainMap:
    """Returns a dictionary-like ChainMap that includes annotations for all
    attributes defined in cls or inherited from superclasses."""
    return ChainMap(*(c.__annotations__ for c in cls.__mro__ if "__annotations__" in c.__dict__))


def __get_absolute_import_path(cls: type | GenericAlias, import_collector: dict[str, set[str]]) -> str:
    module_name = cls.__module__
    module = importlib.import_module(module_name)
    import_collector[module.__name__].add(cls.__name__)

    if isinstance(cls, _GenericAlias):
        return str(cls).split(".")[-1]

    return cls.__name__


def __quantity_str_type_to_range_type(t: type[QuantityStr]) -> type[RangeAmount]:
    """Get the range type corresponding to a given unit."""
    return SUPPORTED_RANGES_BY_UNIT.get(str(t.unit), RangeAmount)


def __resolve_field_type(cls: type, field_name: str, import_collector: dict[str, set[str]]) -> str:
    type_from_hints = typing.get_type_hints(cls)[field_name]
    type_from_annotations = __all_annotations(cls)[field_name]

    # shorthand - if overridden from the above
    if typing.get_origin(type_from_annotations) is typing.Annotated:
        type_parameters = typing.get_args(type_from_annotations)[1:]
        for p in type_parameters:
            if isinstance(p, CodegenSpec):
                override_type = p.override_type
                return f"{__get_absolute_import_path(override_type, import_collector)} | None"

    # special matching required for Optional[] cases
    if typing.get_origin(type_from_hints) in (UnionType, typing.Union) and type(None) in typing.get_args(
        type_from_hints
    ):
        # in spec, everything should be nullable, so we strip the 'nullability' part of the union
        union_members = [a for a in typing.get_args(type_from_hints) if a is not NoneType]

        if len(union_members) != 1:
            print(f"Unexpected union type, passing as is {type_from_hints}")
            return str(type_from_hints)

        # unpack generics
        maybe_generic = union_members[0]
        if isinstance(maybe_generic, GenericAlias):
            real_type = typing.get_origin(maybe_generic)
        else:
            real_type = maybe_generic

        match real_type:
            case type() as t if issubclass(t, BaseOpenEpdHierarchicalSpec):
                range_spec_class_name = __range_spec_class_name_from_spec_name(t.__name__)
                if cls.__module__ != t.__module__:
                    # foreign spec, import required
                    relative_module_last = t.__module__.split(".")[-1]
                    import_collector[f".{relative_module_last}"].add(range_spec_class_name)
                return f"{range_spec_class_name} | None"
            case type() as t if issubclass(t, RatioFloat):
                return f"{__get_absolute_import_path(RangeRatioFloat, import_collector)} | None"
            case type() as t if issubclass(t, float):
                return f"{__get_absolute_import_path(RangeFloat, import_collector)} | None"
            case type() as t if issubclass(t, bool):
                return "bool | None"
            case type() as t if issubclass(t, int):
                return f"{__get_absolute_import_path(RangeInt, import_collector)} | None"
            case type() as t if issubclass(t, QuantityStr):
                return f"{__get_absolute_import_path(__quantity_str_type_to_range_type(t), import_collector)} | None"
            case type() as t if issubclass(t, Enum):
                return f"list[{__get_absolute_import_path(t, import_collector)}] | None"
            case type() as t if issubclass(t, str):
                return "str | None"
            case type() as t if issubclass(t, list):
                list_typing_args = typing.get_args(maybe_generic)
                if not list_typing_args:
                    return "list | None"
                return f"list[{__get_absolute_import_path(list_typing_args[0], import_collector)}] | None"
            case _:
                return f"{__get_absolute_import_path(maybe_generic, import_collector)} | None"

    return type_from_hints


@click.command
@click.argument("specs_source_package")
@click.argument("output_folder")
def generate_range_spec_models(specs_source_package: str, output_folder=None) -> None:
    """
    Generate material extension models (specs) for GenericEstimates and IndustryEPDs.

    EPDs have material specifications attached. For EPDs themselves,these specifications often contain singular value -
    for example, strength_28d=4000psi, fabrication=CLT etc. Generic and average datasets however are based on a range
    of products or some market segment. To match these datasets, ranges are requried in some case, e.g. strength_28d =
    4000 to 5000 psi.

    Not all the properties of normal EPD are converted to ranges however, for example b1_recarbonation for CMU is never
    a range.

    This script generates the range spec models from normal spec models using rules and the code generation specifications
    embedded into spec typings which handle special cases and exceptions.

    Rules:
    1. Quantity -> Range of Quantities
    2. Enum value -> list of Enum values.
    3. Float -> range of Floats.

    We are accessing the source module (norma performance parameter spec) via 2 interfaces at the same time:
    1. AST - gives us code-evel access, retains ordering, etc.
    2. Inspect - gets the actual derived types.
    """
    package = importlib.import_module(specs_source_package)
    try:
        os.mkdir(output_folder)
    except FileExistsError:
        ...

    for importer, module_name, ispkg in [
        *pkgutil.iter_modules(package.__path__),
        (None, "__init__", False),
    ]:
        if ispkg:
            continue

        # module which might contain specs
        module = importlib.import_module(f"{specs_source_package}.{module_name}")

        spec_classes = {}
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseOpenEpdHierarchicalSpec):
                spec_classes[name] = obj

        # no spec classes found; skip to next
        if not spec_classes:
            continue

        # Parse the module's source code into an AST
        with open(module.__file__, "r") as f:
            tree = ast.parse(f.read())

        #  module -> [symbol1, ...] structure. Results in from module import symobol1, ...
        #  If no symbols, direct import will be used (import xxx)
        import_collector: dict[str, set[str]] = defaultdict(set)
        import_collector["openepd.model.specs.base"].add("BaseOpenEpdHierarchicalSpec")

        # save the ordering of the class defs:
        ast_class_defs: dict[str, dict[str, str]] = {}
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                field_declarations = {}
                for n in node.body:
                    if isinstance(n, ast.AnnAssign):
                        field_init_expression = n.value
                        if isinstance(field_init_expression, ast.Call):
                            # assuming this is a rvalue of f =pydantic.Field(default=..., examples=[...])
                            field_init_expression.keywords = [
                                kw for kw in field_init_expression.keywords if kw.arg not in ("example", "ge", "le")
                            ]

                        field_declarations[ast.unparse(n.target)] = ast.unparse(field_init_expression)
                ast_class_defs[node.name] = field_declarations

        include_pydantic_compat_import = False
        class_definitions = []
        for class_name, ast_class_def in ast_class_defs.items():
            if class_name in skip_classes:
                continue
            if not (cls := spec_classes.get(class_name)):
                continue

            class_definition = {}
            class_definitions.append(class_definition)

            class_definition["classname"] = __range_spec_class_name_from_spec_name(class_name)
            class_definition["class"] = cls
            fields = []
            class_definition["fields"] = fields
            for field_name, field in cls.__fields__.items():
                if field_name in skip_fields:
                    continue

                field_init = ast_class_def.get(field_name)
                fields.append(
                    {
                        "name": field_name,
                        "type": __resolve_field_type(cls, field_name, import_collector),
                        "field_init": field_init,
                    }
                )

                if field_init and "pyd" in field_init:
                    import_collector["openepd.compat.pydantic"].add("pyd")

        context = {
            "imports": import_collector,
            "include_pydantic_compat_import": include_pydantic_compat_import,
            "range_specs": class_definitions,
        }

        environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
        environment.filters["format_multiline_comment"] = filter__format_multiline_comment
        template = environment.get_template("range_spec.py.tpl")
        with open(os.path.join(output_folder, f"{module_name}.py"), mode="w") as f_out:
            f_out.write(template.render(**context))


if __name__ == "__main__":
    generate_range_spec_models()
