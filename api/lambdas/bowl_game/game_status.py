import bowl_redis

class GameStatus(object):

    def __init__(self):
        pass

    @staticmethod
    def set(game_id, game_status):
        status = bowl_redis.SetGameStatus(game_id)
        status.set(game_status)
        return
