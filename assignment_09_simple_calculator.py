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

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(n1, n2):
    return n1 + n2

def difference(n1, n2):
    return n1 - n2

def product(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Cannot divide by zero.\n")
        return None
    return round(n1 / n2, 2)

def modulus(n1, n2):
    if n2 == 0:
        print("Error: Cannot perform modulus by zero.\n")
        return None
    return n1 % n2

def exponential(n1, n2):
    return n1 ** n2

def main():
    while True: 
        print("==========================")
        print("        SIMPLE CALCULATOR")
        print("==========================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Quit")

        choice = input("Select an operation (1-7): ")
        print()

        if choice == '7':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                val1 = float(input("Enter first number: "))
                val2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter valid numbers.\n")
                continue

            result = None 
            operation = ""

            if choice == '1':
                result = add(val1, val2)
                operation = "+"
            elif choice == '2':
                result = difference(val1, val2)
                operation = "-"
            elif choice == '3':
                result = product(val1, val2)
                operation = "*"
            elif choice == '4':
                result = divide(val1, val2)
                operation = "/"
            elif choice == '5':
                result = modulus(val1, val2)
                operation = "%"
            elif choice == '6':
                result = exponential(val1, val2)
                operation = "**"

            if result is not None:

                val1_fmt = int(val1) if val1.is_integer() else val1
                val2_fmt = int(val2) if val2.is_integer() else val2 
                res_fmt = int(result) if isinstance(result, float) and result.is_integer() else result

                print(f"Result: {val1_fmt} {operation} {val2_fmt} = {res_fmt}\n")
            else:
                print()
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()