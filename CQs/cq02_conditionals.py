"""Challenge Question 02"""

__author__: str = "730759463"


def guess_a_number() -> None:
    """guessing a number"""
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was", x)
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    elif x > secret:
        print("Your guess was too high! The secret number is", secret)


if __name__ == "__main__":
    guess_a_number()
