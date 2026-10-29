import random

def roll_dice():
    return random.randint(1, 6)

for i in range(5):
    result = roll_dice()
    print(result)