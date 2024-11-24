"""
24.11.2024
"""

import sys
from concurrent.futures import Future, ThreadPoolExecutor

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
list1: list[str] = ["kw63vdxI", "YmSsWblC", "5OJ3Mto9"]
list2: list[str] = ["7GBrUY6t", "bfQjS3gj", "MhTsKf0X"]
list3: list[str] = ["mt05f80F", "haHHiXoX", "v2cYPhRO"]


# Целевая функция;
def worker(texts: list[str], thread_num: int) -> None:
    for string in texts:
        logger.info(f"Поток {thread_num} извлёк текст из списка: {string}")


# Создание пула потоков;
with ThreadPoolExecutor(max_workers=3) as executor:
    for idx, data in zip((1, 2, 3), (list1, list2, list3)):
        future: Future = executor.submit(worker, texts=data, thread_num=idx)
