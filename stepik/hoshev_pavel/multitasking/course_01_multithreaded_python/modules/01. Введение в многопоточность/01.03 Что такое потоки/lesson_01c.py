"""
19.11.2024
"""
import sys
import time
import typing
import threading as thr

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)


# Создать функция, которая будет выполняться в отдельном потоке;
def task():
    # Определить ID-потока, в котором работает функция;
    task_thread_id: typing.Optional[int] = thr.current_thread().ident
    # Перейти в режим ожидания 1 сек;
    time.sleep(1)
    # Вывести поток, который выполняется;
    logger.debug(f"Это сообщение от задачи task из потока {task_thread_id};")

# Время начала выполнения скрипта;
start: float = time.time()

# Определить ID главного потока и вывести его;
base_thread_id: typing.Optional[int] = thr.current_thread().ident
logger.debug(f"ID главного потока: {base_thread_id};")

# Создать и запустить новый поток для выполнения функции task;
thread: thr.Thread = thr.Thread(target=task)
logger.debug("Запускается новый поток;")
thread.start()

# Вывести сообщение ожидания;
logger.debug("Ожидаем завершения выполнения нового потока;")


# Главный поток переходит в режим ожидания;
time.sleep(1)

# Ожидание завершение задачи и завершения работы нового потока;
thread.join()
logger.debug("Работа нового потока завершена;")
logger.info(f"Время выполнения програмы: {time.time() - start:.4f}")
