"""
Тесты функций из урока 2 модуля 2;
"""

import pytest

from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_08 import \
    hello_world
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_09 import \
    lucky_sequence_1
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_10 import \
    lucky_sequence_2
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_11 import \
    star_triangle


@pytest.mark.parametrize(
        ["expected_result"],
        [
            ("Здравствуй, мир!",)
        ]
)
def test_good_case_hello_world(expected_result) -> None:
    assert hello_world() == expected_result


@pytest.mark.parametrize(
        ["expected_result"],
        [
            ((4, 8, 15, 16, 23, 42),)
        ]
)
def test_good_case_lucky_sequence(expected_result) -> None:
    assert lucky_sequence_1() == expected_result
    assert lucky_sequence_2() == expected_result


@pytest.mark.parametrize(
    ["expected_result"],
    [
        (["*" * i for i in range(1, 8)], )
    ]
)
def test_good_case_star_triangle(expected_result) -> None:
    assert star_triangle() == expected_result