import redis
from bowl_redis_dto import RatingDto
from . import RedisKeys

class GetHandRatings(object):

    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

        self.__keys = RedisKeys(game_id)
        self.players_key = self.__keys.game_players()
        self.info_key = self.__keys.game_players_info()

    def execute(self):
        pipe = self.redis.pipeline()

        pipe.lrange(self.players_key, 0, -1)
        pipe.hgetall(self.info_key)

        (player_ids, players) = pipe.execute()

        ratings = []

        for player_id in player_ids:
            self.__keys.player_id = player_id
            rating_key = self.__keys.game_players_rating()
            rating = RatingDto(players[rating_key], player_id)
            ratings.append(rating)

        return ratings
