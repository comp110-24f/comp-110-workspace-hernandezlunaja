"""Basic syntax of lists."""

# Create an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

# print(my_numbers)

# String Analogy
# my_name: str = ""  # literal
# my_name: str = str()  # constructor

# Adding a value to a list
my_numbers.append(1.5)
my_numbers.append(2.3)
# Can only append one value at a time
# print(my_numbers)

# Creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
# print(game_points[2])
last_game: int = game_points[2]
# print(last_game)

# Modifying by Index
game_points[1] = 72
print(game_points)

# Getting the Length
len(game_points)  # Don't need print??

# Removing an item
game_points.pop(1)
print(game_points)

# Function name: display
# Parameter: list of integers
# RV: None
# Print every element in the input list
# Call display on game_points


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""
    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
