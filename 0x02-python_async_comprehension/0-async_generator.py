#!/usr/bin/env python3
"""async_generator
"""
import random
import asyncio


async def async_generator():
    """ async gen:
        loop 10 times; each time asynchronously wait
        one second, yield a random float num at this period
        should be range(0, 10) with random module
    """
    for i in range(10):
        await asyncio.sleep(1)
        ran_num = random.uniform(0, 10)
        yield ran_num
