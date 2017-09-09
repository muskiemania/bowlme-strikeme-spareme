import redis
import bowl_redis
from entities import Player, PlayerStatus

class Players(object):
    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self):
        pipe = self.redis.pipeline()

        key_info = bowl_redis.RedisKeys(self.game_id)
        helpers = bowl_redis.Helpers(pipe)

        pipe.lrange(key_info.game_players(), 0, -1)
        pipe.hgetall(key_info.game_players_info())

        [player_ids, players_info] = pipe.execute()

        players = {}
        for player_id in player_ids:
            key_info = bowl_redis.RedisKeys(self.game_id, player_id)
            player_name = players_info[key_info.game_players_name_key()]
            
            player = Player(player_name, self.game_id)
            player.player_id = player_id
            player.player_status = players_info[key_info.game_players_status_key()]
            players[player_id] = player

        return players
            
        
        
