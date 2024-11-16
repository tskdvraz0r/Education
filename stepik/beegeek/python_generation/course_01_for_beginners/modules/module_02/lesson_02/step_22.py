"""
14.11.2024
"""

def favorite_team(team_name: str) -> str:
    """
    Notes:
        Функция принимает на вход строку с наименованием команды и возвращает фразу:
        f"{team_name} - чемпион!".

    Args:
        team_name (str): Наименование команды.

    Returns:
        (str): Строка: f"{team_name} - чемпион!".
    """

    return f"{team_name} - чемпион!"


if __name__ == "__main__":
    print(favorite_team(team_name="Зенит"))