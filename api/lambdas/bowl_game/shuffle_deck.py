import bowl_redis

class ShuffleDeck(object):

    def __init__(self):
        pass

    @staticmethod
    def shuffle(game_id):
        shuffle = bowl_redis.ShuffleDeck(game_id)
        shuffle.execute()
        return
