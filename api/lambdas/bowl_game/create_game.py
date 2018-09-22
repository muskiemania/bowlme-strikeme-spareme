import bowl_redis
from viewmodels import JoinGameModel

class CreateGame(object):

    def __init__(self):
        pass

    @staticmethod
    def create(host_player_name, number_of_decks):
        create_game = bowl_redis.CreateGame(host_player_name, number_of_decks)
        game_dto = create_game.execute()

        to_return = JoinGameModel(game_dto.game_id, game_dto.host_player_id, game_dto.game_key)
        to_return.other_info = game_dto.redout

        return to_return
