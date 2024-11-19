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

# Получить объект главного потока;
main_thread: thr.Thread = thr.main_thread()

# Вывести имя главного потока по умолчанию;
logger.info(f"Имя главного потока по умолчанию: {main_thread.name}")

# Установить новое имя главного потока и вывести в стандартный поток;
main_thread.name = "My_main_thread"
logger.info(f"Новое имя главного потока: {main_thread.name}")

# Вывести демонический признак главного потока в стандартный вывод;
logger.info(f"Демонический признак главного потока: {main_thread.daemon}")