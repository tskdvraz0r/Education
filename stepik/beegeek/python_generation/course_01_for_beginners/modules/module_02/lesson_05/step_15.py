"""
17.11.2024
"""

def scholars_and_mandarins(scholars: int, mandarins: int) -> tuple[int, int]:
    """
    Notes:
        Функция принимает на вход два целых числа: количество школьников и мандаринов.
        Возвращает, по сколько целых мандаринов получит каждый школьник и сколько останется в
        корзине.

    Args:
        scholars (int): количество школьников.
        mandarins (int): количество мандаринов.

    Returns:

    """

    return mandarins // scholars, mandarins % scholars


if __name__ == "__main__":
    print(*scholars_and_mandarins(scholars=10, mandarins=100), sep="\n")