"""
19.11.2024
"""

import sys
import threading as thr
import time

from loguru import logger

# loguru
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# Локальные функции;
def worker() -> None:
    logger.debug("Начало работы демон-потока;")
    time.sleep(2)
    logger.debug("Завершение работы демон-потока;")


# Создание потока и установка аргумента daemon=True;
thread: thr.Thread = thr.Thread(target=worker, daemon=True)

# Запуск потока;
thread.start()

# Основной поток продолжает выполнение;
logger.debug("Основной поток продолжает завершение;")
