import bowl_redis

class StartGame(object):

    def __init__(self):
        pass

    @staticmethod
    def start(game_id):
        print 'inside start'
        start_game = bowl_redis.StartGame(game_id)
        start_game.execute()
        return
