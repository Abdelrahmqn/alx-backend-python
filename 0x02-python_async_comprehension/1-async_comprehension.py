#!/usr/bin/env python3
""" async_comprehension
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 rand num (uniform them 10 times)
    [list comprehension]: hint
    """

    nums = [n async for n in async_generator()]
    return nums
