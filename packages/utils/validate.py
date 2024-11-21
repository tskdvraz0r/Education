# ##################################################
# ИМПОРТЫ
# ##################################################
import os
import typing

from loguru import logger


# ##################################################
# КЛАССЫ
# ##################################################
class Check:
    """
    Класс отвечает за проверки входных данных.

    Methods:
        is_value_type_correct: Метод проверяет тип входных данных на соответствие ожидаемому типу данных.
        is_value_available: Метод принимает на вход значение и список доступных значений. Производит проверку: доступно ли входное значение для использования.
        is_file_exist: Метод проверяет, существует ли файл по переданной ссылке.

    Raises:
        TypeError: f"Некорректный тип данных! Передан: {type(value)}; Ожидался {expected_type};"
        ValueError: f"Недопустимое значение! Передано: {value}; Доступно: {availables};"
        FileNotFoundError: f"Файла по ссылке не существует: {filepath=};"
    """

    # ##################################################
    # МЕТОДЫ КЛАССА
    # ##################################################
    @classmethod
    def is_value_type_correct(
            cls,
            value: typing.Any,
            expected_type: typing.Any
    ) -> None:
        """
        Метод проверяет тип входных данных на соответствие ожидаемому типу данных.

        Args:
            value (typing.Any): Входные данные.
            expected_type (typing.Any): Ожидаемый тип данных.

        Raises:
            TypeError: f"Некорректный тип данных! Передан: {type(value)}; Ожидался {expected_type};"
        """

        # Проверка входных данных;
        if not isinstance(value, expected_type):
            type_error_msg: str = f"Некорректный тип данных! Передан: {type(value)}; Ожидался {expected_type};"
            logger.critical(type_error_msg)
            raise TypeError(type_error_msg)


    @classmethod
    def is_value_available(
            cls,
            value: typing.Any,
            availables: typing.Iterable
    ) -> None:
        """
        Метод принимает на вход значение и список доступных значений. Производит проверку: 
        доступно ли входное значение для использования.

        Args:
            value (typing.Any): Проверяемое значение;
            availables (typing.Iterable): Доступные значения;

        Raises:
            ValueError: f"Недопустимое значение! Передано: {value}; Доступно: {availables};"
        """

        # Проверить тип входных данных;
        Check.is_value_type_correct(
            value=availables,
            expected_type=typing.Iterable
        )

        # Проверить доступность входных данных;
        if value not in availables:
            value_error_msg: str = f"Недопустимое значение! Передано: {value}; Доступно: {availables};"
            logger.critical(value_error_msg)
            raise ValueError(value_error_msg)


    @classmethod
    def is_file_exist(
            cls,
            filepath: str
    ) -> None:
        """
        Метод проверяет, существует ли файл по переданной ссылке.

        Args:
            filepath (str): Ссылка на файл.

        Raises:
            FileNotFoundError: f"Файла по ссылке не существует: {filepath=};"
        """

        # Проверить тип входных данных;
        Check.is_value_type_correct(
            value=filepath,
            expected_type=str
        )

        # Проверить, что файл по ссылке существует;
        if not os.path.isfile(path=filepath):
            file_error_msg: str = f"Файла по ссылке не существует: {filepath=};"
            logger.critical(file_error_msg)
            raise FileNotFoundError(file_error_msg)