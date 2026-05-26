import random
secret = random.randint(1,100)
guess = 0
attempt = 0
while guess!=secret:
    guess = int(input("enter your number please"))
    attempt+=1
    if guess < secret:
        print("to low please try again")
    elif guess>secret:
        print("to high")
    else:
        print("your a right babe")
print(f"total attempt = {attempt}")