from Player import Player
from Dealer import Dealer


class Game:
    @staticmethod
    def start_game(player, dealer):

        choice_1 = input("Would ypu like to start  new game? "
                         "Print 'y' or 'n': ")

        if choice_1 == "n":
            print("Bye bye")
            exit()

        elif choice_1 == "y":

            player.get_card()
            player.get_card()
            player.sum_of_cards = Player.cards_score(player)
            print("{name} is having {score}.".format(name=player.name, score=player.sum_of_cards))

            if player.sum_of_cards == 21:
                print("You have a BlackJack congratulations!")
                Player.wins_count += 1
                Game.end_game(player, dealer)

            while player.sum_of_cards < 21:
                choice_2 = input("Would you like to get another card? "
                                 "Print 'y' or 'n': ")
                if choice_2 == 'y':
                    player.get_card()
                    player.sum_of_cards = Player.cards_score(player)
                    print("{name} is having {score}.".format(name=player.name, score=player.sum_of_cards))

                    if player.sum_of_cards > 21:
                        Player.loses_count += 1
                        print("You lose.")
                        Game.end_game(player, dealer)

                elif choice_2 == 'n':
                    break

            dealer.get_card()
            dealer.get_card()
            dealer.sum_of_cards = Dealer.cards_score(dealer)
            print("{name} is having {score}.".format(name=dealer.name, score=dealer.sum_of_cards))

            if dealer.sum_of_cards == 21:
                print("Dealer is having BlackJack!")
                Player.loses_count += 1
                Game.end_game(player, dealer)

            while dealer.sum_of_cards < 17:
                dealer.get_card()
                dealer.sum_of_cards = Dealer.cards_score(dealer)
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
        Player.player_cards = []
        Dealer.dealer_cards = []
        Game.start_game(player=player, dealer=dealer)
