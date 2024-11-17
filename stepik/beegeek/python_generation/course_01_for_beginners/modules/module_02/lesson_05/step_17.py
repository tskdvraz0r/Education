"""
17.11.2024
"""

def minutes_to_time(minutes: int) -> str:
    """
    Notes:
        Функция принимает на вход количество минут и возвращает количество часов и минут.

    Args:
        minutes (int): количество минут.

    Returns:
        (str): количество часов и минут.
    """

    return f"{minutes} мин - это {minutes // 60} час {minutes % 60} минут."


if __name__ == "__main__":
    print(minutes_to_time(minutes=150))