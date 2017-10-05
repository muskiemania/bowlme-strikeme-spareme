import redis
from dateutil import parser
from entities import Game, GameStatus
from . import RedisKeys

class GetGame(object):
    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self):
        game = Game(self.game_id, '')
        
        pipe = self.redis.pipeline()

        key_info = RedisKeys(self.game_id)

        pipe.hget(key_info.game_last_updated(), key_info.game_last_updated_key())
        pipe.hget(key_info.game_info(), key_info.game_info_status_key())
        pipe.hget(key_info.game_info(), key_info.game_info_host_id_key())
        
        [last_updated, game_status, host_player_id] = pipe.execute()
        
        game.last_updated = parser.parse(last_updated)
        game.game_status = GameStatus.enum(game_status)
        game.host_player_id = host_player_id
        
        return game
