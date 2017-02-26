import redis
import cards

class EndHand:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.gameId = None
        self.playerId = None

    def Init(self, endHand):
        self.gameId = endHand.gameId
        self.playerId = endHand.playerId

    def Exec(self):

        p = self.r.pipeline()
        p.hmset('game-%s-status' % self.gameId, {'%s' % self.playerId: 0})
        p.execute()
        
        return True

    def Get(self, key, field=None):
        return self.r.hget(key, field)
