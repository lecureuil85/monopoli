class Player:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.money = 1500
        self.card = []
        self.nbDice = 0
        self.position = 1

    def namePlayer(self):
        print("Quel est votre nom de joueur ?")
        self.name = input()
        print("Bienvenu ", self.name)
