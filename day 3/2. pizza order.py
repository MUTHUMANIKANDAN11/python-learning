print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0

if size == "S":
    total = 15
    if pepperoni == "Y":
        total += 2
elif size == "M":
    total = 20
elif size == "L":
    total = 25

if size != "S" and pepperoni == "Y":
    total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is: ${total}")
