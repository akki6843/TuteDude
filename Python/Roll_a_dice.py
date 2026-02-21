"""
Write a program to roll a dice using Python's standard library

A Die has 6 faces with numbers 1 to 6 written on them.

The program should randomly print the number between 1 and 6.
"""

import random


print("Welcome to the Roll A Dice Game!")
while True:
    choice = input("1 to roll a dice or  'q' to quit: ")

    if choice == "q":
        print("Goodbye!")
        break
    elif choice == "1":
        number = random.randint(1, 6)
        print(f"Your number is {number}")
    else :
        print("Invalid choice!")