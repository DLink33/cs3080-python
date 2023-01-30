
from random import randint

class Die():
    def __init__(self, sides) -> None:
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)

def rollDice(dice, numRolls):
    allRolls = []
    for i in range(numRolls):
        rolls = []
        for index, die in enumerate(dice):
            rolls.append(die.roll())
        print(rolls)
        allRolls.append(rolls)
    return allRolls

def main():
    numDice = int(input("Enter the number of dice you wish to roll: "))
    dice = []
    rolls = []
    for i in range(numDice):
        print(f"How many sides does die {i+1} have? ", end="")
        sides = int(input())
        dice.append(Die(sides))
    numRolls = int(input("Enter how many times you want to roll these die: "))
    print("Here are your rolls:")
    rolls = rollDice(dice, numRolls)
    for roll in rolls:
        print(roll)
          
if __name__ == '__main__':
    main()
    