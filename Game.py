from Player import Player


class Game:

    @staticmethod
    def start_game():

        dealer = Player("Dealer")
        Player.wins_count = 0
        Player.loses_count = 0

        choice_1 = input("Would ypu like to start  new game? "
                         "Print 'y' or 'n': ")

        if choice_1 == "n":
            exit()

        elif choice_1 == "y":
            player = Player("")
            player.name = Player(input("Enter your name: "))
            player.get_card()
            player.get_card()
            Game.cards_score(player)

            if Game.cards_score(player) == 21:
                print("You have a BlackJack congratulations!")
                Player.wins_count += 1
                Game.end_game()

            elif Game.cards_score(player) < 21:
                choice_2 = input("Would you like to get another card? "
                                 "Print 'y' or 'n': ")
                while choice_2 == 'y' and Game.cards_score(player) < 21:
                    player.get_card()
                    Game.cards_score(player)

            if Game.cards_score(player) > 21:
                Player.loses_count += 1
                print("You lose")
                Game.end_game()
            else:
                dealer.get_card()
                dealer.get_card()
                Game.cards_score(dealer)

                if Game.cards_score(dealer) == 21:
                    print("Dealer is having BlackJack!")
                    Player.loses_count += 1
                    Game.end_game()

                while Game.cards_score(dealer) < 17:
                    dealer.get_card()
                    Game.cards_score(dealer)

                    if Game.cards_score(dealer) > 21:
                        Player.wins_count += 1
                        print("Yow win.")
                        Game.end_game()

    @staticmethod
    def end_game():
        print("You have win {wins} times and lose {loses} times.".format(wins=Player.wins_count, loses=Player.loses_count))
        ending_choice = input("Would you like to start next game? Print 'y' or 'n'.")
        if ending_choice == "y":
            Game.start_game()
        else:
            print("Bye bye")
            exit()

    @staticmethod
    def cards_score(player):
        sum_of_cards = 0
        sum_of_cards_with_ace = 0

        for card in player.player_cards:
            if card.card_value == "Ace":
                sum_of_cards_with_ace += card.card_points
                if sum_of_cards_with_ace < 21:
                    sum_of_cards = sum_of_cards_with_ace
                else:
                    card.card_points = 1
                    sum_of_cards += card.card_points

        print("{name} is now having {score}.".format(name=player.name, score=sum_of_cards))
        return sum_of_cards
