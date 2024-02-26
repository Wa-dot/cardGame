import random

class Card:
    def __init__(self, value):
        self.value = value


class Deck(Card):
    def __init__(self):
        startCardNumber = 10
        self.cards = []
        for suit in range(4):
            #Card has a random value between 1 and 60
            for i in range(1, startCardNumber):
                self.cards.append(Card(random.randint(1, 60)))
        self.shuffle()
