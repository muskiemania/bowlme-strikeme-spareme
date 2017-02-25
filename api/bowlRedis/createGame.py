import redis
import cards

class CreateGame:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.gameId = None
        self.host = None
        self.players = None
        self.deck = None
        self.discard = None
        self.status = None

    def Init(self, createGame):
        self.gameId = createGame.gameId
        self.host = createGame.host
        self.players = createGame.players
        self.deck =  cards.Deck.ShowCards(createGame.deck.cards)
        self.discard = createGame.discard
        self.status = createGame.status

    def Exec(self):

        #need a list for the deck - game-id-deck
        #need a list for the discard - game-id-discard
        #need a list for each players hand game-id-player-hand
        #need a hash for game info: host, status game-id-info:
        #hash for each players name - game-id-name:playerid
        #hash for each players hand - game-id-status:playerid
        p = self.r.pipeline()

        p.delete('game-%s-deck' % self.gameId)
        p.rpush('game-%s-deck' % self.gameId, *list(self.deck))
        p.hmset('game-%s-info' % self.gameId, {'host': self.host, 'status': self.status})
        p.hmset('game-%s-name' % self.gameId, {'%s' % self.host: self.players[self.host]['playerName']})
        p.hmset('game-%s-status' % self.gameId, {'%s' % self.host: 0})
        p.execute()

        return True

    def Get(self, key, field=None):
        suffix = key.split('-')[2]
        if suffix == 'deck':
            return self.r.lrange(key, 0, -1)
        elif suffix == 'info' or suffix == 'name' or suffix == 'status':
            return self.r.hget(key, field)
