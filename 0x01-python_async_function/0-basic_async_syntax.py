#!/usr/bin/env python3
""" An asynchronous coroutine script """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine function implementation"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
