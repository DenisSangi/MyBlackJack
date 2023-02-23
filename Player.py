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
        for card in player.player_cards:
            sum_of_player_cards += card.card_points
        return sum_of_player_cards

    @staticmethod
    def ace_check(player):
        ace_counter = 0
        for card in player.player_cards:
            for value in card.card_value:
                if value == "A":
                    ace_counter += 1
        return ace_counter
