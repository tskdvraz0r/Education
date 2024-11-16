"""
15.11.2024
"""

def next_and_prev_numbers(number: int) -> tuple[int, int]:
    """
    Notes:
        Функция принимает число и возвращает кортеж из двух чисел:
    первое - следующее за ним число, второе - предыдущее.

    Args:
        number (int): Целое число.

    Returns:
        (tuple[int, int]): Кортеж из двух чисел.
    """

    return number + 1, number - 1


if __name__ == "__main__":
    num: int = 13
    next_num, prev_num = next_and_prev_numbers(number=num)

    print(
            f"Следующее за числом {num} число: {next_num}",
            f"Для числа {num} предыдущее число: {prev_num}",
            sep="\n"
    )
