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
logger.add(sink=sys.stderr, level="DEBUG")

# Константы;
name_threads: typing.Final[list[str]] = [
    "OF95RK", "VH61DX", "NB03WA", "WO40ZF", "NJ48EG",
    "SX21ET", "AT01PA", "MR36DD", "DD84HR", "MI81QY"
]

# Целевая функция;
def worker() -> None:
    logger.debug(f"Поток {thr.current_thread().name} начал выполнение;")
    time.sleep(1)
    logger.debug(f"Поток {thr.current_thread().name} завершил выполнение;")

# Создание потоков;
threads: typing.List[thr.Thread] = []
for name in name_threads:
    thread: thr.Thread = thr.Thread(target=worker, name=name)
    threads.append(thread)

# Запуск потоков;
for thread in threads:
    thread.start()

# Завершение потоков;
for thread in threads:
    thread.join()
