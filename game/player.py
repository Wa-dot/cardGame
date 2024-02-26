from scripts.wallet import Wallet 

class Player(Wallet):
        
        def __init__(self):
            name = input("Enter your name: ")
            super().__init__()
            self.name = name
            self.wallet = Wallet()
            self.wallet.display()
            
        def display(self):
            return { 'type': 'Player', 'name': self.name, 'wallet': self.wallet.display() }