"""
14.11.2024
"""

def lucky_sequence_1() -> tuple[int, int, int, int, int, int]:
    """
    Notes:
        Функция возвращает счастливую последовательность из сериала LOST;

    Returns:
        tuple[int]: Кортеж с числами.
    """

    return 4, 8, 15, 16, 23, 42


if __name__ == "__main__":
    print(*lucky_sequence_1())
