from GameInProgress import playround

cardNumber = 5
# players play

playing = threading.Thread(target=playround)
playing.start()