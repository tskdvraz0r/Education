"""
Тесты функций из урока 1 модуля 4;
"""
import pytest

from modules.module_04.lesson_01.step_05 import is_passwords_equal
from modules.module_04.lesson_01.step_06 import even_or_odd
from modules.module_04.lesson_01.step_07 import ratio
from modules.module_04.lesson_01.step_08 import roskomnadzor
from modules.module_04.lesson_01.step_09 import arithmetic_progression
from modules.module_04.lesson_01.step_10 import smallest_of_two_numbers
from modules.module_04.lesson_01.step_11 import smallest_of_numbers
from modules.module_04.lesson_01.step_12 import age_group
from modules.module_04.lesson_01.step_13 import sum_only_positive_numbers


@pytest.mark.parametrize(
        ["test_password1", "test_password2", "expected_result"], 
        [
            ('password', 'password', True),
            ('password', 'wrong_password', False),
            ('', '', True)
        ]
)
def test_good_case_is_passwords_equal(
        test_password1,
        test_password2,
        expected_result
) -> None:   
    assert is_passwords_equal(
        password1=test_password1,
        password2=test_password2
    ) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (2, "Четное"),
            (3, "Нечетное"),
            (0, "Четное"),
        ]
)
def test_good_case_even_or_odd(test_number, expected_result) -> None:
    assert even_or_odd(number=test_number) == expected_result


@pytest.mark.parametrize(
    ["test_number", "expected_result"],
    [
        (1614, "ДА"),
        (1234, "НЕТ"),
        (7911, "ДА"),
    ]
)
def test_good_case_ratio(test_number, expected_result) -> None:
    assert ratio(number=test_number) == expected_result


@pytest.mark.parametrize(
    ["test_age", "expected_result"],
    [
        (18, "Доступ разрешен"),
        (17, "Доступ запрещен"),
        (21, "Доступ разрешен"),
    ]
)
def test_good_case_roskomnadzor(test_age, expected_result) -> None:
    assert roskomnadzor(age=test_age) == expected_result


@pytest.mark.parametrize(
        ["test_a", "test_d", "test_n", "expected_result"],
        [
            (1, 1, 10, 10),
            (-1, 1, 2, 0),
            (100, 50, 1, 100)
        ]
)
def test_good_case_arithmetic_progression(
        test_a,
        test_d,
        test_n,
        expected_result
) -> None:
    assert arithmetic_progression(
        a=test_a,
        d=test_d,
        n=test_n
    ) == expected_result


@pytest.mark.parametrize(
    ["test_a", "test_b", "expected_result"],
    [
        (8, 11, 8),
        (20, 5, 5),
        (-12, -20, -20),
    ]
)
def test_good_case_smallest_of_two_numbers(
        test_a,
        test_b,
        expected_result
) -> None:
    assert smallest_of_two_numbers(a=test_a, b=test_b) == expected_result


@pytest.mark.parametrize(
    ["test_args", "expected_result"],
    [
        ((1, 2, 3, 4), 1),
        ((10, 9, 11, 12), 9),
        ((100, 200, 5, 300), 5),
    ]
)
def test_good_case_smallest_of_numbers(test_args, expected_result) -> None:
    assert smallest_of_numbers(*test_args) == expected_result


@pytest.mark.parametrize(
    ["test_age", "expected_result"],
    [
        (4, "детство"),
        (19, "молодость"),
        (25, "зрелость"),
        (67, "старость")
    ]
)
def test_good_case_age_group(test_age, expected_result) -> None:
    assert age_group(age=test_age) == expected_result


@pytest.mark.parametrize(
    ["test_agrs", "expected_result"],
    [
        ((4, -22, 1), 5),
        ((-31, -7, -18), 0),
        ((-4, -11, 5), 5)
    ]
)
def test_good_case_sum_of_positive_numbers(test_agrs, expected_result) -> None:
    assert sum_only_positive_numbers(*test_agrs) == expected_result
