"""
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
        1. 	Takes an integer input from the user.
        2. 	Checks whether the number is even or odd using an if-else statement.
        3. 	Displays the result accordingly.
"""

# Collect input from the user
num = int(input("Enter a number: "))

# Checking for ODD and EVEN
# Expect an output string.

if (num%2) == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")