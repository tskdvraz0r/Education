"""
14.11.2024
"""

def custom_sep(sep: str, *args: str) -> str:
    """
    Notes:
        Функция принимает на вход разделитель и кортеж со строками. Формирует единую строку,
        использую переданный разделитель.

    Args:
        sep (str): Разделитель.
        *args (str): Кортеж со строками.

    Returns:
        (str): Созданная строка.
    """

    return sep.join(args)


if __name__ == "__main__":
    words: tuple[str, ...] = ("Times", "New", "Roman")
    print(custom_sep("-", *words))
