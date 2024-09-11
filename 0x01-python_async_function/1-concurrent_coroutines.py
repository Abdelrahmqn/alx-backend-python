#!/usr/bin/env python3
"""file documentation"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function
    """
    # for i in range(n):
    #     i = [wait_random(max_delay)]
    tasks = [wait_random(max_delay) for tasks in range(n)]
    dels = await asyncio.gather(*tasks)
    return dels
