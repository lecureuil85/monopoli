class Player:

    def _init_(self, name, money, card):
        self.name = ""
        self.money = 1500
        self.card = []

    def namePlayer(self):
        print("Quel est votre nom de joueur ?")
        self.name = input()
        print("Bienvenu ", self.name)
    