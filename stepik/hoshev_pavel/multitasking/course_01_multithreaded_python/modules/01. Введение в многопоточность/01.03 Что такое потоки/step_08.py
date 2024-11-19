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
LIST_WITH_NUMBERS: typing.Final[list[int]] = [
    456, 467, 961, 561, 512, 740, 6412, 464, 444, 102, 456, 347, 905, 854, 901, 326, 267, 236, 790, 235, 745, 769, 467, 734, 745, 895, 445, 312, 123, 451, 523, 567, 344, 234
]

# Переменные;
sum_even: int = 0
sum_odd: int = 0

# Локальные функции;
def sum_of_even() -> None:
    logger.debug("Начало расчёта суммы нечётных чисел;")
    global sum_even
    sum_even = sum(i for i in LIST_WITH_NUMBERS if i % 2 == 0)
    logger.debug("Конец расчёта суммы нечётных чисел;")

def sum_of_odd() -> None:
    logger.debug("Начало расчёта суммы чётных чисел;")
    global sum_odd
    sum_odd = sum(i for i in LIST_WITH_NUMBERS if i % 2 != 0)
    logger.debug("Конец расчёта суммы чётных чисел;")

# Создание потока;
thread_even: thr.Thread = thr.Thread(target=sum_of_even)
thread_odd: thr.Thread = thr.Thread(target=sum_of_odd)

# Запуск потока;
thread_even.start()
thread_odd.start()

# Ожидание завершения потока;
thread_even.join()
thread_odd.join()

# Вывод результата;
print(
    f"Сумма четных чисел: {sum_even}",
    f"Сумма нечетных чисел: {sum_odd}",
    sep="\n"
)