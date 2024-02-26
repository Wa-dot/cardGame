from .player import Player


class Game:
    def __init__(self):
        self.playerNumber = 0
        self.isLaunch = False
        self.players = []
        print("Game created")
        
    def register(self, name):
        player = Player(name)
        self.players.append(player)
        self.playerNumber += 1
        print("Player " + player.name + " registered")
        return self.players

    def launchGame(self, numberPlayers):
        if self.playerNumber == numberPlayers:
            self.isLaunch = True
        return self.isLaunch
    
    def display(self):
        return { 'type': 'Game', 'playerNumber': self.playerNumber, 'isLaunch': self.isLaunch, 'players': self.players }
    
    def drawCards(self):
        for player in self.players:
            print("Player " + player.name + " draw a card")
            player.deck.append(self.deck.cards.pop())



    def round(self):
        if self.isLaunch:
            print("Game is launched")
        else:
            print("Game is not launched")
