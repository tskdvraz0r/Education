"""
17.11.2024
"""
import itertools as itt

def digit_permutations(number: int) -> list[int]:
    """
    Notes:
        Функция принимает целое число и возвращает все варианты перестановок его цифр.

    Args:
        number (int): целое число.

    Returns:
        list[int, ...]: список всех вариантов перестановок цифр числа.
    """

    return ["".join(j) for j in list(itt.permutations(str(number)))]


if __name__ == "__main__":
    print(*digit_permutations(number=123), sep="\n")