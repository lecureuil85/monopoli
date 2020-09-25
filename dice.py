import random

class Dice:

    def throwDice(self):
            rdn = random.randint(1,6)
            rdn2 = random.randint(1,6)
            result = rdn + rdn2
            return result



