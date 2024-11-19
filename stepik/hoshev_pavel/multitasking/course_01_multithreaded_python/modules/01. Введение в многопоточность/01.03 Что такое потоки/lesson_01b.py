"""
19.11.2024
"""
import sys
import time
import threading as thr

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)


# Создать функцию, которая будет выполняться в отдельном потоке;
def countdown() -> None:
    logger.debug("Поток начал выполнение;")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    logger.debug("Поток завершил выполнение;")

# Создать поток и передать функцию "countdown" в качестве "target";
thread: thr.Thread = thr.Thread(target=countdown)
logger.debug("Запущен обратный отсчёт;")

# Запуск потока;
thread.start()

# Дождаться завершения выполнения потока;
thread.join()

# Главный поток продолжает свою работу;
logger.debug("Обратный отсчёт завершён. Главный поток продолжает выполнение;")