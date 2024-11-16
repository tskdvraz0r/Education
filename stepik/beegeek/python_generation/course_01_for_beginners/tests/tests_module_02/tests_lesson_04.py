"""
Тесты функций из урока 4 модуля 2;
"""
import pytest

from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_06 import three_consecutive_numbers
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_07 import sum_of_three_numbers
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_08 import cube
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_09 import function_value
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_10 import next_and_prev_numbers
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_11 import purchase_price
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_12 import arithmetics_operations
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_13 import arithmetic_progression
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_04.step_14 import divide_and_conquer


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (1, (1, 2, 3)),
            (2, (2, 3, 4)),
            (3, (3, 4, 5)),
        ]
)
def test_good_case_three_consecutive_numbers(
        test_number: int,
        expected_result: tuple,
) -> None:
    assert three_consecutive_numbers(number=test_number) == expected_result


@pytest.mark.parametrize(
        ["test_numbers", "expected_result"],
        [
            ((1, 2, 3), 6),
            ((1, 2, 3, 4),  10),
            ((10, 20, 30), 60)
        ]
)
def test_good_case_sum_of_three_numbers(
        test_numbers,
        expected_result: int,
) -> None:
    assert sum_of_three_numbers(*test_numbers) == expected_result


@pytest.mark.parametrize(
        ["test_length", "expected_result"],
        [
            (25, (15625, 3750)),
            (13, (2197, 1014)),
            (56, (175616, 18816))
        ]
)
def test_good_case_cube(
        test_length,
        expected_result
) -> None:
    assert cube(length=test_length) == expected_result


@pytest.mark.parametrize(
        ["test_a", "test_b", "expected_result"],
        [
            (1, 1, 131),
            (1, 0, -165),
            (0, 1, 237)
        ]
)
def test_good_case_function_value(
        test_a,
        test_b,
        expected_result
) -> None:
    assert function_value(a=test_a, b=test_b) == expected_result


@pytest.mark.parametrize(
    ["number", "result"],
    [
        (20, (21, 19)),
        (0, (1, -1)),
        (-10, (-9, -11))
    ]
)
def test_good_case_next_and_prev_numbers(number, result) -> None:
    assert next_and_prev_numbers(number) == result


@pytest.mark.parametrize(
        ["test_prices", "expected_result"],
        [
            ((9900, 55600, 3999, 2990), 217467),
            ((15700, 80550, 12050, 5890), 342570),
            ((44990, 123300, 19600, 8990), 590640)
        ]
)
def test_good_case_purchase_price(
        test_prices,
        expected_result
) -> None:
    assert purchase_price(*test_prices) == expected_result


@pytest.mark.parametrize(
        ["test_a", "test_b", "expected_result"],
        [
            (2, 7, ("2 + 7 = 9", "2 - 7 = -5", "2 * 7 = 14")),
            (5, 8, ("5 + 8 = 13", "5 - 8 = -3", "5 * 8 = 40")),
            (10, 10, ("10 + 10 = 20", "10 - 10 = 0", "10 * 10 = 100"))
        ]
)
def test_good_case_arithmetics_operations(
        test_a,
        test_b,
        expected_result
) -> None:
    assert arithmetics_operations(a=test_a, b=test_b) == expected_result


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
    assert arithmetic_progression(a=test_a, d=test_d, n=test_n) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (7, (7, 14, 21, 28, 35)),
            (1, (1, 2, 3, 4, 5)),
            (5, (5, 10, 15, 20, 25))
        ]
)
def test_good_case_divide_and_conquer(test_number, expected_result) -> None:
    assert divide_and_conquer(number=test_number) == expected_result