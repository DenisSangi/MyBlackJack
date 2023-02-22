from Cards import Cards


class Player:
    name = ""
    player_cards = []
    wins_count = 0
    loses_count = 0
    sum_of_cards = 0

    def __init__(self, name):
        self.name = name

    def get_card(self):
        generated_card = Cards()
        Player.player_cards.append(generated_card)
        print("{name} is have {value} of {suit}.".format(name=self.name, value=generated_card.card_value,
                                                         suit=generated_card.card_suit))

    @staticmethod
    def cards_score(player):
        sum_of_player_cards = 0
        sum_with_ace = 0

        for card in player.player_cards:
            ace_counter = 0
            if card.card_value == "Ace" in player.player_cards:
                ace_counter += 1
                sum_with_ace += card.card_points
                if ace_counter == 1 and sum_with_ace > 21:
                    sum_with_ace += card.card_points - ace_counter * 10
                    sum_of_player_cards = sum_with_ace
                elif ace_counter > 1:
                    while sum_with_ace > 21:
                        sum_with_ace += card.card_points - (ace_counter-1) * 10
                        sum_of_player_cards = sum_with_ace
                        break
            else:
                sum_of_player_cards += card.card_points
        return sum_of_player_cards
