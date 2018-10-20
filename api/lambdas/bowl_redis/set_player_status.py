import os
import datetime
import redis
import bowl_redis

class SetPlayerStatus(object):

    def __init__(self, game_id):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
        self.game_id = game_id

    def set(self, player_status):
        pipe = self.redis.pipeline()
        key_info = bowl_redis.RedisKeys(self.game_id)

        pipe.lrange(key_info.game_players(), 0, -1)
        [players] = pipe.execute()

        for player_id in players:
            key_info = bowl_redis.RedisKeys(self.game_id, player_id)
            player_info_key = key_info.game_players_info()
            player_status_key = key_info.game_players_status_key()

            pipe.hset(player_info_key, player_status_key, player_status)

        pipe.execute()

        return
