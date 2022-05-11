# Program to simulate the toss of coins.

import random

coins = [0, 0, 0]
head_count = 0

for i in range(1000):
    x = random.randint(0, 2) # Randomly pick a coin
    if (x == 0):
        head_count += 1
        coins[0] += 1
    elif (x == 1):
        top = random.randint(0, 7) # out of 8 we take on 2 for tail and 6 for head
        if (top > 1):
            head_count += 1
            coins[1] += 1
    else:
        top = random.randint(0, 1) # Even
        if (top == 1):
            head_count += 1
            coins[1] += 1

print(coins[0]/head_count)
