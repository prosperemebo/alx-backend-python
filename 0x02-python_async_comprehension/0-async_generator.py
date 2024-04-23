#!/usr/bin/env python3
""" script for async_generator """
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    The coroutine will loop 10 times
    each time asynchronously wait 1 second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
