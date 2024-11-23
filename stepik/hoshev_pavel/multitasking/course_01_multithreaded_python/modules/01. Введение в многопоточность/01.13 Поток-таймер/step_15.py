"""
22.11.2024
"""

import sys
import threading

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Переменные и константы;
astronauts: list[str] = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks: list[str] = [
    "Ремонт оборудования",
    "Проведение экспериментов",
    "Мониторинг систем",
]
intervals: list[float] = [0.7, 1.3, 1.8]


# Целевая функция;
def space_station(
    intervals: list[float], astronauts: list[str], tasks: list[str]
) -> None:
    astronaut: str = astronauts.pop(0)
    task: str = tasks.pop(0)
    interval: float = intervals.pop(0)
    print(f"{astronaut} выполняет задачу: {task}")
    if astronauts:
        thread_timer: threading.Timer = threading.Timer(
            interval=interval,
            function=space_station,
            args=(intervals, astronauts, tasks),
        )
        thread_timer.start()


space_station(intervals=intervals, astronauts=astronauts, tasks=tasks)
