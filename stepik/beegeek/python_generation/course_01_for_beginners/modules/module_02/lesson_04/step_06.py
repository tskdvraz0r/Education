"""
15.11.2024
"""

def three_consecutive_numbers(number: int) -> tuple[int, ...]:
    """
    Notes:
        Функция принимает целое число и возвращает три последовательных целых числа, начиная с
        переданного.

    Args:
        number (int): Целое число.

    Returns:
        (tuple[int]): Три последовательных целых числа, начиная с переданного.
    """

    return number, number + 1, number + 2


if __name__ == "__main__":
    print(*three_consecutive_numbers(number=13), sep="\n")