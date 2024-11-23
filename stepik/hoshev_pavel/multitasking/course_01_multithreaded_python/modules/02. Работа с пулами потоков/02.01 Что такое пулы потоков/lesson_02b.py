"""
24.11.2024
"""

import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# Функция инициализации потоков;
def thread_initializer(greetings: str) -> None:
    logger.debug(f"{greetings} от {threading.current_thread().name}")


# Целевая функция;
def perform_task(task_number: int) -> None:
    logger.debug(
        f"Задача {task_number} выполняется потоком {threading.current_thread().name}"
    )
    time.sleep(1)
    logger.debug(
        f"Задача {task_number} завершена потоком {threading.current_thread().name}"
    )


# Создание и запуск пула потоков;
with ThreadPoolExecutor(
    max_workers=2,
    thread_name_prefix="DemoThread",
    initializer=thread_initializer,
    initargs=("Привет",),
) as executor:
    for i in range(4):
        executor.submit(perform_task, i)

# После выхода из блока with, пул потоков будет автоматически закрыт, а все задачи завершены;
