from player import Player
from dice import Dice

class Game():

    def main(self):

        players = []

        print("Combien de joueur y a-t-il ?")
        nbPlayer = int(input())

        for i in range(nbPlayer):
            players.append(Player()) 
            players[i].namePlayer()

        for i in range(nbPlayer):
            print(str(players[i].name)+" à toi de jouer")
            test = input("Voulez vous lancer les dés (Y/N) : ")
            while test != 'Y' :
                test
            print("Dés lancés : "+ str(d.throwDice()))
            

d = Dice()
g = Game()
g.main()