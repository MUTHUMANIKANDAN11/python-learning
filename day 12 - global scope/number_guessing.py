import random
def generateNum():
    return random.choice(list(range(1,100)))

def game(life, num):
    while life > 0:
        print(f"You have {life} attempts remaining to guess the number.")
        guss = int(input("Make a guess: "))

        if guss == num:
            print("Congratulations! You guessed the number!")
            break
        elif guss < num:
            print("Sorry, you guessed the number too low.")
            life -= 1
        else:
            print("Sorry, you guessed the number too high.")
            life -= 1

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
ranNum = generateNum()

if diff == "easy":
    game(10, ranNum)
else:
    game(5, ranNum)