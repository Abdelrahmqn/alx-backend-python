#!/usr/bin/env python3
"""file documentation"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    dels = await asyncio.gather(*tasks)
    nums = []

    while dels:
        small = min(dels)
        nums.append(small)
        dels.remove(small)
    return nums  # storing the values here...
