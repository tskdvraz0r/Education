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
def print_numbers(limit: int, delay: int) -> None:
    for number in range(limit):
        logger.info(number)
        time.sleep(delay)


# Создание пула потоков с одним воркером;
with ThreadPoolExecutor(max_workers=1) as executor:
    # Запуск задачи в пуле;
    future: Future[None] = executor.submit(print_numbers, 5, 1)
    # Ожидание результата;
    future.result()

logger.info("Поток завершил выполнение;")
