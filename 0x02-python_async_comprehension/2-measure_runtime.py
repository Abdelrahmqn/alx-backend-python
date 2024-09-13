#!/usr/bin/env python3
"""what is the time
"""
from time import time
import asyncio
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """excute async_com 4 times in parallel using gather
    """
    for i in range(4):
        start = time()
        await gather(async_comprehension())
        after = time()
        return (after - start)
