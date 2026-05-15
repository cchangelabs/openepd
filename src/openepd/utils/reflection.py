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
    modify_field_name: Callable[[str, TypeWithContainer, str], str] | None = None,
) -> dict[str, FieldInfo]:
    """
    Traverse the model type with key field types and return the fields info.

    :param model_type: The model type to traverse.
    :param key_field_types: The key field types to traverse.
    :param delimiter: The delimiter to use between nested field segments.
    :param parent_name: The parent name to use to avoid circular traversal.
    :param modify_prefix_func: Callable that receives a key value and returns the
        prefix to use when traversing the corresponding keyed sub-object.
    :param modify_field_name: Optional callable used to transform individual field
        names. Called as modify_field_name(field_name, data_type, delimiter) and
        expected to return the (possibly modified) field name string.
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
                modify_field_name=modify_field_name,
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


def _safe_unwrap_annotation(annotation: Any) -> TypeWithContainer | None:
    """
    Safely unwrap an annotation returning None on failure.

    :param annotation: The annotation to unwrap.
    :return: A TypeWithContainer instance or None when unwrapping fails.
    """
    try:
        return unwrap_annotation(annotation)
    except ValueError:
        return None


def _is_excluded(name_candidate: str, field_name: str, exclude_list: set[FieldNameMatcher]) -> bool:
    """
    Determine whether a field should be excluded based on the exclude list.

    :param name_candidate: Full candidate name including prefix.
    :param field_name: The original field name.
    :param exclude_list: Set of matchers.
    :return: True if excluded, False otherwise.
    """
    return any(is_field_matched(name_candidate, field_name, m) for m in exclude_list)


def _add_or_recurse_field(
    result: dict[str, FieldInfo],
    field_name: str,
    field_def: Any,
    inner_types: TypeWithContainer,
    annotation: Any,
    prefix: str,
    delimiter: str,
    parent_name: str,
    exclude_list: set[FieldNameMatcher],
    modify_field_name: Callable[[str, TypeWithContainer, str], str] | None,
) -> None:
    """
    Add a simple field to the result mapping or recurse for nested models.

    :param result: Mapping to populate.
    :param field_name: Original field name.
    :param field_def: Pydantic ModelField-like object.
    :param inner_types: Unwrapped TypeWithContainer for the field.
    :param annotation: Original annotation for the field.
    :param prefix: Current prefix for nested paths.
    :param delimiter: Delimiter for nested segments.
    :param parent_name: Name of the parent to avoid cycles.
    :param exclude_list: Set of matchers to exclude.
    :param modify_field_name: Optional modifier for field names.
    """
    effective_field_name = (
        modify_field_name(field_name, inner_types, delimiter) if modify_field_name is not None else field_name
    )

    # If target types list is empty, nothing to add
    if len(inner_types.target_types) == 0:
        return

    first_type = inner_types.target_types[0]

    # Recurse into nested BaseModel subclasses
    if isinstance(first_type, type) and issubclass(first_type, pyd.BaseModel):
        if field_name == parent_name:
            return
        result.update(
            fields_traverse(
                first_type,
                prefix=prefix + effective_field_name + delimiter,
                parent_name=field_name,
                delimiter=delimiter,
                exclude_list=exclude_list,
                modify_field_name=modify_field_name,
            )
        )
        return

    # Otherwise, record the field info
    result[prefix + effective_field_name] = FieldInfo(
        name=prefix + effective_field_name,
        type_annotation=annotation,
        data_type=inner_types,
        description=field_def.description,
        is_optional=is_nullable_annotation(annotation),
    )


def fields_traverse(
    obj: type[pyd.BaseModel],
    delimiter: str = ".",
    prefix: str = "",
    parent_name: str = "",
    exclude_list: set[FieldNameMatcher] | None = None,
    modify_field_name: Callable[[str, TypeWithContainer, str], str] | None = None,
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
    :param modify_field_name: Optional callable to transform a field name before the full
        name is generated. Called as modify_field_name(field_name, data_type, delimiter)
        where data_type is a TypeWithContainer describing the field's inner types and
        any container type. If None, field names are not modified.

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
        annotation = field_def.annotation

        inner_types = _safe_unwrap_annotation(annotation)
        if inner_types is None:
            # Skip fields where annotation unwrapping failed
            continue

        effective_field_name = (
            modify_field_name(field_name, inner_types, delimiter) if modify_field_name is not None else field_name
        )

        name_candidate = prefix + effective_field_name
        if _is_excluded(name_candidate, field_name, exclude_list):
            continue

        # Delegate adding or recursing into a helper to reduce complexity
        _add_or_recurse_field(
            result,
            field_name,
            field_def,
            inner_types,
            annotation,
            prefix,
            delimiter,
            parent_name,
            exclude_list,
            modify_field_name,
        )

    return result
