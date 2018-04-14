import bowl_redis
from scoring import Scorer
import game

class StartGame(object):

    def __init__(self):
        pass

    @staticmethod
    def start(game_id, host_player_id):
        print 'inside start'
        start_game = bowl_redis.StartGame(game_id)
        start_game.default_rating = Scorer.default_rating()
        start_game.execute()
        return
