#!/usr/bin/env python3
"""Defines a type-annotation function."""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of a key in a dictionary."""
    if key in dct:
        return dct[key]
    else:
        return default
