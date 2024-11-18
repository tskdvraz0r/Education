"""
18.11.2024
"""

def sum_only_positive_numbers(*args: int) -> int:
    """
    Notes:
        Функция принимает на вход целые числа и возвращает сумму положительных чисел.
    
    Args:
        *args (int): Целые числа. 

    Returns:
        int: Сумма положительных чисел.
    """
    
    return sum(i for i in args if i > 0)


if __name__ == "__main__":
    print(sum_only_positive_numbers(-1, 2, -3, 4, 5))