"""
23.11.2024
"""

import sys
import threading
import time

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
aircrafts: dict[str, int] = {
    "Boeing 737": 6,
    "Airbus A320": 9,
    "Boeing 747": 6,
    "Airbus A380": 7,
}


# Целевая функция;
def flight_simlation(model: str, flight_time: int) -> None:
    logger.info(f"{model} начал полет. Время полета: {flight_time} сек.")
    time.sleep(flight_time)
    logger.info(f"{model} завершил полет.")


def count_active_threads() -> None:
    logger.info(
        f"Количество самолетов в воздухе после 5 секунд: {threading.active_count() - 2}"  # MainThread и TimerThread не требуется учитывать
    )


for model, flight_time in aircrafts.items():
    thread: threading.Thread = threading.Thread(
        target=flight_simlation, args=(model, flight_time)
    )
    thread.start()

active_threads_timer: threading.Timer = threading.Timer(
    interval=5, function=count_active_threads
)
active_threads_timer.start()
