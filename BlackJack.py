from Cards import Cards
from Player import Player
from Dealer import Dealer
class BlackJack:


    player_cards_score = 0
    dealer_cards_score = 0
    wins_count = 0
    loses_count = 0





    def end_game():
        print("Bye bye")
        quit()


    def dealer_get_card():
        dealer_card = Cards()
        print("Dealer have {value} of {suit}.".format(value=dealer_card.card_value, suit=dealer_card.card_suit))
        return dealer_card

    def start_game():

        BlackJack.player_cards_score = 0
        BlackJack.dealer_cards_score = 0

        choice = input("Would you like to start a game?"
                       "Print 'Y' or 'N'")
        if choice == "N":
            BlackJack.end_game()

        elif choice == "Y":
            player_first_card = Player.player_get_card()
            BlackJack.player_cards_score += player_first_card
            player_second_card = Player.player_get_card()
            BlackJack.player_cards_score += player_second_card.card_points

        if BlackJack.player_cards_score == 21:
            Player.player_blackjack()
            BlackJack.start_game()
        elif BlackJack.player_cards_score > 21:
            Player.player_lose()
            BlackJack.start_game()
        else:
            took_a_card = input("Would you like to take another card?"
                                "Print 'Y' or 'N'")
            if took_a_card == "Y":
                player_third_card = Player.player_get_card()
                BlackJack.player_cards_score += player_third_card
            elif took_a_card == "N":
                dealer_first_card = Dealer.dealer_get_card()
                BlackJack.dealer_cards_score += dealer_first_card
                dealer_second_card = Dealer.dealer_get_card()
                BlackJack.dealer_cards_score += dealer_second_card


