"""
24.11.2024
"""

import sys
import time
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# Целевая функция;
def task(number: int) -> int:
    time.sleep(1)
    return number * number


# Создать пул потоков;
with ThreadPoolExecutor(max_workers=3) as executor:
    # Использование map() для отправки задач в пул;
    results: Iterable[int] = executor.map(task, [2, 17, 8, 11, 14, 5])

    # Ожидание завершения всех задач и получение результата;
    print(*[result for result in results], sep="\n")
