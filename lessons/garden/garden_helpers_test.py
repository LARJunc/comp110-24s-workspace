"""Test my garden functions."""

__author__ = "730711502"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_adding_a_flower() -> None:
    """Checks to see if I could add a flower to an empty dictionary."""
    test_Dict: dict[str, list[str]] = {}
    add_by_kind(test_Dict, "flower", "marigold") 
    assert test_Dict == {'flower': ['marigold']}


def test_adding_an_integer() -> None:
    """Checks to see if I could use an integer as an argument for the function."""
    test_Dict: dict[str, list[str]] = {}
    add_by_kind(test_Dict, 4, 3)
    assert test_Dict == {4: [3]}


def test_adding_a_date() -> None:
    """Checks to see if I can input a month and the seeds I want to plant on that month."""
    test_Dict: dict[str, list[str]] = {}
    add_by_date(test_Dict, "May", "Daisies")
    assert test_Dict == {"May": ["Daisies"]}


def test_adding_a_date_with_ints() -> None:
    """Checks to see if I can input a numerical date for the seeds I want to plant."""
    test_Dict: dict[str, list[str]] = {}
    add_by_date(test_Dict, "4-13-24", "Daisies")
    assert test_Dict == {"4-13-24": ["Daisies"]}


def test_looking_up_a_kind_and_date() -> None:
    """Checks to see if I can find the flowers I want to plant in March."""
    test_Dict_Flower: dict[str, list[str]] = {"flower": ["marigold"]}
    test_Dict_March: dict[str, list[str]] = {"March": ["marigold"]}
    assert lookup_by_kind_and_date(test_Dict_Flower, test_Dict_March, "flower", "March") == "flower to plant in March: ['marigold']"


def test_looking_up_a_wrong_kind_and_date() -> None:
    """Checks to see if I can try and find something that I do not plan to plant in a specific month."""
    test_Dict: dict[str, list[str]] = {"roses": ["daisies"]}
    test_Dict_March: dict[str, list[str]] = {"March": ["marigold"]}
    assert lookup_by_kind_and_date(test_Dict, test_Dict_March, "roses", "March") == "No roses to plant in March"



