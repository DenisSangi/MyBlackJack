from Cards import Cards
from BlackJack import BlackJack

class Player:

    def player_get_card():
        player_card = Cards()
        print("You have {value} of {suit}.".format(value=player_card.card_value, suit=player_card.card_suit))
        return player_card

    def player_lose(self):
        print("It's to much")
        BlackJack.loses_count + 1



    def player_blackjack(self):
        print("You have a BlackJack")
        BlackJack.wins_count + 1


card = Player.player_get_card()
print(card)