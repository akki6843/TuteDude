"""
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

filename = "sample.txt"  # Use this file to test the try case.
# filename = "sample1.txt" # Use this file text the exception handling.


try :
    with open(filename) as file:       # Reading the file using with block so that I do not have to worry about explicitly closing.
        lines = file.readlines()           # Reading all the lines in a list for looping them in next set of code

    print("Reading file content:")     # Just a print statement to match the expected output.
    for i, line in enumerate(lines):   # Using enumerate to get the index for better print output
        print(f"Line {i+1}: {line}")  # printing expected output

except FileNotFoundError:   # Exception handling if File not found error
    print(f"Error : The file {filename} was not found ")  # Graceful exit.