import random

class Dice:

    def throwDice(self, nbDice):
        for i in range(nbDice):
            rdn = random.randint(0,6)
            print(rdn)

D = Dice()

D.throwDice(2)
