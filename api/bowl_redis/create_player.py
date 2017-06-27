import redis
from entities import PlayerStatus
from . import RedisKeys

class CreatePlayer(object):

    def __init__(self, player):
        self.redis = redis.StrictRedis()
        player.player_status = PlayerStatus.JOINED
        self.player = player

    def execute(self, game_id):
        key_info = RedisKeys(game_id, self.player.player_id)

        players_info = {} 
        players_info[key_info.game_players_name_key()] = self.player.player_name
        players_info[key_info.game_players_status_key()] = self.player.player_status.value

        pipe = self.redis.pipeline()
        pipe.rpush(key_info.game_players(), self.player.player_id)
        pipe.hmset(key_info.game_players_info(), players_info)
        pipe.execute()

        return self.player
