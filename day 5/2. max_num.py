scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

mx = float("-inf")

for score in scores:
    if mx < score:
        mx = score

print("Max score is:", mx)