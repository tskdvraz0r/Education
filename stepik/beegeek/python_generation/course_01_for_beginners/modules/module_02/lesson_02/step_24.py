"""
14.11.2024
"""

def repeat_after_me_2(*args: str) -> tuple[str, ...]:
    """
    Notes:
        Функция принимает на вход строки и возвращает их в обратном порядке.
    Args:
        *args (str): Произвольное количество строк.
    Returns:
        (tuple[str, ...]): Строки в обратном порядке.
    """

    return args[::-1]


if __name__ == "__main__":
    words: list[str] = ["I was", "born", "this way"]

    print(*repeat_after_me_2(*words), sep="\n")