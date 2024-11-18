"""
17.11.2024
"""

def reproduction_of_n(number: int) -> str:
    """
    Notes:
        Функция принимает на вход цифру и возвращает результат функции: n + nn + nnn

    Args:
        number (int): цифра.

    Returns:
        (int): результат функции.
    """

    return number + int(str(number) * 2) + int(str(number) * 3)


if __name__ == "__main__":
    print(reproduction_of_n(number=4))