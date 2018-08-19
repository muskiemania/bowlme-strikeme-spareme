import redis
import bowl_redis
from . import RedisKeys

class Players(object):
    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

    def setPlayerStatus(self, new_status):

        pipe = self.redis.pipeline()
        key_info = RedisKeys(self.game_id, self.player_id)
        pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), new_status)
        pipe.execute()

        return
