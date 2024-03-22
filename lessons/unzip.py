"""Splitting a dictionary into two lists."""

__author__ = "730711502"


def get_keys(a: dict[str, int]) -> list[str]:
    """Getting the keys from the dictionary."""
    key_List: list[str] = []
    for key in a:
        key_List.append(key)
    return key_List


def get_values(a: dict[str, int]) -> list[int]:
    """Getting the values from the dictionary."""
    value_List: list[int] = []
    for key in a:
        value_List.append(a[key])
    return value_List
