from .player import Player
import threading
import random

class Game:
    def __init__(self, numberOfPlayers, cardNumber):
        self.isLaunch = False
        self.numberOfPlayers = numberOfPlayers
        self.players = []
        self.cardNumber = cardNumber
        self.cardsSelected = []
        print("Game created")
        
    def register(self, player: Player):
        self.players.append(player)
        print("Player " + player.name + " registered")
        self.launchGame(self.numberOfPlayers)
        return self.isLaunch
    

    def launchGame(self, numberPlayersMax):
        if len(self.players) == numberPlayersMax:
            self.isLaunch = True
            print("Game is launched")
            self.drawCards(self.cardNumber)
        return self.isLaunch
    
    
    def drawCards(self, numberCardToDraw):
        for player in self.players:
            print("Player " + player.name + " draw cards")
            player.deck.createDeck(numberCardToDraw)

    def display(self):
        return { 'type': 'Game', 'isLaunch': self.isLaunch, 'players': self.players }

    # def round(self):
    #     for player in self.players:
    #         print("Player " + player.name + " select a card")
    #         player.cardSelection()
    #     print("Round finished")

    def checkHavePlayed(self):
        count = 0
        while count < len(self.players):
            for player in self.players:

                self.cardsSelected.append(player.cardSelection(random.randint(0, len(player.deck.cards)-1)))

                if player.hasSelected == True:
                    print("Player " + player.name + " selected a card")
                    count += 1
        for player in self.players:
            player.hasSelected = False
        return True

    def checkWinner(self):
        cardValue = []

        for card in self.cardsSelected:
            cardValue.append(card.value)
        maxCardValue = max(cardValue)
        indexWinner = cardValue.index(maxCardValue)
        cardWinner = self.cardsSelected[indexWinner]
        print("\nWinner is " + str(cardWinner.value) + " with " + str(sum(cardValue)) + " points")
        self.cardsSelected.clear()
        return sum(cardValue), cardWinner, indexWinner



    def round(self):
        for round in range(self.cardNumber):
        #check = threading.Thread(target=self.checkHavePlayed)
        #check.start()
            self.checkHavePlayed()
            scoring, winner, indexWinner = self.checkWinner()
            self.players[indexWinner].score += scoring
        
        self.players.sort(key=lambda x: x.score, reverse=True)
        print("Winner is " + self.players[0].name + " with " + str(self.players[0].score) + " points")
            
        
