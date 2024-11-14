"""
14.11.2024
"""

def i_like_python() -> tuple[str, ...]:
    """
    Returns:
        Функция возвращает кортеж из трёх строк: I like Python.
    """

    return "I", "like", "Python"


if __name__ == "__main__":
    print(*i_like_python(), sep="***")