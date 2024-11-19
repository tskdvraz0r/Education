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

# Функция, которая будет выполняться в отдельном потоке;
def task() -> None:
    logger.debug("Поток начал выполнение;")
    for i in range(1, 6):
        print(i)
    logger.debug("Поток завершил выполнение;")

# Создаём и настраиваем новый поток для выполнения функции;
thread: thr.Thread = thr.Thread(target=task)

# Запускаем поток;
thread.start()