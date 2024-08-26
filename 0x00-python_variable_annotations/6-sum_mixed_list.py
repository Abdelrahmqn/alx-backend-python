#!/usr/bin/env python3
"""sum mixed"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """the sum of floats and ints"""
    return sum(mxd_lst)
