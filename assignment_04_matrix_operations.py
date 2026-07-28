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

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def Gen_matrix():

    print("\n")

    this_matrix = []
    row_size = int(input("Enter row: "))
    column_size = int(input("Enter column: "))

    print("\n")

    for i in range(row_size):
        while True:
            this_matrix_row = list(map(int, (input(f"Enter row {i}: " ).split())))

            if len(this_matrix_row) == column_size:
                this_matrix.append(this_matrix_row)
                break
            else:
                print(f"Error: enter exactly {column_size} numbers. Try again\n")

    return this_matrix


def Trn_matrix(a_matrix):
    trn_matrix = []

    row = len(a_matrix)
    col = len(a_matrix[0])

    for c in range(col):
        new_row = []
        for r in range(row):
            new_row.append(a_matrix[r][c])
        trn_matrix.append(new_row)

    return trn_matrix

def Add_matrix(m1, m2):
    m_sum = []

    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Error: Matrices provided cannot be added.\n")
        return None

    row = len(m1)
    col = len(m1[0])

    for r in range(row):
        new_row = []
        for c in range(col):
            new_row.append(m1[r][c] + m2[r][c])
        m_sum.append(new_row)

    return m_sum

def Product_matrix(m1, m2):
    if len(m1[0]) != len(m2[0]):
        print("Error: Incompatible matrices\n")
        return None

    row1 = len(m1)
    col1 = len(m1[0])
    col2 = len(m2[0])

    mult_matrix = []
    for r in range(row1):
        new_row = [0] * col2
        mult_matrix.append(new_row)

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                mult_matrix[i][j] += m1[i][k] + m2[k][j]

    return mult_matrix



usr_matrix = Gen_matrix()

print("\nThe actual matrix.\n")
for row in usr_matrix:
    print(*row, sep=" ")


print("\nThe transposed matrix.\n")
utrn_matrix = Trn_matrix(usr_matrix)

for row in utrn_matrix:
    print(*row, sep=" ")


print("\nMatrix addition.\n")
matrix_1 = Gen_matrix()
matrix_2 = Gen_matrix()

sum_matrix = Add_matrix(matrix_1, matrix_2)


print("\nsum of the matrices entered are: \n")
for row in sum_matrix:
    print(*row, sep=" ")


matrix_3 = Gen_matrix()
matrix_4 = Gen_matrix()

mult_res_matrix = Product_matrix(matrix_3, matrix_4)

print("\nproduct of the matrices entered are: \n")
for row in mult_res_matrix:
    print(*row, sep=" ")

