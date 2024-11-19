"""
19.11.2024
"""
import sys
import threading as thr

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

# Переменные;
total_sum: int = 0
total_prod: int = 1

# Локальные функции;
def sum_of_numbers() -> None:
    logger.debug("Начало расчёта суммы;")
    global total_sum
    total_sum = sum(range(1, 1001))
    logger.debug("Конец расчёта суммы;")

def prod_of_numbers() -> None:
    logger.debug("Начало расчёта произведения;")
    global total_prod
    for i in range(1, 11):
        total_prod *= i
    logger.debug("Конец расчёта произведения;")

# Создать потоки;
thr_sum: thr.Thread = thr.Thread(target=sum_of_numbers)
thr_prod: thr.Thread = thr.Thread(target=prod_of_numbers)

# Запустить потоки;
thr_sum.start()
thr_prod.start()

# Дождаться завершения потоков;
thr_sum.join()
thr_prod.join()

# Вывести результат;
print(
    f"Сумма чисел от 1 до 1000: {total_sum}",
    f"Произведение чисел от 1 до 10: {total_prod}",
    sep="\n"
)