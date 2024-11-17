"""
17.11.2024
"""

def four_digits_number(number: int) -> tuple[str, ...]:
    """
    Notes:
        Функция принимает на вход четырехзначное число и возвращает кортеж с описанием,
        какая цифра находится в каком разряде.

    Args:
        number (int): четырехзначное число.

    Returns:
        (tuple[str, ...]): кортеж с описанием, какая цифра находится в каком разряде.
    """

    fourth_number: int = number % 10
    third_number: int = (number // 10) % 10
    second_number: int = (number // 100) % 10
    first_number: int = (number // 1000) % 10

    return (
        f"Цифра в позиции тысяч равна {first_number}",
        f"Цифра в позиции сотен равна {second_number}",
        f"Цифра в позиции десятков равна {third_number}",
        f"Цифра в позиции единиц равна {fourth_number}"
    )


if __name__ == "__main__":
    print(*four_digits_number(number=1234), sep="\n")