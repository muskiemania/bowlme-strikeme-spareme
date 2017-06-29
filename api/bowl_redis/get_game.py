import redis
from dateutil import parser
from entities import Game, GameStatus
from . import RedisKeys

class GetGame(object):
    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def get(self):
        game = Game(self.game_id, '')
        
        pipe = self.redis.pipeline()

        key_info = RedisKeys(self.game_id)

        pipe.hget(key_info.game_last_updated(), key_info.game_last_updated_key())
        pipe.hget(key_info.game_last_updated(), key_info.game_last_updated_status_key())
        
        [last_updated, game_status] = pipe.execute()

        game.last_updated = parser.parse(last_updated)
        game.game_status = GameStatus.enum(game_status)
        
        return game
