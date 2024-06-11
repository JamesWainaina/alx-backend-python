#!/usr/bin/env python3
"""
creating task but using random delay
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    function similar to task_n but task_wait_random is being called
    """

    tasks = []
    delays = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays