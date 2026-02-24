"""
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

#  Takes user input and writes it to a file named output.txt
user_data = input("Enter text to write to the file: ")
with open("output.txt", "w+") as file:
    file.write(user_data + "\n")

print("Data Successfully written to output.txt")

# Appends additional data to the same file
additional_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

print("Data Successfully appended")

# Reads and displays the final content of the file
print("Final Content of output.txt ")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
