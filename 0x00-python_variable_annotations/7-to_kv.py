#!/usr/bin/env python3
"""Module documentation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """creating a square return ins union"""
    return (k, v ** 2)
