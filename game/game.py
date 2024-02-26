
from player import Player

class Game:
    def __init__(self):
        self.playerNumber = 0
        self.isLaunch = False
        self.players = []
        print("Game created")
        


    def register(self, player1: Player):
        self.players.append(player1)
        self.playerNumber += 1
        print("Player {player1.name} registered")
        return self.players

    def launchGame(self):
        if self.playerNumber == 6:
            isLaunch = True
        return isLaunch
    
    def display(self):
        return { 'type': 'Game', 'playerNumber': self.playerNumber, 'isLaunch': self.isLaunch, 'players': self.players }
    
    def round(self):
        if self.isLaunch:
            print("Game is launched")
        else:
            print("Game is not launched")
