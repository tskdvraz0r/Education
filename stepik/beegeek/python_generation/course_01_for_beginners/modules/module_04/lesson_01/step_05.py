"""
18.11.2024
"""

def is_passwords_equal(password1: str, password2: str)-> bool:
    """
    Notes:
        Функция прнимает на вход два пароля и сравнивает их на идентичность.

    Args:
        password1 (str): Первый пароль.
        password2 (str): Второй пароль.

    Returns:
        bool: Идентичны ои пароли.
    """

    return password1 == password2


if __name__ == "__main__":
    print(is_passwords_equal(password1="password", password2="password"))