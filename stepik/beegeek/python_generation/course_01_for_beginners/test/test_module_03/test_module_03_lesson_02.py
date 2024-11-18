"""
Тесты функций из урока 2 модуля 2;
"""
import pytest

from modules.module_03.lesson_02.step_02 import sum_of_squares_and_square_of_sums
from modules.module_03.lesson_02.step_03 import large_number
from modules.module_03.lesson_02.step_04 import reproduction_of_n


@pytest.mark.parametrize(
        ["test_x", "test_y", "expected_result"],
        [
            (3, 2, ("Квадрат суммы 3 и 2 равен 25", "Сумма квадратов 3 и 2 равна 13")),
            (-5, 1, ("Квадрат суммы -5 и 1 равен 16", "Сумма квадратов -5 и 1 равна 26")),
            (17, 0, ("Квадрат суммы 17 и 0 равен 289", "Сумма квадратов 17 и 0 равна 289"))
        ]
)
def test_good_case_sum_of_squares_and_square_of_sums(
        test_x,
        test_y,
        expected_result
) -> None:
    assert sum_of_squares_and_square_of_sums(
        x=test_x,
        y=test_y
    ) == expected_result


@pytest.mark.parametrize(
        ["test_a", "test_b", "test_c", "test_d", "expected_result"],
        [
            (2, 3, 2, 5, 40),
            (1, 1, 1, 1, 2),
            (7, 8, 9, 10, 3492549202)
        ]
)
def test_good_case_large_number(
        test_a,
        test_b,
        test_d,
        test_c,
        expected_result
) -> None:
    assert large_number(
        a=test_a,
        b=test_b,
        c=test_c,
        d=test_d
    ) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (1, 123),
            (2, 246),
            (3, 369)
        ]
)
def test_good_case_reproduction_of_n(
        test_number,
        expected_result
) -> None:
    assert reproduction_of_n(number=test_number) == expected_result