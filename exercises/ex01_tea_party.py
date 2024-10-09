"""tea party exercise"""

__author__: str = "730759463"


def main_planner(guests: int) -> None:
    """execution of program"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People"
    )  # pay attention to spaces and capitalization
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print(
        "Treats: " + str(treats(people=guests))
    )  # originally calling ints, so convert to str by placing it in front
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """number of tea bags based on attendence"""
    return people * 2


def treats(people: int) -> int:
    """calculate treats based on tea"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """total cost added together"""
    return (tea_count * 0.50) + (treat_count * 0.75)  # use the label names from the def


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
