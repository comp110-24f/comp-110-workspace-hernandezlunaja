"""Mutating functions"""

__author__: str = "730759463"


def manual_append(a: list[int], value: int) -> None:
    """Attach the value parameter to the end of the a parameter"""
    a.append(value)


def double(a: list[int]) -> None:
    # Be explicit with the type
    """Mutate the input by multiplying each element in the list by 2"""
    idx = 0
    while idx < len(a):
        # I have to bring the original idx of a to be able to * 2
        a[idx] = a[idx] * 2
        # Add 1 to move to next idx
        idx += 1
    return


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print("list_1:", list_1)
print("list_2:", list_2)
