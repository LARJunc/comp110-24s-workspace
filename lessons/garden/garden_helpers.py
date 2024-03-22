"""Some functions for my garden plan!"""

__author__ = "730711502"


def add_by_kind(a: dict[str, list[str]], b: str, c: str) -> None:
    """Function 1."""
    if b in a:
        a[b].append(c)
    else:
        a[b] = [c]


def add_by_date(a: dict[str, list[str]], b: str, c: str) -> None:
    """Function 2."""
    if b in a:
        a[b].append(c)
    else:
        a[b] = [c]


def lookup_by_kind_and_date(a: dict[str, list[str]], b: dict[str, list[str]], c: str, d: str) -> str:
    """Function 3."""
    plant_Kinds: list[str] = a[c]
    plant_Dates: list[str] = b[d]
    combined: list[str] = []
    for plant in plant_Kinds:
        for other_Plant in plant_Dates:
            if other_Plant == plant:
                combined.append(other_Plant)
    if len(combined) == 0:
        return f"No {c} to plant in {d}"
    else:
        return f"{c} to plant in {d}: {combined}"