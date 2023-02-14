from Cards import Cards

class Player:
    name = ""
    player_cards = [Cards()]

    def __init__(self, name):
        self.name = name

    def get_card(self):
        generated_card = Cards()
        Player.player_cards.append(generated_card)
        print("{name} is have {value} of {suit}.".format(name=self.name, value=generated_card.card_value, suit=generated_card.card_suit))