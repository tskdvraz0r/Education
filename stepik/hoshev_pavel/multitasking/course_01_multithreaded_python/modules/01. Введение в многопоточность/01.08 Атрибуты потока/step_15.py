"""
22.11.2024
"""
import sys
import time
import typing
import threading

from loguru import logger


# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# КОНСТАНТЫ;
CODE_NAMES: typing.Final[list[str]] = ["Alpha", "Bravo", "Charley", "Delta"]

# Целевая функция;
def task(code_name: str) -> None:
    logger.debug(f"Исходное имя потока: {threading.current_thread().name}")
    time.sleep(1)
    threading.current_thread().name = code_name
    logger.debug(f"Новое имя потока: {threading.current_thread().name}")
    logger.debug(f"Задача выполнена для {threading.current_thread().name}")

# Создание потоков;
threads: list[threading.Thread] = []
for code_name in CODE_NAMES:
    thread: threading.Thread = threading.Thread(
        target=task,
        args=(code_name,)
    )
    
    thread.start()