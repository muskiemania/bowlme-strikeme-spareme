import bowl_redis
import game

class StartGame(object):

    def __init__(self):
        pass

    @staticmethod
    def start(game_id, host_player_id):
        start_game = bowl_redis.StartGame(game_id)
        start_game.execute(host_player_id)

        return game.Game.get(game_id, host_player_id)
