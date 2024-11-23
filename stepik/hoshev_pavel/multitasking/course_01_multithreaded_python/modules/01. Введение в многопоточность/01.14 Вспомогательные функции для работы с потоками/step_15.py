"""
23.11.2024
"""

import sys
import threading
import time

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
delays: list[int] = [1, 3, 2, 5, 4]


# Целевая функция;
def my_task(time_for_work: int) -> None:
    logger.info(f"Поток {threading.current_thread().name} начал работу")
    time.sleep(time_for_work)
    logger.info(f"Поток {threading.current_thread().name} завершил работу")


# Создание и запуск потоков;
for delay in delays:
    thread: threading.Thread = threading.Thread(target=my_task, args=(delay,))
    thread.start()

# Количество активных потоков через 1.5 сек;
time.sleep(1.5)
for thread_name in threading.enumerate():
    logger.info(f"{thread_name.name} еще выполняется")
