"""
19.11.2024
Ожидание результата с помощью join()
"""
import sys
import time
import threading as thr

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

def task() -> None:
    logger.debug("Начало выполенния задачи;")
    # Здесь выполняется некая задача;
    time.sleep(2)
    logger.debug("Задача завершена;")

# Создание и запуск потока;
thread: thr.Thread = thr.Thread(target=task)
thread.start()

# Ожидание завершения работы потока;
thread.join()

logger.debug("Задача завершена, продолжаем выполнение основного потока;")    