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
def print_from_one_to_five() -> None:
    for i in range(1, 6):
        time.sleep(0.5)
        print(i)
    logger.debug("Функция завершила выполнение;")

def print_from_a_to_e() -> None:
    for i in "abcde":
        time.sleep(0.5)
        print(i)
    logger.debug("Функция завершила выполнение;")

# Создать и запустить потоки;
thread1: thr.Thread = thr.Thread(target=print_from_one_to_five)
thread2: thr.Thread = thr.Thread(target=print_from_a_to_e)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Готово!")