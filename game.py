from player import *
from dice import *

class Game():

    def main(self):

        players = []

        print("Combien de joueur y a-t-il ?")
        nbJoueur = int(input())

        for i in range(nbJoueur):
            players.append(Player()) 
            players[i].namePlayer()
     
            # test = input("Voulez vous lancer les dés (Y/N) : ")
            # if test == 'Y' :
            #     for i in range(nbJoueur):
            #         throwDice()
            # else:
            #     print("N")


G = Game()
G.main()