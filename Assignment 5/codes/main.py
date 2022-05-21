import random

box = [0, 0]
red_count = 0

for i in range(100000):
    x = random.randint(0, 1) # Randomly pick a box
    if (x == 0):
        box[0] += 1
        top = random.randint(0, 1000)
        if (top != 0):
            red_count += 1
    else:
        box[1] += 1
        top = random.randint(0, 1000)
        if (top == 0):
            red_count += 1

print(box[0]/red_count)

