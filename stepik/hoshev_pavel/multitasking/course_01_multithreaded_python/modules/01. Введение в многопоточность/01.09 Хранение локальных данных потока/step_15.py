"""
22.11..2024
"""

import sys
import threading
import time
import typing

from loguru import logger

# LOGURU;
logger.remove()
logger.add(sink=sys.stderr, level="DEBUG")

# КОНСТАНТЫ;
STUDENTS_INFO: dict[str, dict[str, typing.Any]] = {
    "Варлаам Бирюкова": {
        "Возраст": 25,
        "Специальность": None,
        "Город": None,
        "Страна": "Россия",
        "Университет": "ЗАО «Миронова-Прохоров»",
        "Курс": 3,
        "Группа": "CK008",
        "Электронная почта": "ostaplitkin@example.com",
        "Телефон": None,
        "Дата рождения": "2005-08-22",
        "Пол": "Женский",
        "Хобби": ["Физика", "Астрономия"],
        "Время обработки": 6,
    },
    "Никандр Мамонтов": {
        "Возраст": 20,
        "Специальность": "Компьютерные науки",
        "Город": "к. Октябрьский (Башк.)",
        "Страна": "Россия",
        "Университет": None,
        "Курс": 3,
        "Группа": "LE057",
        "Электронная почта": "jakub_2001@example.org",
        "Телефон": "+7 919 424 9512",
        "Дата рождения": "2002-01-13",
        "Пол": None,
        "Хобби": None,
        "Время обработки": 5,
    },
}

LOCAL_STORAGE = threading.local()


# ЦЕЛЕВАЯ ФУНКЦИЯ;
def thread_function(student_name: str, data: typing.Any, sleep_time: int = 3) -> None:
    # Сохранение локальных данных потока;
    LOCAL_STORAGE.data = data
    logger.debug("Данные помещены в локальное хранилище;")

    # Изменение имени потока;
    threading.current_thread().name = student_name
    logger.debug("Имя потока изменено;")

    # Время обработки данных;
    if (
        "Время обработки" in LOCAL_STORAGE.data.keys()
        and LOCAL_STORAGE.data["Время обработки"] is not None
    ):
        time.sleep(LOCAL_STORAGE.data["Время обработки"] / 10)
    else:
        time.sleep(sleep_time)

    # Вывод данных;
    for key, value in LOCAL_STORAGE.data.items():
        if value is not None:
            logger.info(
                f"Имя потока - {threading.current_thread().name}, локальные данные потока - {key}: {value}"
            )


# Создание потоков;
for student, data in STUDENTS_INFO.items():
    thread = threading.Thread(
        target=thread_function, kwargs={"student_name": student, "data": data}
    )
    thread.start()
