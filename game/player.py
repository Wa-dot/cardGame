from scripts.wallet import Wallet 
from .card import Deck

class Player:
        
        def __init__(self, name):
            self.name = name
            self.wallet = Wallet() 
            self.score = 0
            print(self.wallet.display())
            self.hasSelected = False
            self.deck = Deck()

        def cardSelection(self, cardSelectedNumber):
            if not self.hasSelected:
                if cardSelectedNumber < len(self.deck.cards):
                    cardSelected = self.deck.cards[cardSelectedNumber]
                    self.hasSelected = True
                    self.deck.cards.pop(cardSelectedNumber)
                else:
                    print("Invalid card number")
                print("Player " + self.name + " played " + str(cardSelected.value))
                return cardSelected
    
            
        def display(self):
            return { 'type': 'Player', 'name': self.name, 'wallet': self.wallet.display(), 'deck': self.deck.showCards()}
        