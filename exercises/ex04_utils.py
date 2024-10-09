"""EX04 - List utility Functions"""

__author__: str = "730759463"


def all(vals: list[int], input: int) -> bool:
    """Indicate if all the ints in the list are the same as the given int."""
    for input in vals:
        if vals != input:
            return False
    return True


def max(input: list[int]) -> int:
    """Return the largest int in the List."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    largest_num = 0
    for elem in input:
        if elem > largest_num:
            largest_num = elem
    return largest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False

    for elem in list1:
        for elem2 in list2:
            if elem != elem2:
                return False
    return True


def extend(list1: list[int], list2: list[int]) -> list:
    for elem in list2:
        list1.append(elem)
    return list1
