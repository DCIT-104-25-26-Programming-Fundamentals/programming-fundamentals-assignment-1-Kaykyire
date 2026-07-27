# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#


def generate_fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    sequence = [0]
    if n == 1:
        return sequence
    sequence.append(1)
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def is_fibonacci(number: int) -> bool:
    if number < 0:
        return False
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number


if __name__ == "__main__":
    try:
        terms = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
    else:
        if terms <= 0:
            print("Error: Number of terms must be a positive integer.")
        else:
            sequence = generate_fibonacci(terms)
            print("Fibonacci sequence:", " ".join(str(value) for value in sequence))

            try:
                number_to_check = int(input("Enter a number to check: "))
            except ValueError:
                print("Invalid input. Please enter a whole number.")
            else:
                if is_fibonacci(number_to_check):
                    print(f"{number_to_check} is a Fibonacci number.")
                else:
                    print(f"{number_to_check} is NOT a Fibonacci number.")

