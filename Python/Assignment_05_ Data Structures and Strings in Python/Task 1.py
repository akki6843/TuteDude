"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

# Student with marks in a dictionary
student_marks = {
    'Alice' : 85,
    'Bob' : 75,
    'Carol' : 65,
    'David' : 55
}

# Note : These names were generated as autogenerate suggestion from PyCharm.

# Get a input from user.
name = input("Enter student's name: ")

# Check for name in the dict if name present give marks else exit gracefully.
if name in student_marks:    # Check by default looks in keys  for presence (in operator).
    marks = student_marks[name]
    print(f"{name}'s marks: {marks}")
else :
    print("Sorry, student name is not available")     # Gracefully exiting