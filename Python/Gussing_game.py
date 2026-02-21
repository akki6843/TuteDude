"""
A game to guess a number
"""

secret  = 23

attempts = 10

while attempts > 0:
    attempts -= 1
    num = int(input("Guess a number: "))

    if num ==secret:
        print("Congrats! You guessed the number!")
        break
    elif num < secret:
        lower_or_higher = "higher"
    elif num > secret:
        lower_or_higher = "lower"

    print(f"Wrong guess you need to guess {lower_or_higher}.")

    print(f"You have {attempts} attempts")

print("Goodbye!")