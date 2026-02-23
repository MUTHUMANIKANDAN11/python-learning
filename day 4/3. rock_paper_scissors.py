import random
move = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

user_choose = int(input("Enter your choice: (rock: 0, paper: 1, scissors: 2): "))
computer_choose = random.randint(0,2)

print("Your move\n", move[user_choose])
print("Computer choose\n", move[computer_choose])

print("Result: ")
if user_choose == computer_choose:
    print("Tie")
elif user_choose == 0:
    if computer_choose == 1:
        print("You lose")
    elif computer_choose == 2:
        print("You win")
elif user_choose == 1:
    if computer_choose == 0:
        print("You win")
    elif computer_choose == 1:
        print("You lose")
elif user_choose == 2:
    if computer_choose == 0:
        print("You lose")
    elif computer_choose == 1:
        print("You win")
else:
    print("Invalid input")