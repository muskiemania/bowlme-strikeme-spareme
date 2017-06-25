import redis
from entities import PlayerStatus
from . import RedisKeys

class CreatePlayer(object):

    def __init__(self, player):
        self.redis = redis.StrictRedis()
        player.player_status = PlayerStatus.JOINED
        self.player = player

    def execute(self, game_id):
        players = {}
        players[self.player.player_id] = self.player.player_name

        statuses = {}
        statuses[self.player.player_id] = str(self.player.player_status.value)

        key_info = RedisKeys(game_id)

        pipe = self.redis.pipeline()
        pipe.hmset(key_info.game_players(), players)
        pipe.hmset(key_info.game_player_statuses(), statuses)
        pipe.execute()
