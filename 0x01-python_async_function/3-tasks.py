#!/usr/bin/env python3
"""
task_wait_random module

This module imports wait_random from 0-basic_async_syntax
task_wait_random that takes an integer max_delay and returns an asyncio.Task.
"""

import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create and return an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: execution of wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
