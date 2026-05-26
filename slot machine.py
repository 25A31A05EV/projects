#python slot machine
import random
def spin_row():
    symbols = [ "🍒","🍉","🍋","⭐"]
    result = []
    for symbol in range(3):
        result.append(random.choice[symbol])
def print_row(row):
    print("|".join(row))
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == " 🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*4
        elif row[0] == "🍋":
            return bet*5
        elif row[0] == "⭐":
            return bet*6
def main():
    balance = 100


    print("Welcome to the Slots Machine")
    print("symbols 🍒🍉 🍋⭐")
    while balance > 0:
        print(f"correct balance {balance}")
        bet = input("please enter your bet: ")
        if not bet.isdigit():
            print("please enter a number")
            continue
        bet =int(bet)
        if bet > balance:
            print("please indufient a higher bet")
            continue
        if bet <= 0:
            print("please enter a higher bet")
            continue
        balance -= bet

        row = spin_row
        print_row(row)
        payout = get_payout(row,bet)
        if payout >0:
            print("you own")
        else:
            print("you don't own")
        balance +=payout
        play_again = input("would you like to play again? (y/n)").upper()
        if play_again != "y":
            break
if __name__ == "__main__":
    main()