# Стандартные библиотеки;
import typing


# Сторонние библиотеки;
from loguru import logger









class Check:
    
    @classmethod
    def value_type(
            cls,
            value: typing.Any,
            expected_type: typing.Type
    ) -> None:
        """
        Notes:
            Метод принимает на вход данные и ожидаемый тип данных. Производится проверка на 
            соответствие переданного типа данных к ожидаемому.

        Args:
            value (typing.Any): Данные.
            expected_type (typing.Type): Ожидаемый тип данных.

        Raises:
            ValueError: "Некорректный тип данных;"
        """
        
        logger.debug(f"INPUT: {value=};")
        logger.debug(f"INPUT: {expected_type=};")
        
        if not isinstance(value, expected_type):
            logger.critical(f"CHECK: type(value) == expected_type: {type(value) == expected_type};")
            raise ValueError(f"Некорректный тип данных;")
        
        logger.debug(f"CHECK: type(value) == expected_type: {type(value) == expected_type};")