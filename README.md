# Card Game in blockchain
## Objective
**Build a card game. The rules are as follows:**
- It plays with 6 players, and a deck of cards where each card is a number from 1 to 60.
- Each player is given 10 cards.
- The game has 10 rounds. Each round goes as follows:
    - Each player secretly selects a card from their hand.
    - Once all players have chosen, all cards are revealed. The player with the highest number takes all revealed cards and set them aside. 
    - At the end of the 10 rounds, each player adds the number of every card they collected during the game. The player with the highest total wins.

## Features
**The following must be implemented in your system:**
- Any user can register to participate in a game. Once 6 players have registered, the game starts.
- There can be multiple games going at the same time.
- At any time, I should be able to check if my game started.
- I should also be able to see my own hand, see how many points I have collected and if
- I should select a card or not (waiting for other players to select).
- I should also have a little history of my performances: how many games I won, what is my average point each game, etc…

## Hints
- The more is handled procedurally on your contract, the better
- The trickiest part is about randomness: how can you handle randomness in a decentralized system?
- I shouldn’t be able to see the cards in other player’s hands.
- You can take great inspiration from what we already did in our blockchain. There are a lot of processes in this project that are similar to the ones we’ve implemented already. 
