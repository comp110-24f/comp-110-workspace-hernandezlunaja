"""Concatenation for Challenge Question 04"""

__author__: str = "730759463"


def concat(str1: str, str2: str) -> str:
    """Concatenates the two input strings"""
    return str1 + str2


word1: str = "happy"
word2: str = "tuesday"

print(concat(word1, word2))

if __name__ == "__main__":
    concat(str1=word1, str2=word2)
