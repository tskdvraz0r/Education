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
def load_data() -> None:
    logger.debug(f"Загрузка данных начата. Поток: {thr.current_thread().name};")
    time.sleep(2)
    logger.debug(f"Загрузка данных завершена. Поток: {thr.current_thread().name};")

def transform_data() -> None:
    logger.debug(f"Преобразование данных начато. Поток: {thr.current_thread().name};")
    time.sleep(3)
    logger.debug(f"Преобразование данных завершено. Поток: {thr.current_thread().name};")

# Создать потоки с описательными именами;
thread_data_load: thr.Thread = thr.Thread(
    target=load_data,
    name="DataLoad"
)
thread_transform_data: thr.Thread = thr.Thread(
    target=transform_data,
    name="DataTransform"
)

# Запустить потоки;
thread_data_load.start()
thread_transform_data.start()

# Ожидание завершения потоков;
thread_data_load.join()
thread_transform_data.join()
