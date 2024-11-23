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


# Целевая функция;
def task(message: str) -> None:
    logger.info(message)


# Создание потока-таймера;
thread_timer: threading.Timer = threading.Timer(
    interval=3, function=task, args=("Hello, World!",)
)

# Запуск потока-таймера;
thread_timer.start()
logger.debug("Поток запушен;")

# Блокировка на короткое время;
time.sleep(1)
logger.debug("Задержка завершилась;")

# Отмена потока-таймера;
thread_timer.cancel()
logger.info("Запуск потока-таймера отменён;")
