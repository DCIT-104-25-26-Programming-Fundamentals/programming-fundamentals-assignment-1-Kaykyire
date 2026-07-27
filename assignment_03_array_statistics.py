# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# --------------# --------------# --------------# --------------# --------------# --------------# --------------# --------------# --------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#


def calculate_sum(numbers: list[float]) -> float:
    total = 0.0
    for value in numbers:
        total += value
    return total


def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return calculate_sum(numbers) / len(numbers)


def find_max(numbers: list[float]) -> float:
    highest = numbers[0]
    for value in numbers:
        if value > highest:
            highest = value
    return highest


def find_min(numbers: list[float]) -> float:
    lowest = numbers[0]
    for value in numbers:
        if value < lowest:
            lowest = value
    return lowest


if __name__ == "__main__":
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid integer.")
    else:
        if count <= 0:
            print("Error: Number of values must be a positive integer.")
        else:
            numbers: list[float] = []
            for i in range(1, count + 1):
                while True:
                    try:
                        num = float(input(f"Enter number {i}: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                numbers.append(num)

            total = calculate_sum(numbers)
            avg = calculate_average(numbers)
            maximum = find_max(numbers)
            minimum = find_min(numbers)

            print("\nResults:")
            print(f"Sum:     {total}")
            print(f"Average: {avg}")
            print(f"Maximum: {maximum}")
            print(f"Minimum: {minimum}")
