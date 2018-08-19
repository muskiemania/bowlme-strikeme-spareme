import bowl_redis
from viewmodels import JoinGameModel

class CreateGame(object):

    def __init__(self):
        pass

    @staticmethod
    def create(host_player_name):
        create_game = bowl_redis.CreateGame(host_player_name)
        game_dto = create_game.execute()

        return JoinGameModel(game_dto.game_id, game_dto.host_player_id, game_dto.game_key)
