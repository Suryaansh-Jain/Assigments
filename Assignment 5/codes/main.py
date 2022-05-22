import random
import numpy as np

box = [0, 0]
red_count = 0

x = np.random.randint(2, size=1000000)

for i in range(1000000):
    if (x[i] == 0):
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
