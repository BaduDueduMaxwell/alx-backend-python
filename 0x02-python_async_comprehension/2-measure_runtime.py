#!/usr/bin/env python3
''' Run time for four parallel comprehensions '''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    return total_time
