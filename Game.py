from Player import Player


class Game:

    @staticmethod
    def start_game():

        player = Player("")
        dealer = Player("Dealer")
        Player.wins_count = 0
        Player.loses_count = 0

        choice_1 = input("Would ypu like to start  new game? "
                         "Print 'y' or 'n': ")

        if choice_1 == "n":
            exit()

        elif choice_1 == "y":

            player.name = input("Enter your name: ")
            player.get_card()
            player.get_card()
            Player.cards_score(player)
            print("{name} is having {score}.".format(name=player.name, score=Player.cards_score(player)))

            if Player.cards_score(player) == 21:
                print("You have a BlackJack congratulations!")
                Player.wins_count += 1
                Game.end_game()

            if Player.cards_score(player) < 21:
                choice_2 = input("Would you like to get another card? "
                                 "Print 'y' or 'n': ")
                while choice_2 == 'y' and Player.cards_score(player) < 21:
                    player.get_card()
                    Player.cards_score(player)
                    print("{name} is having {score}.".format(name=player.name, score=Player.cards_score(player)))

            if Player.cards_score(player) > 21:
                Player.loses_count += 1
                print("You lose")
                Game.end_game()
            else:
                dealer.get_card()
                dealer.get_card()
                Player.cards_score(dealer)
                print("{name} is having {score}.".format(name=dealer.name, score=Player.cards_score(dealer)))

            if Player.cards_score(dealer) == 21:
                print("Dealer is having BlackJack!")
                Player.loses_count += 1
                Game.end_game()

            while Player.cards_score(dealer) < 17:
                dealer.get_card()
                Player.cards_score(dealer)
                print("{name} is having {score}.".format(name=dealer.name, score=Player.cards_score(dealer)))

                if Player.cards_score(dealer) > 21:
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


