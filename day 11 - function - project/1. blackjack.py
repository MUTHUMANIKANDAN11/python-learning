import random

def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def print_cards(computer_cards, user_cards):
    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")


while True:
    game_option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if game_option == 'n':
        break

    user_cards = [random_card(), random_card()]
    computer_cards = [random_card(), random_card()]

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    while True:
        print(f"Your cards: {user_cards} Current score: {user_score}")
        print("Computer's first card: ", computer_cards[0])

        option = input("\nType 'y' to get another card, type 'n' to pass: ")

        if option == 'y':
            card = random_card()

            if user_score + card > 21:
                if card == 11 and user_score + 1 <= 21:
                    user_score += 1
                    user_cards.append(1)

                else:
                    user_cards.append(card)
                    print_cards(computer_cards, user_cards)
                    print("You lose!")
                    computer_cards = []
                    user_cards = []
                    break
            else:
                user_cards.append(card)
                user_score += card

        elif option == 'n':
            while True:
                num = random_card()
                if computer_score + num <= 21:
                    computer_cards.append(num)
                    computer_score += num
                else:
                    break

            print_cards(computer_cards, user_cards)
            if user_score <= 21 and user_score > computer_score:
                print("You win!")
            elif computer_score <= 21 and computer_score > user_score:
                print("You lose!")
            elif computer_score == user_score:
                print("Game Draw")

            user_cards = []
            computer_cards = []
            break