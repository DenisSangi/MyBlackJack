import random


class Cards:
    card_value = ["5", "6", "7", "Ace"]
    card_suit = ["Hearts", "Diamonds", "Cross", "Spades"]
    card_points = 0

    def __init__(self):
        self.card_value = random.choice(self.card_value)
        self.card_suit = random.choice(self.card_suit)

        if self.card_value == "Jack" or self.card_value == "Queen" or self.card_value == "King":
            self.card_points = 10
        elif self.card_value == "Ace":
            self.card_points = 11
        else:
            self.card_points = int(self.card_value)
