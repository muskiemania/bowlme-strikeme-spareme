import hashlib
import datetime
from createPlayer import CreatePlayer
import cards
import bowlRedis

# 0. need a host
# 1. need cards
# 2. need to shuffle cards
# 3. store data
# 4. return unique game id

class CreateGame:

    def __init__(self, gameId = 0, host = None, players = None, deck = None, discard = None, status = 0):
        self.gameId = gameId
        self.host = host
        self.players = players
        self.deck = deck
        self.discard = discard
        self.status = status

    def CreateGameId(self, hostName = None, hashKey = datetime.datetime.now()):
        m = hashlib.md5()
        m.update(hostName)
        m.update(hashKey)
        return m.hexdigest()
        
    def Create(self, hostName = None, hashKey = None):
        gameId = self.CreateGameId(hostName, hashKey) 
        
        hostPlayer = CreatePlayer(hostName, gameId)
        
        host = hostPlayer.playerId

        players = {}
        players[host] = hostPlayer.__dict__

        deck = cards.Deck()
        deck.ShuffleDeck()

        discard = []

        status = 0

        return CreateGame(gameId=gameId,host=host,players=players,deck=deck,discard=discard,status=status)

    def Exec(self):
        r = bowlRedis.CreateGame()
        r.Init(self)
        
        if r.Exec():
            return self.gameId
