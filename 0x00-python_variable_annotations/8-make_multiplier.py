#!/usr/bin/env python3
"""make multipliers"""
from typing import Callable
"""
provides a way to specify types for callable functions or objects
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make a multiplier function"""
    def multiply(mul: float) -> float:
        """inner """
        return mul * multiplier
    return multiply
