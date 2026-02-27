"""
Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
"""
# List comprehension to get the number list

numbers_list = [i for i in range(1,11)]
print(f"Orignal list: {numbers_list}")

# Using Index slicing to get 1st 5 elements,
first_5_numbers_list = numbers_list[:5]
print(f"Extracted first five elements : {first_5_numbers_list}")

# Using negative indexing to reverse the numbers.
reversed_numbers_list = first_5_numbers_list[::-1]
print(f"Reversed extracted elements : {reversed_numbers_list}")

