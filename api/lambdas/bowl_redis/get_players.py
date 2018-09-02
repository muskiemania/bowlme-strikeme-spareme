import os
import redis
from bowl_redis_dto import PlayerDto, PlayerStatus, RatingDto
from . import RedisKeys

class GetPlayers(object):
    def __init__(self, game_id):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
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
            status_key = key_info.game_players_status_key()
            player.player_status = PlayerStatus.enum(player_info[status_key])

            pipe.lrange(key_info.game_player_hand(), 0, -1)
            pipe.hget(key_info.game_players_info(), key_info.game_players_rating())
            pipe.hget(key_info.game_players_info(), key_info.game_players_rank())

            [cards, rating, rank] = pipe.execute()
            player.player_cards = cards
            player.player_rating = RatingDto(rating)
            player.player_rating.rank = rank

            players.append(player)

        return players
