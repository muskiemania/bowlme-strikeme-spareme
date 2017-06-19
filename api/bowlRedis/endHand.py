import redis
import cards

class EndHand:

    
    def __init__(self):
        self.r = redis.StrictRedis()
        self.game_id = None
        self.player_id = None

    def init(self, end_hand):
        self.game_id = end_hand.game_id
        self.player_id = end_hand.player_id

    def execute(self):

        p = self.r.pipeline()
        p.hmset('game-%s-status' % self.game_id, {'%s' % self.player_id: 0})
        p.execute()
        
        return True

    def get(self, key, field=None):
        return self.r.hget(key, field)
