"""
19.11.2024
Ожидание результата с помощью join()
"""
import sys
import time
import threading as thr

from loguru import logger


# logger
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

def task_for_thread2() -> None:
    logger.debug("thread 2 начал выполнение...")
    time.sleep(2)
    logger.debug("thread 2 закончил выполнение...")

def task_for_thread1() -> None:
    logger.debug("thread 1 начал выполнение и ожидает результата от thread 2...")
    
    # Создание и запуск потока thread 2;
    thread2: thr.Thread = thr.Thread(target=task_for_thread2)
    thread2.start()
    
    # Ожидание результата от thread 2;
    thread2.join()
    logger.debug("thread 1 продолжает выполнение...")

# Создание и запуск потока thread 1;
thread1: thr.Thread = thr.Thread(target=task_for_thread1)
thread1.start()
thread1.join()