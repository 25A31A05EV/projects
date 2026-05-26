#banking prgrom
from tokenize import blank_re


def show_balance(balance):
    print(f"your balance is {balance:.2f}")
def deposit():
    amount = float(input("enter your amount: "))
    if amount < 0:
        print("you can't deposit")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("enter your amount: "))
    if amount>balance:
        print("you can't withdraw")
    elif amount<0:
        print("amount must grater than zero ")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True
    while is_running:
        print("******************")
        print("baking program")
        print("1.show_balance"
              "2.deposit"
              "3.withdraw"
              "4 exit")
        print("******************")
        choice = input("enter your choice: ")
        print("*****************************")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("that is not a valid choice")
    print("thank you for your choice")
if __name__ == "__main__":
    main()