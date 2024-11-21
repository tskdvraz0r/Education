"""
20.11.2024
"""
import sys
import time
import threading as thr

from loguru import logger


# loguru:
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

# Целевая функция;
def thread_task() -> None:
    logger.debug(f"Поток {thr.current_thread().name} начал выполнение;")
    time.sleep(3)
    logger.debug(f"Поток {thr.current_thread().name} завершил выполнение;")

# словарь для контроля потоков;
dict_with_threads: dict = {}

# Создаём и созраняем потоки с уникальными именами;
for i in range(5):
    thread_name: str = f"Worker-{i}"
    dict_with_threads[thread_name] = thr.Thread(
        target=thread_task,
        name=thread_name
    )

# Запускаем потоки;
for thread in dict_with_threads.values():
    thread.start()

# Допустим, нам необходимо дождаться завершения работы Worker-2;
dict_with_threads["Worker-2"].join()

# Ожидаем завершения работы остальных потоков;
for thread in dict_with_threads.values():
    thread.join()