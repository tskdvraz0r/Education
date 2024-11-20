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

def task() -> None:
    time.sleep(5)
    logger.debug("Всё готово в новом потоке;")

thread: thr.Thread = thr.Thread(target=task)
thread.start()

# Ожидание завершения потока не более 2 секунд;
thread.join(timeout=2)

# Проверить, "живой" ли поток;
while thread.is_alive():
    logger.debug("Поток не завершён;")
    time.sleep(1)
    
logger.debug("Поток завершён;")
