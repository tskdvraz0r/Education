"""
22.11.2024
"""

import sys
import threading
import time

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Создание локального хранилища;
local_storage = threading.local()

# Установка значения в локальное хранилище главного потока;
local_storage.name = "Хранилище главного потока"
logger.debug(
    f"Имя потока {threading.current_thread().name}; Локальные данные: {local_storage.name};"
)


# Целевая функция;
def thread_function(name: str) -> None:
    # Установка значения в локальное хранилище потока;
    time.sleep(0.1)
    local_storage.name = name
    logger.debug(
        f"Имя потока {threading.current_thread().name}; Локальные данные: {local_storage.name};"
    )


# Создание потоков;
thread1: threading.Thread = threading.Thread(
    target=thread_function, name="Поток-1", args=("Локальные данные потока 1",)
)
thread2: threading.Thread = threading.Thread(
    target=thread_function, name="Поток-2", args=("Локальные данные потока 2",)
)

# Запуск потоков;
thread1.start()
thread2.start()

# Ожидание потоков;
thread1.join()
thread2.join()

# Проверка, сохранились ли локальные данные главного потока, после завершения работы других потоков;
logger.debug(
    f"Имя потокa {threading.current_thread().name}, Локальные данные: {local_storage.name};"
)
