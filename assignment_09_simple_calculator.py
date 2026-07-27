# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


def modulus(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a % b


def exponent(a: float, b: float) -> float:
    return a ** b


def display_menu() -> None:
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_number(prompt: str) -> float | None:
    try:
        return float(input(prompt))
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break

        first = get_number("Enter first number : ")
        if first is None:
            continue
        second = get_number("Enter second number: ")
        if second is None:
            continue

        if choice == "1":
            result = add(first, second)
            print(f"Result: {first} + {second} = {result}")
        elif choice == "2":
            result = subtract(first, second)
            print(f"Result: {first} - {second} = {result}")
        elif choice == "3":
            result = multiply(first, second)
            print(f"Result: {first} * {second} = {result}")
        elif choice == "4":
            result = divide(first, second)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {first} / {second} = {result:.2f}")
        elif choice == "5":
            result = modulus(first, second)
            if result is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {first} % {second} = {result}")
        elif choice == "6":
            result = exponent(first, second)
            print(f"Result: {first} ** {second} = {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

