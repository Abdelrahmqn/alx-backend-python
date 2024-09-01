#!/usr/bin/env python3
"""Async Introduction."""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """
    sleep and return the same float
    (same delay.... whatever)
    """
    uniform(0, max_delay)
    await asyncio.sleep(uniform(0, max_delay))
    return uniform(0, max_delay)
