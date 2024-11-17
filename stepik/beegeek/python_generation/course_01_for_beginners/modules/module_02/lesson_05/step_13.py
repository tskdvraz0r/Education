"""
17.11.2024
"""

def geometric_progression(b: int, q: int, n: int) -> int:
    """
    Notes:
        Функция рассиживает геометрическую прогрессию для n-го числа.

    Args:
        b (int): начальное значение.
        q (int): знаменатель прогрессии.
        n (int): n-ое число прогрессии.

    Returns:
        (int): значение геометрической прогрессии для n-го числа.
    """

    return b * q ** (n - 1)


if __name__ == "__main__":
    print(geometric_progression(b=1, q=2, n=5))
