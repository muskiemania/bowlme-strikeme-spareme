import redis
from . import RedisKeys

class SetHandRankings(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

        self.__keys = RedisKeys(game_id)
        self.info_key = self.__keys.game_players_info()

    def execute(self, rating_dtos):
        pipe = self.redis.pipeline()

        for rating_dto in rating_dtos:
            self.__keys.player_id = rating_dto.player_id
            rating_key = self.__keys.game_players_rank()
            pipe.hset(self.info_key, rating_key, rating_dto.rank)

        pipe.execute()

