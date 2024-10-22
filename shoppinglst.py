# items = ["apple","banne","cherry"]
cart = {}
count = 0

while count < 3:
    fruits = input("Enter item name: ")
    amount = input(f"Enter quantiy of {fruits}:  ")
    print("\n")
    cart[fruits] = amount
    count += 1

print("Your shopping list: ")
for fruit, amount in cart.items():
    print(f" {fruit} {amount}")

