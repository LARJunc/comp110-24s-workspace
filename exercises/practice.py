def odd_and_even(arg: list[int]) -> list[int]:
    idx_tracker: int = 0
    new_list: list[int] = []
    for elem in arg:
        if elem % 2 == 1 and idx_tracker % 2 == 0:
            new_list.append(elem)
        idx_tracker += 1
    return new_list

def value_exist(dict: dict[str,int], a: int) -> bool:
    for key in dict:
        if dict[key] == a:
            return True
    return False

def short_words(list: list[str]) -> list[str]:
    a: list[str] = []
    for element in list:
        if len(element) < 5:
            a.append(element)
    return a

a: list[str] = ["cheese", "poop", "toot"]
print(short_words(a))



def shrink(a: list[int]) -> list[int]:
    """Get values of list that are even and < 13."""
    new_List: list[int] = list()
    for item in a:
        if item % 2 == 0 and item < 13:
            new_List.append(item)
    return new_List

stats: list[int] = [7,8,9]
total: int = 100
for item in stats:
    total -= item

stats: list[int] = [7,8,9]
total: int = 100
for idx in range(0, len(stats)):
    total -= stats[idx]

stats.pop(1)
print(stats)