"""
17.11.2024
"""

def thanos(universe_population: int) -> int:
    """
    Notes:
        Функция принимает на вход население вселенной и возвращает количество выживших после
        щелчка Таноса.

    Args:
        universe_population (int): население вселенной.

    Returns:
        (int): количество выживших после щелчка Таноса.
    """

    return universe_population // 2 + universe_population % 2


if __name__ == "__main__":
    print(thanos(universe_population=1))