"""
19.11.2024
"""
import sys
import typing
import threading as thr

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)


# Константы;
LIST_WITH_NUMBERS: typing.Final[list[int]] = [123456, 7890123, 987654, 114455, 995423, 1000000]

# Переменные;
total_sum: int = 0

# Функция для вычисления суммы элементов;
def sum_of_numbers() -> None:
    logger.debug("Начало рассчёта суммы списка чисел;")
    global total_sum
    total_sum = sum(LIST_WITH_NUMBERS)
    logger.debug("Конец рассчёта суммы списка чисел;")

# Функция для потока, обрабатывающего список;
def thread_task() -> None:
    logger.debug("Начало работы потока;")
    sum_of_numbers()
    logger.debug("Конец работы потока;")

# Создать поток;
thread: thr.Thread = thr.Thread(target=thread_task)

# Запустить поток;
thread.start()

# Дождаться завершения потока;
thread.join()

# Вывести результат;
print(total_sum)