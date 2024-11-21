"""
22.11.2024
"""
import sys
import time
import typing
import random
import threading

from loguru import logger


# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# КОНСТАНТЫ;
MISSIONS: typing.Final[dict[str, str]] = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",
    "Thread-Search": "Поиск информации",
    "Thread-Anonymize": "Обеспечение анонимности",
    "Thread-Analyse": "Анализ данных",
    "Thread-DDoS": "DDoS Атака",
}

THREADS_WITH_MISSIONS: typing.Final[dict[str, threading.Thread]] = {}

# Целевая функция;
def mission(mission_name: str) -> None:
    logger.debug(f"[{mission_name}] Миссия началась.")
    time.sleep(random.randint(1, 3))
    logger.debug(f"[{mission_name}] Миссия успешно выполнена!")

# Создание потоков;
for thread_name, mission_name in MISSIONS.items():
    
    # Создание потока;
    thread: threading.Thread = threading.Thread(
        target=mission,
        name=thread_name,
        args=(mission_name,)
    )
    
    # Статус миссии до запуска;
    logger.debug(f"[{thread_name} ({mission_name})] Статус миссии до запуска: {thread.is_alive()}")
    
    # Добавление потока в словарь;
    THREADS_WITH_MISSIONS[thread_name] = thread

# Запуск потоков;
for thread_name, thread in THREADS_WITH_MISSIONS.items():
    thread.start()
    logger.debug(f"[{thread_name} ({MISSIONS[thread.name]})] Миссия активна: {thread.is_alive()}")

# Ожидание завершения потоков;
for thread in THREADS_WITH_MISSIONS.values():
    thread.join()
    logger.debug(f"[{thread.name} ({MISSIONS[thread.name]})] Статус миссии после завершения: {not thread.is_alive()}")