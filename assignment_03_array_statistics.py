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
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def init_list():
    stop = int(input("\nEnter number of digits to enter: "))

    usr_list = []
    for i in range(0, stop):
        u_int = float(input("\nEnter number " + f"{i} : "))
        usr_list.append(u_int)

    return usr_list




def Sum(this_list):
    sum = 0
    end_pt = len(this_list)
    for itr in range(0, end_pt):
        sum += this_list[itr]

    return int(sum)



def Average(this_list):
    a_sum = 0
    a_ptr = len(this_list)
    for itr in range(0, a_ptr):
        a_sum += this_list[itr]

    return float((a_sum / a_ptr))



def Maximum(this_list):
    this_max = this_list[0]

    for itr in range(0, len(this_list)):
        if this_list[itr] > this_max:
            this_max = this_list[itr]

    return float(this_max)



def Minimum(this_list):
    this_min = this_list[0]

    for itr in range(0, len(this_list)):
        if this_list[itr] < this_min:
            this_min = this_list[itr]

    return float(this_min)




res_list = init_list()
my_sum = Sum(res_list)
my_average = Average(res_list)
my_max = Maximum(res_list)
my_min = Minimum(res_list)

print("\nResults: ")
print("\nSum: " + f"{my_sum}")
print("\nAverage: " + f"{my_average}")
print("\nMaximum: " + f"{my_max}")
print("\nMinimum: " + f"{my_min}")