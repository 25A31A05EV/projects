import random


def random_number():
    number = random.randint(1,100)
    attempt = 0
    print("Guess the number")
    print("welcome to the guessing game")
    while True:
        guess = int(input("Guess the number"))
        attempt += 1
        if guess == number:
            print("You guessed the number")
            print(attempt)
            break
        elif guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        else:
            print("You guessed the number")
if __name__ == "__main__":
    random_number()

