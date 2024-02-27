import random

class Card:
    def __init__(self):
        self.value = 0
        self.createCard()

    def createCard(self):
        self.value = random.randint(1, 60)
        return self.value
    
    def display(self):
        return { 'type': 'Card', 'value': self.value }


class Deck:
    def __init__(self):
        self.cards = []
    
    def createDeck(self, numberCardToDraw):
        for card in range(numberCardToDraw):
            # Card has a random value between 1 and 60
            self.cards.append(Card())
            print("Card value : "+ str(self.cards[card].value))
        print(self.cards)


    def showCards(self):
        for card in self.cards: 
            print("Carte "+ str(self.cards.index(card))+ ' : ' + str(card.value))
        
