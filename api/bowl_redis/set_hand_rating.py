import redis
from bowl_redis_dto import RatingDto
from cards import Card, Deck
from . import RedisKeys

class SetHandRating(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

        keys = RedisKeys(game_id, player_id)
        self.info_key = keys.game_players_info()
        self.rating_key = keys.game_players_rating()

    def execute(self, rating_dto):
        pipe = self.redis.pipeline()
        pipe.hset(self.info_key, self.rating_key, rating_dto.as_string())
        print rating_dto.as_string()
        pipe.execute()
        
