import random


class Cards:
    card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card_suit = ["Hearts", "Diamonds", "Cross", "Spades"]
    card_points = 0

    def __init__(self):
        self.card_value = random.choice(self.card_value)
        self.card_suit = random.choice(self.card_suit)

        if self.card_value == "J" or self.card_value == "Q" or self.card_value == "K":
            self.card_points = 10
        elif self.card_value == "A":
            self.card_points = 11
        else:
            self.card_points = int(self.card_value)
