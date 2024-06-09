#!/usr/bin/env python3
"""Make a multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make a multiplier."""
    def multiplier_fn(n: float) -> float:
        return n * multiplier
    return multiplier_fn
