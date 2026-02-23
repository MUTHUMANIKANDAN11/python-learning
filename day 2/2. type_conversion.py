# type check
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# conversion
name = input("Enter your name: ")
name_len = len(name)

print("Number of letters in your name: " + str(name_len))

#///////////////////

print("Number of letters in your name: " + str(len(input("Enter your name"))))