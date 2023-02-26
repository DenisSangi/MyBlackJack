from Cards import Cards


class Player:
    name = ""
    wins_count = 0
    loses_count = 0
    sum_of_cards = 0
    player_cards = []

    def __init__(self, name):
        self.name = name

    @staticmethod
    def cards_score(self):
        sum_of_player_cards = 0
        for card in self.player_cards:
            sum_of_player_cards += card.card_points
        return sum_of_player_cards

    @staticmethod
    def ace_check(self):
        ace_counter = 0
        for card in self.player_cards:
            for value in card.card_value:
                if value == "A":
                    ace_counter += 1
        return ace_counter
