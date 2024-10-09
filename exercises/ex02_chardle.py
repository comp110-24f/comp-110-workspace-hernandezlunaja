"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730759463"


def input_word() -> str:
    """Function for entering a 5-character word."""
    # This is the local variable to ask for a 5 letter word.  Remember the formatting.
    word: str = input("Enter a 5-character word: ")
    # Think: What length would make the error message appear?
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


# Same thinking as for the input_word definition
def input_letter() -> str:
    """Function for entering a single letter."""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """Function to search for the letter inside of the word."""
    # Start at 0. Make sure lengths for letter and word are followed before the message is printed.
    count: int = 0
    # if len(letter) == 1 and len(word) == 5:
    print("Searching for " + letter + " in " + word)
    # Go through each index individually.
    if letter == word[0]:
        count = count + 1
        print(letter + " found at index 0")
    if letter == word[1]:
        count = count + 1
        print(letter + " found at index 1")
    if letter == word[2]:
        count = count + 1
        print(letter + " found at index 2")
    if letter == word[3]:
        count = count + 1
        print(letter + " found at index 3")
    if letter == word[4]:
        count = count + 1
        print(letter + " found at index 4")
    # Count?
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    elif count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
