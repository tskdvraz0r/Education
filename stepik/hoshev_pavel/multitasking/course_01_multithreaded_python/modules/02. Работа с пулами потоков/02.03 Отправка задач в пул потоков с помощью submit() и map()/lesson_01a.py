"""
24.11.2024
"""

import sys
import time
from concurrent.futures import Future, ThreadPoolExecutor, as_completed

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# Целевая функция;
def task(number: int) -> int:
    time.sleep(1)
    return number + 5


# Создание пула потоков;
with ThreadPoolExecutor(max_workers=2) as executor:
    futures: list[Future[int]] = [executor.submit(task, number=i) for i in range(5)]
    time.sleep(2)

    # Ожидание завершения всех задач и получение результатов по мере их готовности;
    for future in as_completed(futures):
        print(type(future))
        print(future.result())
