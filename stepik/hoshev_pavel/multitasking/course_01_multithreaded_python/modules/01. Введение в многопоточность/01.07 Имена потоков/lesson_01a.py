"""
20.11.2024
"""
import sys
import time
import typing
import threading as thr

from loguru import logger


# loguru;
logger.remove()
logger.add(sys.stderr, level="DEBUG")

# Целевая функция;
def task() -> None:
    current_thread: typing.Final[thr.Thread] = thr.current_thread()
    logger.debug(f"Имя работающего потока: {current_thread.name}")

thread: thr.Thread = thr.Thread(target=task, name="Поток-1")
thread.start()