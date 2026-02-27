"""
Task 2: Using the Math Module for Calculations
    Problem Statement: Write a Python program that:
        1.   Asks the user for a number as input.
        2.   Uses the math module to calculate the:
            -   Square root of the number
            -   Natural logarithm (log base e) of the number
            -   Sine of the number (in radians)
3.   Displays the calculated results.

"""

import math

def square_root(num):
    """
    Calculate the square root of a number
    :param num: input number to calculate the square root of
    :return: square root of number
    """
    return math.sqrt(num)

def natural_log(num):
    """
    Calculate the natural logarithm of a number
    :param num: input number to calculate the natural logarithm of
    :return: natural logarithm of number
    """
    return math.log(num)

def  sine(num):
    """
    Calculate the sine of a number
    :param num: input number to calculate the sine of
    :return: sine of number in radian
    """
    return math.sin(num)

def display_output(num):
    """
    Display the calculated results
    """
    print(f"Square root : {square_root(num)}")
    print(f"Logarithm : {natural_log(num)}")
    print(f"Sine : {sine(num)}")

if __name__ == "__main__":
    # Take an input from user
    num = int(input("Enter a number: "))
    # display output

    if num > 0:
        display_output(num)
    else:
        print("Invalid Input !!!")