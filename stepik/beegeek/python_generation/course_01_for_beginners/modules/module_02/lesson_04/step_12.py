"""
15.11.2024
"""

def arithmetics_operations(a: int, b: int) -> tuple[str, ...]:
    """
    Notes:
        Функция принимает на вход два целых числа и возвращает кортеж с арифметическими
        операциями над ними: суммой, разностью и произведением.

    Args:
        a (int): Целое число.
        b (int): Целое число.

    Returns:
        (tuple[str, ...]): Кортеж с арифметическими операциями.
    """

    return (
        f"{a} + {b} = {a + b}",
        f"{a} - {b} = {a - b}",
        f"{a} * {b} = {a * b}"
    )


if __name__ == "__main__":
    print(*arithmetics_operations(a=1, b=2), sep="\n")