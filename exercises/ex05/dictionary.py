"""Exercises Number 5, Dictionaries."""

__author__ = "730711502"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert function."""
    new_Dict: dict[str, str] = {}
    key_Storage: list[str] = []
    for key in a:
        if a[key] in key_Storage:
            raise KeyError("Cannot invert this dictionary. At least 2 values are the same.")
        else:
            new_Dict[a[key]] = key
            key_Storage.append(a[key])
    return new_Dict
        

def favorite_color(a: dict[str, str]) -> str:
    """Favorite color function."""
    color_Storage: dict[str, int] = {}
    for key in a:
        if a[key] in color_Storage:
            color_Storage[a[key]] += 1
        else:
            color_Storage[a[key]] = 1
    most_Colors: int = 0
    color: str 
    for key in color_Storage:
        if color_Storage[key] > most_Colors:
            color = key
            most_Colors = color_Storage[key]
    return color


def count(a: list[str]) -> dict[str, int]:
    """Count function."""
    new_Dict: dict[str, int] = {}
    for item in a:
        if item in new_Dict:
            new_Dict[item] += 1
        else:
            new_Dict[item] = 1
    return new_Dict


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    """Alphabetize function."""
    new_Dict: dict[str, list[str]] = {}
    for item in a:
        if item[0].lower() not in new_Dict:
            new_Dict[item[0].lower()] = [item]
        else:
            new_Dict[item[0].lower()].append(item)
    return new_Dict


def update_attendance(a: dict[str, list[str]], day: str, person: str) -> None:
    """Update attendance function."""
    if day.capitalize() in a:
        for persona in a[day.capitalize()]:
            if persona == person:
                return
        a[day.capitalize()].append(person)
    else:
        a[day.capitalize()] = [person]
