#!//usr/bin/env python3
""" This module has a generator function
    called async_generator that yields a random
    number between 0 and 10 every 1 second
"""

import asyncio
import random
from typing import Generator


async def async_generator()-> Generator[float, None, None]:
    """
        This function yields a
        random number between 0 and 10 every 1 second
    """

    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)
