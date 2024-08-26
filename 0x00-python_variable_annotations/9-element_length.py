#!/usr/bin/env python3
"""Annotate a function"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotated"""
    return [(i, len(i)) for i in lst]
