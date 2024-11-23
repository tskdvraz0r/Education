"""
22.11.2024
"""

import random
import sys
import threading
import time

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# ЦЕЛЕВАЯ ФУНКЦИЯ;
def task():
    while True:
        thread_id = threading.get_ident()
        # trunk-ignore(bandit/B311)
        if random.random() < 0.25:
            logger.warning(f"Поток: {thread_id} случайно остановлен;")
            break
        logger.debug(f"Поток ID: {thread_id}, выполнение задачи")
        time.sleep(1)


def restart_thread(thread: threading.Thread) -> threading.Thread:
    if not thread.is_alive():
        logger.info("Перезапуск потока;")
        new_thread: threading.Thread = threading.Thread(target=task)
        new_thread.start()
        return new_thread
    return thread


thread = threading.Thread(target=task)
thread.start()


cnt = 0
while cnt < 10:
    thread = restart_thread(thread=thread)
    time.sleep(1)
    cnt += 1
