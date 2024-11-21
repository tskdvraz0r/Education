"""
20.11.2024
"""
import sys
import time
import typing
import threading as thr

from loguru import logger


# loguru;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# Константы;
FILE_NAMES: typing.Final[list[str]] = [
    "file623.xlsx",
    "file538.jpg",
    "file11.rar",
    "file180.jpg",
    "file984.docx"
]

# Переменные;
res: list[str] = []
list_with_etl_threads: list[thr.Thread] = []

# Целевые функции;
def load_file() -> None:
    global file_name
    global res
    
    thread_name: str = thr.current_thread().name
    logger.debug(f"Поток {thread_name} начал выполнение;")
    res.append(f"{thread_name} начал загрузку файла {file_name}.")
    time.sleep(1)
    logger.debug(f"Поток {thread_name} закончил выполнение;")
    res.append(f"{thread_name} завершил загрузку файла {file_name}.")
    

def process_file() -> None:
    global file_name
    global res
    
    thread_name: str = thr.current_thread().name
    logger.debug(f"Поток {thread_name} начал обработку;")
    res.append(f"{thread_name} начал обработку файла {file_name}.")
    time.sleep(1)
    logger.debug(f"Поток {thread_name} закончил обработку;")
    res.append(f"{thread_name} завершил обработку файла {file_name}.")

def save_file() -> None:
    global file_name
    global res
    
    thread_name: str = thr.current_thread().name
    logger.debug(f"Поток {thread_name} начал сохранение;")
    res.append(f"{thread_name} начал сохранение файла {file_name}.")
    time.sleep(1)
    logger.debug(f"Поток {thread_name} закончил сохранение;")
    res.append(f"{thread_name} завершил сохранение файла {file_name}.")

def main(file_name: str) -> None:
    list_with_etl_threads.extend(
        [
            thr.Thread(
                target=load_file,
                name=f"LoadThread-{file_name}"
            ),
            thr.Thread(
                target=process_file,
                name=f"ProcessThread-{file_name}"
            ),
            thr.Thread(
                target=save_file,
                name=f"SaveThread-{file_name}"
            )
        ]   
    )

for file_name in FILE_NAMES:
    main(file_name=file_name)

for thread in list_with_etl_threads:
    thread.start()
    
for thread in list_with_etl_threads:
    thread.join()

for x in res:
    print(x)