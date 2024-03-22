"""Mutating functions."""

__author__ = "730711502"


def manual_append(list: list[int], val: int) -> None:
    """Appending values to a list."""
    list.append(val)


def double(list: list[int]) -> None:
    """Doubling each index in a list."""
    index: int = 0
    while index < len(list):
        val: int = list[index] * 2
        list[index] = val
        index += 1
        

array: list[int] = []
manual_append(array, 2)
print(array)
double(array)
print(array)
print(array[2])
