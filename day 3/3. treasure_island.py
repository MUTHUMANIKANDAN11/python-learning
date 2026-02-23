print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Enter left or right: ")
if direction == "left":
    print("Game over")
else:
    swim = input("Enter swim or wait: ")

    if swim == "swim":
        print("Game over")

    else:
        door = input("Enter door you want to open: (red, blue, green): ");
        if door == "red" or door == "blue":
            print("Game over")
        else:
            print("Congratulations! You win!")