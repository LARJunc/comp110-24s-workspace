"""Summing the elements of a list using different loops."""

__author__ = "730711502"


def w_sum(vals: list[float]) -> float:
    """Using while loop."""
    length: int = len(vals) - 1
    idx: int = 0
    sum: float = 0
    while idx <= length:
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """For loop without index tracking."""
    sum: float = 0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Range for loop."""
    sum: float = 0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum
