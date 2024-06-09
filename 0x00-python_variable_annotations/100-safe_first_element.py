#!/usr/bin/env python3
"""defines ducktyoing annotation"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ducktyping"""
    if lst:
        return lst[0]
    else:
        return None
