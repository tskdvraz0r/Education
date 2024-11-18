"""
18.11.2024
"""

def age_group(age: int) -> str:
    """
    Notes:
        Функция принимает на вход возраст пользовател и возвращает возрастную группу.

    Args:
        age (int): Возраст пользователя.

    Returns:
        str: Возрастная группа.
    """
    
    match age:
        case _ as age if age <= 13:
            return "детство"
        case _ as age if 14 <= age <= 24:
            return "молодость"
        case _ as age if 25 <= age <= 59:
            return "зрелость"
        case _ as age if age >= 60:
            return "старость"


if __name__ == "__main__":
    print(age_group(age=20))