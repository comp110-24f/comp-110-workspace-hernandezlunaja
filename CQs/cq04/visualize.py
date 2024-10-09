"""Vicualize for Challenge Question 04"""

__author__: str = "730759463"

from CQs.cq04.concatenation import concat
from CQs.cq04.visualize import get_coords

word1 = x = "123"
word2 = y = "abc"

result = concat(x, y)
print(result)

print(get_coords(x, y))
