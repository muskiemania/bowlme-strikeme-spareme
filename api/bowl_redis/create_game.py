import redis
from bowl_redis_dto import GameDto, GameStatus, PlayerDto
from . import RedisKeys, CreatePlayer

class CreateGame(object):
    def __init__(self, host_player_name):
        self.redis = redis.StrictRedis()
        self.host_player_name = host_player_name

    def execute(self):
        game_id = self.__get_new_game_id()
        gameDto = GameDto(game_id, self.host_player_name)
        gameDto.game_status = GameStatus.CREATED

        key_info = RedisKeys(game_id)

        last_updated = {}
        last_updated[key_info.game_last_updated_key()] = gameDto.last_updated
        last_updated[key_info.game_last_updated_status_key()] = gameDto.game_status

        pipe = self.redis.pipeline()

        pipe.hset(key_info.game_info(), key_info.game_info_host_name_key(), self.host_player_name)
        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), gameDto.game_status)

        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), gameDto.last_updated)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_status_key(), gameDto.game_status)

        pipe.execute()

        playerDto = PlayerDto(self.host_player_name, gameDto.game_id)

        pipe.hset(key_info.game_info(), key_info.game_info_host_id_key(), playerDto.player_id)
        pipe.execute()

        CreatePlayer(playerDto).execute(gameDto.game_id)

        gameDto.host_player_id = playerDto.player_id
        gameDto.players.append(playerDto)

        return gameDto

    def __get_new_game_id(self):
        key_info = RedisKeys()
        pipe = self.redis.pipeline()
        pipe.incr(key_info.game_id_counter(), 1)
        game_id = pipe.execute()
        if len(game_id) == 1:
            return game_id[0]
        return None
