#!/usr/bin/env python3
"""
2-measure_runtime module

This module imports the wait_n coroutine and defines a measure_time function
to measure the total execution time for wait_n(n, max delay.
"""

import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the total execution time for wait_n(n,max_delay)

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: Average time per iteration.

    Example:
        ```python
        average_time = measure_time(3)
        print(f"Average time per iteration: {average_time:.5f} seconds")
        ```
    """
    start_time = time.time()

    # Asynchronously run wait_n
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
