#!/usr/bin/env python3
"""still annotation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """write a function that return the sum of the list"""
    # return sum(input_list)
    tot = 0.0
    for i in input_list:
        tot += i
    return tot
