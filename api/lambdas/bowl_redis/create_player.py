import os
import redis
import scoring
from .redis_keys import RedisKeys


class CreatePlayer(object):

    def __init__(self, player):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
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

        return {'key': game_id, 'playerId': self.player.player_id}
