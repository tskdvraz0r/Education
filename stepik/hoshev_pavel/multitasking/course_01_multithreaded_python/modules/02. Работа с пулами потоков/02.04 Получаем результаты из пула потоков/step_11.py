"""
24.11.2024
"""

import sys
from concurrent.futures import ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
messages: list[str] = [
    "Привет, давайте обсудим многопоточность в Python!",
    "Да, GIL - это большая проблема для многопоточности в Python.",
]


# Целевая функция;
def task(string: str) -> int:
    return len(string)


# Создание пула процессов;
with ThreadPoolExecutor() as executor:
    results = executor.map(task, messages)
    logger.success(f"Общее количество символов в каждой строке: {[i for i in results]}")
