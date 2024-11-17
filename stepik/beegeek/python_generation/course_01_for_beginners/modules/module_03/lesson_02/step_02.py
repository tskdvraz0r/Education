"""
17.11.2024
"""

def sum_of_squares_and_square_of_sums(x: int, y: int) -> tuple[str, ...]:
    """
    Notes:
        Функция принимает на вход два числа и возвращает квадрат их суммы и сумму их квадратов.

    Args:
        x (int): целое число.
        y (int): целое число.

    Returns:
        tuple[str, ...]: квадрат суммы и сумма квадратов.
    """

    return (
        f"Квадрат суммы {x} и {y} равен {(x + y) ** 2}",
        f"Сумма квадратов {x} и {y} равна {x ** 2 + y ** 2}"
    )


if __name__ == "__main__":
    print(*sum_of_squares_and_square_of_sums(x=3, y=2), sep="\n")