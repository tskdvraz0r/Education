"""
15.11.2024
"""

def cube(length: int) -> tuple[int, ...]:
    """
    Notes:
        Функция принимает длину ребра куба и возвращает объем и площадь.

    Args:
        length (int): Длина ребра куба.

    Returns:
        (int, int): Объем и площадь куба.
    """

    return length ** 3, 6 * length ** 2


if __name__ == "__main__":
    volume, square = cube(length=5)

    print(
            f"Объем куба: {volume}",
            f"Площадь полной поверхности: {square}",
            sep="\n"
    )
