"""
Модуль отвечает за определение затрат времени на выполнение функции;
"""
# ##################################################
# ИМПОРТЫ
# ##################################################
import time
import typing

from loguru import logger

from packages.utils.validate import Check


# ##################################################
# ДЕКОРАТОРЫ
# ##################################################
def time_spend(func):
    """
    Декоратор подсчитывает затраты времени на выполнение переданной функции.

    Args:
        func (typing.Callable[..., None]): Целевая функция.
    """

    # Проверить тип входных данных;
    Check.is_value_type_correct(
        value=func,
        expected_type=typing.Callable
    )

    # Декоратор;
    def wrapper(*args, **kwargs):
        # Время начала выполнения целевой функции;
        script_start_time: float = time.time()

        # Вызов целевой функции;
        func(*args, **kwargs)

        # Время окончания выполнения целевой функции:
        script_end_time: float = time.time()

        # Итого затрачено времени на выполнение целевой функции;
        total_spend_time: str = (
            f"{(script_end_time - script_start_time) // 60:.0f} мин. "
            + f"{(script_end_time - script_start_time) % 60:.0f} сек."
        )
        logger.info(f'Выполнение {func.__name__} заняло: {total_spend_time};')
    return wrapper
