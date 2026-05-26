import random

print("Welcome to this guessing game")

lowest = 1
highest = 100

answer = random.randint(lowest, highest)

guess = 0
is_running = True

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():

        guess = int(guess)

        if guess < lowest or guess > highest:
            print("Out of range")
            print(f"Select a number between {lowest} and {highest}")

        elif guess > answer:
            print("It's very high")

        elif guess < answer:
            print("Too low")

        else:
            print("Correct answer")
            is_running = False

    else:
        print(f"Please enter a number between {lowest} and {highest}")