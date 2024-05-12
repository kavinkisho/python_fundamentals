import random
import math

print("💡" * 10 + "Number Guessing Game (integar only)" + "💡" * 10)
lower = int(input("Enter lower bound: "))
upper = int(input("Enter a upper bound: "))
randomNum = random.randint(lower, upper)
max_tries = round(math.sqrt(upper - lower))


while True:
    guess = int(input("Please guess a number: "))
    if guess == randomNum:
        print("Well Done!")
    elif guess < randomNum:
        print("Guess Higher!")
    else:
        print("Guess Lower")

