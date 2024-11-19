"""
19.11.2924
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

# Локальные функции;
def worker() -> None:
    logger.debug("Начало работы демон-потока;")
    time.sleep(2)
    logger.debug("Завершение работы демон-потока;")

# Создание потока;
thread: thr.Thread = thr.Thread(target=worker)

# Установка аргумента daemon=True;
thread.daemon = True

# Запуск потока;
thread.start()

# Основной поток продолжает выполнение;
logger.debug("Основной поток завершается;")