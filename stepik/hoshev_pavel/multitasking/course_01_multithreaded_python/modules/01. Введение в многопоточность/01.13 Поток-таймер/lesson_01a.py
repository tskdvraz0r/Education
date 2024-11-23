"""
23.11.2024
"""

import sys
import threading

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# ЦЕЛЕВАЯ ФУНКЦИЯ;
def task(message: str) -> None:
    logger.info(message)


# Создание потока с таймером;
thread_timer: threading.Timer = threading.Timer(
    interval=3, function=task, args=("Hello, World!",)
)

# Запуск потока с таймером;
thread_timer.start()

# Ожидание завершения работы потока с таймером;
logger.debug("Ожидаем завершения таймера...")
