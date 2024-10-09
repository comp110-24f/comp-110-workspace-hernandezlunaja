"""Summing the elements of a list using different loops"""

__author__: str = "730759463"


def w_sum(vals: list[float]) -> float:
    """Return the sum of all elements using a while loop."""
    # Need an idx to start a while loop
    idx: int = 0
    sum = 0.0
    while idx < len(vals):
        # Adding each val to the sum
        sum += vals[idx]
        # Remember to increase the idx
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Return the sum of all elements using a for...in... loop."""
    sum = 0.0
    # Takes each elem in vals
    for elem in vals:
        # Adding each elem to the sum
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Return the sum of all elements using a for...in range(...) loop."""
    sum = 0.0
    # The range starts at 0 and ends at len-1
    for elem in range(0, len(vals)):
        # Using elem as my idx
        sum += vals[elem]
    return sum
