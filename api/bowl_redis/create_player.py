import redis
import scoring
from . import RedisKeys


class CreatePlayer(object):

    def __init__(self, player):
        self.redis = redis.StrictRedis()
        default_rating = scoring.Scorer.default_rating()
        player.player_rating = default_rating.as_string()
        self.player = player

    def execute(self, game_id):
        key_info = RedisKeys(game_id, self.player.player_id)
        players_info = key_info.game_players_info()
        players_name_key = key_info.game_players_name_key()
        players_status_key = key_info.game_players_status_key()
        players_rating_key = key_info.game_players_rating()

        pipe = self.redis.pipeline()
        
        pipe.rpush(key_info.game_players(), self.player.player_id)
        pipe.hset(players_info, players_name_key, self.player.player_name)
        pipe.hset(players_info, players_status_key, self.player.player_status)
        pipe.hset(players_info, players_rating_key, self.player.player_rating)
        pipe.execute()

        return self.player
