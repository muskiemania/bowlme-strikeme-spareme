import redis
from entities import Game, GameStatus, Player
from . import RedisKeys, CreatePlayer

class CreateGame(object):
    def __init__(self, host_player_name):
        self.redis = redis.StrictRedis()
        self.host_player_name = host_player_name

    def execute(self):
        game_id = self.__get_new_game_id()
        game = Game(game_id, self.host_player_name)
        game.game_status = GameStatus.CREATED

        key_info = RedisKeys(game_id)

        last_updated = {}
        last_updated[key_info.game_last_updated_key()] = game.last_updated
        last_updated[key_info.game_last_updated_status_key()] = game.game_status.value

        pipe = self.redis.pipeline()

        pipe.hset(key_info.game_info(), key_info.game_info_host_name_key(), self.host_player_name)
        pipe.hset(key_info.game_info(), key_info.game_info_status_key(), game.game_status.value)

        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_key(), game.last_updated)
        pipe.hset(key_info.game_last_updated(), key_info.game_last_updated_status_key(), game.game_status.value)

        pipe.execute()

        player = Player(self.host_player_name, game.game_id)

        pipe.hset(key_info.game_info(), key_info.game_info_host_id_key(), player.player_id)
        pipe.execute()

        CreatePlayer(player).execute(game.game_id)

        game.players.append(player)

        return game

    def __get_new_game_id(self):
        key_info = RedisKeys()
        pipe = self.redis.pipeline()
        pipe.incr(key_info.game_id_counter(), 1)
        game_id = pipe.execute()
        if len(game_id) == 1:
            return game_id[0]
        return None
