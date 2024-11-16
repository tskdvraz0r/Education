"""
15.11.2024
"""

def function_value(a: int, b: int) -> int:
    """
    Notes:
        Функция принимает на вход два целых числа a и b и возвращает значение функции:
     f(a, b) = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41.

    Args:
        a (int): Целое число.
        b (int): Целое число.

    Returns:
        (int): Значение функции.
    """

    return 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41


if __name__ == "__main__":
    print(function_value(a=1, b=1))
