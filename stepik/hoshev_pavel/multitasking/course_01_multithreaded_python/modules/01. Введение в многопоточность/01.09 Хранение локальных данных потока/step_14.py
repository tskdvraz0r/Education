"""
22.11.2024
"""

import sys
import threading

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Локальное хранилище;
thread_data = threading.local()


# Целевая функция;
def process_data() -> None:
    thread_data.data = "HELLO LOCAL STORAGE!"
    logger.info(f"Данные в локальном хранилище: {thread_data.data}")


# Создание и запуск потоков;
for _ in range(3):
    thread = threading.Thread(target=process_data)
    thread.start()
