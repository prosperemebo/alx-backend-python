#!/usr/bin/env python3
""" script for measure_runtime """
import asyncio
import random
from typing import Generator


async def measure_runtime() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times,
    each time asynchronously wait 1 second.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
