"""
17.11.2024
"""

def large_number(a: int, b: int, c: int, d: int) -> int:
    """
    Notes:
        Функция принимает 4 целых числа и возвращает результат функции: a ** b + c ** d.

    Args:
        a (int): целое число.
        b (int): целое число.
        c (int): целое число.
        d (int): целое число.

    Returns:
        (int): результат функции.
    """

    return a ** b + c ** d


if __name__ == "__main__":
    print(large_number(a=9, b=29, c=7, d=27))