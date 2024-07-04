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

from collections.abc import Callable

from mypy.nodes import AssignmentStmt, CallExpr, MemberExpr, TypeInfo
from mypy.plugin import ClassDefContext
import pydantic.mypy
from pydantic.mypy import (
    MODEL_METACLASS_FULLNAME,
    ModelConfigData,
    PydanticModelClassVar,
    PydanticModelField,
    PydanticModelTransformer,
    PydanticPlugin,
)

# Using this plugin fixes the issue.

CUSTOM_OPENEPD_MODEL_METACLASS_FULLNAME = "openepd.model.base.PydanticClassAttributeExposeModelMetaclass"
MODEL_METACLASSES_FULL_NAMES = (MODEL_METACLASS_FULLNAME, CUSTOM_OPENEPD_MODEL_METACLASS_FULLNAME)

DECORATOR_FULLNAMES = pydantic.mypy.DECORATOR_FULLNAMES | {
    "pydantic.v1.class_validators.validator",
}


class CustomPydanticModelTransformer(PydanticModelTransformer):
    """Extension of the mypy/pydantic model transformer which also understands validator definitions via v1 compat."""

    def collect_field_or_class_var_from_stmt(
        self, stmt: AssignmentStmt, model_config: ModelConfigData, class_vars: dict[str, PydanticModelClassVar]
    ) -> PydanticModelField | PydanticModelClassVar | None:
        """Extend implementation of the original Pydantic method with one more case for validator."""
        if not stmt.new_syntax and (
            isinstance(stmt.rvalue, CallExpr)
            and isinstance(stmt.rvalue.callee, CallExpr)
            and isinstance(stmt.rvalue.callee.callee, MemberExpr)
            and stmt.rvalue.callee.callee.fullname in DECORATOR_FULLNAMES
        ):
            # Required to detect compat-imported v1 validators and not treat them as fields.
            return None
        return super().collect_field_or_class_var_from_stmt(stmt, model_config, class_vars)


class CustomMetaclassPydanticPlugin(PydanticPlugin):
    """
    Custom metaclass pydantic plugin.

    Extends a standard pydantic mypy plugin, and adds certain behaviours required for us:
    1. Support for a non-standard metaclass for pydantic models. We use it allow for access via Class.field notation
    2. Support for our modified compat import of pydantic v1 when using this metaclass.
    """

    def get_metaclass_hook(self, fullname: str) -> Callable[[ClassDefContext], None] | None:
        """Update Pydantic `ModelMetaclass` definition."""
        if fullname in MODEL_METACLASSES_FULL_NAMES:
            return self._pydantic_model_metaclass_marker_callback
        return None

    def get_base_class_hook(self, fullname: str) -> Callable[[ClassDefContext], bool] | None:  # type: ignore
        """Update Pydantic model class."""
        sym = self.lookup_fully_qualified(fullname)
        if sym and isinstance(sym.node, TypeInfo):  # pragma: no branch
            # No branching may occur if the mypy cache has not been cleared
            if any(base.fullname in ["pydantic.main.BaseModel", "pydantic.v1.main.BaseModel"] for base in sym.node.mro):
                return self._pydantic_model_class_maker_callback
        return None

    def _pydantic_model_class_maker_callback(self, ctx: ClassDefContext) -> bool:
        # extended to replace the mypy-pydantic transformer with our custom transformer - see validator note.
        transformer = CustomPydanticModelTransformer(ctx.cls, ctx.reason, ctx.api, self.plugin_config)
        return transformer.transform()


def plugin(version: str):
    """Entry point to the mypy plugin."""
    return CustomMetaclassPydanticPlugin
