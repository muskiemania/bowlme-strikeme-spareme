import redis
import cards

class JoinGame:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.gameId = None
        self.player = None

    def Init(self, joinGame):
        self.gameId = joinGame.gameId
        self.player = joinGame.player

    def Exec(self):

        #need a list for the deck - game-id-deck
        #need a list for the discard - game-id-discard
        #need a list for each players hand game-id-player-hand
        #need a hash for game info: host, status game-id-info:
        #hash for each players name - game-id-name:playerid
        #hash for each players hand - game-id-status:playerid
        p = self.r.pipeline()
        p.hmset('game-%s-name' % self.gameId, {'%s' % self.player.playerId: self.player.playerName})
        p.hmset('game-%s-status' % self.gameId, {'%s' % self.player.playerId: 0})
        p.execute()

        return True

    def Get(self, key, field=None):
        suffix = key.split('-')[2]
        if suffix == 'deck':
            return self.r.lrange(key, 0, -1)
        elif suffix == 'info' or suffix == 'name' or suffix == 'status':
            return self.r.hget(key, field)
