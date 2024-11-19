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
ARRAY_DESCENDING: typing.Final[list[int]] = [733, 725, 606, 544, 526, 496, 448, 389, 345, 239]
ARRAY_ASCENDING: typing.Final[list[int]] = [124, 168, 350, 389, 419, 428, 501, 662, 760, 829]
SYMBOLS_ARRAY: typing.Final[list[str]] = ['g', 'e', 'k', 'a', 'w', 'z', 'o', 'b', 'm', 'l', 'h', 'n', 'd', 's', 'q']

# Локальные функции;
def sort_array_descending() -> None:
    logger.debug("Начало сортировки по убыванию;")
    global ARRAY_DESCENDING
    ARRAY_DESCENDING.sort(reverse=True)
    logger.debug("Сортировка по убыванию завершена;")

def sort_array_ascending() -> None:
    logger.debug("Начало сортировки по возрастанию;")
    global ARRAY_ASCENDING
    ARRAY_ASCENDING.sort()
    logger.debug("Сортировка по возрастанию завершена;")

def sort_symbols_array() -> None:
    logger.debug("Начало сортировки массива символов;")
    global SYMBOLS_ARRAY
    SYMBOLS_ARRAY.sort()
    logger.debug("Сортировка массива символов завершена;")

# Создание потоков;
thread1: thr.Thread = thr.Thread(target=sort_array_descending)
thread2: thr.Thread = thr.Thread(target=sort_array_ascending)
thread3: thr.Thread = thr.Thread(target=sort_symbols_array)

# Запуск потоков;
thread1.start()
thread2.start()
thread3.start()

# Ожидание завершения потоков;
thread1.join()
thread2.join()
thread3.join()

# Вывод результатов;
print(
    f"Массив чисел (по убыванию): {ARRAY_DESCENDING}",
    f"Массив чисел (по возрастанию): {ARRAY_ASCENDING}",
    f"Массив символов (лексикографический порядок): {SYMBOLS_ARRAY}",
    sep="\n"
)