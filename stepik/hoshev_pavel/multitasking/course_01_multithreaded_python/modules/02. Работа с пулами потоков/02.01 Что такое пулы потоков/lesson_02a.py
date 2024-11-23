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
def task(message: str) -> str:
    logger.debug("Задача начата;")
    time.sleep(2)
    logger.debug("Задача завершена;")
    return f"Задача выполнена с сообщением: {message}"


# Создание пула потоков;
with ThreadPoolExecutor(max_workers=3) as executor:
    # Отправка задач в пул потоков;
    future: Future[str] = executor.submit(task, "Привет, Мир!")
    future2: Future[str] = executor.submit(task, "Другая задача.")

    # Получение и вывод результата;
    logger.success(future.result())
    logger.success(future2.result())
