"""
19.11.2024
"""

import sys
import threading as thr

from loguru import logger

# loguru
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")


def thread_function() -> None:
    logger.debug("Запуск потока;")
    main_thread: thr.Thread = thr.main_thread()
    current_thread: thr.Thread = thr.current_thread()
    if main_thread != current_thread:
        print(
            f"Рабочий поток: {current_thread.name=}, {current_thread.daemon=}, {current_thread.ident=}"
        )
    else:
        print(
            f"Главный поток: {main_thread.name=}, {main_thread.daemon=}, {main_thread.ident=}"
        )
    logger.debug("Завершение потока;")


# Создать и запустить 5 потоков;
for i in range(5):
    thread: thr.Thread = thr.Thread(target=thread_function, name=f"Worker-{i + 1}")
    thread.start()
