"""
23.11.2024
"""

import sys
import threading

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы и переменные;
initial_bid: int = 0
bid_inctement: int = 18
max_bid: int = 175
interval: int = 1
current_bid: int = initial_bid


# Целевая функция;
def increase_bid(
    bid_increment: int, max_bid: int, current_bid: int, interval: int
) -> None:
    if current_bid < max_bid:
        current_bid += bid_increment
        print(f"Текущая ставка: {current_bid} у.е.")
        timer: threading.Timer = threading.Timer(
            interval=interval,
            function=increase_bid,
            args=(bid_increment, max_bid, current_bid, interval),
        )
        timer.start()
    else:
        print("Ставок нет, аукцион завершен!")


# Вызов;
increase_bid(
    bid_increment=bid_inctement,
    max_bid=max_bid,
    current_bid=current_bid,
    interval=interval,
)
