import redis
from bowl_redis_dto import PlayerStatus, RatingDto
import scoring
from . import RedisKeys


class CreatePlayer(object):

    def __init__(self, player):
        self.redis = redis.StrictRedis()
        player.player_status = PlayerStatus.JOINED
        rating = scoring.Scorer.default_rating()
        player.player_rating = RatingDto(rating).as_string()
        self.player = player

    def execute(self, game_id):
        key_info = RedisKeys(game_id, self.player.player_id)

        pipe = self.redis.pipeline()
        pipe.rpush(key_info.game_players(), self.player.player_id)
        pipe.hset(key_info.game_players_info(), key_info.game_players_name_key(), self.player.player_name)
        pipe.hset(key_info.game_players_info(), key_info.game_players_status_key(), self.player.player_status)
        pipe.hset(key_info.game_players_info(), key_info.game_players_rating(), self.player.player_rating)
        pipe.execute()

        return self.player
