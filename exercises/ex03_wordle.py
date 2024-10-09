"""EX03 - Structured Wordle"""

__author__: str = "730759463"


def input_guess(correct_len: int) -> str:
    """Guessing a word of the correct length"""
    # Use an f string to be able to change the correct len needed
    user_input: str = input(f"Enter a {correct_len} character word: ")
    while len(user_input) != correct_len:
        # Use an f string to allow a new input guess
        new_input: str = input(f"That wasn't {correct_len} chars! Try again: ")
        # Set equal to each other so the new input in stored back in line 8
        user_input = new_input
    # return outside of the while loop to evaluate if it is the correct length again
    return user_input


def contains_char(secret_word: str, char_guess: str) -> bool:
    """A single character that is being searched for in a string"""
    assert len(char_guess) == 1
    # Remember to state the starting index
    idx = 0
    while idx < len(secret_word):
        # Look back at docstring
        if char_guess == secret_word[idx]:
            # Line 18 says we will return a bool T or F
            return True
        # Add to the idx to go through each idx
        idx += 1
    # Line 18 says we will return a bool T or F
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Compare two strings of equal length"""
    assert len(secret_word) == len(user_guess)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx = 0
    # boxes is where we are building the result
    boxes = ""
    while idx < len(secret_word):
        # make sure these are in the same order as in line 34
        if user_guess[idx] == secret_word[idx]:
            boxes += GREEN_BOX
        elif contains_char(secret_word, user_guess[idx]):
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        idx += 1
    return boxes


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(correct_len=len(secret))
        print(emojified(secret_word=secret, user_guess=guess))
        # this is the easiest way to know when all boxes are green and the user won
        if secret == guess:
            print(f"You won in {turns}/6 turns!")
            # return will make it end
            return
        turns += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
