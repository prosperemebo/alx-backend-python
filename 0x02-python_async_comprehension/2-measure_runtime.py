#!/usr/bin/env python3
""" script for measure_runtime """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The coroutine that will execute,
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    """
    start_time = time.perf_counter()
    tasks = (async_comprehension() for _ in range(4))
    await asyncio.gather(*tasks)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time
