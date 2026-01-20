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
from __future__ import annotations

from collections.abc import Callable
import dataclasses
from types import UnionType
from typing import Annotated, Any, NamedTuple, Union, get_args, get_origin

import pydantic as pyd

FieldExclusionFn = Callable[[str, str], bool]
FieldNameMatcher = str | FieldExclusionFn


def is_field_matched(full_name: str, name: str, matcher: FieldNameMatcher) -> bool:
    """
    Check if a field name matches a given matcher.

    If the matcher is a string starting with '^', it checks for an exact match with the full name.
    Otherwise, it checks for an exact match with the name.
    If the matcher is a callable, it invokes the callable with the name and full name.
    """
    if isinstance(matcher, str):
        if matcher.startswith("^"):
            return matcher[1:] == full_name
        else:
            return matcher == name
    else:
        return matcher(name, full_name)


class TypeWithContainer(NamedTuple):
    target_types: tuple[type, ...]
    container_type: type | None


@dataclasses.dataclass
class FieldInfo:
    name: str
    data_type: TypeWithContainer
    description: str | None
    type_annotation: Any
    is_optional: bool


def _traverse_with_keys(
    model_type: type[pyd.BaseModel],
    key_field_types: Any,
    delimiter: str,
    parent_name: str,
    modify_prefix_func: Callable[[Any], str],
) -> dict[str, FieldInfo]:
    """
    Traverse the model type with key field types and return the fields info.

    :param model_type: The model type to traverse.
    :param key_field_types: The key field types to traverse.
    :param delimiter: The delimiter to use.
    :param parent_name: The parent name to use.
    :param modify_prefix_func: The function to modify the prefix.
    """
    results = {}
    for key_value in key_field_types:
        modified_prefix = modify_prefix_func(key_value)
        results.update(
            fields_traverse(
                model_type,
                prefix=modified_prefix,
                parent_name=parent_name,
                delimiter=delimiter,
            )
        )
    return results


def unwrap_annotation(annotation: Any) -> TypeWithContainer:
    """
    Return a tuple of inner types, unwrapping Optional/Union and containers.

    Examples:
    - Optional[int]          -> (int,)
    - Union[int, None]       -> (int,)
    - Union[int, str]        -> (int, str)
    - list[SomeModel]        -> (SomeType,)
    - dict[str, SomeModel]   -> (SomeType,)

    """
    annotation = unwrap_nullable_annotation(annotation)

    origin = get_origin(annotation)
    args = get_args(annotation)

    # Handle Optional/T | None/Union
    if origin is None:
        # Not a parameterized type (plain class, e.g. int, SomeType)
        return TypeWithContainer((annotation,), None)

    if origin is UnionType:
        return TypeWithContainer(tuple(unwrap_annotated_annotation(a) for a in args if a is not type(None)), None)

    if origin is list or origin is tuple or origin is set:
        # list[T], tuple[T, ...], set[T] -> return element types
        return TypeWithContainer(tuple(unwrap_annotated_annotation(a) for a in args if a is not type(None)), origin)

    if origin is dict:
        # dict[K, V] -> return value type(s)
        if len(args) == 2:
            return TypeWithContainer(
                tuple(unwrap_annotated_annotation(a) for a in args[1:] if a is not type(None)), origin
            )

    if origin is type(Union[int, str]):  # noqa: UP007
        # Just in case, but `get_origin` for `|` unions is `types.UnionType`
        pass

    # Generic Union or Optional
    if origin is Any or origin is UnionType:
        return TypeWithContainer(tuple(unwrap_annotated_annotation(a) for a in args if a is not type(None)), None)

    return TypeWithContainer(tuple(unwrap_annotated_annotation(a) for a in args), None)


def is_nullable_annotation(annotation: Any) -> bool:
    """
    Check if the given type annotation is nullable (i.e., allows None).

    Examples:
    - Optional[int]          -> True
    - Union[int, None]       -> True
    - Union[int, str]        -> False
    - int                    -> False

    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is None:
        return False

    if origin is Any or origin is UnionType:
        return any(a is type(None) for a in args)

    return False


def unwrap_nullable_annotation(annotation: Any) -> Any:
    """
    Unwrap nullable type annotations to get the non-nullable type.

    Examples:
    - Optional[int]          -> int
    - Union[int, None]       -> int
    - Union[int, str]        -> Union[int, str]
    - int                    -> int

    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is None:
        return annotation

    if origin is Any or origin is UnionType:
        non_nullable_args = tuple(a for a in args if a is not type(None))
        if len(non_nullable_args) == 1:
            return non_nullable_args[0]
        else:
            return Union[*non_nullable_args]

    return annotation


def unwrap_annotated_annotation(annotation: Any) -> Any:
    """
    Unwrap Annotated type annotations to get the underlying type.

    Examples:
    - Annotated[int, "some metadata"] -> int
    - int                             -> int

    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is Annotated:
        if len(args) >= 1:
            return args[0]
    return annotation


def fields_traverse(
    obj: type[pyd.BaseModel],
    delimiter: str = ".",
    prefix: str = "",
    parent_name: str = "",
    exclude_list: set[FieldNameMatcher] | None = None,
) -> dict[str, FieldInfo]:
    """
    Recursively traverse a Pydantic model's fields and return their metadata.

    This function walks through all fields of a Pydantic model, including nested models,
    and collects information about each field including its type, description, and optionality.
    Fields that are themselves Pydantic models are traversed recursively.

    :param obj: The Pydantic BaseModel class to traverse.
    :param delimiter: The string used to separate nested field names (default: ".").
    :param prefix: The prefix to prepend to field names, used internally for nested traversal.
    :param parent_name: The name of the parent field, used to prevent circular references.
    :param exclude_list: A set of field name matchers to exclude from traversal. Each matcher
        can be a string (exact match or full path match if prefixed with "^") or a
        callable that takes (name, full_name) and returns bool.

    :return: A dictionary mapping full field paths to FieldInfo objects containing metadata
    about each field (name, type, description, annotation, and optionality).

    Examples:
        >>> class Address(pyd.BaseModel):
        ...     street: str
        ...     city: str
        ...
        >>> class Person(pyd.BaseModel):
        ...     name: str
        ...     age: int | None
        ...     address: Address
        ...
        >>> fields = fields_traverse(Person)
        >>> list(fields.keys())
        ['name', 'age', 'address.street', 'address.city']

    """
    result: dict[str, FieldInfo] = {}
    exclude_list = exclude_list or set()
    for field_name, field_def in obj.model_fields.items():
        name_candidate = prefix + field_name
        if any(is_field_matched(name_candidate, field_name, m) for m in exclude_list):
            continue
        annotation = field_def.annotation
        is_optional = is_nullable_annotation(annotation)
        try:
            inner_types = unwrap_annotation(annotation)
        except ValueError:
            continue
        if len(inner_types.target_types) == 0:
            continue

        first_type = inner_types.target_types[0]

        if isinstance(first_type, type) and issubclass(first_type, pyd.BaseModel):
            if field_name == parent_name:
                continue
            result.update(
                fields_traverse(
                    first_type,
                    prefix=prefix + field_name + delimiter,
                    parent_name=field_name,
                    delimiter=delimiter,
                    exclude_list=exclude_list,
                )
            )
        else:
            result[prefix + field_name] = FieldInfo(
                name=prefix + field_name,
                type_annotation=annotation,
                data_type=inner_types,
                description=field_def.description,
                is_optional=is_optional,
            )
    return result
