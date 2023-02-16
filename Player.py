from Cards import Cards


class Player:
    name = ""
    player_cards = []
    wins_count = 0
    loses_count = 0

    def __init__(self, name):
        self.name = name

    def get_card(self):
        generated_card = Cards()
        Player.player_cards.append(generated_card)
        print("{name} is have {value} of {suit}.".format(name=self.name, value=generated_card.card_value,
                                                         suit=generated_card.card_suit))

    @staticmethod
    def cards_score(player):
        sum_of_cards = 0
        sum_of_cards_with_ace = 0

        for card in player.player_cards:
            # if card.card_value == "Ace":
            #     sum_of_cards_with_ace += card.card_points
            #
            # if sum_of_cards_with_ace < 21:
            #     sum_of_cards = sum_of_cards_with_ace
            # else:
            #     card.card_points = 1
            sum_of_cards += card.card_points
        print("{name} is now having {score}.".format(name=player.name, score=sum_of_cards))
        return sum_of_cards

