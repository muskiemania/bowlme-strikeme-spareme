import redis
from bowl_redis_dto import GameDto, GameStatus, VerifyDto, PlayerDto, PlayerStatus
from . import RedisKeys

class VerifyGame(object):
    def __init__(self, game_id = None, player_id = None):
        self.redis = redis.StrictRedis()
        self.game_id = game_id
        self.player_id = player_id

    def __verifyGameOnly(self):
        key_info = RedisKeys(self.game_id)
        pipe = self.redis.pipeline()

        pipe.hget(key_info.game_info(), key_info.game_info_status_key())
        pipe.hget(key_info.game_info(), key_info.game_info_host_name_key())

        result = pipe.execute()

        print result
        
        game_dto = GameDto()
        game_dto.game_id = self.game_id
        game_dto.game_status = result[0]
        game_dto.host_player_name = result[1]
        game_dto.generate_game_key()

        return VerifyDto(game_dto)
        
    def __verifyPlayerToo(self):
        key_info = RedisKeys(self.game_id, self.player_id)
        pipe = self.redis.pipeline()

        pipe.hget(key_info.game_players_info(), key_info.game_players_status_key())

        player_dto = PlayerDto('name', self.game_id, self.player_id)
        player_dto.player_status = pipe.execute()[0]

        return player_dto
        
    def __verifyGameKeyOnly(self, game_key):
        key_info = RedisKeys()
        pipe = self.redis.pipeline()

        pipe.hgetall(key_info.game_hashes_key())
        hashes = pipe.execute()[0]
        
        matches = filter(lambda x: x == game_key, hashes.keys())

        print matches
        
        if len(matches) == 1:
            self.game_id = hashes[matches[0]]
            return self.__verifyGameOnly()

        raise Exception('too many games with key ' + game_key)
        
    def execute(self, key = None):

        if key is not None:
            return self.__verifyGameKeyOnly(key)
        
        verify_game = self.__verifyGameOnly()

        if self.player_id is None:
            #do something
            return verify_game

        verify_game.player = self.__verifyPlayerToo()

        #do something
        return verify_game
