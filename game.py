from player import *

class Game():

    def main(self):

        players = []

        print("Combien de joueur y a-t-il ?")
        nbJoueur = int(input())

        for i in range(nbJoueur):
            players.append(Player()) 
            players[i].namePlayer()

            print(players[i].money)

G = Game()
G.main()