"""
19.11.2024
Ожидание результата с помощью методов wait() и notify()
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

condition: thr.Condition = thr.Condition()
result_ready = False  # Флаг состояния, указывающий на готовность

def preparing_thread() -> None:
    logger.debug("Начало подготовки потока;")
    global result_ready
    with condition:
        logger.debug("Подготовка результата;")
        time.sleep(2)  # Имитация задержки
        result_ready = True  # Смена состояния флага на True
        condition.notify()  # Уведомление о готовности результата

thread: thr.Thread = thr.Thread(target=preparing_thread)
thread.start()

with condition:
    while not result_ready:
        condition.wait()
    logger.debug("Результат готов;")

thread.join()