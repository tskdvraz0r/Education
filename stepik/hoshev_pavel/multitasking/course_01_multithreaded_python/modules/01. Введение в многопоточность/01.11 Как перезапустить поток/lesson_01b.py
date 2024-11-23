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


# КОНСТАНТЫ:
LOCK = threading.Lock()


# ЦЕЛЕВЫЕ ФУНКЦИИ;
def task(thread_id) -> None:
    while True:
        # trunk-ignore(bandit/B311)
        if random.random() < 0.25:
            logger.error(f"Поток: {thread_id} случайно остановлен;")
            break
        logger.success(f"Поток {thread_id} выполнил задачи;")


def restart_thread(thread) -> threading.Thread:
    logger.info("Перезапуск потока...")
    new_thread = threading.Thread(target=task, args=(thread.ident,))
    new_thread.start()
    return new_thread


threads: list = []
for i in range(10):
    thread = threading.Thread(target=task, args=(i,))
    thread.start()
    threads.append(thread)

cnt: int = 0
while cnt < 10:
    for i in range(10):
        threads[i] = restart_thread(threads[i])
    time.sleep(1)
    cnt += 1
