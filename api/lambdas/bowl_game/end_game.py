import bowl_redis

class EndGame(object):

    def __init__(self):
        pass

    @staticmethod
    def end(game_id):
        e = bowl_redis.EndGame(game_id)
        e.execute()

        return
