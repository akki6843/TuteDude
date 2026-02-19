"""
Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
            1.   Uses a for loop to iterate over numbers from 1 to 50.
            2.   Calculates the sum of all integers in this range.
            3.   Displays the final sum.
"""

# Creating an empty list to store the numbers
sum_lst = []

# Looping through the number and storing them into the list using append function
for i in range(1,51):
    sum_lst.append(i)

# Getting the expected result
print(f"The sum of numbers from 1 to 50 is: {sum(sum_lst)}")