#!/usr/bin/env python3
""" An asynchronous coroutine script """

import time
import asyncio
from typing import List

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine function implementation"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter - start_time

    return elapsed_time / n
