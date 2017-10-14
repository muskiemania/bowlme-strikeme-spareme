import redis
from bowl_redis_dto import PlayerDto, PlayerStatus
from . import RedisKeys

class GetPlayers(object):
    def __init__(self, game_id):
        self.redis = redis.StrictRedis()
        self.game_id = game_id

    def execute(self):
        pipe = self.redis.pipeline()

        key_info = RedisKeys(self.game_id)

        pipe.lrange(key_info.game_players(), 0, -1)
        pipe.hgetall(key_info.game_players_info())

        [player_ids, player_info] = pipe.execute()

        players = []

        for player_id in player_ids:
            key_info = RedisKeys(self.game_id, player_id)
            player_name = player_info[key_info.game_players_name_key()]
            player = PlayerDto(player_name, self.game_id, player_id)
            player.player_status = PlayerStatus.enum(player_info[key_info.game_players_status_key()])

            pipe.lrange(key_info.game_player_hand(), 0, 1)
            [cards] = pipe.execute()
            player.player_cards = cards
            #player.player_cards = ['TH','QC']
            
            players.append(player)
        
        return players
