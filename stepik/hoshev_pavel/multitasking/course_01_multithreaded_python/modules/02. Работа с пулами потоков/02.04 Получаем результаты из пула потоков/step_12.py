"""
24.11.2024
"""

import sys
import typing
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
students: dict[int, dict[str, typing.Any]] = {
    1: {"name": "Alice", "age": 20, "grades": [4, 5, 5, 4, 2, 3, 5, 2]},
    2: {"name": "Bob", "age": 21, "grades": [3, 4, 3, 4, 4, 5, 3, 4, 3, 2, 4]},
    3: {"name": "Charlie", "age": 19, "grades": [5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 4]},
    4: {
        "name": "Hannah Thompson",
        "age": 20,
        "grades": [2, 4, 3, 5, 3, 3, 2, 4, 4, 3, 2, 2, 2, 2, 5, 3, 4, 5],
    },
}


# Целевая функция;
def task(data: dict[str, typing.Any]):
    sum_grades: int = sum(data["grades"])
    logger.debug(f"Сумма оценок: {sum_grades}")
    len_grades: int = len(data["grades"])
    logger.debug(f"Количество оценок: {len_grades}")

    return data["name"], round(sum_grades / len_grades, 2)


# Создание пула потоков;
with ThreadPoolExecutor() as executor:
    result = executor.map(task, list(students.values()))

res_dict: dict[str, float] = dict()
for name, avg in result:
    res_dict[name] = avg

print(res_dict)
