import os
import redis
from bowl_redis_dto import GameDto, VerifyDto, PlayerDto, GameStatus
from . import RedisKeys

class VerifyGame(object):

    def __init__(self, game_id=None, player_id=None):
        redis_ip = os.environ['REDIS_SERVER']
        redis_pass = os.environ['REDIS_PASSWORD']
        self.redis = redis.StrictRedis(host=redis_ip, password=redis_pass)
        self.game_id = game_id
        self.player_id = player_id

    def __verify_game_only(self):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()

        pipe.hget(key_info.game_info(), key_info.game_info_status_key())
        pipe.hget(key_info.game_info(), key_info.game_info_host_id_key())
        pipe.hget(key_info.game_info(), key_info.game_info_host_name_key())

        (game_status, host_id, host_name) = pipe.execute()

        game_dto = GameDto()
        game_dto.game_id = self.game_id
        game_dto.game_status = GameStatus.enum(game_status)
        game_dto.host_player_id = host_id
        game_dto.host_player_name = host_name
        game_dto.generate_game_key()

        return game_dto

    def __verify_player_too(self):
        key_info = RedisKeys(self.game_id, self.player_id)
        pipe = self.redis.pipeline()

        pipe.hget(key_info.game_players_info(), key_info.game_players_status_key())

        player_dto = PlayerDto('name', self.game_id, self.player_id)
        player_dto.player_status = pipe.execute()[0]

        return player_dto

    def __verify_game_key_only(self, game_key):
        key_info = RedisKeys()
        pipe = self.redis.pipeline()

        pipe.hgetall(key_info.game_hashes_key())
        hashes = pipe.execute()[0]

        print hashes.keys()
        print game_key

        matches = filter(lambda x: x.upper() == game_key.upper(), hashes.keys())

        #print matches

        if len(matches) == 1:
            self.game_id = hashes[matches[0]]
            return self.__verify_game_only()

        raise Exception('too many games with key ' + game_key)

    def execute(self, key=None):

        if key is not None:
            return self.__verify_game_key_only(key)

        verify_game = self.__verify_game_only()

        if self.player_id is None:
            return verify_game

        verify_game.player = self.__verify_player_too()

        return verify_game
