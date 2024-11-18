"""
18.11.2024
"""

def smallest_of_two_numbers(a: int, b: int) -> int:
    """
    Notes:
        Функция принимает на вход два целых числа и возвращает наименьшее из них.

    Args:
        a (int): Целое число.
        b (int): Целое число.

    Returns:
        int: Меньшее из чисел.
    """
    
    return min(a, b)


if __name__ == "__main__":
    print(smallest_of_two_numbers(a=1, b=2))