"""
17.11.2024
"""

def threedigit_number(number: int) -> tuple[int, int]:
    """
    Notes:
        Функция принимает на вход целое трёхзначное число и возвращает сумму и произведение его цифр.

    Args:
        number (int): трёхзначное число.

    Returns:
        (tuple[int, int]): сумма и произведение цифр трёхзначного числа.
    """

    a: int = number % 10
    b: int = (number // 10) % 10
    c: int = (number // 100) % 10

    return a + b + c, a * b * c


if __name__ == "__main__":
    sum_of_digits, prod_of_digits = threedigit_number(number=123)
    print(
        f"Сумма цифр = {sum_of_digits}",
        f"Произведение цифр = {prod_of_digits}",
        sep="\n"
    )