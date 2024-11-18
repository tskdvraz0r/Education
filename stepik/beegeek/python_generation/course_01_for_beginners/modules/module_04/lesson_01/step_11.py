"""
18.11.2024
"""

def smallest_of_numbers(*args: int) -> int:
    """
    Notes:
        Функция принимает на вход произвольное количество целых чисел и возвращает минимальное из них.
    
    Args:
        *args: Произвольное количество целых чисел.

    Returns:
        int: Целые числа.
    """
    
    return min(args)


if __name__ == "__main__":
    print(smallest_of_numbers(*(3, 5, 2, 4, 6, 7)))