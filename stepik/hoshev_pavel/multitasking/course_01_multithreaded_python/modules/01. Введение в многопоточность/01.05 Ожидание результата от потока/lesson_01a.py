"""
19.11.2024
Ожидание результата с помощью sleep();
"""
import sys
import time

from loguru import logger


# loguru
logger.remove()
logger.add(
    sink=sys.stderr,
    level="DEBUG"
)

def is_result_available() -> bool:
    """
    Notes:
        Функция для проверки наличия результата.
        В реальном примере здесь могут быть условия проверки результата от другого потока.
    """
    logger.debug("Возврат готовности резульатата;")
    return False

# Цикл ожидания результата;
while not is_result_available():  # Бесконечный цикл
    logger.debug("Ждём результата...")
    time.sleep(5)

logger.debug("Результат получен!")