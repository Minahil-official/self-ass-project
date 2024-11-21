import random
def dicesimulate():
    for i in range(0,3):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"the roll of dice1 is {dice1}")
        print(f"the roll of dice1 is {dice2}")
dicesimulate()
