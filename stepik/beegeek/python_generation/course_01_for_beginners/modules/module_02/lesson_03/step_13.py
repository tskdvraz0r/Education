"""
14.11.2024
"""

def greetings(name: str) -> str:
    """
    Notes:
        Функция принимает на вход имя человека и возвращает строку приветствия.
    Args:
        name (str): Имя человека.
    Returns:
        (str): Строка приветствия: f"Привет, {name}!"
    """

    return f"Привет, {name}!"


if __name__ == "__main__":
    print(greetings(name="Джордж"))