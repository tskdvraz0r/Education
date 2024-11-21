"""
20.11.2024
"""
import sys
import time
import threading as thr

from loguru import logger


# loguru;
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

# Целевая функция;
def task() -> None:
    logger.debug(f"Поток {thr.current_thread().name} начал выполнение;")
    time.sleep(3)
    logger.debug(f"Поток {thr.current_thread().name} завершил выполнение;")

thread1: thr.Thread = thr.Thread(target=task)
thread2: thr.Thread = thr.Thread(target=task)

thread1.start()
thread2.start()

thread1.join()
thread2.join()