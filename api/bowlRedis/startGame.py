import redis
import cards

class StartGame:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.gameId = None
        self.playerId = None

    def Init(self, startGame):
        self.gameId = startGame.gameId
        self.playerId = startGame.playerId

    def Exec(self):

        #first check to see if playerId is host
        if self.r.hget('game-%s-info' % self.gameId, 'host') == self.playerId:
            statuses = self.r.hgetall('game-%s-status' % self.gameId)
            filtered = {k:v for k,v in statuses.iteritems() if v == '0'}.items()

            while len(filtered) > 0:
                p = self.r.pipeline()
                for (user,v) in filtered:
                    p.hmset('game-%s-status' % self.gameId, {'%s' % user: 1})
                p.execute()
                
                statuses = self.r.hgetall('game-%s-status' % self.gameId)
                filtered = {k:v for k,v in statuses.iteritems() if v == '0'}.items()

            p = self.r.pipeline()
            p.hmset('game-%s-info' % self.gameId, {'status': 1})
            p.execute()
            return True        

        return False

    def Get(self, key, field=None):
        suffix = key.split('-')[2]
        if suffix == 'status':
            return self.r.hgetall('game-%s-status' % self.gameId)
        elif suffix == 'info':
            return self.r.hget(key, field)
