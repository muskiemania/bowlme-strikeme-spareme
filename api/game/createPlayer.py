import hashlib

class CreatePlayer:

    def __init__(self, playerName, gameId):
        m = hashlib.md5()
        m.update(playerName)
        m.update(gameId)
        playerId = m.hexdigest()
        
        self.playerId = playerId
        self.playerName = playerName
        self.cards = []
        self.status = 0
