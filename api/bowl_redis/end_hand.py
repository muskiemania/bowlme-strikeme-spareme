import redis

class EndHand(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

    def execute(self):

        pipe = self.redis.pipeline()
        pipe.hmset('game-%s-status' % self.game_id, {'%s' % self.player_id: 0})
        pipe.execute()

        return True

    def get(self, key, field=None):
        return self.redis.hget(key, field)
