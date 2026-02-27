"""
Task 1: Calculate Factorial Using a Function
    Problem Statement: Write a Python program that:
        1.   Defines a function named factorial that takes a number as an
            argument and calculates its factorial using a loop or recursion.
        2.   Returns the calculated factorial.
        3.   Calls the function with a sample number and prints the output.
"""

def factorial(num):
    """
    Factorial function, calculating factorial using a recursion.
    :param num: input number for which the factorial is calculated
    :return:  factorial
    """
    if num == 1:    # Checking the exit condition
        return 1
    else:
        return num * factorial(num-1)     # Recursive Call to the function


if __name__ == "__main__":
    # Take an input from user for which the factorial is yo be calculated
    num = int(input("Enter a number: "))

    if num > 0:
        # Calculate the factorial for the number and print the output.
        print(f"The factorial of {num} is {factorial(num)}")
    else :
        print(f"The factorial of {num} not possible. Invalid Input !")