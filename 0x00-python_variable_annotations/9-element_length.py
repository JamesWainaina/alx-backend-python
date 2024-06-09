#!/usr/bin/env python3
"""Get the length of a string."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Get the length of a string."""
    return [(i, len(i)) for i in lst]
