import redis

class GetPlayerIdsByGameId(object):

    def __init__(self):
        self.redis = redis.StrictRedis()

    def execute(self, game_id):
        pipe = self.redis.pipeline()

        key_info = RedisKeys(game_id)
    
        pipe.lrange(key_info.game_players())
        players = pipe.execute()

        return players or []


