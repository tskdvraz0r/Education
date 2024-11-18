"""
18.11.2024
"""

def ratio(number: int) -> str:
    """
    Notes:
        Функция принимает на вход целое четырёхзначное число и проверяет условие: сумма первогй и последней цифр равна разности второй и третьей.

    Args:
        number (int): Целое четырёхзначное число.

    Returns:
        str: "ДА" или "НЕТ", как результата выполнения условия.
    """
    
    fourth_number: int = number % 10
    third_number: int = (number // 10) % 10
    second_number: int = (number // 100) % 10
    first_number: int = (number // 1000) % 10
    
    return (
        "ДА"
        if (first_number + fourth_number) == (second_number - third_number)
        else "НЕТ"
    )


if __name__ == "__main__":
    print(ratio(number=1614))