"""
19.11.2024
"""
import sys
import threading
import time

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

# Создайте целевую функцию;
def print_from_one_to_five() -> None:
    logger.debug("Начало работы потока;")
    for i in range(1, 6):
        time.sleep(0.5)
        print(i)
    logger.debug("Завершение работы потока;")

def print_from_six_to_ten() -> None:
    logger.debug("Начало работы потока;")
    for i in range(6, 11):
        time.sleep(1)
        print(i)
    logger.debug("Завершение работы потока;")

# Создайте и запустите потоки согласно условию задачи;
thread1: threading.Thread = threading.Thread(target=print_from_one_to_five)
thread2: threading.Thread = threading.Thread(target=print_from_six_to_ten)

thread1.start()
thread2.start()

# Дождитесь завершения потоков;
thread1.join()
thread2.join()

# Не забудьте вывести информацию о завершении работы потоков;
print("Оба потока завершили свою работу.")