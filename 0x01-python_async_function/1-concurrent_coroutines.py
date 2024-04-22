#!/usr/bin/env python3
""" An asynchronous coroutine script """

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine function implementation"""
    tasks = [wait_random(max_delay) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
