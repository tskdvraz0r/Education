"""
20.11.2024
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

def task_error() -> None:
    time.sleep(1)
    print(f"Исключение в потоке {thr.current_thread().name}")
    raise RuntimeError("Что-то пошло не так...")

thread: thr.Thread = thr.Thread(target=task_error)
thread.start()
thread.join()
logger.debug("Основной поток продолжает работу...")