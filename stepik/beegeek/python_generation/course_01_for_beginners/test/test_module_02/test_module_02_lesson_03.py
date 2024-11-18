"""
Тесты функций из урока 3 модуля 2;
"""
import pytest

from modules.module_02.lesson_03.step_12 import i_like_python
from modules.module_02.lesson_03.step_13 import greetings
from modules.module_02.lesson_03.step_14 import custom_sep


@pytest.mark.parametrize(
        ["expected_result"],
        [
            (("I", "like", "Python"),)
        ]
)
def test_good_case_i_like_python(expected_result) -> None:
    assert i_like_python() == expected_result


@pytest.mark.parametrize(
        ["test_name", "expected_result"],
        [
            ("Джек", "Привет, Джек!"),
            ("Джон", "Привет, Джон!"),
            ("Джули", "Привет, Джули!")
        ]
)
def test_good_case_greetings(
        test_name,
        expected_result
) -> None:
    assert greetings(name=test_name) == expected_result


@pytest.mark.parametrize(
        ["test_sep", "test_strings", "expected_result"],
        [
            ("*", ("1", "2", "3"), "1*2*3"),
            (",", ("1", "2", "3"), "1,2,3"),
            (";", ("1", "2", "3"), "1;2;3"),
        ]
)
def test_good_case_custom_sep(
        test_sep,
        test_strings,
        expected_result
) -> None:
    assert custom_sep(test_sep, *test_strings) == expected_result
