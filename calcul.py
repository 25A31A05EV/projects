def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return 0
while True:
    print("\n---calucator app---")
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. quit")

    choice = input("Enter your choice: ")
    if choice == "5":
        print("calculator close")
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if choice == "1":
        print(add(num1,num2))
    elif choice == "2":
        print("result =",sub(num1,num2))
    elif choice == "3":
        print("result =",mul(num1,num2))
    elif choice == "4":
        print("result =",div(num1,num2))
    else:
        print("invalid choice")

