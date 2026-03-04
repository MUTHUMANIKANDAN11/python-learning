import game_data
import random

l = len(game_data.data)
def generateNum():
    return random.randint(1, l)

score = 0

n1 = generateNum()
n2 = generateNum()

a = game_data.data[n1]
b = game_data.data[n2]

while True:
    print(f"A: {a["name"]}, {a["description"]}, {a["country"]}")
    print("VS")
    print(f"B: {b["name"]}, {b["description"]}, {b["country"]}")

    print(f"Your current scour: {score}\n")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choice == "a":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            a = b
            b = game_data.data[generateNum()]
            print("\nYou are correct!\n")
        else:
            print("You lost, Your final score was: ", score)
            break
    else:
        if a["follower_count"] < b["follower_count"]:
            score += 1
            a = b
            b = game_data.data[generateNum()]
            print("\nYou are correct!\n")
        else:
            print("\nYou lost, Your final score was: ", score)
            break