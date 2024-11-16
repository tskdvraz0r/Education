"""
14.11.2024
"""

def repeat_after_me(*args: str) -> tuple[str, ...]:
    """
    Notes:
        Функция принимает на вход строки и возвращает их в том же порядке.

    Args:
        *args (str): Произвольное количество строк.

    Returns:
        (tuple[str, ...]): Строки в том же порядке.
    """

    return args


if __name__ == "__main__":
    words: list[str] = ["I was", "born", "this way"]

    print(*repeat_after_me(*words), sep="\n")