import redis
from . import RedisKeys
from entities import GameStatus, PlayerStatus
from scoring import Scorer

class EndHand(object):

    def __init__(self, game_id, player_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

    def execute(self):
        pipe = self.redis.pipeline()

        key_info = RedisKeys(self.game_id, self.player_id)

        #first verify that game is started and player status is dealt
        pipe.hget(key_info.game_info(), key_info.game_info_status_key())
        pipe.hget(key_info.game_players_info(), key_info.game_players_status_key())
        [game_status, player_status] = pipe.execute()

        if game_status != GameStatus.STARTED.value:
            return
        if player_status != PlayerStatus.DEALT.value:
            return

        #then set player status to finished
        pipe.hmset(key_info.game_players_info, key_info.game_players_status_key, PlayerStatus.FINISHED.value)
        pipe.execute()

        return
