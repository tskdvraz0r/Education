"""
19.11.2024
Ожидание жезультата с помощью Event()
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

# Создать объект события;
event: thr.Event = thr.Event()

# Создание функции;
def task() -> None:
    # Задача, результата которой мы ожидаем;
    logger.debug("Задача выполняется;")
    # ...
    time.sleep(5)
    # Сигнализируем о завершении задачи;
    event.set()

# Создание и запуск потока;
thread: thr.Thread = thr.Thread(target=task)
thread.start()

# Ожидание завершения задачи;
logger.debug("Ожидание завершения задачи;")
event.wait()
logger.debug("Задача завершена;")