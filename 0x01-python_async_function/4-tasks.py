#!/usr/bin/env python3
"""file documentation for task_wait_n func"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n function
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    dels = await asyncio.gather(*tasks)
    nums = []

    while dels:
        small = min(dels)
        nums.append(small)
        dels.remove(small)
    return nums  # storing the values here...
