#!/usr/bin/env python3
"""
wait_n module

This module defines an asynchronous coroutine named wait_n that imports
wait_random and spawns it n times with the specified max_delay.

The result is a list of delays in ascending order.
"""

import asyncio
from typing import List

from wait_random import wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous coroutine to spawn wait_random n times.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        List[float]: List of delays in ascending order.

    Example:
        ```python
        delays = await wait_n(3)
        print(delays)
        ```
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
