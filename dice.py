from random import randint

class Die:
    def __init__(self, num_of_sides=6):
        self.sides = num_of_sides

    def roll_dice(self):
        roll = randint(1, self.sides)
        return roll