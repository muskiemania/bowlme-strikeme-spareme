import redis


class GetGameIdByHash(object):

    def __init__(self):
        self.redis = redis.StrictRedis()

    def execute(self, game_key):
        pipe = self.redis.pipeline()

        key_info = RedisKeys()
        
        pipe.hexists(key_info.game_hashes_key(), game_key)

        exists = pipe.execute()
        if not exists:
            return None

        pipe.hget(key_info.game_hashes_key(), game_key)
        game_id = pipe.execute()

        return { game_id }
