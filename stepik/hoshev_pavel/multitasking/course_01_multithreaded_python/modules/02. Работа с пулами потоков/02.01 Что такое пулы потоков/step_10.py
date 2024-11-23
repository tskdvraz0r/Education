"""
24.11.2024
"""

import sys
from concurrent.futures import Future, ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
start_and_end: tuple[tuple[int, int], ...] = ((1, 100), (101, 200), (201, 300))


# Целевая функция
def sum_range(start: int, end: int) -> None:
    result: int = sum(range(start, end + 1))
    logger.success(f"Сумма чисел от {start} до {end}: {result}")


# Создание пула потоков;
with ThreadPoolExecutor() as executor:
    for ranges in start_and_end:
        future: Future = executor.submit(sum_range, *ranges)
        future.result()
