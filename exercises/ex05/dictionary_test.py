"""Dictionary unit testing."""

__author__ = "730711502"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert() -> None:
    """Tests to see if it properly inverts the function."""
    test_New_Dict: dict[str, str] = {"a": "1", "b": "2"}
    test_New_Dict1: dict[str, str] = {"1": "a", "2": "b"}
    assert invert(test_New_Dict) == test_New_Dict1


def test_invert_with_full_words() -> None:
    """Tests to see if it raises."""
    test_New_Dict: dict[str, str] = {"abc": "twelve", "bcd": "thirteen"}
    test_New_Dict1: dict[str, str] = {"twelve": "abc", "thirteen": "bcd"}
    assert invert(test_New_Dict) == test_New_Dict1


def test_with_dict_of_int() -> None:
    """Tests a dictionary of integers."""
    test_New_Dict: dict[int, int] = {4: 1, 9: 2}
    test_New_Dict1: dict[int, int] = {1: 4, 2: 9}
    assert invert(test_New_Dict) == test_New_Dict1


def test_favorite_color_blue() -> None:
    """Tests the favorite color function with the color blue."""
    test_New_Dict: dict[str, str] = {"Alyssa": "Blue", "Jen": "Green", "Guy": "Blue"}
    assert favorite_color(test_New_Dict) == "Blue"


def test_favorite_color_red() -> None:
    """Tests the favorite color function with the color red."""
    test_New_Dict: dict[str, str] = {"Alyssa": "red", "Jen": "red", "Guy": "Blue"}
    assert favorite_color(test_New_Dict) == "red"


def test_favorite_color_with_numbers() -> None:
    """Tests the favorite color function with numbers."""
    test_New_Dict: dict[str, int] = {"Alyssa": 1, "Jen": 1, "Guy": 2}
    assert favorite_color(test_New_Dict) == 1


def test_count() -> None:
    """Tests the count function."""
    test_List: list[str] = ["cheese", "cheese", "banana"]
    test_Dict: dict[str, int] = {"cheese": 2, "banana": 1}
    assert count(test_List) == test_Dict


def test_count_for_colors() -> None:
    """Tests the count function."""
    test_List: list[str] = ["blue", "blue", "green"]
    test_Dict: dict[str, int] = {"blue": 2, "green": 1}
    assert count(test_List) == test_Dict


def test_count_for_numbers() -> None:
    """Tests the count function."""
    test_List: list[int] = [1, 1, 2]
    test_Dict: dict[str, int] = {1: 2, 2: 1}
    assert count(test_List) == test_Dict


def test_alphabetize() -> None:
    """Tests the alphabetize function."""
    test_List: list[str] = ["apple", "airhead", "josefina"]
    test_Dict: dict[str, list[str]] = {"a": ["apple", "airhead"], "j": ["josefina"]}
    assert alphabetizer(test_List) == test_Dict


def test_alphabetize_with_capital_letters() -> None:
    """Tests the alphabetize function with capital letter."""
    test_List: list[str] = ["Apple", "airhead", "Josefina"]
    test_Dict: dict[str, list[str]] = {"a": ["Apple", "airhead"], "j": ["Josefina"]}
    assert alphabetizer(test_List) == test_Dict


def test_alphabetize_with_nothing() -> None:
    """Tests the alphabetize function with nothing."""
    test_List: list[str] = []
    test_Dict: dict[str, list[str]] = {}
    assert alphabetizer(test_List) == test_Dict


def test_update_attendance() -> None:
    """Tests the update attendance function."""
    test_Dict: dict[str, list[str]] = {"Monday": ["James", "Bobby"]}
    test_Dict1: dict[str, list[str]] = {"Monday": ["James", "Bobby", "Miranda"]}
    update_attendance(test_Dict, "Monday", "Miranda")
    assert test_Dict == test_Dict1


def test_update_attendance_lowercase_days() -> None:
    """Tests the update attendance function with lowercase days input."""
    test_Dict: dict[str, list[str]] = {"Monday": ["James", "Bobby"]}
    test_Dict1: dict[str, list[str]] = {"Monday": ["James", "Bobby", "Miranda"]}
    update_attendance(test_Dict, "monday", "Miranda")
    assert test_Dict == test_Dict1


def test_update_attendance_with_a_weird_input() -> None:
    """Tests the update attendance function with a weird input."""
    test_Dict: dict[str, list[str]] = {"Monday": ["James", "Bobby"]}
    test_Dict1: dict[str, list[str]] = {"Monday": ["James", "Bobby"], "Cheese": ["Miranda"]}
    update_attendance(test_Dict, "cheese", "Miranda")
    assert test_Dict == test_Dict1
    