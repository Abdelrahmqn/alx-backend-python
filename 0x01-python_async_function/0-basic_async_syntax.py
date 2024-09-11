#!/usr/bin/env python3
"""Async Introduction."""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """
    sleep and return the same float
    (same delay.... whatever)
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
