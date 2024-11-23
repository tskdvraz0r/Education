"""
24.11.2024
"""

import sys
import typing
from concurrent.futures import Future, ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
STRINGS: typing.Final[list[str]] = [
    "Да Здравствует ThreadPoolExecutor!!!",
    "Многопоточность в Python позволяет выполнять несколько задач одновременно, улучшая производительность.",
    "Многопоточность может увеличить сложность управления памятью и ресурсами.",
    "Правильное использование многопоточности в Python может значительно улучшить производительность приложений.",
]


# Целевая функция;
def to_uppercase(string: str) -> None:
    logger.success(string.upper())


# Создание пула потоков;
with ThreadPoolExecutor() as executor:
    for string in STRINGS:
        # Добавление задач в пул;
        future: Future = executor.submit(to_uppercase, string)
        # Ожидание результата;
        future.result()
