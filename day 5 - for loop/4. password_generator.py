import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letter_cnt = int(input("How many letters would you like in your password: "))
symbol_cnt = int(input(f"How many symbols would you like: "))
number_cnt = int(input(f"How many numbers would you like: "))

total = letter_cnt + symbol_cnt + number_cnt

password = ['-']*total

for i in range(letter_cnt):
    letter = random.choice(letters)
    pass_ind = random.randint(0, total-1)

    while password[pass_ind] != '-':
        pass_ind = random.randint(0, total-1)
    password[pass_ind] = letter

for i in range(symbol_cnt):
    symbol = random.choice(symbols)
    pass_ind = random.randint(0, total-1)

    while password[pass_ind] != '-':
        pass_ind = random.randint(0, total-1)
    password[pass_ind] = symbol

for i in range(number_cnt):
    number = random.choice(numbers)
    pass_ind = random.randint(0, total-1)

    while password[pass_ind] != '-':
        pass_ind = random.randint(0, total-1)
    password[pass_ind] = number

print("Password: ", "".join(password))