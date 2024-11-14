"""
14.11.2024
"""

def star_triangle() -> list[str]:
    """
    Notes:
        Функция возвращает список со строками, которые при построчной распаковке образуют треугольник.
    Returns:
        list[str]: Список со строками.
    """

    return ["*" * i for i in range(1, 8)]


if __name__ == "__main__":
    print(*star_triangle(), sep="\n")
