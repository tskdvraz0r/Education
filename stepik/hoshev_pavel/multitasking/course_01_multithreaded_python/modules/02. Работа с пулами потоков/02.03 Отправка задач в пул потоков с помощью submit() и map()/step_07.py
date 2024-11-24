"""
24.11.2024
"""

import sys
import time
from concurrent.futures import Future, ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# Целевая функция;
def print_from_one_to_five() -> None:
    for i in range(1, 6):
        time.sleep(0.5)
        logger.info(i)


def print_from_a_to_e() -> None:
    for i in "abcde":
        time.sleep(1)
        logger.info(i)


# Создание пула потоков;
with ThreadPoolExecutor() as executor:
    for func in (print_from_one_to_five, print_from_a_to_e):
        future: Future = executor.submit(func)
        future.result()
