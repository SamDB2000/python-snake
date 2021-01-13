import random

for i in range(0, 20):
    x = random.randint(0, 49) * 20
    y = random.randint(0, 35) * 20
    print((x, y) + 10)