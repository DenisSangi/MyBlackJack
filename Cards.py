import random

import self as self

class Cards:

    nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suit = ["Hearts", "Diamonds", "Cross", "Spades"]
    value = 0

    def __init__(self):
        self.nominal = random.choice(self.nominal)
        self.suit = random.choice(self.suit)

    def card_value(self):
        for item in self.nominal:
            if item == "Jack" or item == "Queen" or item == "King":
                value = 10
            elif item == "Ace":
                value = 11
            value = int(item)
            return value


card1 = Cards()
print(card1.nominal)
print(card1.suit)
print(card1.card_value())




