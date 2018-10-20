import os
import datetime
import redis
import bowl_redis
from bowl_redis_dto import GameDto

class SetGameStatus(object):

    def __init__(self, game_id):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
        self.game_id = game_id

    def set(self, game_status):
        pipe = self.redis.pipeline()

        key_info = bowl_redis.RedisKeys(self.game_id)

        game = GameDto()
        game.last_updated = datetime.datetime.now()
        game.game_status = game_status

        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), game.game_status)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), game.last_updated)

        pipe.execute()

        return
