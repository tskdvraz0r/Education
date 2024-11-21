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

# Целевые функции;
def task1() -> None:
    logger.debug(f"Поток {thr.current_thread().name} начал выполнение;")
    print(f"Поток {thr.current_thread().name} запустился.")
    time.sleep(2)
    logger.debug(f"Поток {thr.current_thread().name} завершил выполнение;")

def task2() -> None:
    logger.debug(f"Поток {thr.current_thread().name} начал выполнение;")
    print(f"Поток {thr.current_thread().name} запустился.")
    time.sleep(3)
    logger.debug(f"Поток {thr.current_thread().name} завершил выполнение;")

# Создание потоков;
dict_with_threads: dict = {}

for thread_name, thread_task in zip(("A", "B"), (task1, task2)):
    dict_with_threads[thread_name] = thr.Thread(
        target=thread_task,
        name=thread_name
    )

# Запуск потоков;
for thread in dict_with_threads.values():
    thread.start()

# Ожидание завершения потока;
dict_with_threads["A"].join(timeout=2.1)

# Проверка "is_alive" потоков;
for thread in dict_with_threads.values():
    if thread.is_alive():
        logger.debug(f"Поток {thread.name} не завершил выполнение;")
        print(f"Поток {thread.name} не завершился за установленное время.")
    else:
        logger.debug(f"Поток {thread.name} завершил выполнение;")
        