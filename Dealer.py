from Player import Player
from Cards import Cards
from BlackJack import  BlackJack
class Dealer:
        def dealer_get_card():
            dealer_card = Cards()
            print("I have {value} of {suit}.".format(value=dealer_card.card_value, suit=dealer_card.card_suit))
            return dealer_card

        def dealer_lose(self):
            print("It's to much")
            BlackJack.wins_count + 1

        def player_blackjack(self):
            print("I have a BlackJack")
            BlackJack.loses_count + 1