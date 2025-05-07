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
from typing import Any

from pydantic import utils as pydantic_utils

from openepd.compat.pydantic import pyd


def patch_pydantic_metaclass():
    """
    Patch pydantic's ModelMetaclass to restore class attribute lookup for fields.

    In pydantic, while the model fields are defined in the model as class-level attributes, in runtime they disappear
    due to ModelMetaclass logic. ModelMetaclass takes the defined attributes, removes them from class dict and puts
    into a special __fields__ attribute to avoid naming conflict.

    We would like to be able to access the attributes via dot notation in the runtimes, since it makes refactoring
    easier.

    This class exposes the original fields when accessed via class name. For example, one can call `Pcr.name` and get
    `ModelField`, in addition to calling `pcr.__fields__` on an instance.
    """

    def model_metaclass__getattr__(cls, name: str) -> Any:
        if name in cls.__fields__:
            return cls.__fields__[name]
        return getattr(super, name)

    pyd.main.ModelMetaclass.__getattr__ = model_metaclass__getattr__


def patch_pydantic_metaclass_validator():
    """
    Patch the internal validator function used during model construction to support modified metaclass.

    Pydantic has a special guard which stops execution if a model defines field which shadows a basemodel interface.
    For example, if someone would define a field named `__fields__` this would break code.

    With the modified metaclass functionality, we are exposing the original fields as class attributes, and this
    breaks this check.

    This patcher method modifies the pydantic internals so that the check is retained, but it is not causing exception
    when doing the normal field inheritance.
    """
    model_field_classes = list()

    try:
        from pydantic.v1.fields import ModelField as ModelFieldV1

        model_field_classes.append(ModelFieldV1)
    except ImportError:
        pass

    try:
        from pydantic.fields import ModelField as ModelFieldPydanticV1

        model_field_classes.append(ModelFieldPydanticV1)
    except ImportError:
        pass

    try:
        from pydantic_core.core_schema import ModelField as ModelFieldV2

        model_field_classes.append(ModelFieldV2)
    except ImportError:
        pass
    model_field_classes_tuple = tuple(model_field_classes)

    def pydantic_utils__validate_field_name(bases: list[type[pyd.BaseModel]], field_name: str) -> None:
        for base in bases:
            if attr := getattr(base, field_name, None):
                if isinstance(attr, model_field_classes_tuple):
                    continue

                msg = (
                    f'Field name "{field_name}" shadows a BaseModel attribute; '
                    f"use a different field name with \"alias='{field_name}'\"."
                )
                raise NameError(msg)

    pyd.main.validate_field_name = pydantic_utils__validate_field_name
    pydantic_utils.validate_field_name = pydantic_utils__validate_field_name


def patch_pydantic():
    """
    Modify Pydantic to support field attribute access via class.

    Example: Field the_field in the model TheModel(BaseModel). Before this patch, one can do
     `TheModel().__fields__["the_field"]' to get field descriptor. After the fix, one can do TheModel.the_field.

     To disable, set env variable `OPENEPD_DISABLE_PYDANTIC_PATCH` to "1", "yes" or "true".
    """
    patch_pydantic_metaclass()
    patch_pydantic_metaclass_validator()
