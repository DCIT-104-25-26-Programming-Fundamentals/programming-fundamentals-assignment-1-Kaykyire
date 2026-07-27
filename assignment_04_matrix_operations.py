# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#


def read_matrix(rows: int, cols: int) -> list[list[int]]:
    matrix: list[list[int]] = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").strip().split()
            if len(row_input) != cols:
                print(f"Please enter exactly {cols} values.")
                continue
            try:
                row = [int(value) for value in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter integers only.")
    return matrix


def print_matrix(matrix: list[list[int]]) -> None:
    if not matrix:
        return
    width = max(len(str(value)) for row in matrix for value in row)
    for row in matrix:
        print(" ".join(str(value).rjust(width) for value in row))


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])
    transposed: list[list[int]] = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed


def add_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows = len(a)
    cols = len(a[0])
    result: list[list[int]] = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result: list[list[int]] = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Error: Rows and columns must be whole numbers.")
    else:
        matrix_a = read_matrix(rows, cols)
        print("\nOriginal Matrix:")
        print_matrix(matrix_a)
        print("\nTransposed Matrix:")
        print_matrix(transpose_matrix(matrix_a))

        print("\n--- Matrix Addition ---")
        try:
            rows_b = int(input("Enter number of rows for matrix 1: "))
            cols_b = int(input("Enter number of columns for matrix 1: "))
            rows_c = int(input("Enter number of rows for matrix 2: "))
            cols_c = int(input("Enter number of columns for matrix 2: "))
        except ValueError:
            print("Error: Rows and columns must be whole numbers.")
        else:
            if rows_b != rows_c or cols_b != cols_c:
                print("Error: Matrices must have the same dimensions for addition.")
            else:
                matrix_b = read_matrix(rows_b, cols_b)
                matrix_c = read_matrix(rows_c, cols_c)
                print("\nMatrix Sum:")
                print_matrix(add_matrices(matrix_b, matrix_c))

        print("\n--- Matrix Multiplication ---")
        try:
            rows_d = int(input("Enter number of rows for matrix A: "))
            cols_d = int(input("Enter number of columns for matrix A: "))
            rows_e = int(input("Enter number of rows for matrix B: "))
            cols_e = int(input("Enter number of columns for matrix B: "))
        except ValueError:
            print("Error: Rows and columns must be whole numbers.")
        else:
            if cols_d != rows_e:
                print("Error: Number of columns in A must equal number of rows in B.")
            else:
                matrix_d = read_matrix(rows_d, cols_d)
                matrix_e = read_matrix(rows_e, cols_e)
                print("\nProduct Matrix:")
                print_matrix(multiply_matrices(matrix_d, matrix_e))

