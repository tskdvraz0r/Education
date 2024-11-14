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
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_21 import \
    greetings
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_22 import \
    favorite_team
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_23 import \
    repeat_after_me
from stepik.beegeek.python_generation.course_01_for_beginners.modules.module_02.lesson_02.step_24 import \
    repeat_after_me_2


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


@pytest.mark.parametrize(
        ["test_name", "expected_result"],
        [
            ("Джек", "Привет, Джек"),
            ("Джон", "Привет, Джон"),
            ("Джули", "Привет, Джули")
        ]
)
def test_good_case_greetings(
        test_name,
        expected_result
) -> None:
    assert greetings(name=test_name) == expected_result


@pytest.mark.parametrize(
        ["test_team_name", "expected_result"],
        [
            ("Динамо", "Динамо - чемпион!"),
            ("СКА", "СКА - чемпион!"),
            ("Slaughter to Prevail", "Slaughter to Prevail - чемпион!")
        ]
)
def test_good_case_favorite_team(
        test_team_name,
        expected_result
) -> None:
    assert favorite_team(team_name=test_team_name) == expected_result


@pytest.mark.parametrize(
        ["test_args", "expected_result"],
        [
            (("I was", "born", "this way"), ("I was", "born", "this way")),
            (("Let's", "start", "coding"), ("Let's", "start", "coding")),
            (("I", "am", "a", "python", "programmer"), ("I", "am", "a", "python", "programmer"))
        ]
)
def test_good_case_repeat_after_me(
        test_args,
        expected_result
) -> None:
    assert repeat_after_me(*test_args) == expected_result


@pytest.mark.parametrize(
        ["test_args", "expected_result"],
        [
            (("I was", "born", "this way"), ("this way", "born", "I was")),
            (("Let's", "start", "coding"), ("coding", "start", "Let's")),
            (("I", "am", "a", "python", "programmer"), ("programmer", "python", "a", "am", "I"))
        ]
)
def test_good_case_repeat_after_me_2(
        test_args,
        expected_result
) -> None:
    assert repeat_after_me_2(*test_args) == expected_result