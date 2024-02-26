from scripts.wallet import Wallet 
from .card import Deck

class Player(Wallet):
        
        def __init__(self, name):
            #name = input("Enter your name: ")
            super().__init__()
            self.name = name
            self.wallet = Wallet()
            print(self.wallet.display())
            self.deck = Deck
            
        def display(self):
            return { 'type': 'Player', 'name': self.name, 'wallet': self.wallet.display() }