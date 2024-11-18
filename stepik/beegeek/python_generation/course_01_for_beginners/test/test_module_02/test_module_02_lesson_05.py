"""
Тесты функций из урока 4 модуля 2;
"""
import pytest

from modules.module_02.lesson_05.step_13 import geometric_progression
from modules.module_02.lesson_05.step_14 import distance_in_meters
from modules.module_02.lesson_05.step_15 import scholars_and_mandarins
from modules.module_02.lesson_05.step_16 import thanos
from modules.module_02.lesson_05.step_17 import minutes_to_time
from modules.module_02.lesson_05.step_18 import compartment_number
from modules.module_02.lesson_05.step_21 import threedigit_number
from modules.module_02.lesson_05.step_22 import digit_permutations
from modules.module_02.lesson_05.step_23 import four_digits_number


@pytest.mark.parametrize(
        ["test_b", "test_q", "test_n", "expected_result"],
        [
            (1, 2, 5, 16),
            (10, -2, 6, -320),
            (-2, 10, 3, -200)
        ]
)
def test_good_case_geometric_progression(test_b, test_q, test_n, expected_result) -> None:
    assert geometric_progression(b=test_b, q=test_q, n=test_n) == expected_result


@pytest.mark.parametrize(
        ["test_centimeters", "expected_result"],
        [
            (123, 1),
            (100, 1),
            (1000, 10),
        ]
)
def test_good_case_distance_in_meters(test_centimeters, expected_result) -> None:
    assert distance_in_meters(centimeters=test_centimeters) == expected_result


@pytest.mark.parametrize(
        ["test_scholars", "test_mandarins", "expected_result"],
        [
            (3, 6, (2, 0)),
            (12, 6, (0, 6)),
            (7, 4, (0, 4))
        ]
)
def test_good_case_scholars_and_mandarins(test_scholars, test_mandarins, expected_result) -> None:
    assert scholars_and_mandarins(
            scholars=test_scholars,
            mandarins=test_mandarins
    ) == expected_result


@pytest.mark.parametrize(
        ["test_universe_population", "expected_result"],
        [
            (99, 50),
            (1132, 566),
            (1, 1)
        ]
)
def test_good_case_thanos(test_universe_population, expected_result) -> None:
    assert thanos(universe_population=test_universe_population) == expected_result


@pytest.mark.parametrize(
        ["test_minutes", "expected_result"],
        [
            (150, "150 мин - это 2 час 30 минут."),
            (50, "50 мин - это 0 час 50 минут."),
            (240, "240 мин - это 4 час 0 минут.")
        ]
)
def test_good_case_minutes_to_time(test_minutes, expected_result) -> None:
    assert minutes_to_time(minutes=test_minutes) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (1, 1),
            (17, 5),
            (33, 9)
        ]
)
def test_good_case_compartment_number(test_number, expected_result) -> None:
    assert compartment_number(number=test_number) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (123, (6, 6)),
            (333, (9, 27)),
            (101, (2, 0))
        ]
)
def test_good_case_threedigit_number(test_number, expected_result) -> None:
    assert threedigit_number(number=test_number) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (123, ["123", "132", "213", "231", "312", "321"]),
            (987, ["987", "978", "897", "879", "798", "789"]),
            (658, ["658", "685", "568", "586", "865", "856"])
        ]
)
def test_good_case_digit_permutations(test_number, expected_result) -> None:
    assert digit_permutations(number=test_number) == expected_result


@pytest.mark.parametrize(
        ["test_number", "expected_result"],
        [
            (3281, ("Цифра в позиции тысяч равна 3",
                    "Цифра в позиции сотен равна 2",
                    "Цифра в позиции десятков равна 8",
                    "Цифра в позиции единиц равна 1")),
            (9876, ("Цифра в позиции тысяч равна 9",
                    "Цифра в позиции сотен равна 8",
                    "Цифра в позиции десятков равна 7",
                    "Цифра в позиции единиц равна 6")),
            (1234, ("Цифра в позиции тысяч равна 1",
                    "Цифра в позиции сотен равна 2",
                    "Цифра в позиции десятков равна 3",
                    "Цифра в позиции единиц равна 4")),
        ]
)
def test_good_case_four_digits_number(test_number, expected_result) -> None:
    assert four_digits_number(number=test_number) == expected_result