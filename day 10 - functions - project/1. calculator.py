def add(n1, n2):
    return n1 + n2
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b

operations = ['+', '-', '*', '/']
num1 = 0
num2 = 0
have_number = False


year = 2020

print("Calculator")

while True:
    operation = ''
    if have_number:
        option = input(f"Type 'y' to continue calculating with {num1}\nType 'n' to start a new calculation, \nType 'q' to exit the program: ").lower()
        if option == 'q':
            break
        elif option == 'y':
            operation = input(f"select operation {operations}: ")
            num2 = float(input("Enter second number: "))
        else:
            have_number = False

    if not have_number:
        num1 = float(input("Enter first number: "))
        operation = input(f"select operation {operations}: ")
        num2 = float(input("Enter second number: "))

    if operation == '+':
        num1 = add(num1, num2)
    elif operation == '-':
        num1 = sub(num1, num2)
    elif operation == '*':
        num1 = mult(num1, num2)
    elif operation == '/':
        num1 = div(num1, num2)
    have_number = True

    print("The result is: ", num1)

print()