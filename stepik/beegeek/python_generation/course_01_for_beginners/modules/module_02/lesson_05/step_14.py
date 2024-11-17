"""
17.11.2024
"""

def distance_in_meters(centimeters: int) -> int:
    """
    Notes:
        Функция принимает на вход количество сантиметров и возвращает количество метров.

    Args:
        centimeters (int): Количество сантиметров.

    Returns:
        (int): Количество метров.
    """

    return centimeters // 100


if __name__ == "__main__":
    print(distance_in_meters(centimeters=123))
