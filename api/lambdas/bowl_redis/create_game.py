import datetime
import os
import redis
from bowl_redis_dto import GameDto, GameStatus
from . import RedisKeys

class CreateGame(object):
    def __init__(self, host_player_name, number_of_decks):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
        self.host_player_name = host_player_name
        self.number_of_decks = number_of_decks

    def execute(self):
        game_dto = GameDto()
        game_dto.game_id = self.__get_new_game_id()
        game_dto.host_player_name = self.host_player_name
        game_dto.game_status = GameStatus.CREATED
        game_dto.last_updated = str(datetime.datetime.now())
        game_dto.generate_game_key()

        key_info = RedisKeys(game_dto.game_id)

        pipe = self.redis.pipeline()

        host_name_key = key_info.game_info_host_name_key()
        status_key = key_info.game_info_status_key()
        pipe.hset(key_info.game_info(), host_name_key, self.host_player_name)
        pipe.hset(key_info.game_info(), status_key, game_dto.game_status)

        last_updated = key_info.game_last_updated()
        last_updated_key = key_info.game_last_updated_key()
        last_updated_status_key = key_info.game_last_updated_status_key()
        pipe.hset(last_updated, last_updated_key, game_dto.last_updated)
        pipe.hset(last_updated, last_updated_status_key, game_dto.game_status)
        pipe.hset(key_info.game_hashes_key(), game_dto.game_key, game_dto.game_id)

        pipe.execute()

        #player_dto = PlayerDto(self.host_player_name, game_dto.game_id)
        #player_dto.player_status = PlayerStatus.JOINED

        #host_id_key = key_info.game_info_host_id_key()
        #pipe.hset(key_info.game_info(), host_id_key, player_dto.player_id)
        #pipe.execute()

        #CreatePlayer(player_dto).execute(game_dto.game_id)

        #game_dto.host_player_id = player_dto.player_id
        #game_dto.players.append(player_dto)

        return game_dto.json()

    def __get_new_game_id(self):
        key_info = RedisKeys()
        pipe = self.redis.pipeline()
        pipe.incr(key_info.game_id_counter(), 1)
        game_id = pipe.execute()
        if len(game_id) == 1:
            return game_id[0]
        return None
