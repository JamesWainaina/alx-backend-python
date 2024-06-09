#!/usr/bin/env python3
"""Convert a float to a string."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a float to a string."""
    return (k, v ** 2)
