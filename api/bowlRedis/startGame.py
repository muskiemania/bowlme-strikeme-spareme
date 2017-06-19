import redis
import cards

class StartGame:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.game_id = None
        self.player_id = None

    def init(self, start_game):
        self.game_id = start_game.game_id
        self.player_id = start_game.player_id

    def execute(self):

        #first check to see if playerId is host
        if self.r.hget('game-%s-info' % self.game_id, 'host') == self.player_id:
            statuses = self.r.hgetall('game-%s-status' % self.game_id)
            filtered = {k:v for k,v in statuses.iteritems() if v == '0'}.items()

            while len(filtered) > 0:
                p = self.r.pipeline()
                for (user,v) in filtered:
                    p.hmset('game-%s-status' % self.game_id, {'%s' % user: 1})
                p.execute()
                
                statuses = self.r.hgetall('game-%s-status' % self.game_id)
                filtered = {k:v for k,v in statuses.iteritems() if v == '0'}.items()

            p = self.r.pipeline()
            p.hmset('game-%s-info' % self.game_id, {'status': 1})
            p.execute()
            return True        

        return False

    def Get(self, key, field=None):
        suffix = key.split('-')[2]
        if suffix == 'status':
            return self.r.hgetall('game-%s-status' % self.game_id)
        elif suffix == 'info':
            return self.r.hget(key, field)
