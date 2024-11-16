"""
16.11.2024
"""

def divide_and_conquer(number: int) -> tuple[int, ...]:
    """
    Notes:
        Функция принимает на вход целое число и возвращает кортеж: x, 2x, 3x, 4x, 5x.

    Args:
        number (int): Целое число.

    Returns:
        (tuple[int, ...]): x, 2x, 3x, 4x, 5x.
    """

    return number, 2 * number, 3 * number, 4 * number, 5 * number


if __name__ == "__main__":
    print(*divide_and_conquer(number=10), sep="---")