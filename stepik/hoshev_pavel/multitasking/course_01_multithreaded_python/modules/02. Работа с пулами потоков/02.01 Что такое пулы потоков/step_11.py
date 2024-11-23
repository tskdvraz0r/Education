"""
24.11.2024
"""

import math
import sys
from concurrent.futures import Future, ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


# Целевые функции;
def fib_future() -> None:
    number: int = 20
    result: int = int(
        (((1 + math.sqrt(5)) / 2) ** number - ((1 - math.sqrt(5)) / 2) ** number)
        / math.sqrt(5)
    )
    logger.success(f"20-е число Фибоначчи: {result}")


def sqrt_future() -> None:
    result = sum([math.sqrt(i) for i in range(1, 51)])
    logger.success(f"Сумма квадратных корней чисел от 1 до 50: {result:.4f}")


def fact_future() -> None:
    logger.success(f"Факториал числа 20: {math.factorial(20)}")


# Создание пула потоков;
with ThreadPoolExecutor() as executor:
    # Добавление задач в пул;
    for func in (fib_future, sqrt_future, fact_future):
        future: Future = executor.submit(func)
        future.result()
