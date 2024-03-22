"""List utility functions."""

__author__ = "730711502"


def all(array: list[int], num: int) -> bool:
    """All method."""
    if len(array) == 0: 
        return False
    else:
        for element in array:
            if element != num:
                return False
    return True


def max(array: list[int]) -> int:
    """Max method."""
    if len(array) == 0:
        raise ValueError("max() arg is an empty List.")
    max: int = array[0]
    for elem in array:
        if elem > max:
            max = elem
    return max


def is_equal(array1: list[int], array2: list[int]) -> bool:
    """Is equal method."""
    counter1: int = 0
    counter2: int = 0
    if len(array1) != len(array2):
        return False
    else:
        while counter1 < len(array1) and counter2 < len(array2):
            if array1[counter1] != array2[counter2]:
                return False
            counter1 += 1
            counter2 += 1
    return True
    

def extend(array1: list[int], array2: list[int]) -> None:
    """Extend method."""
    for elem in array2:
        array1.append(elem)
