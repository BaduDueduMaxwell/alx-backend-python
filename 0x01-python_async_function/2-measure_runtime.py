#!/usr/bin/env python3
''' Measure the runtime '''

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ Measuree the total execution time for wait_n(n, max_delay)
    and return the average time per coroutine.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time

    return total_time / n
