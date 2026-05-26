# food store
foods = []
prices = []
total = 0

while True:
    food = input("Enter item: ")

    if food == "no":
        print("Items are finished")
        break

    else:
        price = float(input("Enter price: "))

        foods.append(food)
        prices.append(price)

print("----- Your Cart -----")

for item in foods:
    print(item)

for rup in prices:
    total += rup

print("Total =", total)