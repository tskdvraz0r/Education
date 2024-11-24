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

# Константы и переменные;
data: list[tuple[str, float]] = [
    ("asdf", 0.7),
    ("ghjk", 1.4),
    ("zxcl", 3.2),
    ("vbnm", 4.1),
    ("poiu", 2.7),
    ("ytre", 0.3),
    ("wqsx", 1.1),
]


# Целевая функция;
def task(name: str, delay: float) -> None:
    time.sleep(delay)
    logger.success(name)


# Создание пула потоков;
with ThreadPoolExecutor() as executor:
    for values in data:
        future: Future[None] = executor.submit(task, *values)
        try:
            future.result(timeout=1.5)
        except TimeoutError:
            continue
