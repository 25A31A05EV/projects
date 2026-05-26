import random
his =[]
while True:
    input("enter a dice")
    roll =random.randint(1,6)
    his.append(roll)
    print("yu roll",roll)
    choice = input("yes or not").lower()
    if choice!="y":
        break
print("all rolles",his)