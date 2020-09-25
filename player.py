class Player:

    def __init__(self):
        self.name = ""
        self.money = 1500
        self.dice = 2
        self.card = []

    def namePlayer(self):
        print("Quel est votre nom de joueur ?")
        self.name = input()
        print("Bienvenu ", self.name)
    