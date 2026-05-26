import random
options =("rock", "paper", "scissors")
running = True
attempt= 0
while running:
    attempt+=1
    print(f"you have {attempt} attempts")
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter a rock or paper or scissors").lower()
        print(f"player: {player}")
        print(f"computer: {computer}")
        if player == computer:
            print("its a  tie")
        elif player == "rock" and computer == "scissors":
            print("you win")
        elif player =="paper" and computer =="rock":
            print("you win")
        elif player=="scissors" and computer =="paper":
            print("you win")
        else:
            print("you lose")
        if  input("enter do you want play a again(y/n)").lower() != "y":
            running = False
            print("thank you so munch")
            print("have a nice day and good day")
            break