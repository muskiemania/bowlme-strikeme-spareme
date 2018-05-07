import redis
import bowl_redis
from bowl_redis_dto import GameDto, GameStatus, PlayerStatus
from scoring import Scorer
import datetime

class EndGame(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self):
        pipe = self.redis.pipeline()

        #for all players change status to finished
        #change game status to finished

        key_info = bowl_redis.RedisKeys(self.game_id)

        pipe.lrange(key_info.game_players(), 0, -1)

        [players] = pipe.execute()

        for player_id in players:
            key_info = bowl_redis.RedisKeys(self.game_id, player_id)
            player_info_key = key_info.game_players_info()
            player_status_key = key_info.game_players_status_key()

            pipe.hset(player_info_key, player_status_key, PlayerStatus.FINISHED)

        game = GameDto()
        game.last_updated = datetime.datetime.now()
        game.game_status = GameStatus.FINISHED

        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), game.game_status)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), game.last_updated)

        pipe.execute()

        return
