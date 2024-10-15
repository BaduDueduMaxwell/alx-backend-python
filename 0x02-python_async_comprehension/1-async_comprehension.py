#!/usr/bin/env python3
''' Async Comprehensions '''

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    ''' Coroutine that asynchronously compress
    random numbers from async_generator '''
    return [val async for val in async_generator()]
