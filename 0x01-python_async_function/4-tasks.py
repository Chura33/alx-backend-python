#!/usr/bin/env python3
"""
task_wait_n module

This module imports task_wait_random and defines a function task_wait_n
that takes two integer arguments (n and max_delay) and returns a list of
asyncio.Tasks representing the execution of task_wait_random.
"""

import asyncio
from typing import List
from task_wait_random import task_wait_random  # Import task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[asyncio.Task]:
    """
    Asynchronous coroutine to spawn task_wait_random n times with max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        List[asyncio.Task]: List of asyncio.Tasks representing the execution

    Example:
        ```python
        tasks = await task_wait_n(3)
        results = await asyncio.gather(*tasks)
        print(results)
        ```
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return tasks
