#!/usr/bin/env python3
"""kv ?"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Union int and float"""
    return (k, v ** 2)
