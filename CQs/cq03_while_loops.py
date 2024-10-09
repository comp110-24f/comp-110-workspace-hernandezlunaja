"""Challenge Question 03"""

__author__: str = "730759463"


# I created a function to compare the letters in one phrase to another phrase
def num_instances(phrase: str, search_char: str) -> int:
    # The count is the number of the same letters and the index is the placement of each character
    count: int = 0
    index: int = 0
    # len is the length of a phrase
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count
