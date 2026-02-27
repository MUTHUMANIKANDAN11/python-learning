import random
word_list = ["camel", "letter", "python", "hangman", "computer"]

word = random.choice(word_list)
n = len(word)
life = 6

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

answer = ['-'] * n
print(word)

while n > 0 and life > 0:
    print(f"Life left: {life}/6")
    print("".join(answer))
    ch = input("Enter a letter: ")
    ind = -1
    for i in range(len(word)):
        if ch == word[i] and answer[i] == '-':
            ind = i
            break

    if ind == -1:
        life -= 1
        print("wrong letter")
    else:
        answer[ind] = ch
        n -= 1
        print("correct letter")
    print(stages[life])
    print()
    
if n > 0:
    print("You lose.")
else:
    print("You win.")