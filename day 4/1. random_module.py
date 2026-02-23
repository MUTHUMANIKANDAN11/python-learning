import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

num = random.randint(0, len(friends)-1)

print(f"Friend to pay is: {friends[num]}")