"""
15.11.2024
"""

def sum_of_three_numbers(*args: int) -> int:
    """
    Notes:
        Функция принимает три целых числа и возвращает их сумму.

    Args:
        *args (int): Целые числа.

    Returns:
        (int): Сумма переданных чисел.
    """

    return sum(args)


if __name__ == "__main__":
    print(sum_of_three_numbers(1, 2, 3))