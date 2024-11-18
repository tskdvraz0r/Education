"""
18.11.2024
"""

def even_or_odd(number: int) -> str:
    """
    Notes:
        Функция принимает на вход целое число и проверяет чётное оно или нет.
    
    Args:
        number (int): Целое число.

    Returns:
        str: Четное число или Нечетное.
    """
    
    return "Четное" if number % 2 == 0 else "Нечетное"


if __name__ == "__main__":
    print(even_or_odd(number=5))