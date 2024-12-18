"""
18.11.2024
"""

def roskomnadzor(age: int) -> str:
    """
    Notes:
        Функци принимает целое число - возраст пользователя, и определяет, разрешён ли доступ к ресурсу.

    Args:
        age (int): Целое число - возраст пользователя.

    Returns:
        str: Разрешён ли доступ к ресурсу.
    """
    
    return "Доступ разрешен" if age >= 18 else "Доступ запрещен"


if __name__ == "__main__":
    print(roskomnadzor(age=18))