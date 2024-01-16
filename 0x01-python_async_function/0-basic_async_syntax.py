#!/usr/bin/env python3
"""
wait_random module

This module defines an asynchronous coroutine named wait_random that takes
an integer argument max_delay (default value is 10) and waits for a random
delay between 0 and max_delay (inclusive) seconds, returning the result.

It uses the random module and asyncio for asynchronous functionality.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine to wait for a random delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The randomly generated delay.

    Example:
        ```python
        result = await wait_random()
        print(f"Waited for {result:.2f} seconds.")
        ```
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
