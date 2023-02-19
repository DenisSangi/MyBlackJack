from Dealer import Dealer
from Game import Game
from Player import Player

if __name__ == '__main__':
    dealer = Dealer("Dealer")
    player = Player(input("Enter your name: "))
    Game.start_game(player, dealer)
