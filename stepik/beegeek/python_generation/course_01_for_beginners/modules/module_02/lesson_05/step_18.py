"""
17.11.2024
"""

def compartment_number(number: int) -> int:
    """
    Note:
        Функция принимает на вход целое, положительное число (номер места в вагоне) и возвращает
        номер купе.

    Args:
        number (int): Номер места в вагоне.

    Returns:
        int: Номер купе.
    """

    return ((number - 1) // 4) + 1


if __name__ == "__main__":
    print(compartment_number(number=13))