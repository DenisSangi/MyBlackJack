from Player import Player
from Cards import Cards

class Game:
    @staticmethod
    def start_game(player, dealer):

        choice_1 = input("Would you like to start  new game? "
                         "Print 'y' or 'n': ")

        if choice_1 == "n":
            print("Bye bye")
            exit()

        elif choice_1 == "y":

            Cards.get_card(player)
            Cards.get_card(player)
            player.sum_of_cards = player.cards_score(player)
            ace_number = player.ace_check(player)
            while ace_number != 0 and player.sum_of_cards > 21:
                ace_number -= 1
                player.sum_of_cards -= 10
            print("{name} is having {score}.".format(name=player.name, score=player.sum_of_cards))

            if player.sum_of_cards == 21:
                print("You have a BlackJack congratulations!")
                Player.wins_count += 1
                Game.end_game(player, dealer)

            while player.sum_of_cards < 21:
                choice_2 = input("Would you like to get another card? "
                                 "Print 'y' or 'n': ")
                if choice_2 == 'y':
                    Cards.get_card(player)
                    player.sum_of_cards = player.cards_score(player)
                    ace_number = player.ace_check(player)
                    while ace_number != 0 and player.sum_of_cards > 21:
                        ace_number -= 1
                        player.sum_of_cards -= 10
                    print("{name} is having {score}.".format(name=player.name, score=player.sum_of_cards))

                    if player.sum_of_cards > 21:
                        Player.loses_count += 1
                        print("You lose.")
                        Game.end_game(player, dealer)

                elif choice_2 == 'n':
                    break

            Player.player_cards = []
            Cards.get_card(dealer)
            Cards.get_card(dealer)
            dealer.sum_of_cards = dealer.cards_score(dealer)
            ace_number = dealer.ace_check(dealer)
            while ace_number != 0 and dealer.sum_of_cards > 21:
                ace_number -= 1
                dealer.sum_of_cards -= 10
            print("{name} is having {score}.".format(name=dealer.name, score=dealer.sum_of_cards))

            if dealer.sum_of_cards == 21:
                print("Dealer is having BlackJack!")
                Player.loses_count += 1
                Game.end_game(player, dealer)

            while dealer.sum_of_cards < 17:
                Cards.get_card(dealer)
                dealer.sum_of_cards = dealer.cards_score(dealer)
                ace_number = dealer.ace_check(dealer)
                while ace_number != 0 and dealer.sum_of_cards > 21:
                    ace_number -= 1
                    dealer.sum_of_cards -= 10
                print("{name} is having {score}.".format(name=dealer.name, score=dealer.sum_of_cards))

            if dealer.sum_of_cards > 21:
                Player.wins_count += 1
                print("Yow win.")
                Game.end_game(player, dealer)

            if player.sum_of_cards > dealer.sum_of_cards:
                Player.wins_count += 1
                print("{name} had win.".format(name=player.name))
                Game.end_game(player, dealer)
            elif player.sum_of_cards < dealer.sum_of_cards:
                Player.loses_count += 1
                print("Dealer had win.")
                Game.end_game(player, dealer)
            else:
                print("Draw.")
                Game.end_game(player, dealer)

    @staticmethod
    def end_game(player, dealer):
        print("You have win {wins} times and lose {loses} times.".format(wins=Player.wins_count,
                                                                         loses=Player.loses_count))
        player.player_cards = []
        dealer.dealer_cards = []
        Game.start_game(player=player, dealer=dealer)
